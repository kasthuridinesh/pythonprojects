import requests
import json

url = 'http://localhost:3000/posts/2'

headers = {'Content-Type': 'application/json; charset=UTF-8'}

response = requests.delete(url, headers=headers)

print(response.status_code)  # 200

print(response.ok)  # True

print(type(response.text))  # <class 'str'>

print(response.url)  # https://jsonplaceholder.typicode.com/posts/1

print(response.headers['Content-Type'])  # application/json; charset=utf-8

print(response.encoding)  # utf-8