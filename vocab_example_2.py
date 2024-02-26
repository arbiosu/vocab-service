import requests
import json

# Specify the URL of your Flask app's endpoint
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
