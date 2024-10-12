from src.models.product_model import Product

class ProductService:
    def __init__(self, products = None):
        if products is None:
            self.products = []
        else:
            self.products = products
    def add_new_product(self, products, id_pro, name, price, description, category):
        # Tạo một đối tượng Product mới
        new_product = Product(id_pro, name, price, description, category)
        products.append(new_product)
        return new_product
