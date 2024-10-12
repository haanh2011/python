from models.user_model import UserModel
from services.user_service import UserService
from views.login_view import LoginView
from controllers.login_controller import LoginController

if __name__ == '__main__':
    # Tạo các đối tượng của model, service, view và controller
    user_model = UserModel()  # Model
    user_service = UserService(user_model)  # Service
    # Khởi tạo view trước
    login_view = LoginView(None)  # View tạm thời không có controller
    # Khởi tạo controller với view
    login_controller = LoginController(user_service, login_view)  # Controller với view đã tạo
    # Gán lại controller vào view
    login_view.controller = login_controller
    # Khởi chạy giao diện người dùng
    login_view.mainloop()