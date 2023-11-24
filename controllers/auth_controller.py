import jwt
from flask import jsonify
from werkzeug.security import check_password_hash
from controllers.models_folder.models import users
from datetime import datetime, timedelta

def login(request):
    user_data = request.get_json()
    email = user_data.get('email')
    password = user_data.get('password')

    user = users.query.filter_by(email=email).first()

    if user and user.password == password:
        # Usuario autenticado correctamente
        # Generar el token JWT
        token = jwt.encode({
            'user_id': user.userId,
            'exp': datetime.utcnow() + timedelta(hours=1)  # Expira en 1 hora
        }, 'arbol')
        

        return jsonify({'token': token})
    else:
        # Credenciales inválidas
        return jsonify({'message': 'Credenciales inválidas'}), 401