from flask import render_template

class OrderListView:
    def render(orders):
        return render_template("order_list.html", orders=orders)

from flask import render_template

class OrderDetailView:
    def render(order):
        return render_template("order_detail.html", order=order)