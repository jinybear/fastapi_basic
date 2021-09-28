import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../fastapi_basic')))

from fastapi.testclient import TestClient
from app import app
from controllers.models.test import Calculate_Data
from services.auth import service_auth

client = TestClient(app)

access_token = service_auth.gen_token('johndoe', 'secret')

def test_not_authorization():
    body = Calculate_Data()

    response = client.post(
        "/calculate_profit",
        headers={
            'Content-type': 'application/json',
        },
        json=body.dict()
    )

    print('Result response :', response.json())
    assert response.status_code == 401

def test_calculate_profit():
    body = Calculate_Data()

    response = client.post(
        "/calculate_profit",
        headers={
            'Content-type':'application/json',
            'Authorization': f'Bearer {access_token}',
        },
        json=body.dict()
    )

    print('Result response :', response.json())
    assert response.status_code == 200
