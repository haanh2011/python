from collections import deque

from cafe_management.src.services import CategoryService, ProductService


class CategoryController:
    def __init__(self):
        self._category_service = CategoryService("Data/CategoryData.txt")  # Dịch vụ quản lý danh mục sản phẩm
        self._product_service = ProductService("Data/ProductData.txt")  # Dịch vụ quản lý sản phẩm
        self._categories = deque()  # Lấy danh sách tất cả các loại sản phẩm
        self._products = deque()  # Lấy danh sách tất cả các sản phẩm
