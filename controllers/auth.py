from flask import request, jsonify
# from werkzeug.security import check_password_hash
from .models_folder.models import users

def login():
    user_data = request.get_json()
    username = user_data.get('username')
    password = user_data.get('password')

    user = users.query.filter_by(username=username).first()

    if user and password(user.password, password):
        # Usuario autenticado correctamente
        # Realiza las acciones necesarias, como generar un token de acceso, establecer una sesión, etc.
        return jsonify({'message': 'Inicio de sesión exitoso'})
    else:
        # Credenciales inválidas
        return jsonify({'message': 'Credenciales inválidas'}), 401