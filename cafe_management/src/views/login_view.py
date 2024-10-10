import customtkinter as ctk

class LoginScreen(ctk.CTkFrame):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.controller = controller

        # Thiết lập kích thước cửa sổ
        window_width = int(master.winfo_screenwidth() * 0.3) # 30% chiều rộng màn hình
        window_height = int(master.winfo_screenheight() * 0.35) # 35% chiều cao màn hình
        master.geometry(f"{window_width}x{window_height}")

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

# Khởi tạo ứng dụng
if __name__ == "__main__":
    root = ctk.CTk()  # Tạo cửa sổ chính
    app = LoginScreen(master=root)
    app.pack(expand=True, fill='both')
    root.mainloop()