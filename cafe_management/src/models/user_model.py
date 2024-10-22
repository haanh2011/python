import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
utilities_dir = os.path.join(current_dir , '../utilities')
sys.path.append(utilities_dir)
import data_util

class UserModel:
    def __init__(self):
        '''
        Khởi tạo UserModel và đọc dữ liệu từ sheet 'Users' trong file Excel.
        '''
        # Đọc sheet 'Users' từ file Excel
        self.users_df = data_util.read_data_sheet("Users")

        # Kiểm tra nội dung nếu đọc thành công
        if self.users_df is not None:
            print(self.users_df.head())
        else:
            print("Không thể đọc dữ liệu từ sheet 'Users'.")

    def update_id(self, id):
        self.id = id