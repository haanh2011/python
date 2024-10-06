# from cafe_management.src.Controllers import DataController

class StaffService:
    def __init__(self, file_path):
        """
        Initializes a new instance of the StaffService class.

        :param file_path: Path to the staff data file.
        """
        self._file_path = file_path
        # self.staffs = DataController.load_staffs(self._file_path)  # Load staffs from file
