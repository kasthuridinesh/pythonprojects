import requests

url = 'http://localhost:3000/posts/102'

response = requests.get(url)

# <Response [200]>-success
print(response)

# 200
print(response.status_code)

print(response.text)

print(response.url)

print(response.headers['Content-Type'])

print(response.content)

print(response.json())

print(type(response.json()))