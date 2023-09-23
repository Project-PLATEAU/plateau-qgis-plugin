"""交通モデル 道路 (./tran/) 鉄道 (./rwy/) 徒歩道 (./trk/) 広場 (./squr/) 航路 (./wwy/)"""

from .base import (
    Attribute,
    AttributeGroup,
    FacilityAttributePaths,
    FeatureProcessingDefinition,
    GeometricAttribute,
    GeometricAttributes,
)

_transportation_data_quality_attribute = [
    Attribute(
        name="srcScale",
        path="./uro:srcScale",
        datatype="[]string",
        predefined_codelist="RoadDataQualityAttribute_srcScale",
    ),
    Attribute(
        name="geometrySrcDesc",
        path="./uro:geometrySrcDesc",
        datatype="[]string",
        predefined_codelist="RoadDataQualityAttribute_geometrySrcDesc",
    ),
    Attribute(
        name="thematicSrcDesc",
        path="./uro:thematicSrcDesc",
        datatype="[]string",
        predefined_codelist="RoadDataQualityAttribute_thematicSrcDesc",
    ),
    Attribute(
        name="appearanceSrcDesc",
        path="./uro:appearanceSrcDesc",
        datatype="[]string",
        predefined_codelist="RoadDataQualityAttribute_appearanceSrcDesc",
    ),
    Attribute(
        name="lodType",
        path="./uro:lodType",
        datatype="[]string",
        predefined_codelist="Road_lodType",
    ),
]

ROAD = FeatureProcessingDefinition(
    id="tran:Road",
    name="Road",
    target_elements=["tran:Road"],
    attribute_groups=[
        AttributeGroup(
            base_element=None,
            attributes=[
                Attribute(
                    name="class",
                    path="./tran:class",
                    datatype="string",
                    predefined_codelist="TransportationComplex_class",
                ),
                Attribute(
                    name="function",
                    path="./tran:function",
                    datatype="[]string",
                    predefined_codelist="Road_function",
                ),
                Attribute(
                    name="usage",
                    path="./tran:usage",
                    datatype="[]string",
                    predefined_codelist="Road_usage",
                ),
            ],
        ),
        AttributeGroup(
            base_element="./uro:roadStructureAttribute/uro:RoadStructureAttribute",
            attributes=[
                Attribute(
                    name="width",
                    path="./uro:width",
                    datatype="double",
                ),
                Attribute(
                    name="widthType",
                    path="./uro:widthType",
                    datatype="string",
                    predefined_codelist="RoadStructureAttribute_widthType",
                ),
                Attribute(
                    name="numberOfLanes",
                    path="./uro:numberOfLanes",
                    datatype="integer",
                ),
                Attribute(
                    name="sectionType",
                    path="./uro:sectionType",
                    datatype="string",
                    predefined_codelist="RoadStructureAttribute_sectionType",
                ),
            ],
        ),
        AttributeGroup(
            base_element="./uro:trafficVolumeAttribute/uro:TrafficVolumeAttribute",
            attributes=[
                Attribute(
                    name="averageInboundTravelSpeedInCongestion",
                    path="./uro:averageInboundTravelSpeedInCongestion",
                    datatype="double",
                ),
                Attribute(
                    name="averageInboundTravelSpeedNotCongestion",
                    path="./uro:averageInboundTravelSpeedNotCongestion",
                    datatype="double",
                ),
                Attribute(
                    name="averageOutboundTravelSpeedInCongestion",
                    path="./uro:averageOutboundTravelSpeedInCongestion",
                    datatype="double",
                ),
                Attribute(
                    name="averageOutboundTravelSpeedNotCongestion",
                    path="./uro:averageOutboundTravelSpeedNotCongestion",
                    datatype="double",
                ),
                Attribute(
                    name="averageTravelSpeedInCongestion",
                    path="./uro:averageTravelSpeedInCongestion",
                    datatype="double",
                ),
                Attribute(
                    name="congestionRate",
                    path="./uro:congestionRate",
                    datatype="double",
                ),
                Attribute(
                    name="largeVehicleRate",
                    path="./uro:largeVehicleRate",
                    datatype="double",
                ),
                Attribute(
                    name="observationPointName",
                    path="./uro:observationPointName",
                    datatype="string",
                ),
                Attribute(
                    name="reference",
                    path="./uro:reference",
                    datatype="string",
                ),
                Attribute(
                    name="routeName",
                    path="./uro:routeName",
                    datatype="string",
                ),
                Attribute(
                    name="sectionID",
                    path="./uro:sectionID",
                    datatype="string",
                ),
                Attribute(
                    name="surveyYear",
                    path="./uro:surveyYear",
                    datatype="integer",
                ),
                Attribute(
                    name="weekday12hourTrafficVolume",
                    path="./uro:weekday12hourTrafficVolume",
                    datatype="integer",
                ),
                Attribute(
                    name="weekday24hourTrafficVolume",
                    path="./uro:weekday24hourTrafficVolume",
                    datatype="integer",
                ),
            ],
        ),
        AttributeGroup(
            base_element="./uro:tranDataQualityAttribute/uro:TransportationDataQualityAttribute",
            attributes=_transportation_data_quality_attribute,
        ),
    ],
    dm_attr_container_path="./uro:tranDmAttribute",
    facility_attr_paths=FacilityAttributePaths(
        facility_id="./uro:tranFacilityIdAttribute",
        facility_types="./uro:tranFacilityTypeAttribute",
        facility_attrs="./uro:tranFacilityAttribute",
    ),
    geometries=GeometricAttributes(
        lod0=GeometricAttribute(
            is2d=True,
            lod_detection=["./tran:lod0Network"],
            collect_all=["./tran:lod0Network//gml:LineString"],
        ),
        lod1=GeometricAttribute(
            is2d=True,
            lod_detection=["./tran:lod1MultiSurface"],
            collect_all=["./tran:lod1MultiSurface//gml:Polygon"],
            only_direct=["./tran:lod1MultiSurface//gml:Polygon"],
        ),
        lod2=GeometricAttribute(
            is2d=True,
            lod_detection=["./tran:lod2MultiSurface"],
            collect_all=[".//tran:lod2MultiSurface//gml:Polygon"],
            only_direct=["./tran:lod2MultiSurface//gml:Polygon"],
        ),
        lod3=GeometricAttribute(
            lod_detection=["./tran:lod3MultiSurface"],
            collect_all=[".//tran:lod3MultiSurface//gml:Polygon"],
            only_direct=["./tran:lod3MultiSurface//gml:Polygon"],
        ),
        semantic_parts=[
            "./tran:trafficArea/tran:TrafficArea",
            "./tran:auxiliaryTrafficArea/tran:AuxiliaryTrafficArea",
        ],
    ),
)

