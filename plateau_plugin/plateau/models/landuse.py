from .base import (
    Attribute,
    Emission,
    Emissions,
    LODDetection,
    ProcessorDefinition,
)

LAND_USE = ProcessorDefinition(
    id="LandUse",
    target_elements=[
        "luse:LandUse",
    ],
    lod_detection=LODDetection(
        lod1=["./luse:lod1MultiSurface"],
    ),
    attributes=[
        Attribute(
            name="class",
            xpath="./luse:class/text()",
            datatype="string",
            codelist="Common_landUseType",
        ),
        Attribute(
            name="usage",
            xpath="./luse:usage/text()",
            datatype="string",
            codelist="LandUse_usage",
        ),
    ],
    emissions=Emissions(
        lod1=Emission(
            elem_paths=[
                "./luse:lod1MultiSurface//gml:Polygon",
            ]
        ),
    ),
)
