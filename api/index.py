from flask import Flask, Response, jsonify, request

app = Flask(__name__)

@app.route('/api')
def hello_world():
    return 'Hello, World!'


@app.route('/api/initialize', methods=['POST'])
def initialize():
    return request.get_json()
