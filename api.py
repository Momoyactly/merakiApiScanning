import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def get():
    return "a30ee592b51f2f382a1e9d2dd0baed8920e8d51a"

@app.route('/', methods=['POST'])
def post():
    print(request.data)
    return "a30ee592b51f2f382a1e9d2dd0baed8920e8d51a"

app.run(port=1050,debug=True,ssl_context=('cert.pem', 'key.pem'))