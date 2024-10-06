from collections import deque

from cafe_management.src.services import ProductService

class ProductController:
    def __init__(self):
        self._product_service = ProductService("Data/ProductData.txt")
        self._products = deque()
