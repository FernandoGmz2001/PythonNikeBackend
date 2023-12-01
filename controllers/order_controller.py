from flask import Blueprint, jsonify, request
from controllers.models_folder.models import orders, db

order_controller = Blueprint("order_controller", __name__)


@order_controller.route("/orders", methods=["GET"])
def get_all_orders():
    # Obtener todas las órdenes de la base de datos
    all_orders = orders.query.all()

    # Convertir las órdenes a una lista de diccionarios
    dicOrders = [order.to_dict() for order in all_orders]

    # Devolver las órdenes como una respuesta JSON
    return jsonify(dicOrders)


@order_controller.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()
    new_order = orders(**data)
    db.session.add(new_order)
    db.session.commit()
    return (
        jsonify(
            {"message": "Order created successfully", "Order": new_order.to_dict()}
        ),
        201,
    )

@order_controller.route("/orders/<int:order_id>", methods=["DELETE"])
def delete_order_by_id(order_id):
    order = orders.query.get(order_id)

    if not order:
        return jsonify({"message": "Orden no encontrada"}), 404
    # Si la orden existe, eliminarla y confirmar la transacción
    db.session.delete(order)
    db.session.commit()

    # Devolver un mensaje de éxito
    return jsonify({"message": "Order deleted successfully"}), 200
