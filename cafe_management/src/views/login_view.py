import customtkinter as ctk
from PIL import Image, ImageTk


class LoginView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller  # Lưu controller

        # Cấu hình cửa sổ
        self.title("Login")
        window_width = 800  # Chiều rộng cửa sổ
        window_height = 500  # Chiều cao cửa sổ

        # Tính toán để căn giữa cửa sổ
        screen_width = self.winfo_screenwidth()  # Lấy chiều rộng màn hình
        screen_height = self.winfo_screenheight()  # Lấy chiều cao màn hình
        x_cordinate = int((screen_width - window_width) / 2)  # Tính toán tọa độ x
        y_cordinate = int((screen_height - window_height) / 2)  # Tính toán tọa độ y

        # Thiết lập vị trí và kích thước cửa sổ
        self.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

        # Tải hình ảnh logo và đặt phía trên tiêu đề
        self.image = ctk.CTkImage(Image.open("images/coffeeShop-ico.png"), size=(60, 60))
        self.image_label = ctk.CTkLabel(master=self, image=self.image, text="")
        self.image_label.pack(pady=(10, 10))  # Căn logo với khoảng cách từ trên

        # Nhãn tiêu đề
        self.label_title = ctk.CTkLabel(master=self, text="Login", font=("yu gothic ui", 46, "bold"), text_color="#003366", bg_color="transparent")
        self.label_title.pack(pady=(0, 20))  # Canh giữa tiêu đề, với khoảng cách từ logo

        # Nhãn và ô nhập tên người dùng
        self.label_username = ctk.CTkLabel(master=self, text="Username", font=("Arial", 16), fg_color="transparent", bg_color="transparent")
        self.label_username.place(x=250, y=200)
        self.entry_username = ctk.CTkEntry(master=self, placeholder_text="Enter your username", width=250, height=30, fg_color="transparent", bg_color="transparent")
        self.entry_username.place(x=350, y=200)

        # Nhãn và ô nhập mật khẩu
        self.label_password = ctk.CTkLabel(master=self, text="Password", font=("Arial", 16), fg_color="transparent")
        self.label_password.place(x=250, y=250)
        self.entry_password = ctk.CTkEntry(master=self, placeholder_text="Enter your password", show='*', width=250, height=30, fg_color="transparent")
        self.entry_password.place(x=350, y=250)

        # Khởi tạo nút đăng nhập
        self.button_login = ctk.CTkButton(
            master=self,
            text="Login",
            font=("Arial", 20),
            command=self.handle_login,
            width=200,
            height=50,
            fg_color="#007BFF",  # Màu nền cụ thể (ví dụ: xanh dương)
            hover_color="#0056b3"  # Màu khi hover (ví dụ: xanh đậm hơn)
        )
        self.button_login.place(x=(window_width - 200) // 2, y=350)  # Căn giữa nút đăng nhập

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
