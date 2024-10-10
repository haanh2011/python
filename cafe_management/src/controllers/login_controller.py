from cafe_management.src.main_application import MainApplication


class LoginController:
    def __init__(self, user_service, view):
        self.user_service = user_service
        self.view = view
        self.view.controller = self

    def handle_login(self):
        username  = self.view.get_username()
        password  = self.view.get_password()
        if self.user_service.authenticate(username, password):
            self.view.show_message("Đăng nhập thành công!")
            self.view.destroy()  # Đóng cửa sổ login
            app = MainApplication()  # Khởi động ứng dụng chính
            app.mainloop()
        else:
            self.view.show_message("Sai tên đăng nhập hoặc mật khẩu.")
