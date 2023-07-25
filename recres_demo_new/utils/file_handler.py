import json


class JSONFileHandler:

    def __init__(self, file_path):
        self.file_path = file_path

    def __load_json(self):  # Read entire data from file for Request & Response jsons
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def get_value_by_key(self, key):
        json_data = self.__load_json()
        return json_data[key]

    # def write_to_file(self, file_path, data):  #
    #     pass

    # def update(self, payload):
    #     data = self.load()
    #     data.update(payload)
    #     self.save(data)
