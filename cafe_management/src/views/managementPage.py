from templates import WindowBase
from utilities import setTheme

setTheme()

from customtkinter import *

class ManagementPage(WindowBase):
    def __init__(self, attributes={}, configs={}):
        self.window = CTk()
        super().__init__(self.window, attributes, configs)
        self.window.title("Trang web bán sản phẩm")

        # Tạo Header
        header_frame = CTkFrame(self.window, fg_color="lightblue", height=50)
        header_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

        header_label = CTkLabel(header_frame, text="Cửa hàng của bạn", text_color="black", font=("Arial", 18))
        header_label.pack(pady=10)

        # Tạo Sidebar (Thanh menu bên trái)
        sidebar_frame = CTkFrame(self.window, fg_color="lightgrey", width=150)
        sidebar_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        sidebar_label = CTkLabel(sidebar_frame, text="Danh mục", text_color="black", font=("Arial", 14))
        sidebar_label.pack(pady=10)

        categories = ["Điện thoại", "Laptop", "Phụ kiện", "Đồng hồ"]
        for category in categories:
            CTkButton(sidebar_frame, text=category).pack(pady=5, padx=10)

        # Tạo khu vực hiển thị sản phẩm
        products_frame = CTkFrame(self.window, fg_color="white")
        products_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        # Tạo lưới sản phẩm (3 sản phẩm trên mỗi hàng)
        for i in range(2):  # 2 hàng sản phẩm
            for j in range(3):  # 3 cột sản phẩm
                product_frame = CTkFrame(products_frame, fg_color="lightgrey", corner_radius=10)
                product_frame.grid(row=i, column=j, padx=10, pady=10, sticky="nsew")
                
                product_image = CTkLabel(product_frame, text="[Ảnh sản phẩm]", text_color="black")
                product_image.pack(pady=5)
                
                product_name = CTkLabel(product_frame, text=f"Sản phẩm {i*3+j+1}", text_color="black", font=("Arial", 14))
                product_name.pack(pady=5)
                
                product_price = CTkLabel(product_frame, text="500,000 VND", text_color="green", font=("Arial", 12))
                product_price.pack(pady=5)
                
                buy_button = CTkButton(product_frame, text="Mua ngay")
                buy_button.pack(pady=5)

        # Tạo Footer
        footer_frame = CTkFrame(self.window, fg_color="lightblue", height=50)
        footer_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")

        footer_label = CTkLabel(footer_frame, text="© 2024 Cửa hàng của bạn", text_color="black", font=("Arial", 12))
        footer_label.pack(pady=10)

        # Điều chỉnh trọng số lưới
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_rowconfigure(1, weight=1)
        products_frame.grid_columnconfigure((0, 1, 2), weight=1)
        products_frame.grid_rowconfigure((0, 1), weight=1)

def main():
    managementPage = ManagementPage()
    managementPage.Render()

if __name__ == '__main__':
    main()