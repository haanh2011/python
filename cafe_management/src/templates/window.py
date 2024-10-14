from customtkinter import *
from PIL import Image, ImageTk
import os
import sys
class WindowBase:
    attributes = {
        # 'title': "Widget's title",
        'height': None,
        'width': None,
        'x': 0,
        'y': 0,
    }
    configs = {}
    def __init__(self, window, attributes = {}, configs= {}):
        self.window = window

        # Ghi đè các thuộc tính mặc định của attribute và config vào
        self.configs.update(configs)
        self.attributes.update(attributes)

        self._setAttributes()
        self._setConfigs()
        self._setLogo()
        
    def _setLogo(self):
        logoPath = os.path.join('src', 'assets', 'images', 'CoffeeShop-brand-logo.ico')  # Đảm bảo logo có định dạng .ico
        if os.path.exists(logoPath):
            # Đặt biểu tượng cho cửa sổ bằng iconbitmap
            self.window.iconbitmap(logoPath)  # Đặt icon cho cửa sổ
        else:
            print("Logo path not found.")
    def _setConfigs(self):
        self.window.config(**self.configs)
    def _setConfigs(self):
        self.window.config(**self.configs)

    def _setAttributes(self):
        if 'title' in self.attributes:
            self.window.title(self.attributes['title'])  # Thiết lập tiêu đề cho cửa sổ

        # *** Chỉnh các thuộc tính cho page
        # Nếu không truyền height and width thì mặc định set full màn hình
        if self.attributes['height'] is None and self.attributes['width'] is None:
            self.window.state('zoomed')
        else:
            self.attributes['x'] = (self.window.winfo_screenwidth() // 2) - (self.attributes['width'] // 2)
            self.attributes['y'] = (self.window.winfo_screenheight() // 2) - (self.attributes['height'] // 2)
            self.window.geometry(f"{self.attributes['width']}x{self.attributes['height']}+{self.attributes['x']}+{self.attributes['y']}")
    def Render(self):
        self.window.mainloop()

    def Exit(self):
        sys.exit(self.window.destroy())

class WindowMain(WindowBase):
    header_frame = None
    main_frame = None
    def __init__(self, attributes={}, configs={}):
        self.window = CTk()
        super().__init__(self.window, attributes, configs)
        self.window.title("Trang web bán sản phẩm")

        # Tạo Header
        self.header_frame = CTkFrame(self.window, fg_color="lightblue", height=50)
        self.header_frame.grid(row=0, column=0, sticky="nsew")

        header_label = CTkLabel(self.header_frame, text="Cửa hàng của bạn", text_color="black", font=("Arial", 18))
        header_label.pack(pady=10)

        #Tạo MainFrame
        self.main_frame = CTkFrame(self.window, fg_color="red")
        self.main_frame.grid(row = 1, column = 0, sticky='nsew', pady=10)

        # Tạo Sidebar (Thanh menu bên trái)
        # sidebar_frame = CTkFrame(self.window, fg_color="lightgrey", width=150)
        # sidebar_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # sidebar_label = CTkLabel(sidebar_frame, text="Danh mục", text_color="black", font=("Arial", 14))
        # sidebar_label.pack(pady=10)

        # categories = ["Điện thoại", "Laptop", "Phụ kiện", "Đồng hồ"]
        # for category in categories:
        #     CTkButton(sidebar_frame, text=category).pack(pady=5, padx=10)

        # # Tạo khu vực hiển thị sản phẩm
        # products_frame = CTkFrame(self.window, fg_color="white")
        # products_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        # # Tạo lưới sản phẩm (3 sản phẩm trên mỗi hàng)
        # for i in range(2):  # 2 hàng sản phẩm
        #     for j in range(3):  # 3 cột sản phẩm
        #         product_frame = CTkFrame(products_frame, fg_color="lightgrey", corner_radius=10)
        #         product_frame.grid(row=i, column=j, padx=10, pady=10, sticky="nsew")
                
        #         product_image = CTkLabel(product_frame, text="[Ảnh sản phẩm]", text_color="black")
        #         product_image.pack(pady=5)
                
        #         product_name = CTkLabel(product_frame, text=f"Sản phẩm {i*3+j+1}", text_color="black", font=("Arial", 14))
        #         product_name.pack(pady=5)
                
        #         product_price = CTkLabel(product_frame, text="500,000 VND", text_color="green", font=("Arial", 12))
        #         product_price.pack(pady=5)
                
        #         buy_button = CTkButton(product_frame, text="Mua ngay")
        #         buy_button.pack(pady=5)

        # # Tạo khu vực hóa đơn
        # invoice_frame = CTkFrame(self.window, fg_color="lightgrey", width=200)
        # invoice_frame.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)

        # invoice_label = CTkLabel(invoice_frame, text="Hóa đơn", text_color="black", font=("Arial", 16))
        # invoice_label.pack(pady=10)

        # # Khung này sẽ hiển thị các sản phẩm đã chọn (danh sách động)
        # selected_products = CTkLabel(invoice_frame, text="Sản phẩm đã chọn:\n- Không có", text_color="black", justify="left")
        # selected_products.pack(pady=10)

        # # Tổng tiền
        # total_price_label = CTkLabel(invoice_frame, text="Tổng: 0 VND", text_color="black", font=("Arial", 14))
        # total_price_label.pack(pady=10)

        # Điều chỉnh trọng số lưới
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=1)

        # products_frame.grid_columnconfigure((0, 1, 2), weight=1)
        # products_frame.grid_rowconfigure((0, 1), weight=1)