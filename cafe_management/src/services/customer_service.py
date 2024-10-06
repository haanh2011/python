from cafe_management.src.controllers import DataController

class CustomerService:
    def __init__(self, file_path):
        """
        Initializes a new instance of the CustomerService class.

        :param file_path: Path to the customer data file.
        """
        self._file_path = file_path
        self.customers = DataController.load_customers(self._file_path)  # Load customers from file
