class Invoice:
    def __init__(self, id, order_id):
        self.id = id
        self.order_id = order_id
        self.total_amount = 0
    def update_id(self, id):
        self.id = id
    def update_total_amount(self, total_amount):
        self.total_amount = total_amount
