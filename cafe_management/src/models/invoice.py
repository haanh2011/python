from CafeManagement.src.utilities.id_generator import InvoiceIdGenerator

class Invoice:
    def __init__(self, maDH, thoiGian):
        self.maHD = InvoiceIdGenerator.generate_id()
        self.maDH = maDH
        self.thoiGian = thoiGian
