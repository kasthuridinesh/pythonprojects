# Json support different primitive data type :
#list, tuple, string,integer, float,boolean

import json
#list convert into Array
print(json.dumps(['welcome','to','Atmecs']))

# tuple conversion to Array
print(json.dumps(("Welcome", "to", "Atmecs")))

# string conversion to String
print(json.dumps("Hi"))

# int conversion to Number
print(json.dumps(123))

# float conversion to Number
print(json.dumps(23.572))

# Boolean conversion to their respective values
print(json.dumps(True))
print(json.dumps(False))

# None value to null
print("None value to null:",json.dumps(None))