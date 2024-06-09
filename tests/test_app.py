import sys
from pathlib import Path

# Add the project root to the PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent))

from fastapi.testclient import TestClient
from src.main import app, IrisModelInput

client = TestClient(app)

def test_predict():
    response = client.post("/predict/", json={
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    })
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_invalid_input():
    response = client.post("/predict/", json={
        "sepal_length": "invalid",
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    })
    assert response.status_code == 422  # FastAPI's validation error