RAILWAY = FeatureProcessingDefinition(
    id="tran:Railway",
    name="Railway",
    target_elements=["tran:Railway"],
    attribute_groups=[
        AttributeGroup(
            base_element=None,
            attributes=[
                Attribute(
                    name="class",
                    path="./tran:class",
                    datatype="string",
                    predefined_codelist="TransportationComplex_class",
                ),
                Attribute(
                    name="function",
                    path="./tran:function",
                    datatype="[]string",
                    predefined_codelist="Railway_function",
                ),
            ],
        ),
        AttributeGroup(
            base_element="./uro:railwayRouteAttribute/uro:RailwayRouteAttribute",
            attributes=[
                Attribute(
                    name="operatorType",
                    path="./uro:operatorType",
                    datatype="string",
                    predefined_codelist="RailwayRouteAttribute_operatorType",
                ),
                Attribute(
                    name="operator",
                    path="./uro:operator",
                    datatype="string",
                ),
                Attribute(
                    name="alternativeName",
                    path="./uro:alternativeName",
                    datatype="[]string",
                ),
                Attribute(
                    name="startStation",
                    path="./uro:startStation",
                    datatype="string",
                ),
                Attribute(
                    name="endStation",
                    path="./uro:endStation",
                    datatype="string",
                ),
            ],
        ),
        AttributeGroup(
            base_element="./uro:tranDataQualityAttribute/uro:TransportationDataQualityAttribute",
            attributes=_transportation_data_quality_attribute,
        ),
    ],
    dm_attr_container_path="./uro:tranDmAttribute",
    facility_attr_paths=FacilityAttributePaths(
        facility_id="./uro:tranFacilityIdAttribute",
        facility_types="./uro:tranFacilityTypeAttribute",
        facility_attrs="./uro:tranFacilityAttribute",
    ),
    geometries=GeometricAttributes(
        lod0=GeometricAttribute(
            is2d=True,
            lod_detection=["./tran:lod0Network"],
            collect_all=["./tran:lod0Network//gml:LineString"],
        ),
        lod1=GeometricAttribute(
            is2d=True,
            lod_detection=["./tran:lod1MultiSurface"],
            collect_all=["./tran:lod1MultiSurface//gml:Polygon"],
            only_direct=["./tran:lod1MultiSurface//gml:Polygon"],
        ),
        lod2=GeometricAttribute(
            is2d=True,
            lod_detection=["./tran:lod2MultiSurface"],
            collect_all=[".//tran:lod2MultiSurface//gml:Polygon"],
            only_direct=["./tran:lod2MultiSurface//gml:Polygon"],
        ),
        lod3=GeometricAttribute(
            lod_detection=["./tran:lod3MultiSurface"],
            collect_all=[".//tran:lod3MultiSurface//gml:Polygon"],
            only_direct=["./tran:lod3MultiSurface//gml:Polygon"],
        ),
        semantic_parts=[
            "./tran:trafficArea/tran:TrafficArea",
            "./tran:auxiliaryTrafficArea/tran:AuxiliaryTrafficArea",
        ],
    ),
)

