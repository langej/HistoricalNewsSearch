from flask import Flask
from elasticsearch import Elasticsearch


app = Flask(__name__)
es = Elasticsearch('http://localhost:9200')


@app.route("/")
def hello_docker() -> str:
    return "Hello Docker!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")