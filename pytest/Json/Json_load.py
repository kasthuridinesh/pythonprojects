import json
import logging

# opening json file
with open("data.json", "r") as json_file:
    data = json.load(json_file)
    for p in data["students"]:
        logging.info("printing data one by one", p)

logging.info("printing all items ", data.items())

# ****  creating json file ***
with open("data2.json", "w") as json_file:
    json.dump(data, json_file)
