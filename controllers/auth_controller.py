import jwt
from flask import jsonify
from werkzeug.security import check_password_hash
from controllers.models_folder.models import users
from controllers.models_folder.models import db
from datetime import datetime, timedelta

def login(request):
    user_data = request.get_json()
    email = user_data.get('email')
    password = user_data.get('password')
    userId = user_data.get('userId')

    user = users.query.filter_by(email=email).first()

    print(user.userId)
    if user and user.password == password:
        # Usuario autenticado correctamente
        # Generar el token JWT solo para el usuario con ID 3
        if user.userId == 3:
            token = jwt.encode({
                'user_id': user.userId,
                'exp': datetime.utcnow() + timedelta(hours=1)  # Expira en 1 hora
            }, 'arbol')
            print(token)
            return jsonify({'token': token, 'status': 200, 'email': email, 'userId': user.userId}), 200
        return jsonify({'status': 200, 'email': email}), 200
    else:
        # Credenciales inválidas
        return jsonify({'message': 'Credenciales inválidas', 'status': 401}), 401

def register(request):
    user_data = request.get_json()
    email = user_data.get('email')
    username = user_data.get('username')
    print(email)
    print(username)
    password = user_data.get('password')

    # Verificar si el usuario ya existe en la base de datos
    existing_user = users.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'message': 'El usuario ya existe'}), 400

    # Crear un nuevo usuario
    new_user = users(email=email, password=password,username=username)
    # Guardar el nuevo usuario en la base de datos
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Usuario registrado exitosamente'}), 201


def decode_token(token):
    try:
        decoded_token = jwt.decode(token, 'arbol', algorithms=['HS256'])
        return decoded_token
    except jwt.ExpiredSignatureError:
        # El token ha expirado
        return {'error': 'Token expirado'}
    except jwt.InvalidTokenError:
        # El token es inválido
        return {'error': 'Token inválido'}