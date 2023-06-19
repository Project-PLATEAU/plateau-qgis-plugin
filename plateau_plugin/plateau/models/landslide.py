"""災害リスク (土砂災害) モデル (lsld)"""

from .base import (
    Attribute,
    Emission,
    Emissions,
    LODDetection,
    ProcessorDefinition,
)

LAND_SLIDE = ProcessorDefinition(
    id="SedimentDisasterProneArea",
    target_elements=[
        "urf2:SedimentDisasterProneArea",
        "urf3:SedimentDisasterProneArea",
    ],
    lod_detection=LODDetection(
        lod1=["./urf:lod1MultiSurface"],
    ),
    attributes=[
        Attribute(
            name="prefecture",
            path="./urf:prefecture",
            datatype="string",
            codelist="Common_prefecture",
        ),
        Attribute(
            name="location",
            path="./urf:location",
            datatype="string",
        ),
        Attribute(
            name="disasterType",
            path="./urf:disasterType",
            datatype="string",
            codelist="SedimentDisasterProneArea_disasterType",
        ),
        Attribute(
            name="areaType",
            path="./urf:areaType",
            datatype="string",
            codelist="SedimentDisasterProneArea_areaType",
        ),
        Attribute(
            name="status",
            path="./urf:status",
            datatype="string",
            codelist="SedimentDisasterProneArea_status",
        ),
        Attribute(
            name="zoneName",
            path="./urf:zoneName",
            datatype="string",
        ),
        Attribute(
            name="zoneNumber",
            path="./urf:zoneNumber",
            datatype="string",
        ),
    ],
    emissions=Emissions(
        lod1=Emission(
            elem_paths=[
                "./urf:lod1MultiSurface//gml:Polygon",
            ]
        ),
    ),
)
