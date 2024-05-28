from app.models import Order

class OrderController:
    def get_orders():
        # Obtener lista de órdenes de la base de datos
        orders = Order.query.all()
        return orders

    def get_order(order_id):
        # Obtener una orden específica de la base de datos
        order = Order.query.get(order_id)
        return order