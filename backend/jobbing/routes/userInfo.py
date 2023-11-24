from flask import Flask, request, jsonify
from jobbing.models.user import User
from jobbing.utils.google import get_id
from jobbing import app, db


@app.route('/me', methods=['GET'])
def get_basic_info():
    jwt_token = request.cookies.get('jwt_token')
    print(request.cookies)
    if not jwt_token:
        return jsonify({'error': 'No jwt found.'}), 401
    user_id = get_id(jwt_token)
    
    user = User.query.filter_by(id=user_id).first()
    
    return jsonify({'picture': user.picture, 'given_name': user.given_name})