from flask import Flask, json, request, send_file, Response
from flask_cors import CORS
from elasticsearch_helper import ElasticsearchHelper
from evaluation_handler import persist_evaluation_data
import os
import difflib

app = Flask(__name__)
CORS(app)
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

@app.route('/evaluation', methods=['POST'])
def evaluate():
    if request.method == 'POST':
        post_data = request.get_json()
        persist_evaluation_data(json.dumps(post_data))
        return json.dumps(post_data)

@app.route('/recommendation/<query>')
def get_recommendation(query):
    logs = []
    matches = {}
    with open('./logs/log.txt') as log:
        content = log.readlines()
        for line in content:
            log_json = json.loads(line)
            logs.append(log_json['query'])
    for log in logs:
        seq = difflib.SequenceMatcher(a=query.lower(), b=log.lower())
        matches[log] = seq.ratio()
        s = [(k, matches[k]) for k in sorted(matches, key=matches.get, reverse=True)]
    return json.dumps(s[:5])

@app.route('/image/<id>')
def get_image(id):
    image = './Xml_Converter/Data/View/' + id + '.png'
    if os.path.isfile(image):
        return send_file(image, mimetype='image/png')
    else:
        return Response(status=404)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

