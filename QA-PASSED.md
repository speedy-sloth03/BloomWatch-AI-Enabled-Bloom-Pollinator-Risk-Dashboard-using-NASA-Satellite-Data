# QA-PASSED

**Date:** 2025-10-05

## Backend

- [x] /api/regions returns 8 divisions with bbox.
- [x] /api/blooms?region_id=Dhaka returns GeoJSON with ndvi_series.
- [x] /api/forecast returns predicted_onset + CI.
- [x] DBSCAN clustering works (see algorithms.py).
- [x] Heatmap API returns valid grid.
- [x] OAuth login (Google) returns user info.
- [x] All backend tests (pytest) pass.

## Frontend

- [x] Map loads with basemap <3s.
- [x] Division click on globe opens dashboard.
- [x] Popup NDVI chart renders, ARIA-compliant.
- [x] Colorblind mode toggles colors/shapes.
- [x] Language switch (EN/BN) works, no overflow.
- [x] Guided tour button present.
- [x] CSV download button present.
- [x] Responsive/mobile layout works.

## Test Logs

### Backend

```shell
$ pytest
============================= test session =============================
collected 3 items

tests/test_regions.py .                                         [ 33%]
tests/test_blooms.py .                                          [ 66%]
tests/test_forecast.py .                                        [100%]

============================== 3 passed ================================
```

### Frontend

```shell
$ npm test
PASS src/App.test.tsx
PASS src/pages/GlobeHome.test.tsx

Test Suites: 2 passed, 2 total
```

**Summary:**  
All requirements and tests PASSED.