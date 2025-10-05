import os
import requests
import rasterio
import numpy as np
import xarray as xr
import rioxarray
from datetime import datetime, timedelta

LAADS_API = "https://ladsweb.modaps.eosdis.nasa.gov/api/v1/"
PRODUCTS = {
    "VIIRS": "VNP13A1",
    "MODIS": "MOD13A1"
}

def get_laads_token():
    """Authenticate to LAADS and return token (from .netrc or env)."""
    token = os.getenv("LAADS_TOKEN")
    if token:
        return token
    # fallback: read .netrc or error
    raise Exception("LAADS_TOKEN env not set")

def fetch_granules(product, start_date, end_date, bbox):
    """
    Download VIIRS/MODIS NDVI/EVI granules for a bounding box and time window.
    Returns file paths of downloaded granules.
    """
    # For demo, assume files are local or mock URLs
    granule_paths = []
    # Sample: download from Earthdata/LADS
    # Real code: Use requests with LAADS token, paging, QA mask, etc.
    return granule_paths

def apply_qa_mask(raster_path):
    """Apply QA mask to raster. For demo, returns input."""
    return raster_path

def reproject_resample(raster_path, dst_crs="EPSG:4326", res=500):
    """Reproject raster to EPSG:4326, resample to 500m."""
    with rasterio.open(raster_path) as src:
        # For demo: Return path unchanged
        return raster_path

def composite_ndvi(granules):
    """Composite multiple granules (median). For demo, return array."""
    arrs = [np.random.rand(100, 100) for g in granules]
    composite = np.median(arrs, axis=0)
    return composite

def build_time_series(region_id, dates):
    """Build per-pixel NDVI time series for region. Save to Zarr."""
    # For demo, generate random NDVI stack
    stack = xr.DataArray(np.random.rand(len(dates), 100, 100),
                         dims=("time", "lat", "lon"),
                         coords={"time": dates})
    # Save to Zarr or NetCDF in data/
    stack.to_netcdf(f"./data/{region_id}_ndvi_stack.nc")
    return stack