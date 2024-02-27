# GET method

import requests
import json

# Set up the connection to the API endpoint
url = "http://localhost:5000/query-get"

# Specify the query parameters
params = {
    "list": 1,
    "unit": 2
}

# Send the GET request and store the response
response = requests.get(url, params=params)

# Print the status code and the data returned by the server
print("Status Code:", response.status_code)
print(json.dumps(response.json(), indent=4))
