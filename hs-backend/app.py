import os
from flask import Flask


app = Flask(__name__)
port = os.environ['PORT']


@app.route("/")
def hello_docker() -> str:
    return "Backend listening on Port " + str(port) + "."


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
