"""汎用都市オブジェクトモデル"""

from .base import (
    FeatureEmission,
    FeatureEmissions,
    FeatureProcessingDefinition,
    LODDetection,
)

GENERIC_CITY_OBJECT = FeatureProcessingDefinition(
    id="GenericCityObject",
    target_elements=["gen:GenericCityObject"],
    lod_detection=LODDetection(
        lod0=["./gen:lod0Geometry"],
        lod1=["./gen:lod1Geometry"],
        lod2=["./gen:lod2Geometry"],
        lod3=["./gen:lod3Geometry"],
    ),
    property_groups=[],
    emissions=FeatureEmissions(
        lod0=FeatureEmission(collect_all=["./gen:lod0Geometry//gml:Polygon"]),
        lod1=FeatureEmission(collect_all=["./gen:lod1Geometry//gml:Polygon"]),
        lod2=FeatureEmission(collect_all=["./gen:lod2Geometry//gml:Polygon"]),
        lod3=FeatureEmission(collect_all=["./gen:lod3Geometry//gml:Polygon"]),
    ),
)
