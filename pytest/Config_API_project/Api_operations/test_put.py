import requests
import yaml


def test_post():

    with open("API_endpoint.yaml", "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        print(data)
        yr = data['put']['endpoint']
        print(yr)

        todo = {"userId": 1, "title": "Wash car", "completed": True}
        print("*********************Put****************")
        response = requests.put(yr,json=todo)
        print(response.json())
        {'userId': 1, 'title': 'Wash car', 'completed': True, 'id': 10}
        print(response.status_code)
        assert response.status_code == 200

