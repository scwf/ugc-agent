import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "backend"))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "UGC Agent API", "version": "1.0.0"}


def test_health_endpoint():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "healthy"}


def test_api_health_endpoint():
    resp = client.get("/api/v1/health/")
    assert resp.status_code == 200
    assert resp.json() == {
        "status": "healthy",
        "service": "UGC Agent API",
        "version": "1.0.0",
    }
