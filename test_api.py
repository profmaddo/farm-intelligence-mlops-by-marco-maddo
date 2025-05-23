import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_prediction():
    payload = {
        "temperature": 25.0,
        "rainfall": 100.0,
        "soil_ph": 6.5,
        "fertilizer_amount": 50.0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "predicted_yield" in response.json()
