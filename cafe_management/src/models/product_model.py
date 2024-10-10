import pandas as pd

class Product:
    def __init__(self, excel_file):
        # Đọc tất cả các sheet trong tệp Excel vào một dictionary
        self.sheet_dict = pd.read_excel(excel_file, sheet_name=None)
        # Truy cập từng sheet bằng tên của nó
        self.product_df = self.sheet_dict['Products']
        # Kiểm tra nội dung
        print(self.product_df.head())


