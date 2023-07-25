#Converting python dictionary into json data
import json

# Data to be written
dictionary = {
    "id": "04",
    "name": "kasthuri",
    "department": "QA"
}

# Serializing json
# json.dump() method can be used for writing to JSON file.

""" converting python object into json object, this process is known as serialization """
json_object = json.dumps(dictionary, indent=4)
print(json_object)

"""
dictionary – name of dictionary which should be converted to JSON object.
file pointer – pointer of the file opened in write or append mode.
"""
