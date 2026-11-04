from __future__ import annotations

import re
from dataclasses import dataclass
from functools import cached_property
from typing import Iterable, Iterator, Literal, Sequence

import lxml.etree as et

from ..namespaces import BASE_NS

AttributeDatatype = Literal[
    "string",
    "[]string",
    "integer",
    "double",
    "[]double",
    "datetime",
    "boolean",
    "date",
    "object",
    "[]object",
    "xAL",
]


@dataclass
class GeometricAttribute:
    """ジオメトリ属性 (a.k.a 空間属性)"""

    lod_detection: Sequence[str]
    """lodを検出するための element paths"""

    collect_all: Sequence[str]
    """このFeatureの階層下にある全ジオメトリを収集するための element path (部分要素に分けずに読み込む場合に使う) """

    only_direct: list[str] | None = None
    """このFeatureの直下にあるジオメトリを収集するための element paths"""

    is2d: bool = False
    """PLATEAUの仕様において高さ0のジオメトリかどうか"""


@dataclass
class GeometricAttributes:
    """Featureの出力について記述する"""

    lod0: GeometricAttribute | None = None
    lod1: GeometricAttribute | None = None
    lod2: GeometricAttribute | None = None
    lod3: GeometricAttribute | None = None
    lod4: GeometricAttribute | None = None

    lod_n: str | None = None
    lod_n_paths: GeometricAttribute | None = None

    semantic_parts: list[str] | None = None
    """子Featureへの element paths"""


@dataclass
class Attribute:
    """1つの属性抽出についての定義"""

    name: str
    path: str
    datatype: AttributeDatatype
    predefined_codelist: str | dict[str, str] | None = None


@dataclass
class AttributeGroup:
    """属性抽出をグルーピングする"""

    base_element: str | None
    """属性抽出の起点とするXML要素への element path。None の場合はこのFeature自体を起点とする。"""

    attributes: Sequence[Attribute]
    # mode: Literal["flatten", "map"] = "flatten"


@dataclass
class FacilityAttributePaths:
    facility_types: str
    facility_id: str
    facility_attrs: str
    large_customer_facility_attrs: str | None = None


@dataclass
class FeatureProcessingDefinition:
    """各 Feature の処理方法を定める"""

    id: str
    """このProcessorのID"""

    name: str
    """このProcessorの表示名"""

    target_elements: list[str]
    """処理対象とするFeature要素 (e.g. "tran:Road", "tran:TrafficArea", "bldg:WallSurface")"""

    attribute_groups: list[AttributeGroup]
    """抽出したい属性の定義"""

    geometries: GeometricAttributes
    """ジオメトリの抽出についての定義"""

    load_generic_attributes: bool = False
    """汎用属性 (gen:stringAttribute など) を読み込むかどうか"""

    dm_attr_container_path: str | None = None
    """公共測量標準図式 uro:DmAttribute を包含する要素 (e.g. bldg:bldgDmAttribute) への element path"""

    facility_attr_paths: FacilityAttributePaths | None = None
    """施設管理の応用スキーマ関連の属性への element path"""

    disaster_risk_attr_conatiner_path: str | Sequence[str] | None = None
    """災害リスク属性 uro:(Building)DisasterRiskAttribute を包含する要素への element path (複数指定可)"""

    nested_attributes: list[str] | None = None
    """ネストされた属性として表現すべき属性"""

    non_geometric: bool = False
    """ジオメトリを持たない Feature かどうか

    Trueの場合は、ジオメトリをもたない場合も地物として出力する
    """

    def detect_lods(self, elem: et._Element, nsmap: dict[str, str]) -> tuple[bool, ...]:
        """どの LoD が存在するかを返す。

        例: LoD1と2が存在するとき → (False, True, True, False, False)
        """
        det = self.geometries
        if det.lod_n:
            # dem では <lod>1</lod> のスタイルでLODが記述されている
            lod = int(elem.find(det.lod_n, BASE_NS).text)
            return tuple(lod == i for i in range(5))
        else:
            # そのほかの場合
            return tuple(
                bool(
                    em
                    and any(elem.find(p, nsmap) is not None for p in em.lod_detection)
                )
                for em in self.lod_list
            )

    @cached_property
    def lod_list(self) -> tuple[GeometricAttribute | None, ...]:
        return (
            self.geometries.lod0,
            self.geometries.lod1,
            self.geometries.lod2,
            self.geometries.lod3,
            self.geometries.lod4,
        )


