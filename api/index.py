from flask import Flask, Response, jsonify, request

app = Flask(__name__)

@app.route('/api')
def hello_world():
    return 'Hello, World!'
