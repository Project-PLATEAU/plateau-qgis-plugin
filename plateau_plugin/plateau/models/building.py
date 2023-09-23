"""建築物モデル (./bldg/)"""

from .base import (
    Attribute,
    AttributeGroup,
    FacilityAttributePaths,
    FeatureProcessingDefinition,
    GeometricAttribute,
    GeometricAttributes,
)

BUILDING = FeatureProcessingDefinition(
    id="bldg:Building",
    name="Building",
    target_elements=["bldg:Building"],
    attribute_groups=[
        AttributeGroup(
            base_element=None,
            attributes=[
                Attribute(
                    name="usage",
                    path="./bldg:usage",
                    datatype="[]string",
                    predefined_codelist="Building_usage",
                ),
                Attribute(
                    name="yearOfConstruction",
                    path="./bldg:yearOfConstruction",
                    datatype="integer",
                ),
                Attribute(
                    name="yearOfDemolition",
                    path="./bldg:yearOfDemolition",
                    datatype="integer",
                ),
                Attribute(
                    name="roofType",
                    path="./bldg:roofType",
                    datatype="string",
                    predefined_codelist="Building_roofType",
                ),
                Attribute(
                    name="measuredHeight",
                    path="./bldg:measuredHeight",
                    datatype="double",
                ),
                Attribute(
                    name="storeysAboveGround",
                    path="./bldg:storeysAboveGround",
                    datatype="integer",
                ),
                Attribute(
                    name="storeysBelowGround",
                    path="./bldg:storeysBelowGround",
                    datatype="integer",
                ),
                Attribute(
                    name="address",
                    path="./bldg:address",
                    datatype="xAL",
                ),
            ],
        ),
        AttributeGroup(
            base_element="./uro:buildingIDAttribute/uro:BuildingIDAttribute",
            attributes=[
                Attribute(
                    name="buildingID",
                    path="./uro:buildingID",
                    datatype="string",
                ),
                Attribute(
                    name="branchID",
                    path="./uro:branchID",
                    datatype="integer",
                ),
                Attribute(
                    name="partID",
                    path="./uro:partID",
                    datatype="integer",
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
            ],
        ),
        # TODO: これらは入れ子的データ [0..*]
        # AttributeGroup(
        #     base_element="./uro:buildingDetailAttribute/uro:BuildingDetailAttribute",
        #     attributes=[
        #         Attribute(
        #             name="serialNumberOfBuildingCertification",
        #             path="./uro:serialNumberOfBuildingCertification",
        #             datatype="string",
        #         ),
        #         Attribute(
        #             name="siteArea",
        #             path="./uro:siteArea",
        #             datatype="double",
        #         ),
        #         Attribute(
        #             name="totalFloorArea",
        #             path="./uro:totalFloorArea",
        #             datatype="double",
        #         ),
        #         Attribute(
        #             name="buildingFootprintArea",
        #             path="./uro:buildingFootprintArea",
        #             datatype="double",
        #         ),
        #         Attribute(
        #             name="buildingRoofEdgeArea",
        #             path="./uro:buildingRoofEdgeArea",
        #             datatype="double",
        #         ),
        #         Attribute(
        #             name="developmentArea",
        #             path="./uro:developmentArea",
        #             datatype="double",
        #         ),
        #         Attribute(
        #             name="buildingStructureType",
        #             path="./uro:buildingStructureType",
        #             datatype="string",
        #             predefined_codelist="BuildingDetailAttribute_buildingStructureType",
        #         ),
        #         Attribute(
        #             name="buildingStructureOrgType",
        #             path="./uro:buildingStructureOrgType",
        #             datatype="string",
        #         ),
        #         Attribute(
        #             name="fireproofStructureType",
        #             path="./uro:fireproofStructureType",
        #             datatype="string",
        #             predefined_codelist="BuildingDetailAttribute_fireproofStructureType",
        #         ),
        #         Attribute(
        #             name="urbanPlanType",
        #             path="./uro:urbanPlanType",
        #             datatype="string",
        #             predefined_codelist="Common_urbanPlanType",
        #         ),
        #         Attribute(
        #             name="areaClassificationType",
        #             path="./uro:areaClassificationType",
        #             datatype="string",
        #             predefined_codelist="Common_areaClassificationType",
        #         ),
        #         Attribute(
        #             name="districtsAndZonesType",
        #             path="./uro:districtsAndZonesType",
        #             datatype="[]string",
        #             predefined_codelist="Common_districtsAndZonesType",
        #         ),
        #         Attribute(
        #             name="landUseType",
        #             path="./uro:landUseType",
        #             datatype="string",
        #             predefined_codelist="Common_landUseType",
        #         ),
        #         Attribute(
        #             name="reference",
        #             path="./uro:reference",
        #             datatype="string",
        #         ),
        #         Attribute(
        #             name="majorUsage",
        #             path="./uro:majorUsage",
        #             datatype="string",
        #         ),
        #         Attribute(
        #             name="majorUsage2",
        #             path="./uro:majorUsage2",
        #             datatype="string",
        #         ),
        #         Attribute(
        #             name="orgUsage",
        #             path="./uro:orgUsage",
        #             datatype="string",
        #         ),
        #         Attribute(
        #             name="orgUsage2",
        #             path="./uro:orgUsage2",
        #             datatype="string",
        #         ),
        #         Attribute(
        #             name="detailedUsage",
        #             path="./uro:detailedUsage",
        #             datatype="string",
        #         ),
        #         Attribute(
        #             name="detailedUsage2",
        #             path="./uro:detailedUsage2",
        #             datatype="string",
        #         ),
        #         Attribute(
        #             name="detailedUsage3",
        #             path="./uro:detailedUsage3",
        #             datatype="string",
        #         ),
        #         Attribute(
        #             name="groundFloorUsage",
        #             path="./uro:groundFloorUsage",
        #             datatype="string",
        #         ),
        #         Attribute(
        #             name="secondFloorUsage",
        #             path="./uro:secondFloorUsage",
        #             datatype="string",
        #         ),
        #         Attribute(
        #             name="thirdFloorUsage",
        #             path="./uro:thirdFloorUsage",
        #             datatype="string",
        #         ),
        #         Attribute(
        #             name="basementUsage",
        #             path="./uro:basementUsage",
        #             datatype="string",
        #         ),
        #         Attribute(
        #             name="basementFirstUsage",
        #             path="./uro:basementFirstUsage",
        #             datatype="string",
        #         ),
        #         Attribute(
        #             name="basementSecondUsage",
        #             path="./uro:basementSecondUsage",
        #             datatype="string",
        #         ),
        #         Attribute(
        #             name="vacancy",
        #             path="./uro:vacancy",
        #             datatype="string",
        #             predefined_codelist="BuildingDetailAttribute_vacancy",
        #         ),
        #         Attribute(
        #             name="buildingCoverageRate",
        #             path="./uro:buildingCoverageRate",
        #             datatype="double",
        #         ),
        #         Attribute(
        #             name="floorAreaRate",
        #             path="./uro:floorAreaRate",
        #             datatype="double",
        #         ),
        #         Attribute(
        #             name="specifiedBuildingCoverageRate",
        #             path="./uro:specifiedBuildingCoverageRate",
        #             datatype="double",
        #         ),
        #         Attribute(
        #             name="specifiedFloorAreaRate",
        #             path="./uro:specifiedFloorAreaRate",
        #             datatype="double",
        #         ),
        #         Attribute(
        #             name="standardFloorAreaRate",
        #             path="./uro:standardFloorAreaRate",
        #             datatype="double",
        #         ),
        #         Attribute(
        #             name="buidingHeight",
        #             path="./uro:buidingHeight",
        #             datatype="double",
        #         ),
        #         Attribute(
        #             name="eaveHeight",
        #             path="./uro:eaveHeight",
        #             datatype="double",
        #         ),
        #         Attribute(
        #             name="surveyYear",
        #             path="./uro:surveyYear",
        #             datatype="integer",
        #         ),
        #     ],
        # ),
        # AttributeGroup(
        #     base_element="./uro:largeCustomerFacilityAttribute/uro:LargeCustomerFacilityAttribute",
        #     attributes=[
        #         Attribute(
        #             name="class",
        #             path="./uro:class",
        #             datatype="string",
        #             predefined_codelist="LargeCustomerFacilityAttribute_class",
        #         ),
        #         Attribute(
        #             name="name",
        #             path="./uro:name",
        #             datatype="string",
        #         ),
        #         Attribute(
        #             name="capacity",
        #             path="./uro:capacity",
        #             datatype="integer",
        #         ),
        #         Attribute(
        #             name="owner",
        #             path="./uro:owner",
        #             datatype="string",
        #         ),
        #         Attribute(
        #             name="totalFloorArea",
        #             path="./uro:totalFloorArea",
        #             datatype="double",
        #         ),
        #         Attribute(
        #             name="totalStoreFloorArea",
        #             path="./uro:totalStoreFloorArea",
        #             datatype="double",
        #         ),
        #         Attribute(
        #             name="inauguralDate",
        #             path="./uro:inauguralDate",
        #             datatype="date",
        #         ),
        #         Attribute(
        #             name="yearOpened",
        #             path="./uro:yearOpened",
        #             datatype="integer",
        #         ),
        #         Attribute(
        #             name="yearClosed",
        #             path="./uro:yearClosed",
        #             datatype="integer",
        #         ),
        #         Attribute(
        #             name="keyTenants",
        #             path="./uro:keyTenants",
        #             datatype="string",
        #         ),
        #         Attribute(
        #             name="availability",
        #             path="./uro:availability",
        #             datatype="boolean",
        #         ),
        #         Attribute(
        #             name="urbanPlanType",
        #             path="./uro:urbanPlanType",
        #             datatype="string",
        #             predefined_codelist="Common_urbanPlanType",
        #         ),
        #         Attribute(
        #             name="areaClassificationType",
        #             path="./uro:areaClassificationType",
        #             datatype="string",
        #             predefined_codelist="Common_areaClassificationType",
        #         ),
        #         Attribute(
        #             name="districtsAndZonesType",
        #             path="./uro:districtsAndZonesType",
        #             datatype="[]string",
        #             predefined_codelist="Common_districtsAndZonesType",
        #         ),
        #         Attribute(
        #             name="landUseType",
        #             path="./uro:landUseType",
        #             datatype="string",
        #             predefined_codelist="Common_landUseType",
        #         ),
        #         Attribute(
        #             name="reference",
        #             path="./uro:reference",
        #             datatype="string",
        #         ),
        #         Attribute(
        #             name="note",
        #             path="./uro:note",
        #             datatype="string",
        #         ),
        #         Attribute(
        #             name="surveyYear",
        #             path="./uro:surveyYear",
        #             datatype="integer",
        #         ),
        #     ],
        # ),
        AttributeGroup(
            base_element="./uro:buildingDataQualityAttribute/uro:BuildingDataQualityAttribute",
            attributes=[
                Attribute(
                    name="srcScale",
                    path="./uro:srcScale",
                    datatype="[]string",
                    predefined_codelist="BuildingDataQualityAttribute_srcScale",
                ),
                Attribute(
                    name="geometrySrcDesc",
                    path="./uro:geometrySrcDesc",
                    datatype="[]string",
                    predefined_codelist="BuildingDataQualityAttribute_geometrySrcDesc",
                ),
                Attribute(
                    name="thematicSrcDesc",
                    path="./uro:thematicSrcDesc",
                    datatype="[]string",
                    predefined_codelist="BuildingDataQualityAttribute_thematicSrcDesc",
                ),
                Attribute(
                    name="appearanceSrcDesc",
                    path="./uro:appearanceSrcDesc",
                    datatype="[]string",
                    predefined_codelist="BuildingDataQualityAttribute_appearanceSrcDesc",
                ),
                Attribute(
                    name="lod1HeightType",
                    path="./uro:lod1HeightType",
                    datatype="string",
                    predefined_codelist="BuildingDataQualityAttribute_lod1HeightType",
                ),
                Attribute(
                    name="lodType",
                    path="./uro:lodType",
                    datatype="[]string",
                ),
            ],
        ),
        # TODO: uro:keyValuePairAttribute
        # (TODO: uro:ifcBuildingAttribute)
        # TODO: uro:indoorBuildingAttribute
    ],
    disaster_risk_attr_conatiner_path="./uro:buildingDisasterRiskAttribute",
    dm_attr_container_path="./uro:bldgDmAttribute",
    facility_attr_paths=FacilityAttributePaths(
        facility_id="./uro:bldgFacilityIdAttribute",
        facility_types="./uro:bldgFacilityTypeAttribute",
        facility_attrs="./uro:bldgFacilityAttribute",
        large_customer_facility_attrs="./uro:largeCustomerFacilityAttribute",
    ),
    geometries=GeometricAttributes(
        lod0=GeometricAttribute(
            is2d=True,
            lod_detection=["./bldg:lod0RoofEdge", "./bldg:lod0FootPrint"],
            collect_all=[
                ".//bldg:lod0RoofEdge//gml:Polygon",
                ".//bldg:lod0FootPrint//gml:Polygon",
            ],
        ),
        lod1=GeometricAttribute(
            lod_detection=["./bldg:lod1Solid"],
            collect_all=[".//bldg:lod1Solid//gml:Polygon"],
        ),
        lod2=GeometricAttribute(
            lod_detection=["./bldg:lod2Solid"],
            collect_all=[
                ".//bldg:lod2MultiSurface//gml:Polygon",
                ".//bldg:lod2Geometry//gml:Polygon",
            ],
            only_direct=["./bldg:lod2Solid//gml:Polygon"],
        ),
        lod3=GeometricAttribute(
            lod_detection=["./bldg:lod3Solid"],
            collect_all=[
                ".//bldg:lod3MultiSurface//gml:Polygon",
                ".//bldg:lod3Geometry//gml:Polygon",
                ".//bldg:lod3Solid//gml:Polygon",
            ],
            only_direct=["./bldg:lod3Solid//gml:Polygon"],
        ),
        lod4=GeometricAttribute(
            lod_detection=["./bldg:lod4Solid", "./bldg:lod4MultiSurface"],
            collect_all=[
                ".//bldg:lod4MultiSurface//gml:Polygon",
                ".//bldg:lod4Geometry//gml:Polygon",
                ".//bldg:lod4Solid//gml:Polygon",
            ],
            only_direct=[
                "./bldg:lod4MultiSurface//gml:Polygon",
                "./bldg:lod4Solid//gml:Polygon",
            ],
        ),
        semantic_parts=[
            ".//bldg:GroundSurface",
            ".//bldg:WallSurface",
            ".//bldg:RoofSurface",
            ".//bldg:OuterCeilingSurface",
            ".//bldg:OuterFloorSurface",
            ".//bldg:ClosureSurface",
            ".//bldg:CeilingSurface",
            ".//bldg:InteriorWallSurface",
            ".//bldg:FloorSurface",
            ".//bldg:BuildingInstallation",
            ".//bldg:IntBuildingInstallation",
            ".//bldg:BuildingFurniture",
            # TODO: 現状、 bldg:Room と bldg:BuildingPart の概念は考慮していない
        ],
    ),
)

BUILDING_BOUNDARY_SURFACE = FeatureProcessingDefinition(
    id="bldg:_BoundarySurface",
    name="BoundarySurface",
    target_elements=[
        "bldg:GroundSurface",
        "bldg:WallSurface",
        "bldg:RoofSurface",
        "bldg:OuterCeilingSurface",
        "bldg:OuterFloorSurface",
        "bldg:ClosureSurface",
        "bldg:CeilingSurface",
        "bldg:InteriorWallSurface",
        "bldg:FloorSurface",
    ],
    attribute_groups=[],
    geometries=GeometricAttributes(
        lod2=GeometricAttribute(
            lod_detection=["./bldg:lod2MultiSurface"],
            collect_all=[".//bldg:lod2MultiSurface//gml:Polygon"],
            only_direct=["./bldg:lod2MultiSurface//gml:Polygon"],
        ),
        lod3=GeometricAttribute(
            lod_detection=["./bldg:lod3MultiSurface"],
            collect_all=[".//bldg:lod3MultiSurface//gml:Polygon"],
            only_direct=["./bldg:lod3MultiSurface//gml:Polygon"],
        ),
        lod4=GeometricAttribute(
            lod_detection=["./bldg:lod4MultiSurface"],
            collect_all=[".//bldg:lod4MultiSurface//gml:Polygon"],
            only_direct=["./bldg:lod4MultiSurface//gml:Polygon"],
        ),
        semantic_parts=[
            "./bldg:opening/bldg:Door",
            "./bldg:opening/bldg:Window",
        ],
    ),
)

BUILDING_OPENING = FeatureProcessingDefinition(
    id="bldg:_Opening",
    name="Opening",
    target_elements=[
        "bldg:Window",
        "bldg:Door",
    ],
    attribute_groups=[
        # TODO: uro:indoorOpeningAttribute
    ],
    geometries=GeometricAttributes(
        lod3=GeometricAttribute(
            lod_detection=["./bldg:lod3MultiSurface"],
            collect_all=[".//bldg:lod3MultiSurface//gml:Polygon"],
        ),
        lod4=GeometricAttribute(
            lod_detection=["./bldg:lod4MultiSurface"],
            collect_all=[".//bldg:lod4MultiSurface//gml:Polygon"],
        ),
    ),
)

BUILDING_INSTALLATION = FeatureProcessingDefinition(
    id="bldg:BuildingInstallation",
    name="BuildingInstallation",
    target_elements=[
        "bldg:BuildingInstallation",
    ],
    attribute_groups=[
        AttributeGroup(
            base_element=None,
            attributes=[
                Attribute(
                    name="class",
                    path="./bldg:class",
                    datatype="string",
                    predefined_codelist="BuildingInstallation_class",
                ),
                Attribute(
                    name="function",
                    path="./bldg:function",
                    datatype="[]string",
                    predefined_codelist="BuildingInstallation_function",
                ),
            ],
        )
    ],
    geometries=GeometricAttributes(
        lod2=GeometricAttribute(
            lod_detection=["./bldg:lod2Geometry"],
            collect_all=[".//bldg:lod2Geometry//gml:Polygon"],
        ),
        lod3=GeometricAttribute(
            lod_detection=["./bldg:lod3Geometry"],
            collect_all=[".//bldg:lod3Geometry//gml:Polygon"],
        ),
        lod4=GeometricAttribute(
            lod_detection=["./bldg:lod4Geometry"],
            collect_all=[".//bldg:lod4Geometry//gml:Polygon"],
        ),
    ),
)

BUILDING_INT_INSTALLATION = FeatureProcessingDefinition(
    id="bldg:IntBuildingInstallation",
    name="IntBuildingInstallation",
    target_elements=["bldg:IntBuildingInstallation"],
    attribute_groups=[
        AttributeGroup(
            base_element=None,
            attributes=[
                Attribute(
                    name="class",
                    path="./bldg:class",
                    datatype="string",
                    predefined_codelist="IntBuildingInstallation_class",
                ),
                Attribute(
                    name="function",
                    path="./bldg:function",
                    datatype="[]string",
                    predefined_codelist="IntBuildingInstallation_function",
                ),
            ],
        ),
        # TODO: uro:indoorInstallationAttribute
    ],
    geometries=GeometricAttributes(
        lod2=GeometricAttribute(
            lod_detection=["./bldg:lod2Geometry"],
            collect_all=[".//bldg:lod2Geometry//gml:Polygon"],
        ),
        lod3=GeometricAttribute(
            lod_detection=["./bldg:lod3Geometry"],
            collect_all=[".//bldg:lod3Geometry//gml:Polygon"],
        ),
        lod4=GeometricAttribute(
            lod_detection=["./bldg:lod4Geometry"],
            collect_all=[".//bldg:lod4Geometry//gml:Polygon"],
        ),
    ),
)


BUILDING_FURNITURE = FeatureProcessingDefinition(
    id="bldg:BuildingFurniture",
    name="BuildingFurniture",
    target_elements=["bldg:BuildingFurniture"],
    attribute_groups=[
        AttributeGroup(
            base_element=None,
            attributes=[
                Attribute(
                    name="class",
                    path="./bldg:class",
                    datatype="string",
                    predefined_codelist="BuildingFurniture_class",
                ),
                Attribute(
                    name="function",
                    path="./bldg:function",
                    datatype="[]string",
                    predefined_codelist="BuildingFurniture_function",
                ),
            ],
        ),
        # TODO: uro:indoorFurnitureAttribute
    ],
    geometries=GeometricAttributes(
        lod4=GeometricAttribute(
            lod_detection=["./bldg:lod4Geometry"],
            collect_all=[".//bldg:lod4Geometry//gml:Polygon"],
        ),
    ),
)
