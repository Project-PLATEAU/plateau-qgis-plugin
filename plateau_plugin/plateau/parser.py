from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Iterable, Optional, Union

import lxml.etree as et

from .appearance import Appearance, parse_appearances
from .codelists import CodelistStore
from .geometry import parse_geometry
from .models import processors
from .models.base import FeatureProcessingDefinition
from .namespaces import Namespace
from .types import CityObject

_BOOLEAN_TRUE_STRINGS = frozenset({"true", "True", "1"})


@dataclass
class ParseSettings:
    load_semantic_parts: bool = False
    """部分要素 (e.g. Road の細分化の TrafficArea) に分けて読み込むかどうか"""

    only_highest_lod: bool = False
    """各Featureの最高の LoD だけ出力するかどうか"""

    load_apperance: bool = False


class Parser:
    def __init__(
        self,
        settings: ParseSettings,
        ns: Namespace,
        codelist_store: CodelistStore,
        appearance: Optional[Appearance] = None,
    ) -> None:
        self._settings = settings
        self._ns: Namespace = ns
        self._nsmap: dict[str, str] = ns.nsmap
        self._codelist_store = codelist_store
        self.appearance = appearance

    def _get_id_and_name(self, elem: et._Element):
        """@gml:id と gml:name (あれば) を読む"""
        nsmap = self._nsmap
        gml_id = elem.get("{http://www.opengis.net/gml}id", None)
        if (name_elem := elem.find("./gml:name", nsmap)) is not None:
            gml_name = name_elem.text
            if path := name_elem.get("codeSpace"):
                gml_name = self._codelist_store.lookup(None, path, gml_name)
        else:
            gml_name = None

        return (gml_id, gml_name)

    def _get_basic_dates(
        self, elem: et._Element
    ) -> tuple[Optional[date], Optional[date]]:
        """基本形な日付 core:creationDate (あれば) と core:terminationDate (あれば) を読む"""
        nsmap = self._nsmap
        creation_date = (
            date.fromisoformat(name_elem.text)
            if (name_elem := elem.find("./core:creationDate", nsmap)) is not None
            else None
        )
        termination_date = (
            date.fromisoformat(name_elem.text)
            if (name_elem := elem.find("./core:terminationDate", nsmap)) is not None
            else None
        )
        return (creation_date, termination_date)

    def _get_codelist(
        self, base_elem: et._Element, codelist: Union[str, dict[str, str], None]
    ) -> Optional[str]:
        if codelist is None or isinstance(codelist, str):
            return codelist

        return codelist[self._ns.to_prefixed_name(base_elem.tag)]

    def _load_props(  # noqa: C901
        self, processor: FeatureProcessingDefinition, feature_elem: et._Element
    ) -> dict[str, Any]:
        """属性値を読み込む"""
        nsmap = self._nsmap
        props: dict[str, Any] = {}
        codelist_lookup = self._codelist_store.lookup

        if processor.load_generic_attributes:
            props["generic"] = self._parse_generic_attributes(feature_elem)

        for group in processor.attribute_groups:
            if group.base_element is None:
                base_elem = feature_elem
            else:
                base_elem = feature_elem.find(group.base_element, nsmap)
                if base_elem is None:
                    continue

            for prop in group.attributes:
                assert prop.name in prop.path, f"{prop.name} not in {prop.path}"
                if prop.datatype == "[]string":
                    values = []
                    for child_elem in base_elem.iterfind(prop.path, nsmap):
                        v = child_elem.text
                        path = child_elem.get("codeSpace")
                        if prop.predefined_codelist or path:
                            pcl = self._get_codelist(
                                base_elem, prop.predefined_codelist
                            )
                            v = codelist_lookup(pcl, path, v)
                        values.append(v)
                    props[prop.name] = values
                elif prop.datatype == "xAL":
                    if (child_elem := base_elem.find(prop.path, nsmap)) is not None:
                        value = " ".join(
                            s.strip() for s in child_elem.itertext() if s.strip()
                        )
                        props[prop.name] = value
                    else:
                        continue
                else:
                    if (child_elem := base_elem.find(prop.path, nsmap)) is not None:
                        value = child_elem.text
                    else:
                        continue

                    if prop.datatype == "string":
                        v = str(value)
                        path = child_elem.get("codeSpace")
                        if prop.predefined_codelist or path:
                            pcl = self._get_codelist(
                                base_elem, prop.predefined_codelist
                            )
                            v = codelist_lookup(pcl, path, v)
                        props[prop.name] = v
                    elif prop.datatype == "double":
                        props[prop.name] = float(value)
                    elif prop.datatype == "integer":
                        props[prop.name] = int(value)
                    elif prop.datatype == "boolean":
                        props[prop.name] = bool(value in _BOOLEAN_TRUE_STRINGS)
                    elif prop.datatype == "date":
                        props[prop.name] = date.fromisoformat(value)
                    else:
                        raise NotImplementedError(f"Unknown datatype: {prop.datatype}")
        return props

    def _parse_generic_attributes(  # noqa: C901
        self, elem: et._Element
    ) -> dict[str, Any]:
        nsmap = self._nsmap
        generic_attrs = {}

        for gen in elem.findall("./gen:*", nsmap):
            tag = self._ns.to_prefixed_name(gen.tag)
            if tag.startswith("gen:lod"):
                continue
            if tag == "gen:genericAttributeSet":
                if name := gen.get("name"):
                    generic_attrs[name] = self._parse_generic_attributes(gen)
            elif tag == "gen:stringAttribute":
                if (name := gen.get("name")) and (
                    value := gen.find("./gen:value", nsmap)
                ) is not None:
                    generic_attrs[name] = value.text
            elif tag == "gen:intAttribute":
                if (name := gen.get("name")) and (
                    value := gen.find("./gen:value", nsmap)
                ) is not None:
                    generic_attrs[name] = int(value.text)
            elif tag == "gen:doubleAttribute" or tag == "gen:measureAttribute":
                if (name := gen.get("name")) and (
                    value := gen.find("./gen:value", nsmap)
                ) is not None:
                    generic_attrs[name] = float(value.text)
            elif tag == "gen:dateAttribute":
                if (name := gen.get("name")) and (
                    value := gen.find("./gen:value", nsmap)
                ) is not None:
                    generic_attrs[name] = value.text
            else:
                raise NotImplementedError(f"Unknown generic attribute: {tag}")

        return generic_attrs

    def process_cityobj_element(  # noqa: C901
        self,
        elem: et._Element,
        parent: Optional[CityObject],  # 祖先Featureの Processor
    ) -> Iterable[CityObject]:
        ns = self._ns
        nsmap = self._nsmap
        appearance = self.appearance

        (gml_id, gml_name) = self._get_id_and_name(elem)
        (creation_date, termination_date) = self._get_basic_dates(elem)

        # この要素のための Processor を得る
        processor = processors.get_processor_by_tag(elem.tag)
        if processor is None:
            return

        # 属性を収集する
        props = self._load_props(processor, elem)

        # 親Feature (ジオメトリなし) を用意する
        nogeom_obj = CityObject(
            type=ns.to_prefixed_name(elem.tag),
            id=gml_id,
            name=gml_name,
            creation_date=creation_date,
            termination_date=termination_date,
            lod=None,
            geometry=None,
            attributes=props,
            processor=processor,
            parent=parent,
        )
        nogeom_emitted = False

        # リスク属性
        if processor.disaster_risk_attr_conatiner_path:
            for risk in elem.iterfind(
                processor.disaster_risk_attr_conatiner_path + "/*", nsmap
            ):
                for child_obj in self.process_cityobj_element(risk, nogeom_obj):
                    if not nogeom_emitted:
                        yield nogeom_obj
                        nogeom_emitted = True
                    yield child_obj

        # 公共測量標準図式 (DM)
        if processor.dm_attr_container_path:
            for dm in elem.iterfind(processor.dm_attr_container_path + "/*", nsmap):
                for child_obj in self.process_cityobj_element(dm, nogeom_obj):
                    if not nogeom_emitted:
                        yield nogeom_obj
                        nogeom_emitted = True
                    yield child_obj

        # 子Feature (部分要素) を個別に読み込む設定の場合は、子Featureを探索する
        if self._settings.load_semantic_parts and processor.geometries.semantic_parts:
            for path in processor.geometries.semantic_parts:
                for child_elem in elem.iterfind(path, nsmap):
                    # 子Featureの Processor に処理を委ねる
                    for child_obj in self.process_cityobj_element(
                        child_elem, nogeom_obj
                    ):
                        if not nogeom_emitted:
                            yield nogeom_obj
                            nogeom_emitted = True
                        yield child_obj

        # ジオメトリをもたない場合は、ここで終了
        if processor.non_geometric:
            if not nogeom_emitted:
                yield nogeom_obj
                nogeom_emitted = True
            return

        # ジオメトリを読んで出力する
        lod_defs = processor.lod_list
        has_lods = processor.detect_lods(elem, nsmap)
        for lod in (4, 3, 2, 1, 0):
            if not has_lods[lod]:
                continue

            if processor.geometries.lod_n is not None:
                emission = processor.geometries.lod_n_paths
            else:
                emission = lod_defs[lod]
            if emission is None:
                continue

            # 子Featureを読む設定かどうかによってジオメトリの抽出方法を変える
            geom_paths = (
                emission.only_direct or emission.collect_all
                if self._settings.load_semantic_parts
                else emission.collect_all
            )

            if geom := parse_geometry(
                elem, geom_paths, nsmap=nsmap, appearance=appearance
            ):
                yield CityObject(
                    lod=lod,
                    type=ns.to_prefixed_name(elem.tag),
                    id=gml_id,
                    name=gml_name,
                    creation_date=creation_date,
                    termination_date=termination_date,
                    attributes=props,
                    geometry=geom,
                    processor=processor,
                    parent=parent,
                )

                if self._settings.only_highest_lod:
                    # 各Featureの最高 LoD だけ出力する設定の場合はここで離脱
                    break


