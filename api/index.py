from flask import Flask, Response, jsonify, request

app = Flask(__name__)


@app.route('/api')
def hello_world():
    return 'Hello, World!'


@app.route('/api/initialize', methods=['POST'])
def initialize():
    import hashlib
    import hmac

    INTERCOM_CLIENT_SECRET = os.environ.get('INTERCOM_CLIENT_SECRET')

    intercom_signature = request.headers.get('X-Body-Signature')
    print('Intercom signature', intercom_signature)
    return {
        'canvas': {
            'content': {
                'components': [
                    {
                        'type': 'button',
                        'label': 'Click me boi!',
                        'style': 'primary',
                        'id': 'button_id',
                        'action': {'type': 'submit'},
                    }
                ]
            }
        }
    }
