"""Processing algorithm for converting plateau files"""

# Copyright (C) 2023 MIERUNE Inc.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import datetime
import json
from typing import Any

from PyQt5.QtCore import QCoreApplication, QDate
from qgis.core import (
    QgsCoordinateReferenceSystem,
    QgsCoordinateTransform,
    QgsFeature,
    # QgsLayerTreeGroup,
    # QgsLayerTreeGroup,
    QgsProcessingAlgorithm,
    QgsProcessingException,  # pyright: ignore
    QgsProcessingParameterBoolean,
    QgsProcessingParameterCrs,
    QgsProcessingParameterFile,
    QgsProject,
)

from ..geometry import to_qgis_geometry
from ..plateau.parser import FileParser, ParseSettings
from .utils.layermanger import LayerManager


def _convert_to_qt_value(v: Any) -> Any:
    if isinstance(v, list):
        if not v:
            return None
        elif isinstance(v[0], str):
            return ",".join(v)
        else:
            return json.dumps(v, ensure_ascii=False)
    else:
        # not a list
        if isinstance(v, dict):
            return json.dumps(v, ensure_ascii=False)
        elif isinstance(v, datetime.date):
            return QDate(v.year, v.month, v.day)
        else:
            return v


_DESCRIPTION = """3D都市モデル標準製品仕様書 第3.0版に対応した、PLATEAU 3D都市モデルのCityGML (.gml) ファイルを読み込みます。

データは一時スクラッチレイヤに読み込まれます。

同一の都市オブジェクトに複数のLOD (詳細度) が用意されている場合は、デフォルトでは最も詳細なLODのみを読み込みます。すべてのLODを読み込みたい場合は「各地物の最高 LOD のみを読み込む」オプションを無効にしてください。

「意味的な子要素に分ける」を有効にすると、一部のモデルのLOD2以上において、壁や屋根、車道や歩道といった意味的な部分に分けて地物を読み込みます。このオプションを有効にすると生成される地物の数が大幅に増える可能性があります。

「3Dデータを強制的に平面化する」を有効にすると、3次元の情報を捨てて平面データとして読み込みます。高さをもたないモデル (都市計画決定情報など) はこのオプションにかかわらず常に平面として読み込みます。
"""


class PlateauVectorLoaderAlrogithm(QgsProcessingAlgorithm):
    """Processing algorithm to load PLATEAU 3D City models as vector layers"""

    INPUT = "INPUT"
    ONLY_HIGHEST_LOD = "ONLY_HIGHEST_LOD"
    LOAD_SEMANTIC_PARTS = "LOAD_SEMANTIC_PARTS"
    FORCE_2D = "FORCE_2D"
    CRS = "CRS"

    def tr(self, string: str):
        return QCoreApplication.translate("Processing", string)

    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterFile(
                self.INPUT,
                self.tr("PLATEAU CityGML ファイル"),
                fileFilter=self.tr("PLATEAU CityGML ファイル (*.gml)"),
            )
        )
        self.addParameter(
            QgsProcessingParameterBoolean(
                self.ONLY_HIGHEST_LOD,
                self.tr("各地物の最高 LOD のみを読み込む"),
                defaultValue=True,
                optional=True,
            )
        )
        self.addParameter(
            QgsProcessingParameterBoolean(
                self.LOAD_SEMANTIC_PARTS,
                self.tr("意味的な子要素に分ける"),
                defaultValue=False,
                optional=True,
            )
        )
        self.addParameter(
            QgsProcessingParameterBoolean(
                self.FORCE_2D,
                self.tr("3次元データを強制的に2次元化する"),
                defaultValue=False,
                optional=True,
            )
        )
        self.addParameter(
            QgsProcessingParameterCrs(
                self.CRS,
                self.tr("変換先CRS"),
                defaultValue="EPSG:4326",
                optional=True,
            )
        )

    def createInstance(self):
        return PlateauVectorLoaderAlrogithm()

    def name(self):
        return "load_as_vector"

    def group(self):
        return None

    def groupId(self):
        return None

    def displayName(self):
        return self.tr("PLATEAU 3D都市モデルを読み込む")

    def shortHelpString(self) -> str:
        return self.tr(_DESCRIPTION)

    def _make_parser(self, parameters, context) -> FileParser:
        """プロセシングの設定をもとにパーサを作る"""
        load_semantic_parts = self.parameterAsBoolean(
            parameters, self.LOAD_SEMANTIC_PARTS, context
        )
        only_highest_lod = self.parameterAsBoolean(
            parameters, self.ONLY_HIGHEST_LOD, context
        )
        settings = ParseSettings(
            load_semantic_parts=load_semantic_parts,
            only_highest_lod=only_highest_lod,
        )

        filename = self.parameterAsFile(parameters, self.INPUT, context)
        if filename is None:
            raise QgsProcessingException(
                self.invalidSourceError(parameters, self.INPUT)
            )  # pragma: no cover

        return FileParser(filename, settings)

    def processAlgorithm(self, parameters, context, feedback):
        destination_crs = self.parameterAsCrs(parameters, self.CRS, context)
        force2d = self.parameterAsBoolean(parameters, self.FORCE_2D, context)
        layers = LayerManager(force2d=force2d, crs=destination_crs)

        parser = self._make_parser(parameters, context)
        total_count = parser.count_toplevel_cityobjs()
        feedback.pushInfo(f"{total_count}個のトップレベル都市オブジェクトが含まれています。")
        feedback.pushInfo("都市オブジェクトを読み込んでいます...")
        top_level_count = 0
        count = 0

        crs_transform = QgsCoordinateTransform(
            QgsCoordinateReferenceSystem("epsg:6697"),
            destination_crs,
            QgsProject.instance(),
        )

        # NOTE: 例外のハンドリングはプロセッシングフレームワークに任せている
        for top_level_count, cityobj in parser.iter_cityobjs():
            if feedback.isCanceled():
                return {}

            layer = layers.get_layer(cityobj)
            provider = layer.dataProvider()
            feature = QgsFeature(provider.fields())

            # Set attributes
            feature.setAttribute("id", cityobj.id)
            feature.setAttribute("type", cityobj.type)
            feature.setAttribute("lod", cityobj.lod)
            feature.setAttribute("name", cityobj.name)
            feature.setAttribute(
                "creationDate",
                QDate(cityobj.creation_date) if cityobj.creation_date else None,  # type: ignore
            )
            feature.setAttribute(
                "terminationDate",
                QDate(cityobj.creation_date) if cityobj.termination_date else None,  # type: ignore
            )
            if cityobj.parent:
                # 親Featureと結合 (join) できるように親Featureの ID を持たせる
                feature.setAttribute("parent", cityobj.parent.id)

            for name, value in cityobj.attributes.items():
                feature.setAttribute(name, _convert_to_qt_value(value))

            if cityobj.geometry:
                # Should be treated as 2D?
                as2d = False
                if cityobj.lod is not None:
                    lod_def = cityobj.processor.lod_list[cityobj.lod]
                    if lod_def:
                        as2d = force2d or lod_def.is2d

                # Set geometry
                geom = to_qgis_geometry(cityobj.geometry, as2d=as2d)
                geom.transform(crs_transform, transformZ=False)
                feature.setGeometry(geom)

            provider.addFeature(feature)
            count += 1
            if count % 100 == 0:
                feedback.setProgress(top_level_count / total_count * 100)
                feedback.pushInfo(f"{count} 個の地物を読み込みました。")

        feedback.pushInfo(f"{count} 個の地物を読み込みました。")
        layers.add_to_project()

        return {}
