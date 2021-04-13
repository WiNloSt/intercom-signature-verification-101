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
                        "text": "Thanks for submitting feedback ♥♥♥",
                        "style": "paragraph",
                    }
                ]
            }
        },
    }


@app.route('/api/initialize-inbox', methods=['POST'])
def initialize_inbox():
    verify_request(request)
    print('/initialize payload', request.get_json())

    return {
        'canvas': {
            'content': {
                'components': [
                    {"type": "text", "text": "Latest response", "style": "header"},
                    {
                        "type": "data-table",
                        "items": [
                            {"field": "Survey", "value": "Quarterly NPS survey with the name that is really long"},
                            {"field": "Timestamp", "value": "April 5, 2021 12:34PM UTC"},
                            {"field": "Responses", "value": "10"},
                            {"field": "Positive", "value": "5"},
                            {"field": "Neutral", "value": "3"},
                            {"field": "Negative", "value": "2"},
                        ],
                    },
                    {
                        "type": "list",
                        "items": [
                            {
                                "id": "1",
                                "title": "How likely are you to recommend Simple Shop to a friend or colleague?",
                                "subtitle": "\"Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of \"de Finibus Bonorum et Malorum\" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, \"Lorem ipsum dolor sit amet..\", comes from a line in section 1.10.32.\"",
                                "image": "https://user-images.githubusercontent.com/1937582/114507562-7ee8a700-9c5d-11eb-8fd1-0897071d3cc2.png",
                                "image_width": 50,
                                "image_height": 50,
                            },
                            {
                                "id": "2",
                                "title": "What is your favorite dish (choice)?",
                                "subtitle": "Sushi",
                                "image": "https://user-images.githubusercontent.com/1937582/114507878-f3234a80-9c5d-11eb-8689-9c3a8d37c4e3.png",
                                "image_width": 30,
                                "image_height": 30,
                            },
                            {
                                "id": "3",
                                "title": "Any other comments?",
                                "subtitle": "Two-liter bottle. US market Coke Zero bottles, showing 2 L (70.4 imp fl oz; 67.6 US fl oz) imperial conversion. Russian market 2.5 litre, 2 litre and 1.5 litre beer bottles. The two-litre bottle is a common container for soft drinks.",
                                "image": "https://user-images.githubusercontent.com/1937582/114514842-ea367700-9c65-11eb-9d36-657f90f650aa.png",
                                "image_width": 30,
                                "image_height": 30,
                            },
                        ],
                    },
                    {
                        "type": "button",
                        "id": "secondary-1",
                        "label": "See more on Simplesat",
                        "style": "secondary",
                        "action": {"type": "url", "url": "https://app.simplesat.io/customers/32094/"},
                    },
                ]
            }
        },
    }


@app.route('/api/submit-inbox', methods=['POST'])
def submit_inbox():
    verify_request(request)
    print('/submit payload', request.get_json())

    return {
        'canvas': {
            'content': {
                'components': [
                    {
                        "type": "text",
                        "text": "Thanks for submitting feedback ♥♥♥",
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
