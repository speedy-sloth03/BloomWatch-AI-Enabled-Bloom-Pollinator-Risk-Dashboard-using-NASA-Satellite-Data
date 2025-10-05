from pydantic import BaseModel
from typing import List

class Region(BaseModel):
    id: str
    name_en: str
    name_bn: str
    bbox: List[float]