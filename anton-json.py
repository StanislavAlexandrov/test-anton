import json
from urllib.request import urlopen
import requests


# url = "https://jsonplaceholder.typicode.com/users/1/todos"

# response = urlopen(url)

# data = json.loads(response.read())

# print(data[0])

x = requests.get('https://jsonplaceholder.typicode.com/users/1/todos')

print(x)
print(x.text)
