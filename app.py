from flask import Flask, request, jsonify
import sqlite3


app = Flask(__name__)


@app.route('/query', methods=['POST'])
def query_db():
    """
    Receives JSON in body, parses it, constructs an SQLite query, returns query
    result in JSON.
    """
    list_id = request.json['list']
    unit_id = request.json['unit']

    # Connect to database
    conn = sqlite3.connect('GRE_3333.db')
    cur = conn.cursor()
    # Construct SQLite query for GRE_3333.db
    query = """
    SELECT Vocabulary.word, Meaning.word_id, Meaning.meaning_US,
    Meaning.sentence
    FROM Meaning
    INNER JOIN Vocabulary ON Meaning.word_id = Vocabulary.word_id
    WHERE Meaning.list = ? AND Meaning.unit = ?
    """

    cur.execute(query, (list_id, unit_id))

    result = cur.fetchall()
    output = {}

    for word, word_id, meaning_US, sentence in result:
        output[word] = {
            "word_id": word_id,
            "meaning_US": meaning_US,
            "sentence": sentence
        }

    conn.close()

    return jsonify(output)


@app.route('/query-get', methods=['GET'])
def query_get():
    """
    Receives list and unit IDs, constructs an SQLite query, returns query
    result in JSON.
    """
    list_id = request.args.get('list')
    unit_id = request.args.get('unit')
    print(f'Received parameters: list={list_id}, unit={unit_id}')

    # Connect to database
    conn = sqlite3.connect('GRE_3333.db')
    cur = conn.cursor()
    # Construct SQLite query for GRE_3333.db
    query = """
    SELECT Vocabulary.word, Meaning.word_id, Meaning.meaning_US,
    Meaning.sentence
    FROM Meaning
    INNER JOIN Vocabulary ON Meaning.word_id = Vocabulary.word_id
    WHERE Meaning.list = ? AND Meaning.unit = ?
    """

    cur.execute(query, (list_id, unit_id))

    result = cur.fetchall()
    output = {}

    for word, word_id, meaning_US, sentence in result:
        output[word] = {
            "word_id": word_id,
            "meaning_US": meaning_US,
            "sentence": sentence
        }

    conn.close()

    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)
