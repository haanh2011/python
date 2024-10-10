import customtkinter
from product_management import ProductManagement
from category_management import CategoryManagement

class MainApplication(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Main Application")
        self.geometry("800x600")

        # Khai báo biến để quản lý cửa sổ hiện tại
        self.opened_window = None

        btn_product = customtkinter.CTkButton(self, text="Quản lý sản phẩm", command=self.open_product_management)
        btn_product.pack(pady=10)

        btn_category = customtkinter.CTkButton(self, text="Quản lý loại sản phẩm", command=self.open_category_management)
        btn_category.pack(pady=10)

    def open_window(self, window_class):
        try:
            # Ẩn cửa sổ chính
            self.withdraw()
            # Mở cửa sổ con mới
            new_window = window_class(self)
            # Thiết lập sự kiện khi đóng cửa sổ con, cửa sổ chính sẽ hiện lại
            new_window.protocol("WM_DELETE_WINDOW", lambda: self.on_child_close(new_window))
        except Exception as e:
            print(f"Error opening window: {e}")

    def on_child_close(self, window):
        # Đóng cửa sổ con và hiển thị lại cửa sổ chính
        window.destroy()
        self.deiconify()

    def open_product_management(self):
        self.open_window(ProductManagement)

    def open_category_management(self):
        self.open_window(CategoryManagement)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()