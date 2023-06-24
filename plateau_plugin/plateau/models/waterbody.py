"""水辺モデル および 災害リスク (浸水) モデル"""

from .base import (
    FeatureEmission,
    FeatureEmissions,
    FeatureProcessingDefinition,
    LODDetection,
    Property,
    PropertyGroup,
)

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
                    codelist="WaterBody_class",
                ),
                Property(
                    name="function",
                    path="./wtr:function",
                    datatype="[]string",
                    codelist="WaterBody_function",
                ),
            ],
        ),
        PropertyGroup(
            base_element="./uro:floodingRiskAttribute",
            properties=[
                # uro:WaterBodyRiverFloodingRiskAttribute
                Property(
                    name="uro:description",
                    path="./uro:WaterBodyRiverFloodingRiskAttribute/uro:description",
                    datatype="string",
                ),
                Property(
                    name="uro:rank",
                    path="./uro:WaterBodyRiverFloodingRiskAttribute/uro:rank",
                    datatype="string",
                    codelist="RiverFloodingRiskAttribute_rank",
                ),
                Property(
                    name="uro:rankOrg",
                    path="./uro:WaterBodyRiverFloodingRiskAttribute/uro:rankOrg",
                    datatype="string",
                ),
                Property(
                    name="uro:depth",
                    path="./uro:WaterBodyRiverFloodingRiskAttribute/uro:depth",
                    datatype="double",
                ),
                Property(
                    name="uro:adminType",
                    path="./uro:WaterBodyRiverFloodingRiskAttribute/uro:adminType",
                    datatype="string",
                    codelist="RiverFloodingRiskAttribute_adminType",
                ),
                Property(
                    name="uro:scale",
                    path="./uro:WaterBodyRiverFloodingRiskAttribute/uro:scale",
                    datatype="string",
                    codelist="RiverFloodingRiskAttribute_scale",
                ),
                # uro:WaterBodyHighTideRiskAttribute
                Property(
                    name="uro:description",
                    path="./uro:WaterBodyHighTideRiskAttribute/uro:description",
                    datatype="string",
                ),
                Property(
                    name="uro:rank",
                    path="./uro:WaterBodyHighTideRiskAttribute/uro:rank",
                    datatype="string",
                    codelist="HighTideRiskAttribute_rank",
                ),
                Property(
                    name="uro:rankOrg",
                    path="./uro:WaterBodyHighTideRiskAttribute/uro:rankOrg",
                    datatype="string",
                ),
                Property(
                    name="uro:depth",
                    path="./uro:WaterBodyHighTideRiskAttribute/uro:depth",
                    datatype="double",
                ),
                # uro:WaterBodyTsunamiRiskAttribute
                Property(
                    name="uro:description",
                    path="./uro:WaterBodyTsunamiRiskAttribute/uro:description",
                    datatype="string",
                ),
                Property(
                    name="uro:rank",
                    path="./uro:WaterBodyTsunamiRiskAttribute/uro:rank",
                    datatype="string",
                    codelist="TsunamiRiskAttribute_rank",
                ),
                Property(
                    name="uro:rankOrg",
                    path="./uro:WaterBodyTsunamiRiskAttribute/uro:rankOrg",
                    datatype="string",
                ),
                Property(
                    name="uro:depth",
                    path="./uro:WaterBodyTsunamiRiskAttribute/uro:depth",
                    datatype="double",
                ),
                # uro:WaterBodyHighTideRiskAttribute
                Property(
                    name="uro:description",
                    path="./uro:WaterBodyHighTideRiskAttribute/uro:description",
                    datatype="string",
                ),
                Property(
                    name="uro:rank",
                    path="./uro:WaterBodyHighTideRiskAttribute/uro:rank",
                    datatype="string",
                    codelist="HighTideRiskAttribute_rank",
                ),
                Property(
                    name="uro:rankOrg",
                    path="./uro:WaterBodyHighTideRiskAttribute/uro:rankOrg",
                    datatype="string",
                ),
                Property(
                    name="uro:depth",
                    path="./uro:WaterBodyHighTideRiskAttribute/uro:depth",
                    datatype="double",
                ),
                # uro:WaterBodyInlandFloodingRiskAttribute
                Property(
                    name="uro:description",
                    path="./uro:WaterBodyInlandFloodingRiskAttribute/uro:description",
                    datatype="string",
                    codelist="InlandFloodingRiskAttribute_description",
                ),
                Property(
                    name="uro:rank",
                    path="./uro:WaterBodyInlandFloodingRiskAttribute/uro:rank",
                    datatype="string",
                    codelist="InlandFloodingRiskAttribute_rank",
                ),
                Property(
                    name="uro:rankOrg",
                    path="./uro:WaterBodyInlandFloodingRiskAttribute/uro:rankOrg",
                    datatype="string",
                ),
            ],
        ),
    ],
    emissions=FeatureEmissions(
        lod1=FeatureEmission(
            collect_all=[
                "./wtr:lod1MultiSurface//gml:Polygon",
            ]
        ),
        lod2=FeatureEmission(
            collect_all=[
                ".//wtr:lod2MultiSurface//gml:Polygon",
            ]
        ),
        lod3=FeatureEmission(
            collect_all=[
                ".//wtr:lod3MultiSurface//gml:Polygon",
            ]
        ),
        # semantic_parts=[
        #      ".//wtr:WaterSurface",
        #      ".//wtr:WaterGroundSurface",
        #      ".//wtr:WaterClosureSurface",
        # ]
    ),
)
