import yaml


def test_delete():
    with open("API_endpoint.yaml", "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        print(data)
        yr = data['delete']['endpoint']
        print(yr)

