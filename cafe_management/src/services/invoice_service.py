from cafe_management.src.controllers import DataController

class InvoiceService:
    def __init__(self, file_path):
        """
        Initializes a new instance of the InvoiceService class.

        :param file_path: Path to the invoice data file.
        """
        self._file_path = file_path
        self.invoices = DataController.load_invoices(self._file_path)  # Load invoices from file