class FileParser:
    def __init__(self, filename: str, settings: ParseSettings):
        self._base_dir = Path(filename).parent
        self._doc = et.parse(filename, None)
        self._settings = settings

        # ドキュメントで使われている i-UR のバージョンを検出して
        # uro: と urf: 接頭辞が指すべきXML名前空間を自動で決定する
        self._ns = Namespace.from_document_nsmap(self._doc.getroot().nsmap)
        codelists = CodelistStore(self._base_dir)

        self._parser = Parser(self._settings, ns=self._ns, codelist_store=codelists)

    def load_apperance(self, theme: Optional[str] = None):
        for app in parse_appearances(self._doc):
            self._parser.appearance = app
            break

    def count_toplevel_cityobjs(self) -> int:
        """ファイルに含まれるトップレベルのFeatureの数を返す"""
        return sum(
            1 for _ in self._doc.iterfind("./core:cityObjectMember", self._ns.nsmap)
        )

    def iter_cityobjs(self) -> Iterable[tuple[int, CityObject]]:
        """都市オブジェクトをパースして返す"""

        toplevel_count = 0
        for city_object in self._doc.iterfind(
            "./core:cityObjectMember/*", self._ns.nsmap
        ):
            for cityobj in self._parser.process_cityobj_element(
                city_object, parent=None
            ):
                yield (toplevel_count, cityobj)
            toplevel_count += 1