TRACK = FeatureProcessingDefinition(
    id="tran:Track",
    name="Track",
    target_elements=["tran:Track"],
    attribute_groups=[
        AttributeGroup(
            base_element=None,
            attributes=[
                Attribute(
                    name="class",
                    path="./tran:class",
                    datatype="string",
                    predefined_codelist="TransportationComplex_class",
                ),
                Attribute(
                    name="function",
                    path="./tran:function",
                    datatype="[]string",
                    predefined_codelist="Track_function",
                ),
            ],
        ),
        AttributeGroup(
            base_element="./uro:trackAttribute/uro:TrackAttribute",
            attributes=[
                Attribute(
                    name="adminType",
                    path="./uro:adminType",
                    datatype="string",
                    predefined_codelist="TrackAttribute_adminType",
                ),
                Attribute(
                    name="alternativeName",
                    path="./uro:alternativeName",
                    datatype="[]string",
                ),
                Attribute(
                    name="isTollRoad",
                    path="./uro:isTollRoad",
                    datatype="boolean",
                ),
                Attribute(
                    name="relativeLevel",
                    path="./uro:relativeLevel",
                    datatype="integer",
                ),
                Attribute(
                    name="separator",
                    path="./uro:separator",
                    datatype="double",
                ),
                Attribute(
                    name="structureType",
                    path="./uro:structureType",
                    datatype="string",
                    predefined_codelist="TrackAttribute_structureType",
                ),
                Attribute(
                    name="widthType",
                    path="./uro:widthType",
                    datatype="string",
                    predefined_codelist="TrackAttribute_widthType",
                ),
            ],
        ),
        AttributeGroup(
            base_element="./uro:tranDataQualityAttribute/uro:TransportationDataQualityAttribute",
            attributes=_transportation_data_quality_attribute,
        ),
    ],
    dm_attr_container_path="./uro:tranDmAttribute",
    facility_attr_paths=FacilityAttributePaths(
        facility_id="./uro:tranFacilityIdAttribute",
        facility_types="./uro:tranFacilityTypeAttribute",
        facility_attrs="./uro:tranFacilityAttribute",
    ),
    geometries=GeometricAttributes(
        lod0=GeometricAttribute(
            is2d=True,
            lod_detection=["./tran:lod0Network"],
            collect_all=["./tran:lod0Network//gml:LineString"],
        ),
        lod1=GeometricAttribute(
            is2d=True,
            lod_detection=["./tran:lod1MultiSurface"],
            collect_all=["./tran:lod1MultiSurface//gml:Polygon"],
            only_direct=["./tran:lod1MultiSurface//gml:Polygon"],
        ),
        lod2=GeometricAttribute(
            is2d=True,
            lod_detection=["./tran:lod2MultiSurface"],
            collect_all=[".//tran:lod2MultiSurface//gml:Polygon"],
            only_direct=["./tran:lod2MultiSurface//gml:Polygon"],
        ),
        lod3=GeometricAttribute(
            lod_detection=["./tran:lod3MultiSurface"],
            collect_all=[".//tran:lod3MultiSurface//gml:Polygon"],
            only_direct=["./tran:lod3MultiSurface//gml:Polygon"],
        ),
        semantic_parts=[
            "./tran:trafficArea/tran:TrafficArea",
            "./tran:auxiliaryTrafficArea/tran:AuxiliaryTrafficArea",
        ],
    ),
)

