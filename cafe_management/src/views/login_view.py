import customtkinter as ctk

class LoginView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller  # Lưu controller
        self.title("Login")
        # Thiết lập kích thước cửa sổ
        window_width = int(self.winfo_screenwidth() * 0.3) # 30% chiều rộng màn hình
        window_height = int(self.winfo_screenheight() * 0.35) # 35% chiều cao màn hình
        self.geometry(f"{window_width}x{window_height}")
        # Nhãn tiêu đề
        self.label_title = ctk.CTkLabel(master=self, text="Login", font=("yu gothic ui", 24, "bold"))
        self.label_title.pack(pady=20)
        # Nhãn và ô nhập tên người dùng
        self.label_username = ctk.CTkLabel(master=self, text="Username")
        self.label_username.pack(pady=(10, 0))
        self.entry_username = ctk.CTkEntry(master=self, placeholder_text="Enter your username")
        self.entry_username.pack(pady=(0, 10))
        # Nhãn và ô nhập mật khẩu
        self.label_password = ctk.CTkLabel(master=self, text="Password")
        self.label_password.pack(pady=(10, 0))
        self.entry_password = ctk.CTkEntry(master=self, placeholder_text="Enter your password", show='*')
        self.entry_password.pack(pady=(0, 20))
        # Khởi tạo nút đăng nhập
        self.button_login = ctk.CTkButton(master=self, text="Login", command=self.handle_login)
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