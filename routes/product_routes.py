from flask import Blueprint, jsonify, request
from controllers.product_controller import (
    get_all_products,
    create_products,
    update_product,
    delete_product,
)

product_routes = Blueprint("product_routes", __name__)


@product_routes.route("/products", methods=["GET"])
def products():
    products = get_all_products()
    return jsonify(products)


@product_routes.route("/products", methods=["POST"])
def add_product():
    create_products()
    return jsonify({"message": "Product created successfully"}), 201


@product_routes.route("/products/<product_id>", methods=["PUT"])
def update_product_route(product_id):
    product_data = request.get_json()
    update_product(product_id, product_data)
    return jsonify({"message": "Product updated successfully"}), 200


@product_routes.route("/products/<product_id>", methods=["DELETE"])
def delete_product_route(product_id):
    delete_product(product_id)
    return jsonify({"message": "Product deleted successfully"}), 200
