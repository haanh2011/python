from collections import deque

from cafe_management.src.services import OrderService

class OrderController:
    def __init__(self):
        self._order_service = OrderService("Data/OrderData.txt")  # Dịch vụ quản lý danh mục sản phẩm
        self._orders = deque()  # Lấy danh sách tất cả các loại sản phẩm
