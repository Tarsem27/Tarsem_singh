from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_list_controls() -> None:
    payload = {
        "framework": "SOC2",
        "title": "Enable MFA for privileged accounts",
        "owner": "Security Team",
        "status": "in_progress",
        "is_critical": True,
    }
    create_response = client.post("/controls", json=payload)
    assert create_response.status_code == 201

    list_response = client.get("/controls?framework=SOC2")
    assert list_response.status_code == 200
    data = list_response.json()
    assert len(data) >= 1
    assert data[0]["framework"] == "SOC2"