class ProcessorRegistory:
    """Feature を処理する Processors を登録しておくレジストリ"""

    def __init__(
        self, processors: Iterable[FeatureProcessingDefinition] | None = None
    ) -> None:
        self._tag_map: dict[str, FeatureProcessingDefinition] = {}
        self._id_map: dict[str, FeatureProcessingDefinition] = {}
        if processors:
            for processor in processors:
                self.register_processor(processor)

    def _make_prefix_variants(self, prefixed_names: Iterable[str]) -> Iterator[str]:
        for name in prefixed_names:
            prefix, n = name.split(":", 1)
            if prefix == "uro":
                yield "uro14:" + n
                yield "uro15:" + n
                yield "uro2:" + n
                yield "uro3:" + n
                yield "uro31:" + n
                yield "uro32:" + n
            elif prefix == "urf":
                yield "urf14:" + n
                yield "urf15:" + n
                yield "urf2:" + n
                yield "urf3:" + n
            else:
                yield name

    def register_processor(self, processor: FeatureProcessingDefinition) -> None:
        """Processor を登録する"""
        if processor.id in self._id_map:
            raise ValueError(f"Processor id {processor.id} is already registered")

        self._id_map[processor.id] = processor
        closed_target = set()
        for prefixed_name in self._make_prefix_variants(processor.target_elements):
            if prefixed_name in closed_target:
                raise ValueError(f"Duplicate target element: {prefixed_name}")
            closed_target.add(prefixed_name)

            qualified_name = re.sub(
                r"^(.+?):()", lambda m: "{" + BASE_NS[m.group(1)] + "}", prefixed_name
            )
            if prefixed_name in self._tag_map:
                raise ValueError(f"{prefixed_name} is already registered")
            self._tag_map[prefixed_name] = processor
            if qualified_name in self._tag_map:
                raise ValueError(f"{qualified_name} is already registered")
            self._tag_map[qualified_name] = processor

    def get_processor_by_tag(
        self, target_tag: str
    ) -> FeatureProcessingDefinition | None:
        """XMLの要素名をもとに Processor を取得する"""
        return self._tag_map.get(target_tag)

    def validate_processors(self) -> None:  # noqa: C901
        """Processor の定義を検証する処理 (テスト用)"""
        from pathlib import Path

        from ..codelists import CodelistStore

        codelists = CodelistStore(Path("./"))

        for processor in self._id_map.values():
            for target in processor.nested_attributes or []:
                target = target.rsplit("/", 1)[1]
                for prefixed in self._make_prefix_variants([target]):
                    if prefixed not in self._tag_map:
                        raise ValueError(f"{prefixed} is not registered")

            for target in processor.geometries.semantic_parts or []:
                target = target.rsplit("/", 1)[1]
                if target == "*":
                    continue
                for prefixed in self._make_prefix_variants([target]):
                    if prefixed not in self._tag_map:
                        raise ValueError(f"{prefixed} is not registered")

            for group in processor.attribute_groups:
                for attr in group.attributes:
                    if attr.name not in attr.path:
                        raise ValueError(f"{attr.name} not in {attr.path}")
                    if attr.predefined_codelist:
                        if isinstance(attr.predefined_codelist, str):
                            codelists.get_predefined(attr.predefined_codelist)
                        else:
                            for a in attr.predefined_codelist.values():
                                codelists.get_predefined(a)

        # for i, lod in enumerate(processor.lod_list):
        #     if lod is None:
        #         continue

        #     if any(str(i) not in a for a in lod.collect_all):
        #         raise ValueError(f"{i} not in {lod.collect_all} for {processor.id}")

        #     if any(str(i) not in a for a in lod.lod_detection):
        #         raise ValueError(
        #             f"{i} not in {lod.lod_detection} for {processor.id}"
        #         )
