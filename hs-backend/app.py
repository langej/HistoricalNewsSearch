from flask import Flask, json
from elasticsearch_helper import ElasticsearchHelper


app = Flask(__name__)
es_helper = ElasticsearchHelper()

@app.route("/")
def hello_docker() -> str:
    return "Backend listening on Port 5000."


@app.route('/<input>')
def search(input):
    """response = app.response_class(
        #response=json.dumps(es_helper.search(input)),
        response=es_helper.search(input),
        status=200,
        mimetype='application/json'
    )"""
    return json.dumps(es_helper.search(input, 100))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
