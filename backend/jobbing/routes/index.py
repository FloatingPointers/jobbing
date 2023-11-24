from flask import Flask, request, jsonify
from jobbing import app, db
from jobbing.models.user import User

@app.route('/', methods=['GET'])
def index_function():
    return 'Hello, world!'


@app.route('/user', methods=['GET', 'POST', 'DELETE'])
def addUser():
    if request.method == 'DELETE':
        user = User.query.filter_by(username='new_username').first()
        db.session.delete(user)
        db.session.commit()
        return 'deleting'
    elif request.method == 'POST':
        new_user = User(username='new_username', email='new_email@example.com')
        db.session.add(new_user)
        db.session.commit()
        return 'posted up'
    elif request.method == 'GET':
        users = User.query.all()
        users_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
        return jsonify(users_list)
    else:
        return 'Kaboom'

@app.route('/get_user_info/<id>', methods=['GET'])
def get_user_info(id):
    user = User.query.filter_by(id=id).first()
    return jsonify({'picture': user.picture, 'given_name': user.given_name})

    