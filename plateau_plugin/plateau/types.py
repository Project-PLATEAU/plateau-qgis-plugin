from dataclasses import dataclass
from datetime import date
from typing import Any, Literal, Optional, Union

import numpy as np

from .models.base import AttributeDatatype, FeatureProcessingDefinition


@dataclass
class PointCollection:
    __slots__ = ("points",)
    points: np.ndarray


@dataclass
class LineStringCollection:
    __slots__ = ("lines",)
    lines: list[np.ndarray]


@dataclass
class PolygonCollection:
    __slots__ = ("polygons", "materials", "textures", "uvs")
    polygons: list[list[np.ndarray]]

    # appearance
    materials: Optional[list[Optional["Material"]]]
    textures: Optional[list[Optional["Texture"]]]
    uvs: Optional[list[Optional[list[np.ndarray]]]]


Geometry = Union[PolygonCollection, LineStringCollection, PointCollection]


@dataclass
class CityObject:
    """都市オブジェクト (Feature) を表す"""

    lod: Literal[0, 1, 2, 3, 4, None]
    """LoD (0, 1, 2, 3, 4) または None (ジオメトリなし)"""

    type: str
    """このFeatureの型名 (e.g. tran:Road, tran:TrafficArea, etc.)"""

    id: Optional[str]
    """@gml:id"""

    name: Optional[str]
    """gml:name"""

    creation_date: Optional[date]
    """core:creationDate"""

    termination_date: Optional[date]
    """core:terminationDate"""

    attributes: dict[str, Any]
    """Featureのプロパティ値"""

    geometry: Optional[Geometry]
    """Featureのジオメトリ"""

    processor: FeatureProcessingDefinition

    parent: Optional["CityObject"]
    """親のCityObject"""


@dataclass
class FieldDefinition:
    """QGIS 等にテーブルを作る際のフィールド定義"""

    name: str
    datatype: AttributeDatatype


@dataclass
class TableDefinition:
    """QGIS 等にテーブルを作る際のテーブル定義"""

    fields: list[FieldDefinition]


def get_table_definition(cityobj: CityObject) -> TableDefinition:
    processor = cityobj.processor
    fields = [
        FieldDefinition("id", "string"),
        FieldDefinition("type", "string"),
        FieldDefinition("name", "string"),
        FieldDefinition("creationDate", "date"),
        FieldDefinition("terminationDate", "date"),
    ]
    if processor.load_generic_attributes:
        fields.append(FieldDefinition("generic", "object"))
    closed: dict[str, str] = {}
    for group in processor.attribute_groups:
        for prop in group.attributes:
            if prop.name not in closed:
                fields.append(FieldDefinition(prop.name, prop.datatype))
                closed[prop.name] = prop.datatype
            else:
                # 同名のフィールドが既にある場合は、型が一致しているか確認する
                assert (
                    closed[prop.name] == prop.datatype
                ), f"{prop.name}, {closed[prop.name]} != {prop.datatype}"

    return TableDefinition(fields=fields)


@dataclass
class Material:
    __slots__ = ("diffuse_color", "specular_color", "shininess")
    diffuse_color: Optional[tuple[float, ...]]
    specular_color: Optional[tuple[float, ...]]
    shininess: Optional[float]


@dataclass
class Texture:
    __slots__ = ("image_uri",)
    image_uri: str


@dataclass
class Appearance:
    target_material: dict[str, Material]
    ring_texture: dict[str, tuple[Texture, np.ndarray]]
