"""災害リスク (土砂災害) モデル (./lsld/)"""

from .base import (
    Attribute,
    AttributeGroup,
    FeatureProcessingDefinition,
    GeometricAttribute,
    GeometricAttributes,
)

URF_SEDIMENT_DISASTER_PRONE_AREA = FeatureProcessingDefinition(
    id="urf:SedimentDisasterProneArea",
    name="SedimentDisasterProneArea",
    target_elements=[
        "urf:SedimentDisasterProneArea",
    ],
    load_generic_attributes=True,
    attribute_groups=[
        AttributeGroup(
            base_element=None,
            attributes=[
                Attribute(
                    name="validFrom",
                    path="./urf:validFrom",
                    datatype="date",
                ),
                Attribute(
                    name="validFromType",
                    path="./urf:validFromType",
                    datatype="string",
                    predefined_codelist="Common_validType",
                ),
                Attribute(
                    name="prefecture",
                    path="./urf:prefecture",
                    datatype="string",
                    predefined_codelist="Common_localPublicAuthorities",
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
                    predefined_codelist="SedimentDisasterProneArea_disasterType",
                ),
                Attribute(
                    name="areaType",
                    path="./urf:areaType",
                    datatype="string",
                    predefined_codelist="SedimentDisasterProneArea_areaType",
                ),
                Attribute(
                    name="status",
                    path="./urf:status",
                    datatype="string",
                    predefined_codelist="SedimentDisasterProneArea_status",
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
        )
    ],
    geometries=GeometricAttributes(
        lod1=GeometricAttribute(
            is2d=True,
            lod_detection=["./urf:lod1MultiSurface"],
            collect_all=[
                "./urf:lod1MultiSurface//gml:Polygon",
            ],
        ),
    ),
)
