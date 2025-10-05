from fastapi import APIRouter, Query
from app.models.blooms import BloomFeatureCollection
from fastapi.responses import JSONResponse
import os
import json

router = APIRouter()

@router.get("/blooms", response_model=BloomFeatureCollection, tags=["Blooms"])
async def get_blooms(region_id: str = Query(...), date: str = Query(...)):
    """
    Return bloom detection points GeoJSON for region/date.
    For demo, load from sample file.
    """
    sample_file = os.path.join(os.path.dirname(__file__), "../../../data/sample_bangladesh.geojson")
    if not os.path.exists(sample_file):
        return JSONResponse(status_code=404, content={"error": "Sample data not found"})
    with open(sample_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    # Optionally filter by region_id/date
    return data