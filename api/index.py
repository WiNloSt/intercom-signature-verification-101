import hashlib
import hmac
import os

from flask import Flask, Request, abort, request

app = Flask(__name__)


@app.route('/api')
def hello_world():
    return 'Hello, World!'


@app.route('/api/initialize', methods=['POST'])
def initialize():
    verify_request(request)
    print('/initialize payload', request.get_json())

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
        },
    }


@app.route('/api/submit', methods=['POST'])
def submit():
    verify_request(request)
    print('/submit payload', request.get_json())

    return {
        'canvas': {
            'content': {
                'components': [
                    {
                        "type": "text",
                        "text": "Thanks for submitting feedback (without submit) ♥♥♥",
                        "style": "paragraph",
                    }
                ]
            }
        },
    }


def verify_request(request: Request) -> None:
    intercom_signature = request.headers.get('X-Body-Signature') or ''
    INTERCOM_CLIENT_SECRET = os.environ['INTERCOM_CLIENT_SECRET']
    calculated_intercom_signature = hmac.new(
        INTERCOM_CLIENT_SECRET.encode(), request.get_data(), hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(intercom_signature, calculated_intercom_signature):
        abort(401)
