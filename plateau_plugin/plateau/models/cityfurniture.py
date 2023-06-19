from .base import (
    Attribute,
    Emission,
    Emissions,
    LODDetection,
    ProcessorDefinition,
)

CITY_FURNITURE = ProcessorDefinition(
    id="CityFurniture",
    target_elements=["frn:CityFurniture"],
    lod_detection=LODDetection(
        lod1=["./frn:lod1Geometry"],
        lod2=["./frn:lod2Geometry"],
        lod3=["./frn:lod3Geometry"],
    ),
    attributes=[
        Attribute(
            name="class",
            xpath="./frn:class/text()",
            datatype="string",
            codelist="CityFurniture_class",
        ),
        Attribute(
            name="function",
            xpath="./frn:function/text()",
            datatype="[]string",
            codelist="CityFurniture_function",
        ),
        Attribute(
            name="usage",
            xpath="./frn:usage/text()",
            datatype="[]string",
        ),
    ],
    emissions=Emissions(
        lod1=Emission(elem_paths=["./frn:lod1Geometry/gml:MultiSurface//gml:Polygon"]),
        lod2=Emission(elem_paths=["./frn:lod2Geometry/gml:MultiSurface//gml:Polygon"]),
        lod3=Emission(elem_paths=["./frn:lod3Geometry/gml:MultiSurface//gml:Polygon"]),
    ),
)
