# POST method

import requests
import json

# Set up the connection to the API endpoint
url = 'http://localhost:5000/query'

# Specify the query parameters
data = {
    "list": 2,
    "unit": 1
}

# Send the GET request and store the response
response = requests.post(url, json=data)

# Print the status code and the data returned by the server
print("Status Code:", response.status_code)
print(json.dumps(response.json(), indent=4))
