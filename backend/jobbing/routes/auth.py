from flask import Flask, request, jsonify, abort
from jobbing import app, db
from jobbing.models.user import User
import logging

from jobbing.utils.google import exchange_code


@app.route('/auth/google', methods=['POST'])
def google_auth():
    try:
        code = request.json['code']
        if code is None:
            abort(401)
        credentials = exchange_code(code)
        if credentials is None:
            abort(401)
        print(credentials)
        
        return 'Hello, world!'
    except Exception as e:
        print(e)
        abort(500)

@app.route('/auth/redirect', methods=['GET', 'POST'])
def google_auth_redirect():
    print('Got auth redirect callback')
    print(str(request.json))