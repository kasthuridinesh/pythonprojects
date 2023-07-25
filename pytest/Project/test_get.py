import requests
from aiohttp import payload
from Project.Testing_api_todo import get_task, ENDPOINT
from test_create import *


def test_get():
    task_id = data["task"]["task_id"]
    get_task_response = get_task(task_id)

    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    print(get_task_data)
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]


def test_get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

