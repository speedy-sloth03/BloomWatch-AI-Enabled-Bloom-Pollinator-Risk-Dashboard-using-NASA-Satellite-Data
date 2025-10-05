from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import regions, blooms, forecast
import os

app = FastAPI(
    title="BloomWatch API",
    description="BloomWatch — NASA-powered bloom/pollinator risk detection for Bangladesh divisions.",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# CORS setup (allow all for demo; restrict in prod)
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ALLOW_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(regions.router, prefix="/api")
app.include_router(blooms.router, prefix="/api")
app.include_router(forecast.router, prefix="/api")

# Health endpoint
@app.get("/api/status", tags=["Health"])
def get_status():
    # Demo: Return fixed health status. Real: pull from pipeline state!
    return {
        "last_fetch_time": "2025-10-01T05:00:00Z",
        "last_processed_date": "2025-09-30",
        "LAADS_auth_status": "OK"
    }