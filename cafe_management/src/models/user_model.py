import pandas as pd

class User():
    def __init__(self, excel_file):
        # Đọc tất cả các sheet trong tệp Excel vào một dictionary
        self.sheet_dict = pd.read_excel(excel_file, sheet_name=None)
        # Truy cập từng sheet bằng tên của nó
        self.users_df = self.sheet_dict['Users']
        # Kiểm tra nội dung
        print(self.users_df.head())

    def validate_user(self, username, password):
        return any((self.users_df['Username'] == username) & (self.users_df['Password'] == password))