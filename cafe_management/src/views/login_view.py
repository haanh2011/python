import customtkinter

class LoginView(customtkinter.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller  # Lưu controller
        self.title("Login")
        self.geometry("400x300")

        # Nhãn tiêu đề
        self.label_title = customtkinter.CTkLabel(master=self, text="Login", font=("yu gothic ui", 24, "bold"))
        self.label_title.pack(pady=20)

        # Nhãn và ô nhập tên người dùng
        self.label_username = customtkinter.CTkLabel(master=self, text="Username")
        self.label_username.pack(pady=(10, 0))
        self.entry_username = customtkinter.CTkEntry(master=self, placeholder_text="Enter your username")
        self.entry_username.pack(pady=(0, 10))

        # Nhãn và ô nhập mật khẩu
        self.label_password = customtkinter.CTkLabel(master=self, text="Password")
        self.label_password.pack(pady=(10, 0))
        self.entry_password = customtkinter.CTkEntry(master=self, placeholder_text="Enter your password", show='*')
        self.entry_password.pack(pady=(0, 20))

        # Khởi tạo nút đăng nhập
        self.button_login = customtkinter.CTkButton(master=self, text="Login", command=self.handle_login)
        self.button_login.pack(pady=10)

    def handle_login(self):
        if self.controller is not None:
            self.controller.handle_login()  # Gọi phương thức handle_login từ controller
        else:
            print("Controller is not set")

    def get_username(self):
        return self.entry_username.get()

    def get_password(self):
        return self.entry_password.get()

    def show_message(self, message):
        print(message)
