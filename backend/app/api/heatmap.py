from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
import numpy as np

router = APIRouter()

@router.get("/heatmap", tags=["Heatmap"])
async def get_heatmap(region_id: str = Query(...), date_range: str = Query(...)):
    """
    Returns a simplified grid heatmap for the region and date range.
    For demo, returns a 10x10 grid with random values.
    """
    grid = np.random.rand(10, 10).tolist()
    return {"region_id": region_id, "date_range": date_range, "heatmap_grid": grid}