import customtkinter as ctk
from src.views.product_view import ProductView
# Khởi tạo CustomTkinter
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Main Application")
        window_width = 800  # Chiều rộng cửa sổ
        window_height = 500  # Chiều cao cửa sổ

        # Tính toán để căn giữa cửa sổ
        screen_width = self.winfo_screenwidth()  # Lấy chiều rộng màn hình
        screen_height = self.winfo_screenheight()  # Lấy chiều cao màn hình
        x_cordinate = int((screen_width / 2) - (window_width / 2))  # Tính toán tọa độ x
        y_cordinate = int((screen_height / 2) - (window_height / 2))  # Tính toán tọa độ y

        # Thiết lập vị trí và kích thước cửa sổ
        self.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

        # Nhãn tiêu đề
        self.label_main = ctk.CTkLabel(master=self, text="Welcome to The Coffee App", font=("yu gothic ui", 24, "bold"))
        self.label_main.pack(pady=20)

        # Nút mở quản lý sản phẩm
        self.button_product = ctk.CTkButton(master=self, text="Manage Products", command=self.open_product_view)
        self.button_product.pack(pady=10)

        # Nút đăng xuất
        self.button_logout = ctk.CTkButton(master=self, text="Logout", command=self.logout)
        self.button_logout.pack(pady=10)

        # Frame ProductView
        self.product_view = None
    def open_product_view(self):
        # Ẩn MainApplication khi ProductView được mở
        self.withdraw()  # Ẩn cửa sổ chính
        # Mở ProductView dưới dạng một cửa sổ mới
        product_window = ProductView(self)
        product_window.grab_set()  # Đảm bảo chỉ thao tác với ProductView cho đến khi nó được đóng

    def logout(self):
        self.destroy()  # Đóng cửa sổ chính
        print("Đã đăng xuất!")
