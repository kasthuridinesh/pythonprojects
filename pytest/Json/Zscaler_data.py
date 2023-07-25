import json

# open zscaler employee json file in pycharm
with open("Zscaler_employee.json", "r") as json_file:
    data = json.load(json_file)
    # printing all data in zscaler employee data
    for i in data["Zscaler employee data"]:
        print(i)

    '''#  printing datas in the key valuve pair
    for (k, v) in data.items("Zscaler employee data"):
        print("key:" + k)
        print("value:" + str(v))
'''

data1 = json.dumps(data, indent=2)
print(data1.find('Name'))