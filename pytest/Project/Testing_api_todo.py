import requests
import uuid

ENDPOINT = "https://todo.pixegami.io"

'''
'test_check_endpoint' function defines whether we call endpoint.If the endpoint responses ,the status code will be 200,
If not it gives some other status code like 404. Here ,we use assert to   validate response of the request. 
If status_code is 200, the assertion will be passed.
If status_code is different, it gives assertion error. And the test will be failed
'''


def test_check_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200


'''
Here we give put request and we have to pass the payload
Payload are return in a new payload variable

'''


def test_can_create_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200

    data = create_task_response.json()
    print(data)
    return data

    task_id = data["task"]["task_id"]
    get_task_response = get_task(task_id)

    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    print(get_task_data)
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]


def test_can_update_task():
    # create a task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    task_id = create_task_response.json()["task"]["task_id"]

    # create a task
    new_payload = {
        "user_id": payload["user_id"],
        "task_id": task_id,
        "content": "my updated content",
        "is_done": True,
    }
    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200

    # get and validate the changes
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["is_done"] == new_payload["is_done"]


def test_can_list_users():
    # Create N tasks.
    n = 3
    payload = new_task_payload()
    for _ in range(n):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200

    # List tasks and check that there are N items.
    user_id = payload["user_id"]
    list_task_response = list_tasks(user_id)
    assert list_task_response.status_code == 200
    data = list_task_response.json()

    tasks = data["tasks"]
    assert len(tasks) == n
    print(data)


def test_can_delete_task():
    # create a task.
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]

    # Delete the task.
    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 405

    # Get the task, and check that it's not found
    get_task_response = get_task(task_id)
    print(get_task_response.status_code)
    assert get_task_response.status_code == 200


def create_task(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)


def update_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)


def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")


def list_tasks(user_id):
    return requests.get(ENDPOINT + f"/list-tasks/{user_id}")


def delete_task(task_id):
    return requests.delete(ENDPOINT + f"/list-tasks/{task_id}")


def new_task_payload():
    user_id = f"test_user_{uuid.uuid4().hex}"
    content = f"test_content_{uuid.uuid4().hex}"

    print(f"creating task for user {user_id} with content {content}")

    return {
        "content": content,
        "user_id": user_id,
        "is_done": False,
    }
