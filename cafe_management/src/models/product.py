class ProductIdGenerator:
    """
    Bộ sinh mã sản phẩm tự động với định dạng SP0001.
    """

    current_id = 0  # Biến lưu ID hiện tại

    @classmethod
    def generate_id(cls):
        """
        Sinh ID mới với định dạng SP0001, SP0002,...

        :return: Mã sản phẩm dưới dạng chuỗi.
        """
        cls.current_id += 1
        return f"SP{cls.current_id:04d}"


class Product:
    """
    Định nghĩa một sản phẩm trong quản lý bán hàng quán cà phê.
    """
    def __init__(self, tenSP, maLSP, giaTien):
        self.maSP = ProductIdGenerator.generate_id()
        self.tenSP = tenSP
        self.maLSP = maLSP
        self.giaTien = giaTien