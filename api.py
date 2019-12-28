import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def get():
    return "9239238"

@app.route('/', methods=['POST'])
def post():
    print(request.data)
    return request.data

app.run(port=1050,debug=True)