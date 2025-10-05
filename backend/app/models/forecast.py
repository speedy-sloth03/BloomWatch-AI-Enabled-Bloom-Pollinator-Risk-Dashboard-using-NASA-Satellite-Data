from pydantic import BaseModel
from typing import List

class ForecastSeriesItem(BaseModel):
    date: str
    ndvi: float

class ForecastRequest(BaseModel):
    lat: float
    lon: float
    ndvi_series: List[ForecastSeriesItem]

class ForecastResponse(BaseModel):
    predicted_onset: str
    ci_lower: str
    ci_upper: str
    rmse: float