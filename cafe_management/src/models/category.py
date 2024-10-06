from CafeManagement.src.utilities.id_generator import CategoryIdGenerator

class Category:
    def __init__(self, tenLSP):
        self.maLSP = CategoryIdGenerator.generate_id()
        self.name = tenLSP
