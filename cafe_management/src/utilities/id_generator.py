class CategoryIdGenerator:
    """
    Bộ sinh mã loại sản phẩm tự động với định dạng LSP0001.
    """

    current_id = 0  # Biến lưu ID hiện tại

    @classmethod
    def generate_id(cls):
        """
        Sinh ID mới với định dạng LSP0001, LSP0002,...

        :return: Mã sản phẩm dưới dạng chuỗi.
        """
        cls.current_id += 1
        return f"LSP{cls.current_id:04d}"

class CustomerIdGenerator:
    """
    Bộ sinh mã khách hàng tự động với định dạng KH0001.
    """

    current_id = 0  # Biến lưu ID hiện tại

    @classmethod
    def generate_id(cls):
        """
        Sinh ID mới với định dạng KH0001, KH0002,...

        :return: Mã khách hàng dưới dạng chuỗi.
        """
        cls.current_id += 1
        return f"KH{cls.current_id:04d}"
    
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
        return f"NV{cls.current_id:04d}"

class OrderIdGenerator:
    """
    Bộ sinh mã đơn hàng tự động với định dạng NV0001.
    """

    current_id = 0  # Biến lưu ID hiện tại

    @classmethod
    def generate_id(cls):
        """
        Sinh ID mới với định dạng DH0001, DH0002,...

        :return: Mã đơn hàng dưới dạng chuỗi.
        """
        cls.current_id += 1
        return f"DH{cls.current_id:04d}"

class InvoiceIdGenerator:
    """
    Bộ sinh mã hoá đơn tự động với định dạng HD0001.
    """

    current_id = 0  # Biến lưu ID hiện tại

    @classmethod
    def generate_id(cls):
        """
        Sinh ID mới với định dạng HD0001, HD0002,...

        :return: Mã hoá đơn dưới dạng chuỗi.
        """
        cls.current_id += 1
        return f"HD{cls.current_id:04d}"
