from .base import ProcessorRegistory
from .building import BOUNDARY_SURFACE, BUILDING
from .cityfurniture import CITY_FURNITURE
from .landslide import LAND_SLIDE
from .landuse import LAND_USE
from .transportation import ROAD, TRAFFIC_AREA

processors = ProcessorRegistory(
    [
        BUILDING,
        BOUNDARY_SURFACE,
        ROAD,
        TRAFFIC_AREA,
        CITY_FURNITURE,
        LAND_SLIDE,
        LAND_USE,
    ]
)
