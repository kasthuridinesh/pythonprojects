# post function
import json
import jsonpath
import requests
import yaml


def test_post():

    with open("API_endpoint.yaml", "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        print(data)
        yr = data['post']['endpoint']
        print(yr)
        f = open("api.json", "r")
        request_json = json.loads(f.read())
        response = requests.post(yr, request_json)
        id = jsonpath.jsonpath(response.json(), "id")
        print(id[0])