_square_urban_plan_attribute_attrs = [
    Attribute(
        name="areaCompleted",
        path="./uro:areaCompleted",
        datatype="double",
    ),
    Attribute(
        name="areaImproved",
        path="./uro:areaImproved",
        datatype="double",
    ),
    Attribute(
        name="areaInService",
        path="./uro:areaInService",
        datatype="double",
    ),
    Attribute(
        name="areaPlanned",
        path="./uro:areaPlanned",
        datatype="double",
    ),
    Attribute(
        name="city",
        path="./uro:city",
        datatype="string",
        predefined_codelist="Common_localPublicAuthorities",
    ),
    Attribute(
        name="dateOfDecision",
        path="./uro:dateOfDecision",
        datatype="date",
    ),
    Attribute(
        name="dateOfRevision",
        path="./uro:dateOfRevision",
        datatype="date",
    ),
    Attribute(
        name="enforcer",
        path="./uro:enforcer",
        datatype="[]string",
    ),
    Attribute(
        name="isAuthorized",
        path="./uro:isAuthorized",
        datatype="boolean",
    ),
    Attribute(
        name="isCompleted",
        path="./uro:isCompleted",
        datatype="boolean",
    ),
    Attribute(
        name="note",
        path="./uro:note",
        datatype="string",
    ),
    Attribute(
        name="numberOfBerthsInService",
        path="./uro:numberOfBerthsInService",
        datatype="integer",
    ),
    Attribute(
        name="numberOfBerthsPlanned",
        path="./uro:numberOfBerthsPlanned",
        datatype="integer",
    ),
    Attribute(
        name="prefecture",
        path="./uro:prefecture",
        datatype="string",
        predefined_codelist="Common_localPublicAuthorities",
    ),
    Attribute(
        name="projectEndDate",
        path="./uro:projectEndDate",
        datatype="date",
    ),
    Attribute(
        name="projectStartDate",
        path="./uro:projectStartDate",
        datatype="date",
    ),
    Attribute(
        name="purpose",
        path="./uro:purpose",
        datatype="string",
    ),
    Attribute(
        name="railwayType",
        path="./uro:railwayType",
        datatype="[]string",
        predefined_codelist="StationSquareAttribute_railwayType",
    ),
    Attribute(
        name="remarks",
        path="./uro:remarks",
        datatype="string",
    ),
    Attribute(
        name="route",
        path="./uro:route",
        datatype="[]string",
    ),
    Attribute(
        name="station",
        path="./uro:station",
        datatype="[]string",
    ),
    Attribute(
        name="status",
        path="./uro:status",
        datatype="string",
        predefined_codelist="Common_status",
    ),
    Attribute(
        name="structure",
        path="./uro:structure",
        datatype="string",
    ),
    Attribute(
        name="terminalType",
        path="./uro:terminalType",
        datatype="string",
        predefined_codelist="TerminalAttribute_terminalType",
    ),
    Attribute(
        name="urbanPlanningAreaName",
        path="./uro:urbanPlanningAreaName",
        datatype="string",
    ),
    Attribute(
        name="userType",
        path="./uro:userType",
        datatype="string",
        predefined_codelist="TerminalAttribute_userType",
    ),
]

