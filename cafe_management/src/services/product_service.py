from cafe_management.src.controllers import DataController

class ProductService:
    def __init__(self, file_path):
        """
        Initializes a new instance of the ProductService class.

        :param file_path: Path to the product data file.
        """
        self._file_path = file_path
        self.products = DataController.load_products(self._file_path)  # Load products from file
