import requests
import json


url = 'http://localhost:5000/query'

data = {
    "list": 2,
    "unit": 1
}

response = requests.post(url, json=data)

print(json.dumps(response.json(), indent=4))
