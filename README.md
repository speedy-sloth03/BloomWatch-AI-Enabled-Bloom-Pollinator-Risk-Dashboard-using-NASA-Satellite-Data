# BloomWatch

BloomWatch is a globe-first, interactive web app for detecting and forecasting flower bloom events and pollinator risks in Bangladesh using NASA satellite observation data.

## Features

- Interactive 3D globe to select Bangladesh division.
- Division-level dashboard: map, heatmap, NDVI charts, clusters, forecast.
- Multilingual: English & Bangla (বাংলা).
- Colorblind and accessibility support.
- Real NASA data (demo sample included).
- OAuth (Google) login.
- Dockerized for local development.
- Export CSV/PNG, guided tour, and test suite.

## Run Locally

1. **Clone repo**  
   `git clone ...`
2. **Set up .env**  
   Copy `.env.example` and fill out Google OAuth client variables.
3. **Build and run demo**  
   `docker-compose up --build`
4. **Access demo**  
   - Frontend: `http://localhost:3000`
   - Backend: `http://localhost:8000/api/docs`
5. **Run tests**  
   - Backend: `docker exec bloomwatch-backend pytest`
   - Frontend: `docker exec bloomwatch-frontend npm test`

## Environment Variables

See `.env.example` for Google OAuth and CORS settings.

## Demo Data

- `data/sample_bangladesh.geojson`
- `data/sample_ndvi_timeseries.json`

## Docs & QA

- `docs/technical-documentation.md`
- `docs/impact-story.md`
- `QA-PASSED.md`

---

References:  
- [Leaflet.js](https://leafletjs.com/)  
- [Cesium 3D Globe](https://github.com/fengsiyu/cesium-3D-Earth-Map)  
- [NASA Earthdata](https://earthdata.nasa.gov/)  
- [MODIS Info](https://modis.gsfc.nasa.gov/)  
- [Prophet](https://facebook.github.io/prophet/)  