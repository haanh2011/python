class Order():
    def __init__(self, order_id, customer, order_date, total_amount):
        self.order_id = order_id
        self.customer = customer  # Có thể là một đối tượng Customer
        self.order_date = order_date
        self.total_amount = total_amount
        self.order_details = []  # Danh sách các đối tượng OrderDetail

    def add_order_detail(self, product, quantity, price):
        order_detail = OrderDetail(product, quantity, price)
        self.order_details.append(order_detail)

    def update_id(self, id):
        self.id = id
class OrderDetail:
    def __init__(self, id_product, quantity, price):
        self.id_product = id_product  # Có thể là một đối tượng Product
        self.quantity = quantity
        self.price = price

    def update_id(self, id):
        self.id = id