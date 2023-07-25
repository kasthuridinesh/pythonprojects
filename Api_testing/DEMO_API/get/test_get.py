# Importing Yaml and getting Get Api endpoint
import yaml


#
def test_get():
    with open("API_endpoint.yaml", "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        print(data)
        yr = data['get']['endpoint']
        print(yr)
