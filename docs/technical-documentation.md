# BloomWatch Technical Documentation

## Overview

BloomWatch is a globe-first web app for detecting and forecasting flowering/bloom events and pollinator risk in Bangladesh using NASA satellite data.

## Backend

- **FastAPI** REST APIs for divisions, blooms, heatmap, forecast, OAuth.
- **NASA Data Ingestion:** VIIRS VNP13A1 and MODIS MOD13A1 via LAADS API.
- **Processing:** Uses rasterio, xarray, rioxarray, numpy, pandas, scipy, scikit-learn.
- **Phenology Detection:** NDVI time series smoothing (Savitzky–Golay), bloom onset detection, clustering (DBSCAN), forecast (Prophet/STL).
- **OAuth2:** Google login (Authlib).
- **Storage:** Zarr/NetCDF for raster stacks, demo JSON/GeoJSON.

## Frontend

- **React (TypeScript):** 3D Cesium globe, Leaflet map, Chart.js.
- **i18next:** Multilingual EN/BN.
- **Accessibility:** ARIA, keyboard nav, colorblind palette, shape markers.
- **Exports:** CSV, PNG chart.
- **Demo Data:** Provided for offline demo.

## Data Flow

1. User selects region on globe.
2. Frontend requests /api/blooms, /api/heatmap, /api/forecast.
3. Backend loads sample data or processed raster stacks.
4. NDVI series processed, clusters detected, forecast computed.
5. Results visualized in dashboard.

## Validation

- Backend unit tests (pytest).
- Frontend unit tests (Jest/RTL).
- Manual QA checklist (see QA-PASSED.md).

## References

- [NASA Earthdata](https://earthdata.nasa.gov/)
- [MODIS Info](https://modis.gsfc.nasa.gov/)
- [Prophet](https://facebook.github.io/prophet/)