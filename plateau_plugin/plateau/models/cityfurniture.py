from .base import (
    FeatureEmission,
    FeatureEmissions,
    LODDetection,
    ProcessorDefinition,
    Property,
    PropertyGroup,
)

CITY_FURNITURE = ProcessorDefinition(
    id="CityFurniture",
    target_elements=["frn:CityFurniture"],
    lod_detection=LODDetection(
        lod1=["./frn:lod1Geometry"],
        lod2=["./frn:lod2Geometry"],
        lod3=["./frn:lod3Geometry"],
    ),
    property_groups=[
        PropertyGroup(
            base_element=None,
            properties=[
                Property(
                    name="class",
                    path="./frn:class",
                    datatype="string",
                    codelist="CityFurniture_class",
                ),
                Property(
                    name="function",
                    path="./frn:function",
                    datatype="[]string",
                    codelist="CityFurniture_function",
                ),
                Property(
                    name="usage",
                    path="./frn:usage",
                    datatype="[]string",
                ),
            ],
        ),
        # uro:CityFurnitureDataQualityAttribute
        PropertyGroup(
            base_element="./uro:cityFurnitureDataQualityAttribute/uro:CityFurnitureDataQualityAttribute",
            properties=[
                Property(
                    name="uro:srcScale",
                    path="./uro:srcScale",
                    datatype="[]string",
                    codelist="CityFurnitureDataQualityAttribute_srcScale",
                ),
                Property(
                    name="uro:geometrySrcDesc",
                    path="./uro:geometrySrcDesc",
                    datatype="[]string",
                    codelist="CityFurnitureDataQualityAttribute_geometrySrcDesc",
                ),
                Property(
                    name="uro:thematicSrcDesc",
                    path="./uro:thematicSrcDesc",
                    datatype="[]string",
                    codelist="CityFurnitureDataQualityAttribute_thematicSrcDesc",
                ),
                Property(
                    name="uro:appearanceSrcDesc",
                    path="./uro:appearanceSrcDesc",
                    datatype="[]string",
                    codelist="CityFurnitureDataQualityAttribute_appearanceSrcDesc",
                ),
                Property(
                    name="uro:lodType",
                    path="./uro:appearanceSrcDesc",
                    datatype="[]string",
                ),
            ],
        ),
    ],
    emissions=FeatureEmissions(
        lod1=FeatureEmission(collect_all=["./frn:lod1Geometry//gml:Polygon"]),
        lod2=FeatureEmission(collect_all=["./frn:lod2Geometry//gml:Polygon"]),
        lod3=FeatureEmission(collect_all=["./frn:lod3Geometry//gml:Polygon"]),
    ),
)
