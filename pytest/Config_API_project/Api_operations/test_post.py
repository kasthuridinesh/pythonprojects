import json
import jsonpath
import requests
import yaml
import pytest
from _pytest import mark
from Post_Json import *

from fixtures import conftest


# @pytest.fixture(scope="module")
# def start_exec():
#     global data
#     with open("API_endpoint.yaml", "r") as yamlfile:
#         data = yaml.load(yamlfile, Loader=yaml.FullLoader)
#     yield
#     print("quite")

@pytest.mark.selenium_exam
def test_post(start_exec):
    data = start_exec
    # with open("API_endpoint.yaml", "r") as yamlfile:
    #     data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    # print(data)
    yr = data['post']['endpoint']
    print(yr)
    f = open("api.json", "r")
    request_json = json.loads(f.read())
    response = requests.post(yr, request_json)
    id = jsonpath.jsonpath(response.json(), "id")
    print(id[0])
    print(response)
    print(response.json())
    return response.json()

