from templates import WindowMain
from utilities import setTheme

setTheme()

from customtkinter import *

class OrderPage(WindowMain):
    sidebarFrame = None
    productFrame = None
    orderFrame = None
    def __init__(self, attributes={}, configs={}):
        super().__init__(attributes, configs)

        # Tạo Sidebar (Thanh menu bên trái)
        self.sidebarFrame = CTkFrame(self.main_frame, fg_color="yellow")
        self.sidebarFrame.grid(row=0, column=0, sticky="nsew")

        sidebar_label = CTkLabel(self.sidebarFrame, text="Danh mục", text_color="black", font=("Arial", 14))
        sidebar_label.pack(pady=10)

        categories = ["Điện thoại", "Laptop", "Phụ kiện", "Đồng hồ"]
        for category in categories:
            CTkButton(self.sidebarFrame, text=category).pack(pady=5, padx=10)

        # Tạo khu vực hiển thị sản phẩm
        self.productFrame = CTkFrame(self.main_frame, fg_color="white")
        self.productFrame.grid(row=0, column=1, sticky="nsew")

        # Tạo lưới sản phẩm (3 sản phẩm trên mỗi hàng)
        for i in range(2):  # 2 hàng sản phẩm
            for j in range(3):  # 3 cột sản phẩm
                product_frame = CTkFrame(self.productFrame, fg_color="lightgrey", corner_radius=10)
                product_frame.grid(row=i, column=j, padx=10, pady=10, sticky="nsew")
                
                product_image = CTkLabel(product_frame, text="[Ảnh sản phẩm]", text_color="black")
                product_image.pack(pady=5)
                
                product_name = CTkLabel(product_frame, text=f"Sản phẩm {i*3+j+1}", text_color="black", font=("Arial", 14))
                product_name.pack(pady=5)
                
                product_price = CTkLabel(product_frame, text="500,000 VND", text_color="green", font=("Arial", 12))
                product_price.pack(pady=5)
                
                buy_button = CTkButton(product_frame, text="Mua ngay")
                buy_button.pack(pady=5)

        # Tạo khu vực hóa đơn
        self.orderFrame = CTkFrame(self.main_frame, fg_color="lightgrey")
        self.orderFrame.grid(row=0, column=2, sticky="nsew")

        invoice_label = CTkLabel(self.orderFrame, text="Hóa đơn", text_color="black", font=("Arial", 16), width=200)
        invoice_label.pack(pady=10)

        # Khung này sẽ hiển thị các sản phẩm đã chọn (danh sách động)
        selected_products = CTkLabel(self.orderFrame, text="Sản phẩm đã chọn:\n- Không có", text_color="black", justify="left")
        selected_products.pack(pady=10)

        # Tổng tiền
        total_price_label = CTkLabel(self.orderFrame, text="Tổng: 0 VND", text_color="black", font=("Arial", 14))
        total_price_label.pack(pady=10)

        # Điều chỉnh lưới
        self.main_frame.columnconfigure(1,weight=1)
        self.main_frame.rowconfigure(0,weight=1)
        self.productFrame.columnconfigure((0,1,2), weight=1)
        self.productFrame.rowconfigure((0,1),weight=1)


def main():
    managementPage = OrderPage(attributes={
        'width': 1200,
        'height': 900
    })
    managementPage.Render()

if __name__ == '__main__':
    main()