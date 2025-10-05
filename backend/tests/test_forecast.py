from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_post_forecast():
    req = {
        "lat": 23.7,
        "lon": 90.4,
        "ndvi_series": [
            {"date": "2025-02-01", "ndvi": 0.12},
            {"date": "2025-02-17", "ndvi": 0.18},
            {"date": "2025-03-08", "ndvi": 0.62}
        ]
    }
    resp = client.post("/api/forecast", json=req)
    assert resp.status_code == 200
    data = resp.json()
    assert "predicted_onset" in data
    assert "rmse" in data