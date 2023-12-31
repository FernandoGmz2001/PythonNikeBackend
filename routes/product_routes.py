from flask import Blueprint, jsonify, request
from controllers.product_controller import (
    get_all_products,
    create_products,
    update_product,
    delete_product,
    delete_product_by_name,
    get_product_by_id,
    export_products,
    import_excel
)

product_routes = Blueprint("product_routes", __name__)


@product_routes.route("/products", methods=["GET"])
def products():
    products = get_all_products()
    return jsonify(products)

@product_routes.route("/products/<int:product_id>", methods=["GET"])
def product_by_id(product_id):
    product = get_product_by_id(product_id)
    if product:
        return jsonify(product)
    else:
        return jsonify({"message": "Product not found"}), 404

@product_routes.route("/products", methods=["POST"])
def add_product():
    create_products()
    return jsonify({"message": "Product created successfully"}), 201


@product_routes.route("/products/<product_id>", methods=["PUT"])
def update_product_route(product_id):
    product_data = request.get_json()
    update_product(product_id, product_data)
    return jsonify({"message": "Product updated successfully"}), 200


@product_routes.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product_route(product_id):
    product = get_product_by_id(product_id)
    if product:
        delete_product(product_id)
        return jsonify({"message": "Product deleted successfully"}), 200
    else:
        return jsonify({"error": "The product was binded to an order"}), 404

def delete_product_by_name_route(product_name):
    delete_product_by_name(product_name)
    return jsonify({"message": "Product deleted successfully"}), 200

@product_routes.route("/products/export", methods=["GET"])
def generate_excel():
    export_products()
    return jsonify({"message": "Products exported successfully"}), 200


@product_routes.route("/products/import", methods=["POST"])
def import_excel_route():
    file = request.files["file"]
    if file and file.filename.endswith(".xlsx"):
        file.save("temp.xlsx")  # Guardar el archivo temporalmente
        import_excel("temp.xlsx")  # Importar el archivo Excel
        return jsonify({"message": "File imported successfully"}), 200
    else:
        return jsonify({"error": "Invalid file format"}), 400