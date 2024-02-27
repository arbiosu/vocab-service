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

## Example Output

    - output for the following parameters: list=1, unit=3
    ```
    {
  "comestible": {
    "meaning_US": "that can be eaten",
    "sentence": "A way of separating some comestible red pigment from the red turnip is studied by this paper.",
    "word_id": "1ff01173de374d78ae2d51a9be77761b"
  },
  "denunciation": {
    "meaning_US": "an act of criticizing strongly in public",
    "sentence": "All parties joined in bitter denunciation of the terrorists.",
    "word_id": "87ea2db2099147c897bd82274a9bceda"
  },
  "fraudulent": {
    "meaning_US": "characterized by, based on, or done by fraud",
    "sentence": "The protests started after the parliamentary elections last December which were widely seen as fraudulent.",
    "word_id": "f54e80cdc1724fdc80b95ad2d4efe8be"
  },
  "horrific": {
    "meaning_US": "causing horror or shock",
    "sentence": "Professor Edward Baranowski of California State University said that the results reflected the horrific drop-out rates of US high schools.",
    "word_id": "88114ca638e344ddaf57c6e64d4eda97"
  },
  "infraction": {
    "meaning_US": "the act or an instance of infringing; a violation",
    "sentence": "He was criticized for his infraction of the discipline.",
    "word_id": "3b7def4330404d5e90683e194dce4238"
  },
  "odious": {
    "meaning_US": "arousing or deserving hatred or repugnance",
    "sentence": "Mr. Smith is certainly the most odious man I have ever met.",
    "word_id": "c3fc3aaf43fb45db976e96cb2f75560a"
  },
  "oust": {
    "meaning_US": "to remove from or dispossess of property or position by legal action, by force, or by the compulsion of necessity",
    "sentence": "The leaders have been ousted from power by nationalists.",
    "word_id": "4115e2440fc244a1981d32e7099b9cd0"
  },
  "pillory": {
    "meaning_US": "to expose to public contempt, ridicule, or scorn",
    "sentence": "A man has been forced to resign as a result of being pilloried by some of the press.",
    "word_id": "cd33eb8cf2fa4e9daa49f586199c40ca"
  },
  "rhapsody": {
    "meaning_US": "the expression of great enthusiasm or happiness in speech or writing",
    "sentence": "The mayor launched into a long rhapsody about his plans for the city.",
    "word_id": "20492a7530984d39825dc351812ddbe4"
  },
  "stemma": {
    "meaning_US": "a family tree; a tree diagram showing a reconstruction of the transmission of manuscripts of a literary work",
    "sentence": "Stemma is a scroll recording the genealogy of a family and the stories of key members.",
    "word_id": "3d046cabee084301b95c3ca03f7a42ea"
  }
}
    ```

## UML Sequence Diagram
![UML diagram](/sequence_diagram_vocab_service.PNG)
