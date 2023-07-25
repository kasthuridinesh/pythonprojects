
import requests
import json

url = 'http://localhost:3000/posts'

data = {'title': 'buy new mouse', 'body': 'I need to buy a new mouse !', 'userId': 8, 'id': 112}
headers = {'content-type': 'application/json; charset=UTF-8'}

response = requests.post(url, data=json.dumps(data), headers=headers)

# 201
print(response.status_code)

# True
print(response.ok)

# b'{\n  "title": "buy new mouse",\n  "body": "I need to buy a new mouse !",\n  "userId": 5,\n  "id": 101\n}'
print(response.content)

# {
#   "title": "buy new mouse",
#   "body": "I need to buy a new mouse !",
#   "userId": 5,
#   "id": 101
# }
print(response.text)

# <class 'str'>
print(type(response.text))

# https://jsonplaceholder.typicode.com/posts
print(response.url)

# application/json; charset=utf-8
print(response.headers['Content-Type'])

# utf-8
print(response.encoding)