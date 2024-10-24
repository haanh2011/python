class Order():
    def __init__(self, id, staff_id, customer_id, total_price):
        self.id = id
        self.customer_id = customer_id  # Có thể là một đối tượng Customer
        self.total_price = total_price
        self.staff_id = staff_id

    def update_id(self, id):
        self.id = id


class OrderDetail:
    def __init__(self, id, order_id, product_name, price, quantity):
        self.id = id
        self.order_id = order_id
        self.product_name = product_name  # Có thể là một đối tượng Product
        self.quantity = quantity
        self.price = price

    def update_id(self, id):
        self.id = id
