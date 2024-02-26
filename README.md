# vocab-service

## How to programmatically REQUEST data from vocab-service
1. Start server
    - python3 app.py
    - starts a server on http://localhost:5000
2. Send JSON vocab-service
    - using requests and json:
    ```
    import requests
    import json
    url = url = 'http://localhost:5000/query'
    data = {
    "list": list_id,
    "unit": unit_id
    }
    response = requests.post(url, json=data)

### How to programmatically RECEIVE data from vocab-service