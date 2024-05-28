from app.models import User, Order
from app.views import OrderListView, OrderDetailView
from app.controllers import OrderController
from app.services import PaymentService, ShippingService

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the app!"

@app.route("/orders", methods=["GET"])
def order_list():
    orders = OrderController.get_orders()
    return OrderListView.render(orders)

@app.route("/orders/<int:order_id>", methods=["GET"])
def order_detail(order_id):
    order = OrderController.get_order(order_id)
    return OrderDetailView.render(order)

if __name__ == "__main__":
    app.run(debug=True)