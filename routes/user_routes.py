from flask import Blueprint, jsonify, request
from controllers.user_controller import (
    create_user,update_user,delete_user_by_id,get_all_users
)

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/users", methods=["GET"])
def users():
    users = get_all_users()
    return jsonify(users)


@user_routes.route("/users", methods=["POST"])
def add_user():
    create_user()
    return jsonify({"message": "User created successfully"}), 201


@user_routes.route("/users/<user_id>", methods=["PUT"])
def update_user_route(user_id):
    # user_data = request.get_json()
    update_user(user_id)
    return jsonify({"message": "User updated successfully"}), 200


@user_routes.route("/users/<user_id>", methods=["DELETE"])
def delete_user_route(user_id):
    delete_user_by_id(user_id)
    return jsonify({"message": "User deleted successfully"}), 200

# @user_routes.route("/users/<username>", methods=["DELETE"])
# def delete_user_by_username_route(username):
#     delete_user_by_username(username)
#     return jsonify({"message": "User deleted successfully"}), 200