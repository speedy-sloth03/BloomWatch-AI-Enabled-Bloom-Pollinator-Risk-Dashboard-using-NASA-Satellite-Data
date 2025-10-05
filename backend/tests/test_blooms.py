from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_blooms():
    response = client.get("/api/blooms?region_id=Dhaka&date=2025-03-08")
    assert response.status_code == 200
    data = response.json()
    assert data['type'] == 'FeatureCollection'
    assert 'features' in data
    for f in data['features']:
        assert 'properties' in f and 'ndvi_series' in f['properties']