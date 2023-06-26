"""土地利用モデル (./luse/)"""

from .base import (
    FeatureEmission,
    FeatureEmissions,
    FeatureProcessingDefinition,
    LODDetection,
    Property,
    PropertyGroup,
)

LAND_USE = FeatureProcessingDefinition(
    id="LandUse",
    target_elements=[
        "luse:LandUse",
    ],
    lod_detection=LODDetection(
        lod0=["./luse:lod0MultiSurface"],
        lod1=["./luse:lod1MultiSurface"],
    ),
    property_groups=[
        PropertyGroup(
            base_element=None,
            properties=[
                Property(
                    name="class",
                    path="./luse:class",
                    datatype="string",
                    predefined_codelist="Common_landUseType",
                ),
                Property(
                    name="usage",
                    path="./luse:usage",
                    datatype="string",
                    predefined_codelist="LandUse_usage",
                ),
            ],
        ),
        PropertyGroup(
            base_element="./uro:landUseDetailAttribute/uro:LandUseDetailAttribute",
            properties=[
                Property(
                    name="uro:id",
                    path="./uro:id",
                    datatype="string",
                ),
                Property(
                    name="uro:orgLandUse",
                    path="./uro:orgLandUse",
                    datatype="string",
                ),
                Property(
                    name="uro:nominalArea",
                    path="./uro:nominalArea",
                    datatype="double",
                ),
                Property(
                    name="uro:ownerType",
                    path="./uro:ownerType",
                    datatype="string",
                    predefined_codelist="Common_ownerType",
                ),
                Property(
                    name="uro:owner",
                    path="./uro:owner",
                    datatype="string",
                ),
                Property(
                    name="uro:areaInSquareMeter",
                    path="./uro:areaInSquareMeter",
                    datatype="double",
                ),
                Property(
                    name="uro:areaInHa",
                    path="./uro:areaInHa",
                    datatype="double",
                ),
                Property(
                    name="uro:buildingCoverageRate",
                    path="./uro:buildingCoverageRate",
                    datatype="double",
                ),
                Property(
                    name="uro:floorAreaRate",
                    path="./uro:floorAreaRate",
                    datatype="double",
                ),
                Property(
                    name="uro:specifiedBuildingCoverageRate",
                    path="./uro:specifiedBuildingCoverageRate",
                    datatype="double",
                ),
                Property(
                    name="uro:specifiedFloorAreaRate",
                    path="./uro:specifiedFloorAreaRate",
                    datatype="double",
                ),
                Property(
                    name="uro:standardFloorAreaRate",
                    path="./uro:standardFloorAreaRate",
                    datatype="double",
                ),
                Property(
                    name="uro:urbanPlanType",
                    path="./uro:urbanPlanType",
                    datatype="string",
                    predefined_codelist="Common_urbanPlanType",
                ),
                Property(
                    name="uro:areaClassificationType",
                    path="./uro:areaClassificationType",
                    datatype="string",
                    predefined_codelist="Common_areaClassificationType",
                ),
                Property(
                    name="uro:districtsAndZonesType",
                    path="./uro:districtsAndZonesType",
                    datatype="[]string",
                    predefined_codelist="Common_districtsAndZonesType",
                ),
                Property(
                    name="uro:prefecture",
                    path="./uro:prefecture",
                    datatype="string",
                    predefined_codelist="Common_prefecture",
                ),
                Property(
                    name="uro:city",
                    path="./uro:city",
                    datatype="string",
                    predefined_codelist="Common_localPublicAuthorities",
                ),
                Property(
                    name="uro:reference",
                    path="./uro:reference",
                    datatype="string",
                ),
                Property(
                    name="uro:note",
                    path="./uro:note",
                    datatype="string",
                ),
                Property(
                    name="uro:surveyYear",
                    path="./uro:surveyYear",
                    datatype="integer",
                ),
            ],
        ),
    ],
    emissions=FeatureEmissions(
        lod0=FeatureEmission(
            collect_all=[
                "./luse:lod0MultiSurface//gml:Polygon",
            ]
        ),
        lod1=FeatureEmission(
            collect_all=[
                "./luse:lod1MultiSurface//gml:Polygon",
            ]
        ),
    ),
)
