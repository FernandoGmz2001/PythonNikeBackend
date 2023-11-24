from flask import Blueprint, request, jsonify
from controllers.auth_controller import login

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/login', methods=['POST'])
def login_route():
    return login(request)