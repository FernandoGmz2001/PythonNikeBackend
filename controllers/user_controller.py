from flask import Blueprint, request
from controllers.models_folder.models import db, users

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['GET'])
def get_all_users():
    Users = users.query.all()
    return {'users': [user.to_dict() for user in Users]}, 200

@user_routes.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    if isinstance(user_data, list):
        for data in user_data:
            existing_user = users.query.filter_by(username=data['username']).first()
            if existing_user is None:
                new_user = users(
                    username=data['username'],
                    email=data['email'],
                    password=data['password']
                )
                db.session.add(new_user)
        db.session.commit()
        return {'message': 'Usuarios creados exitosamente'}, 201
    elif isinstance(user_data, dict):
        existing_user = users.query.filter_by(username=user_data['username']).first()
        if existing_user is None:
            new_user = users(
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password']
            )
            db.session.add(new_user)
            db.session.commit()
            return {'message': 'Usuario creado exitosamente'}, 201
        else:
            return {'message': 'El usuario ya existe'}, 200
    else:
        return {'error': 'Los datos enviados no son válidos'}, 400

@user_routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = users.query.get(user_id)
    if user:
        user_data = request.get_json()
        user.username = user_data['username']
        user.email = user_data['email']
        user.password = user_data['password']
        db.session.commit()
        return {'message': 'Usuario actualizado exitosamente'}, 200
    else:
        return {'error': 'Usuario no encontrado'}, 404

@user_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = users.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'message': 'Usuario eliminado exitosamente'}, 200
    else:
        return {'error': 'Usuario no encontrado'}, 404

@user_routes.route('/users/<string:username>', methods=['DELETE'])
def delete_user_by_username(username):
    user = users.query.filter_by(username=username).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'message': 'Usuario eliminado exitosamente'}, 200
    else:
        return {'error': 'Usuario no encontrado'}, 404