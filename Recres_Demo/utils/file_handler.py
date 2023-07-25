import json


class JSONFileHandler:  # file handler mandatory for json ...
    # reading and writing jsons
    def __init__(self, file_path):
        self.file_path = file_path

    def __load_json(self):  # 1. read entire data from file for R & R
        with open(self.file_path, 'r') as file:
            return json.load(file)

    # def update(self, payload):
    #     data = self.load()
    #     data.update(payload)
    #     self.save(data)

    def get_value_by_key(self, key):
        json_data = self.__load_json()
        return json_data[key]

    # def write_to_file(self, file_path, data):  #
    #     pass
