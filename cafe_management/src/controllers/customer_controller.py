from collections import deque

from cafe_management.src.services import CustomerService

class CustomerController:
    def __init__(self):
        self._category_service = CustomerService("Data/CategoryData.txt")  # Dịch vụ quản lý danh mục sản phẩm
        self._customers = deque()  # Lấy danh sách tất cả các loại sản phẩm