SQUARE = FeatureProcessingDefinition(
    id="tran:Square",
    name="Square",
    target_elements=["tran:Square"],
    attribute_groups=[
        AttributeGroup(
            base_element=None,
            attributes=[
                Attribute(
                    name="class",
                    path="./tran:class",
                    datatype="string",
                    predefined_codelist="TransportationComplex_class",
                ),
                Attribute(
                    name="function",
                    path="./tran:function",
                    datatype="[]string",
                    predefined_codelist="Square_function",
                ),
            ],
        ),
        AttributeGroup(
            base_element="./uro:squareUrbanPlanAttribute/uro:SquareUrbanPlanAttribute",
            attributes=_square_urban_plan_attribute_attrs,
        ),
        AttributeGroup(
            base_element="./uro:squareUrbanPlanAttribute/uro:StationSquareAttribute",
            attributes=_square_urban_plan_attribute_attrs,
        ),
        AttributeGroup(
            base_element="./uro:squareUrbanPlanAttribute/uro:TerminalAttribute",
            attributes=_square_urban_plan_attribute_attrs,
        ),
        AttributeGroup(
            base_element="./uro:tranDataQualityAttribute/uro:TransportationDataQualityAttribute",
            attributes=_transportation_data_quality_attribute,
        ),
    ],
    dm_attr_container_path="./uro:tranDmAttribute",
    facility_attr_paths=FacilityAttributePaths(
        facility_id="./uro:tranFacilityIdAttribute",
        facility_types="./uro:tranFacilityTypeAttribute",
        facility_attrs="./uro:tranFacilityAttribute",
    ),
    geometries=GeometricAttributes(
        lod0=GeometricAttribute(
            is2d=True,
            lod_detection=["./tran:lod0Network"],
            collect_all=["./tran:lod0Network//gml:LineString"],
        ),
        lod1=GeometricAttribute(
            is2d=True,
            lod_detection=["./tran:lod1MultiSurface"],
            collect_all=["./tran:lod1MultiSurface//gml:Polygon"],
            only_direct=["./tran:lod1MultiSurface//gml:Polygon"],
        ),
        lod2=GeometricAttribute(
            is2d=True,
            lod_detection=["./tran:lod2MultiSurface"],
            collect_all=[".//tran:lod2MultiSurface//gml:Polygon"],
            only_direct=["./tran:lod2MultiSurface//gml:Polygon"],
        ),
        lod3=GeometricAttribute(
            lod_detection=["./tran:lod3MultiSurface"],
            collect_all=[".//tran:lod3MultiSurface//gml:Polygon"],
            only_direct=["./tran:lod3MultiSurface//gml:Polygon"],
        ),
        semantic_parts=[
            "./tran:trafficArea/tran:TrafficArea",
            "./tran:auxiliaryTrafficArea/tran:AuxiliaryTrafficArea",
        ],
    ),
)

WATERWAY = FeatureProcessingDefinition(
    id="uro:Waterway",
    name="Waterway",
    target_elements=["uro:Waterway"],
    attribute_groups=[
        AttributeGroup(
            base_element=None,
            attributes=[
                Attribute(
                    name="class",
                    path="./tran:class",
                    datatype="string",
                    predefined_codelist="TransportationComplex_class",
                ),
                Attribute(
                    name="function",
                    path="./tran:function",
                    datatype="[]string",
                    predefined_codelist="Waterway_function",
                ),
            ],
        ),
        AttributeGroup(
            base_element="./uro:watewayDetailAttribute/uro:WaterwayDetailAttribute",
            attributes=[
                Attribute(
                    name="length",
                    path="./uro:length",
                    datatype="double",
                ),
                Attribute(
                    name="maximumWidth",
                    path="./uro:maximumWidth",
                    datatype="double",
                ),
                Attribute(
                    name="minimumWidth",
                    path="./uro:minimumWidth",
                    datatype="double",
                ),
                Attribute(
                    name="navigation",
                    path="./uro:navigation",
                    datatype="string",
                ),
                Attribute(
                    name="plannedDepth",
                    path="./uro:plannedDepth",
                    datatype="double",
                ),
                Attribute(
                    name="routeDirection",
                    path="./uro:routeDirection",
                    datatype="string",
                    predefined_codelist="WaterwayDetailAttribute_routeDirection",
                ),
                Attribute(
                    name="routeID",
                    path="./uro:routeID",
                    datatype="integer",
                ),
                Attribute(
                    name="speedLimit",
                    path="./uro:speedLimit",
                    datatype="double",
                ),
                Attribute(
                    name="targetShipType",
                    path="./uro:targetShipType",
                    datatype="[]string",
                ),
            ],
        ),
        AttributeGroup(
            base_element="./uro:tranDataQualityAttribute/uro:TransportationDataQualityAttribute",
            attributes=_transportation_data_quality_attribute,
        ),
    ],
    facility_attr_paths=FacilityAttributePaths(
        facility_id="./uro:tranFacilityIdAttribute",
        facility_types="./uro:tranFacilityTypeAttribute",
        facility_attrs="./uro:tranFacilityAttribute",
    ),
    geometries=GeometricAttributes(
        lod0=GeometricAttribute(
            is2d=True,
            lod_detection=["./tran:lod0Network"],
            collect_all=["./tran:lod0Network//gml:LineString"],
        ),
        lod1=GeometricAttribute(
            is2d=True,
            lod_detection=["./tran:lod1MultiSurface"],
            collect_all=["./tran:lod1MultiSurface//gml:Polygon"],
            only_direct=["./tran:lod1MultiSurface//gml:Polygon"],
        ),
        lod2=GeometricAttribute(
            is2d=True,
            lod_detection=["./tran:lod2MultiSurface"],
            collect_all=[".//tran:lod2MultiSurface//gml:Polygon"],
            only_direct=["./tran:lod2MultiSurface//gml:Polygon"],
        ),
        lod3=GeometricAttribute(
            lod_detection=["./tran:lod3MultiSurface"],
            collect_all=[".//tran:lod3MultiSurface//gml:Polygon"],
            only_direct=["./tran:lod3MultiSurface//gml:Polygon"],
        ),
        semantic_parts=[
            "./tran:trafficArea/tran:TrafficArea",
            "./tran:auxiliaryTrafficArea/tran:AuxiliaryTrafficArea",
        ],
    ),
)

