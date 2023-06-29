"""水辺モデル (./wtr/) および 災害リスク (浸水) モデル (./fld/, ./htd/, ./ifld/, ./tnm/)"""

from .base import (
    Attribute,
    AttributeGroup,
    FeatureEmission,
    FeatureEmissions,
    FeatureProcessingDefinition,
    LODDetection,
)
from .common import facility_id_attribute_attrs

WATER_BODY = FeatureProcessingDefinition(
    id="WaterBody",
    target_elements=[
        "wtr:WaterBody",
    ],
    lod_detection=LODDetection(
        lod1=["./wtr:lod1MultiSurface"],
        lod2=["./wtr:lod2Solid"],
        lod3=["./wtr:lod3Solid"],
    ),
    attribute_groups=[
        AttributeGroup(
            base_element=None,
            attributes=[
                Attribute(
                    name="class",
                    path="./wtr:class",
                    datatype="string",
                    predefined_codelist="WaterBody_class",
                ),
                Attribute(
                    name="function",
                    path="./wtr:function",  # 浸水リスクモデルで使われる
                    datatype="[]string",
                    predefined_codelist="WaterBody_function",
                ),
            ],
        ),
        AttributeGroup(
            base_element="./uro:floodingRiskAttribute/uro:WaterBodyRiverFloodingRiskAttribute",
            attributes=[
                Attribute(
                    name="description",
                    path="./uro:description",
                    datatype="string",
                ),
                Attribute(
                    name="rank",
                    path="./uro:rank",
                    datatype="string",
                    predefined_codelist="RiverFloodingRiskAttribute_rank",
                ),
                Attribute(
                    name="rankOrg",
                    path="./uro:rankOrg",
                    datatype="string",
                ),
                Attribute(
                    name="depth",
                    path="./uro:depth",
                    datatype="double",
                ),
                Attribute(
                    name="adminType",
                    path="./uro:adminType",
                    datatype="string",
                    predefined_codelist="RiverFloodingRiskAttribute_adminType",
                ),
                Attribute(
                    name="scale",
                    path="./uro:scale",
                    datatype="string",
                    predefined_codelist="RiverFloodingRiskAttribute_scale",
                ),
                Attribute(
                    name="duration",
                    path="./uro:duration",
                    datatype="double",
                ),
            ],
        ),
        AttributeGroup(
            base_element="./uro:floodingRiskAttribute/uro:WaterBodyHighTideRiskAttribute",
            attributes=[
                Attribute(
                    name="description",
                    path="./uro:description",
                    datatype="string",
                ),
                Attribute(
                    name="rank",
                    path="./uro:rank",
                    datatype="string",
                    predefined_codelist="HighTideRiskAttribute_rank",
                ),
                Attribute(
                    name="rankOrg",
                    path="./uro:rankOrg",
                    datatype="string",
                ),
                Attribute(
                    name="depth",
                    path="./uro:depth",
                    datatype="double",
                ),
            ],
        ),
        AttributeGroup(
            base_element="./uro:floodingRiskAttribute/uro:WaterBodyTsunamiRiskAttribute",
            attributes=[
                Attribute(
                    name="description",
                    path="./uro:description",
                    datatype="string",
                ),
                Attribute(
                    name="rank",
                    path="./uro:rank",
                    datatype="string",
                    predefined_codelist="TsunamiRiskAttribute_rank",
                ),
                Attribute(
                    name="rankOrg",
                    path="./uro:rankOrg",
                    datatype="string",
                ),
                Attribute(
                    name="depth",
                    path="./uro:depth",
                    datatype="double",
                ),
            ],
        ),
        AttributeGroup(
            base_element="./uro:floodingRiskAttribute/uro:WaterBodyHighTideRiskAttribute",
            attributes=[
                Attribute(
                    name="description",
                    path="./uro:description",
                    datatype="string",
                ),
                Attribute(
                    name="rank",
                    path="./uro:rank",
                    datatype="string",
                    predefined_codelist="HighTideRiskAttribute_rank",
                ),
                Attribute(
                    name="rankOrg",
                    path="./uro:rankOrg",
                    datatype="string",
                ),
                Attribute(
                    name="depth",
                    path="./uro:depth",
                    datatype="double",
                ),
            ],
        ),
        AttributeGroup(
            base_element="./uro:floodingRiskAttribute/uro:WaterBodyInlandFloodingRiskAttribute",
            attributes=[
                Attribute(
                    name="description",
                    path="./uro:description",
                    datatype="string",
                    predefined_codelist=None,
                ),
                Attribute(
                    name="rank",
                    path="./uro:rank",
                    datatype="string",
                    predefined_codelist="InlandFloodingRiskAttribute_rank",
                ),
                Attribute(
                    name="rankOrg",
                    path="./uro:rankOrg",
                    datatype="string",
                ),
                Attribute(
                    name="depth",
                    path="./uro:depth",
                    datatype="double",
                ),
            ],
        ),
        AttributeGroup(
            base_element="./uro:waterBodyDetailAttribute/uro:WaterBodyDetailAttribute",
            attributes=[
                Attribute(
                    name="adminType",
                    path="./uro:adminType",
                    datatype="string",
                    predefined_codelist=None,
                ),
                Attribute(
                    name="area",
                    path="./uro:area",
                    datatype="double",
                ),
                Attribute(
                    name="city",
                    path="./uro:city",
                    datatype="[]string",
                    predefined_codelist="Common_localPublicAuthorities",
                ),
                Attribute(
                    name="flowDirection",
                    path="./uro:flowDirection",
                    datatype="boolean",
                ),
                Attribute(
                    name="kana",
                    path="./uro:kana",
                    datatype="string",
                ),
                Attribute(
                    name="maximumDepth",
                    path="./uro:maximumDepth",
                    datatype="double",
                ),
                Attribute(
                    name="measurementYearMonth",
                    path="./uro:measurementYearMonth",
                    datatype="string",
                ),
                Attribute(
                    name="prefecture",
                    path="./uro:prefecture",
                    datatype="[]string",
                    predefined_codelist="Common_localPublicAuthorities",
                ),
                Attribute(
                    name="riverCode",
                    path="./uro:riverCode",
                    datatype="string",
                    predefined_codelist=None,
                ),
                Attribute(
                    name="waterSurfaceElevation",
                    path="./uro:waterSurfaceElevation",
                    datatype="double",
                ),
                Attribute(
                    name="waterSystemCode",
                    path="./uro:waterSystemCode",
                    datatype="string",
                    predefined_codelist=None,
                ),
            ],
        ),
        AttributeGroup(
            base_element="./uro:wtrFacilityIdAttribute/uro:FacilityIdAttribute",
            attributes=facility_id_attribute_attrs,
        ),
        # TODO: uro:wtrDmAttribute
        # TODO: uro:wtrFacilityTypeAttribute
        # TODO: uro:wtrFacilityAttribute
    ],
    emissions=FeatureEmissions(
        lod1=FeatureEmission(
            collect_all=[
                "./wtr:lod1MultiSurface//gml:Polygon",
            ],
            only_direct=[
                "./wtr:lod1MultiSurface//gml:Polygon",
            ],
        ),
        lod2=FeatureEmission(
            collect_all=[
                ".//wtr:lod2Surface//gml:Polygon",
            ],
            only_direct=[
                "./wtr:lod2Surface//gml:Polygon",
            ],
        ),
        lod3=FeatureEmission(
            collect_all=[
                ".//wtr:lod3Surface//gml:Polygon",
            ],
            only_direct=[
                "./wtr:lod3Surface//gml:Polygon",
            ],
        ),
        semantic_parts=[
            ".//wtr:WaterSurface",
            ".//wtr:WaterGroundSurface",
            ".//wtr:WaterClosureSurface",
        ],
    ),
)

WATER_BOUNDARY_SURFACE = FeatureProcessingDefinition(
    id="WaterBoundarySurface",
    target_elements=[
        "wtr:WaterSurface",
        "wtr:WaterGroundSurface",
        "wtr:WaterClosureSurface",
    ],
    lod_detection=LODDetection(
        lod2=["./wtr:lod2Surface"],
        lod3=["./wtr:lod3Surface"],
    ),
    attribute_groups=[],
    emissions=FeatureEmissions(
        lod2=FeatureEmission(
            collect_all=[
                "./wtr:lod2Surface//gml:Polygon",
            ]
        ),
        lod3=FeatureEmission(
            collect_all=[
                "./wtr:lod3Surface//gml:Polygon",
            ]
        ),
    ),
)
