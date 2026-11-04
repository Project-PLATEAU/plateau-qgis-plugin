"""PLATEAU CityGML の XML名前空間を扱う"""

from __future__ import annotations

import re

BASE_NS = {
    # GML
    "gml": "http://www.opengis.net/gml",
    # CityGML 2.0
    "core": "http://www.opengis.net/citygml/2.0",
    "app": "http://www.opengis.net/citygml/appearance/2.0",
    "bldg": "http://www.opengis.net/citygml/building/2.0",
    "brid": "http://www.opengis.net/citygml/bridge/2.0",
    "dem": "http://www.opengis.net/citygml/relief/2.0",
    "frn": "http://www.opengis.net/citygml/cityfurniture/2.0",
    "gen": "http://www.opengis.net/citygml/generics/2.0",
    "grp": "http://www.opengis.net/citygml/cityobjectgroup/2.0",
    "luse": "http://www.opengis.net/citygml/landuse/2.0",
    "tran": "http://www.opengis.net/citygml/transportation/2.0",
    "veg": "http://www.opengis.net/citygml/vegetation/2.0",
    "wtr": "http://www.opengis.net/citygml/waterbody/2.0",
    "tun": "http://www.opengis.net/citygml/tunnel/2.0",
    # i-UR
    "uro14": "http://www.kantei.go.jp/jp/singi/tiiki/toshisaisei/itoshisaisei/iur/uro/1.4",
    "urf14": "http://www.kantei.go.jp/jp/singi/tiiki/toshisaisei/itoshisaisei/iur/urf/1.4",
    "uro15": "https://www.chisou.go.jp/tiiki/toshisaisei/itoshisaisei/iur/uro/1.5",
    "urf15": "https://www.chisou.go.jp/tiiki/toshisaisei/itoshisaisei/iur/urf/1.5",
    "uro2": "https://www.geospatial.jp/iur/uro/2.0",
    "urf2": "https://www.geospatial.jp/iur/urf/2.0",
    "uro3": "https://www.geospatial.jp/iur/uro/3.0",
    "uro31": "https://www.geospatial.jp/iur/uro/3.1",
    "uro32": "https://www.geospatial.jp/iur/uro/3.2",
    "urf3": "https://www.geospatial.jp/iur/urf/3.0",
}
"""XML Namespaces used in PLATEAU 3D City Models"""


class Namespace:
    """PLATEAU関連の XML Namespaces や、それらの標準的な prefix を管理する

    特に、uro, urf のバージョン (2 or 3) が配布物ごとに異なることに対応する役目をする。
    """

    def __init__(self, update: dict) -> None:
        self.nsmap: dict[str, str] = dict(**BASE_NS, **update)
        self.inverted = {v: k for k, v in self.nsmap.items()}

    @classmethod
    def from_document_nsmap(
        cls: type[Namespace], src_nsmap: dict[str, str]
    ) -> Namespace:
        """XML文書をもとに、接頭辞と名前空間の対応を作成する

        特に、与えられた文書において uro および urf 接頭辞が指すべきXML名前空間を特定する
        """
        _ns_update = {}
        for ns in src_nsmap.values():
            if ns.startswith(
                (
                    "https://www.geospatial.jp/iur/uro/",
                    "http://www.kantei.go.jp/jp/singi/tiiki/toshisaisei/itoshisaisei/iur/uro/",
                    "https://www.chisou.go.jp/tiiki/toshisaisei/itoshisaisei/iur/uro/",
                )
            ):
                _ns_update["uro"] = ns
            elif ns.startswith(
                (
                    "https://www.geospatial.jp/iur/urf/",
                    "http://www.kantei.go.jp/jp/singi/tiiki/toshisaisei/itoshisaisei/iur/urf/",
                    "https://www.chisou.go.jp/tiiki/toshisaisei/itoshisaisei/iur/urf/",
                )
            ):
                _ns_update["urf"] = ns

        _ns_update.setdefault("uro", "https://www.geospatial.jp/iur/uro/3.0")
        _ns_update.setdefault("urf", "https://www.geospatial.jp/iur/urf/3.0")
        return cls(_ns_update)

    def to_qualified_name(self, prefixed_name: str) -> str:
        """接頭辞を使ったタグ名を、名前空間を使ったタグ名に変換する

        gml:Polygon -> {http://www.opengis.net/gml}Polygon
        """
        return re.sub(
            r"^(.+?):()", lambda m: "{" + self.nsmap[m.group(1)] + "}", prefixed_name
        )

    def to_prefixed_name(self, qualified_name: str) -> str:
        """名前空間を使ったタグ名を、接頭辞を使ったタグ名に変換する

        {http://www.opengis.net/gml}Polygon -> gml:Polygon
        """
        return re.sub(
            r"^{([^}]+)}", lambda m: f"{self.inverted[m.group(1)]}:", qualified_name
        )
