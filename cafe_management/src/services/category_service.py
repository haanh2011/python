from cafe_management.src.controllers import DataController

class CategoryService:
    def __init__(self, file_path):
        """
        Initializes a new instance of the CategoryService class.

        :param file_path: Path to the category data file.
        """
        self._file_path = file_path
        self.categories = DataController.load_categories(self._file_path)  # Load categories from file
