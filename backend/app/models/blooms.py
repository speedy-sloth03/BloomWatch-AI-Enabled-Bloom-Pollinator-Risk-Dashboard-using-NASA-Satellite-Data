from pydantic import BaseModel
from typing import List, Dict, Any

class NDVISeriesItem(BaseModel):
    date: str
    ndvi: float

class BloomProperties(BaseModel):
    id: str
    ndvi_series: List[NDVISeriesItem]
    intensity: float

class BloomFeature(BaseModel):
    type: str
    geometry: Dict[str, Any]
    properties: BloomProperties

class BloomFeatureCollection(BaseModel):
    type: str
    features: List[BloomFeature]