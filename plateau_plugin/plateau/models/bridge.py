"""橋梁モデル"""

from .base import (
    FeatureEmission,
    FeatureEmissions,
    FeatureProcessingDefinition,
    LODDetection,
    Property,
    PropertyGroup,
)

BRIDGE = FeatureProcessingDefinition(
    id="Bridge",
    target_elements=["brid:Bridge"],
    lod_detection=LODDetection(
        lod1=["./brid:lod1Solid"],
        lod2=["./brid:lod2Solid", "./brid:lod2MultiSurface"],
        lod3=["./brid:lod3Solid", "./brid:lod3MultiSurface"],
        lod4=["./brid:lod4Solid", "./brid:lod4MultiSurface"],
    ),
    property_groups=[
        PropertyGroup(
            base_element=None,
            properties=[
                Property(
                    name="class",
                    path="./brid:class",
                    datatype="string",
                    codelist="Bridge_class",
                ),
                Property(
                    name="function",
                    path="./brid:function",
                    datatype="[]string",
                    codelist="Bridge_function",
                ),
                Property(
                    name="yearOfConstruction",
                    path="./brid:yearOfConstruction",
                    datatype="integer",
                ),
                Property(
                    name="yearOfDemolition",
                    path="./brid:yearOfDemolition",
                    datatype="integer",
                ),
                Property(
                    name="isMovable",
                    path="./brid:isMovable",
                    datatype="boolean",
                ),
            ],
        )
    ],
    emissions=FeatureEmissions(
        lod1=FeatureEmission(collect_all=["./brid:lod1Solid//gml:Polygon"]),
        lod2=FeatureEmission(
            collect_all=[
                ".//brid:lod2MultiSurface//gml:Polygon",
                ".//brid:lod2Geometry//gml:Polygon",
            ],
            only_direct=[
                "./brid:lod2MultiSurface//gml:Polygon",
                "./brid:lod2Geometry//gml:Polygon",
            ],
        ),
        lod3=FeatureEmission(
            collect_all=[
                ".//brid:lod3MultiSurface//gml:Polygon",
                ".//brid:lod3Geometry//gml:Polygon",
            ],
            only_direct=[
                "./brid:lod3MultiSurface//gml:Polygon",
                "./brid:lod3Geometry//gml:Polygon",
            ],
        ),
        semantic_parts=[
            ".//brid:GroundSurface",
            ".//brid:WallSurface",
            ".//brid:RoofSurface",
            ".//brid:OuterCeilingSurface",
            ".//brid:OuterFloorSurface",
            ".//brid:ClosureSurface",
            ".//brid:BridgeConstructionElement",
            ".//brid:BridgeInstallation",
        ],
    ),
)

BRIDGE_BOUNDARY_SURFACE = FeatureProcessingDefinition(
    id="brid:_BoundarySurface",
    target_elements=[
        "brid:GroundSurface",
        "brid:WallSurface",
        "brid:RoofSurface",
        "brid:OuterCeilingSurface",
        "brid:OuterFloorSurface",
        "brid:ClosureSurface",
    ],
    property_groups=[],
    lod_detection=LODDetection(
        lod2=["./brid:lod2MultiSurface"],
        lod3=["./brid:lod3MultiSurface"],
        lod4=["./brid:lod4MultiSurface"],
    ),
    emissions=FeatureEmissions(
        lod2=FeatureEmission(
            collect_all=[
                ".//brid:lod2MultiSurface//gml:Polygon",
                ".//brid:lod2Geometry//gml:Polygon",
            ]
        ),
        lod3=FeatureEmission(
            collect_all=[
                ".//brid:lod3MultiSurface//gml:Polygon",
                ".//brid:lod3Geometry//gml:Polygon",
            ]
        ),
        lod4=FeatureEmission(
            collect_all=[
                ".//brid:lod4MultiSurface//gml:Polygon",
                ".//brid:lod4Geometry//gml:Polygon",
            ]
        ),
    ),
)

BRIDGE_CONSTRUCTION_ELEMENT = FeatureProcessingDefinition(
    id="Construction Element",
    target_elements=[
        "brid:BridgeConstructionElement",
    ],
    property_groups=[
        PropertyGroup(
            base_element=None,
            properties=[
                Property(
                    name="function",
                    path="./brid:function",
                    datatype="[]string",
                    codelist="BridgeConstructionElement_function",
                ),
            ],
        )
    ],
    lod_detection=LODDetection(
        lod2=["./brid:lod2Geometry"],
        lod3=["./brid:lod3Geometry"],
        lod4=["./brid:lod4Geometry"],
    ),
    emissions=FeatureEmissions(
        lod2=FeatureEmission(collect_all=[".//brid:lod2Geometry//gml:Polygon"]),
        lod3=FeatureEmission(collect_all=[".//brid:lod3Geometry//gml:Polygon"]),
        lod4=FeatureEmission(collect_all=[".//brid:lod4Geometry//gml:Polygon"]),
    ),
)

BRIDGE_INSTALLATION = FeatureProcessingDefinition(
    id="BridgeInstallation",
    target_elements=[
        "brid:BridgeInstallation",
    ],
    property_groups=[
        PropertyGroup(
            base_element=None,
            properties=[
                Property(
                    name="class",
                    path="./brid:class",
                    datatype="string",
                ),
                Property(
                    name="function",
                    path="./brid:function",
                    datatype="[]string",
                    codelist="BridgeInstallation_function",
                ),
                Property(
                    name="usage",
                    path="./brid:usage",
                    datatype="[]string",
                ),
            ],
        )
    ],
    lod_detection=LODDetection(
        lod2=["./brid:lod2Geometry"],
        lod3=["./brid:lod3Geometry"],
        lod4=["./brid:lod4Geometry"],
    ),
    emissions=FeatureEmissions(
        lod2=FeatureEmission(collect_all=[".//brid:lod2Geometry//gml:Polygon"]),
        lod3=FeatureEmission(collect_all=[".//brid:lod3Geometry//gml:Polygon"]),
        lod4=FeatureEmission(collect_all=[".//brid:lod4Geometry//gml:Polygon"]),
    ),
)
