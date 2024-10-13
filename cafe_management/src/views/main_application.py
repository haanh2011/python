import customtkinter as ctk
from src.views.product_view import ProductView
from PIL import Image

class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("The Coffee Application")
        window_width = 800
        window_height = 500

        # Tính toán để căn giữa cửa sổ
        screen_width = self.winfo_screenwidth()  # Lấy chiều rộng màn hình
        screen_height = self.winfo_screenheight()  # Lấy chiều cao màn hình
        x_cordinate = int((screen_width - window_width) / 2)  # Tính toán tọa độ x
        y_cordinate = int((screen_height - window_height) / 2)  # Tính toán tọa độ y

        # Thiết lập vị trí và kích thước cửa sổ
        self.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

        # Thiết lập hình nền sử dụng CTkImage
        self.bg_image = ctk.CTkImage(
            light_image=Image.open("images/home_bg3.jpg"),
            size=(window_width, window_height)
        )

        # Đặt hình nền bằng place
        self.label_bg = ctk.CTkLabel(self, image=self.bg_image, text="")
        self.label_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Sự kiện thay đổi kích thước cửa sổ
        self.bind("<Configure>", self.resize_bg_image)

        # Tạo Frame chính với bo góc để chứa toàn bộ nội dung
        self.main_frame = ctk.CTkFrame(
            master=self,
            width=500,
            height=300,
            corner_radius=30,  # Giảm bán kính bo góc
            fg_color="#FCD9C4"  # Đặt màu nền khung ngoài để tạo sự đồng nhất
        )
        self.main_frame.pack(pady=20, padx=20, expand=True)

        # Nhãn tiêu đề bên trong main_frame
        self.label_main = ctk.CTkLabel(
            master=self.main_frame,
            text="Welcome to The Coffee Management",
            font=("yu gothic ui", 24, "bold"),
            fg_color = "#FCD9C4"
        )
        self.label_main.pack(pady=(20, 10))

        # Tạo Frame mới bên trong main_frame để chứa các nút với bo góc
        self.button_frame = ctk.CTkFrame(
            master=self.main_frame,
            width=400,
            height=200,
            fg_color="#FCD9C4",  # Nền trong suốt cho frame này
            corner_radius=20  # Thêm thuộc tính bo góc với bán kính 20
        )
        self.button_frame.pack(pady=20, expand=True)

        # Tải hình ảnh cho các nút sử dụng CTkImage
        self.img_category = ctk.CTkImage(light_image=Image.open("images/category.png"), size=(40, 40))
        self.img_product = ctk.CTkImage(light_image=Image.open("images/product.png"), size=(40, 40))
        self.img_customer = ctk.CTkImage(light_image=Image.open("images/customer.png"), size=(40, 40))
        self.img_order = ctk.CTkImage(light_image=Image.open("images/order.png"), size=(40, 40))
        self.img_invoice = ctk.CTkImage(light_image=Image.open("images/invoice.png"), size=(40, 40))
        self.img_logout = ctk.CTkImage(light_image=Image.open("images/logout.png"), size=(40, 40))

        # Nút mở quản lý loại sản phẩm
        self.button_category = ctk.CTkButton(
            master=self.button_frame,
            text="Manage Category",
            image=self.img_category,
            text_color="white",
            fg_color="#D0770B",
            hover_color="#945305",
            width=150,
            height=50,
            corner_radius=10
        )
        self.button_category.grid(row=0, column=0, padx=10, pady=10, sticky='ew')  # Hàng 0, cột 0

        # Nút mở quản lý sản phẩm
        self.button_product = ctk.CTkButton(
            master=self.button_frame,
            text="Manage Products",
            image=self.img_product,
            command=self.open_product_view,
            text_color="white",
            fg_color="#D0770B",
            hover_color="#945305",
            width=150,
            height=50,
            corner_radius=10
        )
        self.button_product.grid(row=0, column=1, padx=10, pady=10, sticky='ew')  # Hàng 0, cột 1

        # Nút mở quản lý khách hàng
        self.button_customer = ctk.CTkButton(
            master=self.button_frame,
            text="Manage Customers",
            image=self.img_customer,
            text_color="white",
            fg_color="#D0770B",
            hover_color="#945305",
            width=150,
            height=50,
            corner_radius=10
        )
        self.button_customer.grid(row=0, column=2, padx=10, pady=10, sticky='ew')  # Hàng 0, cột 2

        # Nút mở quản lý đơn hàng
        self.button_order = ctk.CTkButton(
            master=self.button_frame,
            text="Manage Order",
            image=self.img_order,
            text_color="white",
            fg_color="#D0770B",
            hover_color="#945305",
            width=150,
            height=50,
            corner_radius=10
        )
        self.button_order.grid(row=1, column=0, padx=10, pady=10, sticky='ew')  # Hàng 1, cột 0

        # Nút mở quản lý hóa đơn
        self.button_invoice = ctk.CTkButton(
            master=self.button_frame,
            text="Manage Invoice",
            image=self.img_invoice,
            text_color="white",
            fg_color="#D0770B",
            hover_color="#945305",
            width=150,
            height=50,
            corner_radius=10
        )
        self.button_invoice.grid(row=1, column=1, padx=10, pady=10, sticky='ew')  # Hàng 1, cột 1

        # Nút đăng xuất
        self.button_logout = ctk.CTkButton(
            master=self.button_frame,
            text="Logout",
            image=self.img_logout,
            command=self.logout,
            text_color="white",
            fg_color="#D0770B",
            hover_color="#945305",
            width=150,
            height=50,
            corner_radius=10
        )
        self.button_logout.grid(row=1, column=2, padx=10, pady=10, sticky='ew')  # Hàng 1, cột 2

        # Cài đặt độ rộng cho cột
        for i in range(3):  # Ba cột
            self.button_frame.grid_columnconfigure(i, weight=1)

    def resize_bg_image(self, event):
        # Cập nhật kích thước hình nền khi cửa sổ thay đổi
        new_width = event.width
        new_height = event.height
        self.bg_image.configure(size=(new_width, new_height))

    def open_product_view(self):
        self.withdraw()
        product_window = ProductView(self)
        product_window.grab_set()

    def logout(self):
        self.destroy()
        print("Đã đăng xuất!")
