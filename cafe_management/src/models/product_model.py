class Product:
    def __init__(self, id, category_id, name, price, description):
        self.id = id
        self.category_id = category_id  # Đây là đối tượng của Category
        self.name = name
        self.price = price
        self.description = description

    def get_info(self):
        print(f"Mã sản phẩm: {self.id}")
        print(f"Loại: {self.category_id}")  # Lấy tên từ Category
        print(f"Tên sản phẩm: {self.name}")
        print(f"Giá: {self.price}")
        print(f"Mô tả: {self.description}")

    def update_id(self, id):
        self.id = id