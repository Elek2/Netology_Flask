from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello():

    json_data = request.json
    headers = request.headers
    arg = request.args

    return jsonify({"answer": 'Hello'})


if __name__ == '__main__':
    app.run(debug=True)
