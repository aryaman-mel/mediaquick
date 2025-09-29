from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_predict_basic():
    r = client.post("/predict", json={"symptoms": ["fever", "cough"]})
    assert r.status_code == 200
    body = r.json()
    assert "predictions" in body and isinstance(body["predictions"], list)

def test_nearby():
    r = client.post("/nearby", json={"lat": -37.8136, "lng": 144.9631, "query": "clinic"})
    assert r.status_code == 200
