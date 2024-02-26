# vocab-service

## How to programmatically REQUEST data from vocab-service
1. Start server
    - python3 app.py
    - starts a server on http://localhost:5000
2. Using Python: POST method
    **replace list_id and unit_id with whatever values
    you need to query.**
    ```
    import requests
    import json
    url = 'http://localhost:5000/query'
    data = {
    "list": list_id,
    "unit": unit_id
    }
    response = requests.post(url, json=data)
    ```
3. Using Python: GET method
    ```
    import requests
    import json
    url = "http://localhost:5000/query-get"
    params = {
    "list": 1,
    "unit": 2
    }
    response = requests.get(url, params=params)
    print("Status Code:", response.status_code)
    print(json.dumps(response.json(), indent=4))

3. Send JSON to vocab-service using cURL: POST method
    ```
    curl -i -X POST -H "Content-Type: application/json" -d "{\"list\":1, \"unit\": 2}" http://localhost:5000/query
    ```


## How to programmatically RECEIVE data from vocab-service
