import customtkinter as ctk

class ProductView(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Product Management")
        window_width = 800  # Chiều rộng cửa sổ
        window_height = 500  # Chiều cao cửa sổ

        # Tính toán để căn giữa cửa sổ
        screen_width = self.winfo_screenwidth()  # Lấy chiều rộng màn hình
        screen_height = self.winfo_screenheight()  # Lấy chiều cao màn hình
        x_cordinate = int((screen_width / 2) - (window_width / 2))  # Tính toán tọa độ x
        y_cordinate = int((screen_height / 2) - (window_height / 2))  # Tính toán tọa độ y

        # Thiết lập vị trí và kích thước cửa sổ
        self.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
        # Tạo tiêu đề cho ProductView
        self.label_title = ctk.CTkLabel(master=self, text="Product Management", font=("yu gothic ui", 20, "bold"))
        self.label_title.pack(pady=20)
        # Tạo nút thêm sản phẩm
        self.button_add = ctk.CTkButton(master=self, text="Add Product", command=self.add_product)
        self.button_add.pack(pady=10)
        # Nút trở về Main Application
        self.button_back = ctk.CTkButton(master=self, text="Back to Main", command=self.back_to_main)
        self.button_back.pack(pady=10)
        # Để xử lý khi đóng cửa sổ
        self.protocol("WM_DELETE_WINDOW", self.back_to_main)
        # Lưu tham chiếu tới MainApplication
        self.master = master

    def add_product(self):
        # Logic cho việc thêm sản phẩm
        print("Thêm sản phẩm mới!")

    def back_to_main(self):
        # Hiển thị lại cửa sổ chính và đóng cửa sổ hiện tại
        self.master.deiconify()  # Hiển thị lại MainApplication
        self.destroy()  # Đóng cửa sổ ProductView