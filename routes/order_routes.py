from flask import Blueprint
from controllers.order_controller import get_all_orders,create_order

order_routes = Blueprint('order_routes', __name__)

@order_routes.route('/orders', methods=['GET'])
def get_orders():
    return get_all_orders()

@order_routes.route('/orders', methods=['POST'])
def post_order():
    return create_order()