from flask import Blueprint, request, jsonify
from controllers.auth_controller import login,register,decode_token

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/login', methods=['POST'])
def login_route():
    return login(request)

@auth_routes.route('/register', methods=['POST'])
def register_route():
    return register(request)

@auth_routes.route('/decode/<token>', methods=['POST'])
def decode_token_route(token):
    return decode_token(token)