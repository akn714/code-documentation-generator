#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports
from flask import Flask, jsonify, request
# from flask_limiter import Limiter
# from flask_limiter.util import get_remote_address
from generator import generate

# web app
app = Flask(__name__)
# limiter = Limiter(app, key_func=get_remote_address)

# keep alive
@app.route('/')
def index():
    return jsonify(
        {
            'status': "ONLINE"
        }
    )

# API endpoint
@app.route('/api/generate', methods=['POST'])
# @limiter.limit("2/minute")  # Set the rate limit to 10 requests per minute
def generate_doc():
    try:
        content_type = request.headers.get('Content-Type')
        if content_type == 'text/plain':
            data = request.get_data().decode('utf-8')
        elif content_type == 'application/json':
            data = request.get_json()['text']
        elif content_type == 'application/x-www-form-urlencoded':
            text = request.form.get('text')
        else:
            return jsonify(
                {
                    'error': 'Unsupported Content-Type'
                }
            ), 415

        response = generate(code=data)
        return jsonify(
            {
                'markdown': response
            }
        )

    except Exception as e:
        error_message = str(e)
        return jsonify({'error': error_message}), 500


# main function
def start_web_server():
    app.run(host="0.0.0.0", debug=True)

# Run the application
if __name__ == '__main__':
    start_web_server()

