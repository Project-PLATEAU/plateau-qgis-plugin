"""建築物モデル (./bldg/)"""

from .base import (
    FeatureEmission,
    FeatureEmissions,
    FeatureProcessingDefinition,
    LODDetection,
    Property,
    PropertyGroup,
)

BUILDING = FeatureProcessingDefinition(
    id="Building",
    target_elements=["bldg:Building"],
    lod_detection=LODDetection(
        lod1=["./bldg:lod1Solid"],
        lod2=["./bldg:lod2Solid"],
        lod3=["./bldg:lod3Solid"],
        lod4=["./bldg:lod4Solid", "./bldg:lod4MultiSurface"],
    ),
    property_groups=[
        PropertyGroup(
            base_element=None,
            properties=[
                Property(
                    name="usage",
                    path="./bldg:usage",
                    datatype="[]string",
                    predefined_codelist="Building_usage",
                ),
                Property(
                    name="yearOfConstruction",
                    path="./bldg:yearOfConstruction",
                    datatype="integer",
                ),
                Property(
                    name="yearOfDemolition",
                    path="./bldg:yearOfDemolition",
                    datatype="integer",
                ),
                Property(
                    name="roofType",
                    path="./bldg:roofType",
                    datatype="string",
                    predefined_codelist="Building_roofType",
                ),
                Property(
                    name="measuredHeight",
                    path="./bldg:measuredHeight",
                    datatype="double",
                ),
                Property(
                    name="storeysAboveGround",
                    path="./bldg:storeysAboveGround",
                    datatype="integer",
                ),
                Property(
                    name="storeysBelowGround",
                    path="./bldg:storeysBelowGround",
                    datatype="integer",
                ),
                # Property(
                #     name="address",
                #     path="./bldg:address",
                #     datatype="string",  # TODO: xAL をどう読むか
                # ),
            ],
        ),
        # uro:buildingIDAttribute
        PropertyGroup(
            base_element="./uro:buildingIDAttribute/uro:BuildingIDAttribute",
            properties=[
                Property(
                    name="uro:buildingID",
                    path="./uro:buildingID",
                    datatype="string",
                ),
                Property(
                    name="uro:branchID",
                    path="./uro:branchID",
                    datatype="integer",
                ),
                Property(
                    name="uro:partID",
                    path="./uro:partID",
                    datatype="integer",
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
            ],
        ),
        # uro:BuildingDetailAttribute
        PropertyGroup(
            base_element="./uro:buildingDetailAttribute/uro:BuildingDetailAttribute",
            properties=[
                Property(
                    name="uro:serialNumberOfBuildingCertification",
                    path="./uro:serialNumberOfBuildingCertification",
                    datatype="string",
                ),
                Property(
                    name="uro:siteArea",
                    path="./uro:siteArea",
                    datatype="double",
                ),
                Property(
                    name="uro:totalFloorArea",
                    path="./uro:totalFloorArea",
                    datatype="double",
                ),
                Property(
                    name="uro:buildingFootprintArea",
                    path="./uro:buildingFootprintArea",
                    datatype="double",
                ),
                Property(
                    name="uro:buildingRoofEdgeArea",
                    path="./uro:buildingRoofEdgeArea",
                    datatype="double",
                ),
                Property(
                    name="uro:developmentArea",
                    path="./uro:developmentArea",
                    datatype="double",
                ),
                Property(
                    name="uro:buildingStructureType",
                    path="./uro:buildingStructureType",
                    datatype="string",
                    predefined_codelist="BuildingDetailAttribute_buildingStructureType",
                ),
                Property(
                    name="uro:buildingStructureOrgType",
                    path="./uro:buildingStructureOrgType",
                    datatype="string",
                ),
                Property(
                    name="uro:fireproofStructureType",
                    path="./uro:fireproofStructureType",
                    datatype="string",
                    predefined_codelist="BuildingDetailAttribute_fireproofStructureType",
                ),
                Property(
                    name="uro:urbanPlanType",
                    path="./uro:urbanPlanType",
                    datatype="string",
                    predefined_codelist="BuildingDetailAttribute_urbanPlanType",
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
                    datatype="string",
                    predefined_codelist="Common_districtsAndZonesType",
                ),
                Property(
                    name="uro:landUseType",
                    path="./uro:landUseType",
                    datatype="string",
                    predefined_codelist="Common_landUseType",
                ),
                Property(
                    name="uro:reference",
                    path="./uro:reference",
                    datatype="string",
                ),
                Property(
                    name="uro:majorUsage",
                    path="./uro:majorUsage",
                    datatype="string",
                ),
                Property(
                    name="uro:majorUsage2",
                    path="./uro:majorUsage2",
                    datatype="string",
                ),
                Property(
                    name="uro:orgUsage",
                    path="./uro:orgUsage",
                    datatype="string",
                ),
                Property(
                    name="uro:orgUsage2",
                    path="./uro:orgUsage2",
                    datatype="string",
                ),
                Property(
                    name="uro:detailedUsage",
                    path="./uro:detailedUsage",
                    datatype="string",
                ),
                Property(
                    name="uro:detailedUsage2",
                    path="./uro:detailedUsage2",
                    datatype="string",
                ),
                Property(
                    name="uro:detailedUsage3",
                    path="./uro:detailedUsage3",
                    datatype="string",
                ),
                Property(
                    name="uro:groundFloorUsage",
                    path="./uro:groundFloorUsage",
                    datatype="string",
                ),
                Property(
                    name="uro:secondFloorUsage",
                    path="./uro:secondFloorUsage",
                    datatype="string",
                ),
                Property(
                    name="uro:thirdFloorUsage",
                    path="./uro:thirdFloorUsage",
                    datatype="string",
                ),
                Property(
                    name="uro:basementUsage",
                    path="./uro:basementUsage",
                    datatype="string",
                ),
                Property(
                    name="uro:basementFirstUsage",
                    path="./uro:basementFirstUsage",
                    datatype="string",
                ),
                Property(
                    name="uro:basementSecondUsage",
                    path="./uro:basementSecondUsage",
                    datatype="string",
                ),
                Property(
                    name="uro:vacancy",
                    path="./uro:vacancy",
                    datatype="string",
                    predefined_codelist="BuildingDetailAttribute_vacancy",
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
                    name="uro:buidingHeight",
                    path="./uro:buidingHeight",
                    datatype="double",
                ),
                Property(
                    name="uro:eaveHeight",
                    path="./uro:eaveHeight",
                    datatype="double",
                ),
                Property(
                    name="uro:surveyYear",
                    path="./uro:surveyYear",
                    datatype="integer",
                ),
            ],
        ),
        # uro:largeCustomerFacilityAttribute
        PropertyGroup(
            base_element="./uro:largeCustomerFacilityAttribute/uro:LargeCustomerFacilityAttribute",
            properties=[
                Property(
                    name="uro:class",
                    path="./uro:class",
                    datatype="string",
                    predefined_codelist="LargeCustomerFacilityAttribute_class",
                ),
                Property(
                    name="uro:name",
                    path="./uro:name",
                    datatype="string",
                ),
                Property(
                    name="uro:capacity",
                    path="./uro:capacity",
                    datatype="integer",
                ),
                Property(
                    name="uro:owner",
                    path="./uro:owner",
                    datatype="string",
                ),
                Property(
                    name="uro:totalFloorArea",
                    path="./uro:totalFloorArea",
                    datatype="double",
                ),
                Property(
                    name="uro:totalStoreFloorArea",
                    path="./uro:totalStoreFloorArea",
                    datatype="double",
                ),
                Property(
                    name="uro:inauguralDate",
                    path="./uro:inauguralDate",
                    datatype="date",
                ),
                Property(
                    name="uro:yearOpened",
                    path="./uro:yearOpened",
                    datatype="integer",
                ),
                Property(
                    name="uro:yearClosed",
                    path="./uro:yearClosed",
                    datatype="integer",
                ),
                Property(
                    name="uro:keyTenants",
                    path="./uro:keyTenants",
                    datatype="string",
                ),
                Property(
                    name="uro:availability",
                    path="./uro:availability",
                    datatype="boolean",
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
                    name="uro:landUseType",
                    path="./uro:landUseType",
                    datatype="[]string",
                    predefined_codelist="Common_landUseType",
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
        # uro:BuildingDataQualityAttribute
        PropertyGroup(
            base_element="./uro:buildingDataQualityAttribute/uro:BuildingDataQualityAttribute",
            properties=[
                Property(
                    name="uro:srcScale",
                    path="./uro:srcScale",
                    datatype="[]string",
                    predefined_codelist="BuildingDataQualityAttribute_srcScale",
                ),
                Property(
                    name="uro:geometrySrcDesc",
                    path="./uro:geometrySrcDesc",
                    datatype="[]string",
                    predefined_codelist="BuildingDataQualityAttribute_geometrySrcDesc",
                ),
                Property(
                    name="uro:thematicSrcDesc",
                    path="./uro:thematicSrcDesc",
                    datatype="[]string",
                    predefined_codelist="BuildingDataQualityAttribute_thematicSrcDesc",
                ),
                Property(
                    name="uro:appearanceSrcDesc",
                    path="./uro:appearanceSrcDesc",
                    datatype="[]string",
                    predefined_codelist="BuildingDataQualityAttribute_appearanceSrcDesc",
                ),
                Property(
                    name="uro:lod1HeightType",
                    path="./uro:lod1HeightType",
                    datatype="string",
                    predefined_codelist="BuildingDataQualityAttribute_lod1HeightType",
                ),
                Property(
                    name="uro:lodType",
                    path="./uro:lodType",
                    datatype="[]string",
                ),
            ],
        ),
        # TODO: uro:keyValuePairAttribute
        # TODO: uro:buildingDisasterRiskAttribute
        # (TODO: uro:ifcBuildingAttribute)
        # (TODO: uro:indoorBuildingAttribute)
        # TODO: uro:bldgFacilityTypeAttribute
        # TODO: uro:bldgFacilityIdAttribute
        # TODO: uro:bldgFacilityAttribute
        # TODO: uro:bldgDmAttribute
    ],
    emissions=FeatureEmissions(
        lod1=FeatureEmission(collect_all=[".//bldg:lod1Solid//gml:Polygon"]),
        lod2=FeatureEmission(
            collect_all=[
                ".//bldg:lod2MultiSurface//gml:Polygon",
                ".//bldg:lod2Geometry//gml:Polygon",
            ],
            only_direct=["./bldg:lod2Solid//gml:Polygon"],
        ),
        lod3=FeatureEmission(
            collect_all=[
                ".//bldg:lod3MultiSurface//gml:Polygon",
                ".//bldg:lod3Geometry//gml:Polygon",
                ".//bldg:lod3Solid//gml:Polygon",
            ],
            only_direct=["./bldg:lod3Solid//gml:Polygon"],
        ),
        lod4=FeatureEmission(
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
        semantic_parts=[  # NOTE: Room と BuildingPart はとりあえず無視している
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
        ],
    ),
)

BUILDING_BOUNDARY_SURFACE = FeatureProcessingDefinition(
    id="bldg:_BoundarySurface",
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
    property_groups=[],
    lod_detection=LODDetection(
        lod2=["./bldg:lod2MultiSurface"],
        lod3=["./bldg:lod3MultiSurface"],
        lod4=["./bldg:lod4MultiSurface"],
    ),
    emissions=FeatureEmissions(
        lod2=FeatureEmission(
            collect_all=[".//bldg:lod2MultiSurface//gml:Polygon"],
            only_direct=["./bldg:lod2MultiSurface//gml:Polygon"],
        ),
        lod3=FeatureEmission(
            collect_all=[".//bldg:lod3MultiSurface//gml:Polygon"],
            only_direct=["./bldg:lod3MultiSurface//gml:Polygon"],
        ),
        lod4=FeatureEmission(
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
    target_elements=[
        "bldg:Window",
        "bldg:Door",
    ],
    property_groups=[],
    lod_detection=LODDetection(
        lod3=["./bldg:lod3MultiSurface"],
        lod4=["./bldg:lod4MultiSurface"],
    ),
    emissions=FeatureEmissions(
        lod3=FeatureEmission(collect_all=[".//bldg:lod3MultiSurface//gml:Polygon"]),
        lod4=FeatureEmission(collect_all=[".//bldg:lod4MultiSurface//gml:Polygon"]),
    ),
)

BUILDING_INSTALLATION = FeatureProcessingDefinition(
    id="BuildingInstallation",
    target_elements=[
        "bldg:BuildingInstallation",
    ],
    property_groups=[
        PropertyGroup(
            base_element=None,
            properties=[
                Property(
                    name="class",
                    path="./bldg:class",
                    datatype="string",
                    predefined_codelist="BuildingInstallation_class",
                ),
                Property(
                    name="function",
                    path="./bldg:function",
                    datatype="[]string",
                    predefined_codelist="BuildingInstallation_function",
                ),
            ],
        )
    ],
    lod_detection=LODDetection(
        lod2=["./bldg:lod2Geometry"],
        lod3=["./bldg:lod3Geometry"],
        lod4=["./bldg:lod4Geometry"],
    ),
    emissions=FeatureEmissions(
        lod2=FeatureEmission(collect_all=[".//bldg:lod2Geometry//gml:Polygon"]),
        lod3=FeatureEmission(collect_all=[".//bldg:lod3Geometry//gml:Polygon"]),
        lod4=FeatureEmission(collect_all=[".//bldg:lod4Geometry//gml:Polygon"]),
    ),
)

BUILDING_INT_INSTALLATION = FeatureProcessingDefinition(
    id="IntBuildingInstallation",
    target_elements=[
        "bldg:IntBuildingInstallation",
    ],
    property_groups=[
        PropertyGroup(
            base_element=None,
            properties=[
                Property(
                    name="class",
                    path="./bldg:class",
                    datatype="string",
                    predefined_codelist="IntBuildingInstallation_class",
                ),
                Property(
                    name="function",
                    path="./bldg:function",
                    datatype="[]string",
                    predefined_codelist="IntBuildingInstallation_function",
                ),
            ],
        )
    ],
    lod_detection=LODDetection(
        lod2=["./bldg:lod2Geometry"],
        lod3=["./bldg:lod3Geometry"],
        lod4=["./bldg:lod4Geometry"],
    ),
    emissions=FeatureEmissions(
        lod2=FeatureEmission(collect_all=[".//bldg:lod2Geometry//gml:Polygon"]),
        lod3=FeatureEmission(collect_all=[".//bldg:lod3Geometry//gml:Polygon"]),
        lod4=FeatureEmission(collect_all=[".//bldg:lod4Geometry//gml:Polygon"]),
    ),
)
