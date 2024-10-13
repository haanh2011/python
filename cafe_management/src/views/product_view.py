import customtkinter as ctk
from PIL import Image

class ProductView(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Product Management")
        window_width = 800  # Chiều rộng cửa sổ
        window_height = 500  # Chiều cao cửa sổ

        # Tính toán để căn giữa cửa sổ
        screen_width = self.winfo_screenwidth()  # Lấy chiều rộng màn hình
        screen_height = self.winfo_screenheight()  # Lấy chiều cao màn hình
        x_cordinate = int((screen_width - window_width) / 2)  # Tính toán tọa độ x
        y_cordinate = int((screen_height - window_height) / 2)  # Tính toán tọa độ y

        # Thiết lập vị trí và kích thước cửa sổ
        self.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

        # Tạo tiêu đề cho ProductView
        self.label_title = ctk.CTkLabel(master=self, text="Product Management", font=("yu gothic ui", 20, "bold"))
        self.label_title.pack(pady=20)

        # Tạo khung cuộn cho bảng sản phẩm
        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.pack(pady=10, fill='both', expand=True)

        self.table_headers = ["ID", "Name", "Price", "Desc"]
        self.products = []  # Danh sách lưu trữ thông tin sản phẩm

        self.create_table()

        # Form để thêm/sửa sản phẩm
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.pack(pady=10)

        # Chia cột cho thông tin sản phẩm và nút
        self.create_form()

        # Tải hình ảnh cho các nút sử dụng CTkImage
        self.img_back = ctk.CTkImage(light_image=Image.open("images/back.png"), size=(40, 40))

        # Nút trở về Main Application
        self.button_back = ctk.CTkButton(master=self,
                                         text="",
                                         fg_color="#FACE9C",
                                         image=self.img_back,
                                         command=self.back_to_main,
                                         hover_color="#F09C42")

        self.button_back.place(relx=0.98, rely=0.07, anchor='e')  # Đặt ở góc phải trên cùng

        # Để xử lý khi đóng cửa sổ
        self.protocol("WM_DELETE_WINDOW", self.back_to_main)

    def create_table(self):
        # Tạo tiêu đề cho bảng
        for header in self.table_headers:
            label = ctk.CTkLabel(self.scrollable_frame, text=header)
            label.grid(row=0, column=self.table_headers.index(header), padx=10, pady=5)

        # Thêm cột cho các nút (Edit và Delete)
        self.scrollable_frame.grid_columnconfigure(len(self.table_headers) - 2, weight=1)  # Cột Edit
        self.scrollable_frame.grid_columnconfigure(len(self.table_headers) - 1, weight=1)  # Cột Delete

        # Cập nhật danh sách headers để có thể hiển thị tên cột cho nút
        self.table_headers.append("Edit")
        self.table_headers.append("Delete")

        # Thêm một số sản phẩm mẫu vào danh sách
        self.products = [
            ["1", "Product A", "$10", "Description A"],
            ["2", "Product B", "$20", "Description B"],
            ["3", "Product C", "$30", "Description C"],
            ["4", "Product D", "$40", "Description D"],
            ["5", "Product E", "$50", "Description E"],
            ["6", "Product F", "$60", "Description F"],
            ["7", "Product G", "$70", "Description G"],
            ["8", "Product H", "$80", "Description H"],
        ]

        for index, product in enumerate(self.products):
            for j, value in enumerate(product):
                label = ctk.CTkLabel(self.scrollable_frame, text=value)
                label.grid(row=index + 1, column=j, padx=10, pady=5)

            # Nút sửa sản phẩm
            edit_button = ctk.CTkButton(self.scrollable_frame, text="Edit", width=8,
                                        command=lambda idx=index: self.edit_product(idx))
            edit_button.grid(row=index + 1, column=len(product), padx=10, pady=5)

            # Nút xóa sản phẩm
            delete_button = ctk.CTkButton(self.scrollable_frame, text="Delete", width=8,
                                          command=lambda idx=index: self.delete_product(idx))
            delete_button.grid(row=index + 1, column=len(product) + 1, padx=10, pady=5)

    def create_form(self):
        # Cột cho thông tin sản phẩm
        info_column = ctk.CTkFrame(self.form_frame)
        info_column.grid(row=0, column=0, padx=10, pady=10)

        # Cột cho nút
        button_column = ctk.CTkFrame(self.form_frame)
        button_column.grid(row=0, column=1, padx=10, pady=10)

        # Trường ID sản phẩm (chỉ để xem)
        self.label_id = ctk.CTkLabel(info_column, text="Product ID:")
        self.label_id.grid(row=0, column=0, padx=10, pady=5)

        self.entry_id = ctk.CTkEntry(info_column, state="readonly", width=200)  # Chỉ đọc và tăng chiều rộng
        self.entry_id.grid(row=0, column=1, padx=10, pady=5)

        # Trường tên sản phẩm
        self.label_name = ctk.CTkLabel(info_column, text="Product Name:")
        self.label_name.grid(row=1, column=0, padx=10, pady=5)

        self.entry_name = ctk.CTkEntry(info_column, placeholder_text="Product Name", width=200)  # Tăng chiều rộng
        self.entry_name.grid(row=1, column=1, padx=10, pady=5)

        # Trường giá sản phẩm
        self.label_price = ctk.CTkLabel(info_column, text="Product Price:")
        self.label_price.grid(row=2, column=0, padx=10, pady=5)

        self.entry_price = ctk.CTkEntry(info_column, placeholder_text="Product Price", width=200)  # Tăng chiều rộng
        self.entry_price.grid(row=2, column=1, padx=10, pady=5)

        # Trường mô tả sản phẩm
        self.label_desc = ctk.CTkLabel(info_column, text="Product Desc:")
        self.label_desc.grid(row=3, column=0, padx=10, pady=5)

        self.entry_desc = ctk.CTkEntry(info_column, placeholder_text="Product Desc", width=200)  # Tăng chiều rộng
        self.entry_desc.grid(row=3, column=1, padx=10, pady=5)

        # Nút thêm sản phẩm
        self.button_add = ctk.CTkButton(master=button_column, text="Add Product", command=self.add_product)
        self.button_add.grid(row=0, column=0, pady=10)

        # Nút sửa sản phẩm
        self.button_edit = ctk.CTkButton(master=button_column, text="Edit Product", command=lambda: self.edit_product())
        self.button_edit.grid(row=1, column=0, pady=5)

    def add_product(self):
        # Logic cho việc thêm sản phẩm
        print("Thêm sản phẩm mới!")

    def edit_product(self, index=None):
        # Logic cho việc sửa sản phẩm
        if index is not None:
            print(f"Sửa sản phẩm tại chỉ số {index}!")
        else:
            print("Sửa sản phẩm!")

    def delete_product(self, index):
        print(f"Xóa sản phẩm tại chỉ số {index}!")

    def back_to_main(self):
        # Hiển thị lại cửa sổ chính và đóng cửa sổ hiện tại
        self.master.deiconify()  # Hiển thị lại MainApplication
        self.destroy()  # Đóng cửa sổ ProductView