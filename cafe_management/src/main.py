from models.user_model import User
from services.user_service import UserService
from views.login_view import LoginView
from controllers.login_controller import LoginController
from utilities.data_util import read_data_sheet

if __name__ == '__main__':
    # print(get_text("vi", "FORMAT_DATE"))  # Output: Xin chào
    # Đọc dữ liệu từ tệp Excel
    excel_file = ('data/dataTemplate.xlsx')
    df = read_data_sheet('data/dataTemplate.xlsx')
    # In toàn bộ DataFrame
    print(df)
    # Tạo các đối tượng của model, service, view và controller
    user_model = User(excel_file)  # Model
    user_service = UserService(user_model)  # Service

    # Khởi tạo view trước
    login_view = LoginView(None)  # View tạm thời không có controller

    # Khởi tạo controller với view
    login_controller = LoginController(user_service, login_view)  # Controller với view đã tạo

    # Gán lại controller vào view
    login_view.controller = login_controller

    # Khởi chạy giao diện người dùng
    login_view.mainloop()
