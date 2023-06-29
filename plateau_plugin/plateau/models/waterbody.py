"""水辺モデル (./wtr/) および 災害リスク (浸水) モデル (./fld/, ./htd/, ./ifld/, ./tnm/)"""

from .base import (
    FeatureEmission,
    FeatureEmissions,
    FeatureProcessingDefinition,
    LODDetection,
    Property,
    PropertyGroup,
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
    property_groups=[
        PropertyGroup(
            base_element=None,
            properties=[
                Property(
                    name="class",
                    path="./wtr:class",
                    datatype="string",
                    predefined_codelist="WaterBody_class",
                ),
                Property(
                    name="function",
                    path="./wtr:function",  # 浸水リスクモデルで使われる
                    datatype="[]string",
                    predefined_codelist="WaterBody_function",
                ),
            ],
        ),
        PropertyGroup(
            base_element="./uro:floodingRiskAttribute",
            properties=[
                # uro:WaterBodyRiverFloodingRiskAttribute
                Property(
                    name="description",
                    path="./uro:WaterBodyRiverFloodingRiskAttribute/uro:description",
                    datatype="string",
                ),
                Property(
                    name="rank",
                    path="./uro:WaterBodyRiverFloodingRiskAttribute/uro:rank",
                    datatype="string",
                    predefined_codelist="RiverFloodingRiskAttribute_rank",
                ),
                Property(
                    name="rankOrg",
                    path="./uro:WaterBodyRiverFloodingRiskAttribute/uro:rankOrg",
                    datatype="string",
                ),
                Property(
                    name="depth",
                    path="./uro:WaterBodyRiverFloodingRiskAttribute/uro:depth",
                    datatype="double",
                ),
                Property(
                    name="adminType",
                    path="./uro:WaterBodyRiverFloodingRiskAttribute/uro:adminType",
                    datatype="string",
                    predefined_codelist="RiverFloodingRiskAttribute_adminType",
                ),
                Property(
                    name="scale",
                    path="./uro:WaterBodyRiverFloodingRiskAttribute/uro:scale",
                    datatype="string",
                    predefined_codelist="RiverFloodingRiskAttribute_scale",
                ),
                Property(
                    name="duration",
                    path="./uro:WaterBodyRiverFloodingRiskAttribute/uro:duration",
                    datatype="double",
                ),
                # uro:WaterBodyHighTideRiskAttribute
                Property(
                    name="description",
                    path="./uro:WaterBodyHighTideRiskAttribute/uro:description",
                    datatype="string",
                ),
                Property(
                    name="rank",
                    path="./uro:WaterBodyHighTideRiskAttribute/uro:rank",
                    datatype="string",
                    predefined_codelist="HighTideRiskAttribute_rank",
                ),
                Property(
                    name="rankOrg",
                    path="./uro:WaterBodyHighTideRiskAttribute/uro:rankOrg",
                    datatype="string",
                ),
                Property(
                    name="depth",
                    path="./uro:WaterBodyHighTideRiskAttribute/uro:depth",
                    datatype="double",
                ),
                # uro:WaterBodyTsunamiRiskAttribute
                Property(
                    name="description",
                    path="./uro:WaterBodyTsunamiRiskAttribute/uro:description",
                    datatype="string",
                ),
                Property(
                    name="rank",
                    path="./uro:WaterBodyTsunamiRiskAttribute/uro:rank",
                    datatype="string",
                    predefined_codelist="TsunamiRiskAttribute_rank",
                ),
                Property(
                    name="rankOrg",
                    path="./uro:WaterBodyTsunamiRiskAttribute/uro:rankOrg",
                    datatype="string",
                ),
                Property(
                    name="depth",
                    path="./uro:WaterBodyTsunamiRiskAttribute/uro:depth",
                    datatype="double",
                ),
                # uro:WaterBodyHighTideRiskAttribute
                Property(
                    name="description",
                    path="./uro:WaterBodyHighTideRiskAttribute/uro:description",
                    datatype="string",
                ),
                Property(
                    name="rank",
                    path="./uro:WaterBodyHighTideRiskAttribute/uro:rank",
                    datatype="string",
                    predefined_codelist="HighTideRiskAttribute_rank",
                ),
                Property(
                    name="rankOrg",
                    path="./uro:WaterBodyHighTideRiskAttribute/uro:rankOrg",
                    datatype="string",
                ),
                Property(
                    name="depth",
                    path="./uro:WaterBodyHighTideRiskAttribute/uro:depth",
                    datatype="double",
                ),
                # uro:WaterBodyInlandFloodingRiskAttribute
                Property(
                    name="description",
                    path="./uro:WaterBodyInlandFloodingRiskAttribute/uro:description",
                    datatype="string",
                    predefined_codelist="InlandFloodingRiskAttribute_description",
                ),
                Property(
                    name="rank",
                    path="./uro:WaterBodyInlandFloodingRiskAttribute/uro:rank",
                    datatype="string",
                    predefined_codelist="InlandFloodingRiskAttribute_rank",
                ),
                Property(
                    name="rankOrg",
                    path="./uro:WaterBodyInlandFloodingRiskAttribute/uro:rankOrg",
                    datatype="string",
                ),
                Property(
                    name="depth",
                    path="./uro:WaterBodyInlandFloodingRiskAttribute/uro:depth",
                    datatype="double",
                ),
            ],
        ),
        PropertyGroup(
            base_element="./uro:waterBodyDetailAttribute/uro:WaterBodyDetailAttribute",
            properties=[
                Property(
                    name="adminType",
                    path="./uro:adminType",
                    datatype="string",
                    predefined_codelist=None,
                ),
                Property(
                    name="area",
                    path="./uro:area",
                    datatype="double",
                ),
                Property(
                    name="city",
                    path="./uro:city",
                    datatype="[]string",
                    predefined_codelist="Common_localPublicAuthorities",
                ),
                Property(
                    name="flowDirection",
                    path="./uro:flowDirection",
                    datatype="boolean",
                ),
                Property(
                    name="kana",
                    path="./uro:kana",
                    datatype="string",
                ),
                Property(
                    name="maximumDepth",
                    path="./uro:maximumDepth",
                    datatype="double",
                ),
                Property(
                    name="measurementYearMonth",
                    path="./uro:measurementYearMonth",
                    datatype="string",
                ),
                Property(
                    name="prefecture",
                    path="./uro:prefecture",
                    datatype="[]string",
                    predefined_codelist="Common_localPublicAuthorities",
                ),
                Property(
                    name="riverCode",
                    path="./uro:riverCode",
                    datatype="string",
                    predefined_codelist=None,
                ),
                Property(
                    name="waterSurfaceElevation",
                    path="./uro:waterSurfaceElevation",
                    datatype="double",
                ),
                Property(
                    name="waterSystemCode",
                    path="./uro:waterSystemCode",
                    datatype="string",
                    predefined_codelist=None,
                ),
            ],
        ),
        PropertyGroup(
            base_element="./uro:wtrFacilityIdAttribute/uro:FacilityIdAttribute",
            properties=facility_id_attribute_attrs,
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
    property_groups=[],
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
