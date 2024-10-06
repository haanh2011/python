from cafe_management.src.controllers import DataController

class OrderService:
    def __init__(self, file_path):
        """
        Initializes a new instance of the OrderService class.

        :param file_path: Path to the order data file.
        """
        self._file_path = file_path
        self.orders = DataController.load_orders(self._file_path)  # Load orders from file
