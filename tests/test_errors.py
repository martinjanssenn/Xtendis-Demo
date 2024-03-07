import pytest
from src.app import app 

def test_errors():
    response = app.test_client().get('/testje')
    assert response.status_code == 404