"""土地利用モデル (./luse/)"""

from .base import (
    Attribute,
    AttributeGroup,
    FacilityAttributePaths,
    FeatureProcessingDefinition,
    GeometricAttribute,
    GeometricAttributes,
)

LAND_USE = FeatureProcessingDefinition(
    id="luse:LandUse",
    name="LandUse",
    target_elements=["luse:LandUse"],
    attribute_groups=[
        AttributeGroup(
            base_element=None,
            attributes=[
                Attribute(
                    name="class",
                    path="./luse:class",
                    datatype="string",
                    predefined_codelist="Common_landUseType",
                ),
                Attribute(
                    name="usage",
                    path="./luse:usage",
                    datatype="string",
                    predefined_codelist="LandUse_usage",
                ),
            ],
        ),
        AttributeGroup(
            base_element="./uro:landUseDetailAttribute/uro:LandUseDetailAttribute",
            attributes=[
                Attribute(
                    name="uro:id",
                    path="./uro:id",
                    datatype="string",
                ),
                Attribute(
                    name="orgLandUse",
                    path="./uro:orgLandUse",
                    datatype="string",
                ),
                Attribute(
                    name="nominalArea",
                    path="./uro:nominalArea",
                    datatype="double",
                ),
                Attribute(
                    name="ownerType",
                    path="./uro:ownerType",
                    datatype="string",
                    predefined_codelist="Common_ownerType",
                ),
                Attribute(
                    name="owner",
                    path="./uro:owner",
                    datatype="string",
                ),
                Attribute(
                    name="areaInSquareMeter",
                    path="./uro:areaInSquareMeter",
                    datatype="double",
                ),
                Attribute(
                    name="areaInHa",
                    path="./uro:areaInHa",
                    datatype="double",
                ),
                Attribute(
                    name="buildingCoverageRate",
                    path="./uro:buildingCoverageRate",
                    datatype="double",
                ),
                Attribute(
                    name="floorAreaRate",
                    path="./uro:floorAreaRate",
                    datatype="double",
                ),
                Attribute(
                    name="specifiedBuildingCoverageRate",
                    path="./uro:specifiedBuildingCoverageRate",
                    datatype="double",
                ),
                Attribute(
                    name="specifiedFloorAreaRate",
                    path="./uro:specifiedFloorAreaRate",
                    datatype="double",
                ),
                Attribute(
                    name="standardFloorAreaRate",
                    path="./uro:standardFloorAreaRate",
                    datatype="double",
                ),
                Attribute(
                    name="urbanPlanType",
                    path="./uro:urbanPlanType",
                    datatype="string",
                    predefined_codelist="Common_urbanPlanType",
                ),
                Attribute(
                    name="areaClassificationType",
                    path="./uro:areaClassificationType",
                    datatype="string",
                    predefined_codelist="Common_areaClassificationType",
                ),
                Attribute(
                    name="districtsAndZonesType",
                    path="./uro:districtsAndZonesType",
                    datatype="[]string",
                    predefined_codelist="Common_districtsAndZonesType",
                ),
                Attribute(
                    name="prefecture",
                    path="./uro:prefecture",
                    datatype="string",
                    predefined_codelist="Common_localPublicAuthorities",
                ),
                Attribute(
                    name="city",
                    path="./uro:city",
                    datatype="string",
                    predefined_codelist="Common_localPublicAuthorities",
                ),
                Attribute(
                    name="reference",
                    path="./uro:reference",
                    datatype="string",
                ),
                Attribute(
                    name="note",
                    path="./uro:note",
                    datatype="string",
                ),
                Attribute(
                    name="surveyYear",
                    path="./uro:surveyYear",
                    datatype="integer",
                ),
            ],
        ),
    ],
    dm_attr_container_path="./uro:luseDmAttribute",
    facility_attr_paths=FacilityAttributePaths(
        facility_id="./uro:luseFacilityIdAttribute",
        facility_types="./uro:luseFacilityTypeAttribute",
        facility_attrs="./uro:luseFacilityAttribute",
    ),
    geometries=GeometricAttributes(
        lod1=GeometricAttribute(
            is2d=True,
            lod_detection=[
                "./luse:lod0MultiSurface",  # NOTE: PLATEAU 2.0 compatibility
                "./luse:lod1MultiSurface",
            ],
            collect_all=[
                "./luse:lod0MultiSurface//gml:Polygon"  # NOTE: PLATEAU 2.0 compatibility
                "./luse:lod1MultiSurface//gml:Polygon"
            ],
        ),
    ),
)
