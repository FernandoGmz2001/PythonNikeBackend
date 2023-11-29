from flask import Blueprint, jsonify
from controllers.models_folder.models import orders

order_controller = Blueprint('order_controller', __name__)

@order_controller.route('/orders', methods=['GET'])
def get_all_orders():
    # Obtener todas las órdenes de la base de datos
    all_orders = orders.query.all()

    # Convertir las órdenes a una lista de diccionarios
    dicOrders = [order.to_dict() for order in all_orders]

    # Devolver las órdenes como una respuesta JSON
    return jsonify(dicOrders)