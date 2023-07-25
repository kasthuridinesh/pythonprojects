# Read data from json file

import json
# opening json file
Myjsonfile=open('Employee.json', 'r')
# for reading file
Jsondata = Myjsonfile.read()

# parse the json data. loads method is used to parse json data
# after parse the data is changed as json object, we can extract data by giving key
obj = json.loads(Jsondata)

# extract data from json using keys
print(str(obj['firstname']))
print(str(obj['lastname']))

# Extracting  address from json
print(str(obj['address']))

# printing line by line object in json file
for i in obj["address"]:
    print(i)
# converting  json object into python list
list = obj['address']

print(list)
# extracting specific element like street name
for i in range(len(list)):
    print("address of", i, "is.......")
    print("street",list[i].get("street"))
    # for printing city
    print("city is:",list[i].get("city"))
    # for printing state
    print("state is:",list[i].get("state"))


