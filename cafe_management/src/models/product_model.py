class Product:
    def __init__(self, id_pro, name, price, description, category):
        self.id_pro = id_pro
        self.name = name
        self.price = price
        self.description = description
        self.category = category # Đây là đối tượng của Category

    def get_product_info(self):
        print(f"Mã sản phẩm: {self.id}")
        print(f"Tên sản phẩm: {self.name}")
        print(f"Giá: {self.price}")
        print(f"Mô tả: {self.description}")
        print(f"Loại: {self.category.name}")  # Lấy tên từ Category



