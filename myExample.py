import json
from urllib.request import urlopen
import requests

url = "https://jsonplaceholder.typicode.com/users/1/todos"
z=urlopen(url)
print(z)
y=json.loads(z.read())
print(y)

xx=requests.get("https://jsonplaceholder.typicode.com/users/1/todos")
print(xx)