# TrafficArea, AuxiliaryTrafficArea を扱う
# これらは Road, Railway, Track, Square (いずれもLoD2-4) の子として使われる
TRAFFIC_AREA = FeatureProcessingDefinition(
    id="tran:TrafficArea",
    name="TrafficArea",
    target_elements=["tran:TrafficArea", "tran:AuxiliaryTrafficArea"],
    attribute_groups=[
        AttributeGroup(
            base_element=None,
            attributes=[
                Attribute(
                    name="function",
                    path="./tran:function",
                    datatype="[]string",
                    predefined_codelist="TrafficArea_function",
                ),
                Attribute(
                    name="surfaceMaterial",
                    path="./tran:surfaceMaterial",
                    datatype="string",
                    predefined_codelist="TrafficArea_surfaceMaterial",
                ),
            ],
        ),
        # uro:TrafficAreaStructureAttribute (Road)
        AttributeGroup(
            base_element="./uro:trafficAreaStructureAttribute/uro:TrafficAreaStructureAttribute",
            attributes=[
                Attribute(
                    name="numberOfLanes",
                    path="./uro:numberOfLanes",
                    datatype="integer",
                ),
            ],
        ),
        # uro:RailwayTrackAttribute (Railway)
        AttributeGroup(
            base_element="./uro:railwayTrackAttribute/uro:RailwayTrackAttribute",
            attributes=[
                Attribute(
                    name="routeName",
                    path="./uro:routeName",
                    datatype="string",
                ),
                Attribute(
                    name="directionType",
                    path="./uro:directionType",
                    datatype="string",
                    predefined_codelist="RailwayTrackAttribute_directionType",
                ),
                Attribute(
                    name="trackType",
                    path="./uro:trackType",
                    datatype="string",
                    predefined_codelist="RailwayTrackAttribute_trackType",
                ),
                Attribute(
                    name="startPost",
                    path="./uro:startPost",
                    datatype="string",
                ),
                Attribute(
                    name="endPost",
                    path="./uro:endPost",
                    datatype="string",
                ),
                Attribute(
                    name="alignmentType",
                    path="./uro:alignmentType",
                    datatype="string",
                    predefined_codelist="RailwayTrackAttribute_alignmentType",
                ),
                # TODO: uro:controlType
            ],
        ),
    ],
    geometries=GeometricAttributes(
        lod2=GeometricAttribute(
            is2d=True,
            lod_detection=[
                "./tran:lod2MultiSurface",
                "./uro:railwayTrackAttribute/uro:RailwayTrackAttribute/uro:lod2Network",
            ],
            collect_all=[
                "./tran:lod2MultiSurface//gml:Polygon",
                "./uro:railwayTrackAttribute/uro:RailwayTrackAttribute/uro:lod2Network//gml:LineString",
            ],
        ),
        lod3=GeometricAttribute(
            lod_detection=[
                "./tran:lod3MultiSurface",
                "./uro:railwayTrackAttribute/uro:RailwayTrackAttribute/uro:lod3Network",
            ],
            collect_all=[
                "./tran:lod3MultiSurface//gml:Polygon",
                "./uro:railwayTrackAttribute/uro:RailwayTrackAttribute/uro:lod3Network//gml:LineString",
            ],
        ),
    ),
    dm_attr_container_path="./uro:tranDmAttribute",
)
