from typing import List


class OrderItem:
    def __init__(self, maSP, soLuong, donGia):
        self.maSP = maSP
        self.soLuong = soLuong
        self.donGia = donGia

    def total_price(self) -> float:
        return self.soLuong * self.donGia


class Order:

    def __init__(
        self,
        maDH,
        maKH,
        thoiGian,
        items: List[OrderItem],
        points,
    ):
        self.id = maDH  # Order ID
        self.maKH = maKH  # Customer ID
        self.thoiGian = thoiGian  # Order date
        self.points = points  # Points redeemable
        self.items = items  # List of order items

    def total(self) -> float:
        """Calculate total value of the order."""
        total_price = sum(item.total_price() for item in self.items)
        total_after_points = total_price - self.points * 1000
        return max(0, total_after_points)  # Ensure the total doesn't go below zero