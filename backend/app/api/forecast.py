from fastapi import APIRouter, HTTPException
from app.models.forecast import ForecastRequest, ForecastResponse
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/forecast", response_model=ForecastResponse, tags=["Forecast"])
async def forecast_bloom(req: ForecastRequest):
    # Demo: stub model — always returns same prediction.
    try:
        # Validate NDVI series
        if not req.ndvi_series or len(req.ndvi_series) < 2:
            raise ValueError("Not enough NDVI data")
        # Example: compute RMSE, CI, onset
        return ForecastResponse(
            predicted_onset="2025-03-10",
            ci_lower="2025-03-08",
            ci_upper="2025-03-12",
            rmse=2.8
        )
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})