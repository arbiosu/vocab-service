# vocab-service
1. Start server on http://localhost:5000
    ```
    python3 app.py
    ```

## API endpoints:
1. POST:
    - http://localhost:5000/query
    - receives JSON in body
2. GET:
    - http://localhost:5000/query-get
    - receives JSON in the url as parameters

## How to programmatically REQUEST data from vocab-service

1. Using Python: POST method

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

2. Using Python: GET method
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

## How to programmatically RECEIVE data from vocab-service

1. Using Python - POST/GET method:
    - follow instructions for REQUESTING data, and then print the json:
    ```
    ...
    ...
    print(json.dumps(response.json(), indent=4))
    ```

2. using cURL: POST method
    ```
    # replace list_id and unit_id with whatever values you need to query.
    curl -i -X POST -H "Content-Type: application/json" -d "{\"list\":list_id, \"unit\": unit_id}" http://localhost:5000/query
    ```
    - this will print the output to the terminal. Alternatively, you can save
    the output to a file by adding -o [filename]
3. using cURL: GET method
    ```
    # replace list_id and unit_id with whatever values you need to query.
    curl -i -X GET "http://localhost:5000/query-get?list=list_id&unit=unit_id"
    ```
    - this will print the output to the terminal. Alternatively, you can save
    the output to a file by adding -o [filename]

## UML Sequence Diagram
![UML diagram](/sequence_diagram_vocab_service.PNG)
