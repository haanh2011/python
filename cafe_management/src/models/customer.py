from CafeManagement.src.utilities.id_generator import CustomerIdGenerator


class Customer:
    def __init__(self, tenKH, ngaySinh, sdt, email):
        self.maKH = CustomerIdGenerator.generate_id()
        self.tenKH = tenKH
        self.ngaySinh = ngaySinh
        self.sdt = sdt
        self.email = email
        self.points = 0

    def add_points(self, points):
        """
        Cộng thêm điểm tích lũy cho khách hàng.

        :param points: Số điểm cần thêm vào điểm tích lũy của khách hàng.
        """
        self.points += points

    def subtract_points(self, points):
        """
        Trừ điểm tích lũy khách hàng đã sử dụng.

        :param points: Số điểm cần trừ trong điểm tích lũy của khách hàng.
        """
        if self.points > points:
            self.points -= points
        else:
            self.points = 0
