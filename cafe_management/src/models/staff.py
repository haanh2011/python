class StaffIdGenerator:
    """
    Bộ sinh mã nhân viên tự động với định dạng NV0001.
    """

    current_id = 0  # Biến lưu ID hiện tại

    @classmethod
    def generate_id(cls):
        """
        Sinh ID mới với định dạng NV0001, NV0002,...

        :return: Mã nhân viên dưới dạng chuỗi.
        """
        cls.current_id += 1
        return f"KH{cls.current_id:04d}"


class Staff:
    """
    Định nghĩa một đối tượng nhân viên trong hệ thống quản lý quán cà phê.
    """

    def __init__(self, tenNV, ngaySinh, sdt, email):
        self.maNV = StaffIdGenerator.generate_id()
        self.tenNV = tenNV
        self.ngaySinh = ngaySinh
        self.sdt = sdt
        self.email = email