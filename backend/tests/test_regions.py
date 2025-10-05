from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_regions():
    response = client.get("/api/regions")
    assert response.status_code == 200
    regions = response.json()
    assert len(regions) == 8
    assert all("id" in r for r in regions)