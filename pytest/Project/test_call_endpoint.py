import requests
import uuid

from Project.Testing_api_todo import ENDPOINT


def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
