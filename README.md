# vocab-service

## How to programmatically REQUEST data from vocab-service
1. Start server
    - python3 app.py
    - starts a server on http://localhost:5000
2. Using Python: POST method

    ```
    # replace list_id and unit_id with whatever values you need to query.
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
    # replace list_id and unit_id with whatever values you need to query.
    import requests
    import json
    url = "http://localhost:5000/query-get"
    params = {
    "list": list_id,
    "unit": unit_id
    }
    response = requests.get(url, params=params)
    print(json.dumps(response.json(), indent=4))

3. using cURL: POST method
    ```
    curl -i -X POST -H "Content-Type: application/json" -d "{\"list\":list_id, \"unit\": unit_id}" http://localhost:5000/query
    ```
4. using cURL: GET method
    ```
    # replace (list_id) and (unit_id) with whatever values you need to query.
    curl -i -X GET "http://localhost:5000/query-get?list=(list_id)&unit=(unit_id)"
    ```

## How to programmatically RECEIVE data from vocab-service
