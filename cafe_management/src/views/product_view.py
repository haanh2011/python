import customtkinter as ctk
from PIL import Image

class ProductView(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Product Management")
        window_width = 800  # Chiều rộng cửa sổ
        window_height = 600  # Chiều cao cửa sổ

        # Tính toán để căn giữa cửa sổ
        screen_width = self.winfo_screenwidth()  # Lấy chiều rộng màn hình
        screen_height = self.winfo_screenheight()  # Lấy chiều cao màn hình
        x_cordinate = int((screen_width - window_width) / 2)  # Tính toán tọa độ x
        y_cordinate = int((screen_height - window_height) / 2)  # Tính toán tọa độ y

        # Thiết lập vị trí và kích thước cửa sổ
        self.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

        # Tạo tiêu đề cho ProductView
        self.label_title = ctk.CTkLabel(
            master=self,
            text="Product Management",
            font=("yu gothic ui", 28, "bold"),  # Tăng kích thước chữ
            text_color="#FF6F61",  # Sử dụng màu nổi bật hơn
            fg_color="#FFFFFF",  # Màu nền trắng cho tiêu đề
            padx=10,  # Thêm khoảng cách padding xung quanh chữ
            pady=10  # Thêm khoảng cách padding xung quanh chữ
        )
        self.label_title.pack(pady=10, padx=10)  # Giữ khoảng cách với các thành phần khác

        # Khung cuộn chứa bảng sản phẩm
        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=780, height=200)  # Giới hạn chiều cao khung
        self.scrollable_frame.pack(pady=10, fill='both', expand=False)  # Không để khung expand

        self.table_headers = ["ID", "Name", "Price", "Desc", "Actions"]
        self.products = []  # Danh sách lưu trữ thông tin sản phẩm

        self.create_table()

        # Form để thêm/sửa sản phẩm
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.pack(pady=10)  # Đặt form_frame để mở rộng theo cửa sổ

        # Chia cột cho thông tin sản phẩm và nút
        self.create_form()

        # Tải hình ảnh cho các nút sử dụng CTkImage
        self.img_back = ctk.CTkImage(light_image=Image.open("images/back.png"), size=(40, 40))

        # Nút trở về Main Application với kích thước lớn hơn
        self.button_back = ctk.CTkButton(
            master=self,
            text="",  # Không cần văn bản
            fg_color="#FACE9C",  # Màu nền nút
            image=self.img_back,  # Hình ảnh nút
            command=self.back_to_main,
            hover_color="#F09C42",
            width=60,  # Đặt chiều rộng nút
            height=60,  # Đặt chiều cao nút
            corner_radius=10,  # Bo góc nút cho mềm mại
        )
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
            ["1", "Product A", "$10", "Description A Description A"],
            ["2", "Product B", "$20", "Description B Description B"],
            ["3", "Product C", "$30", "Description C"],
            ["4", "Product D", "$40", "Description D"],
            ["5", "Product E", "$50", "Description E"],
            ["6", "Product F", "$60", "Description F"],
            ["7", "Product G", "$70", "Description G"],
            ["8", "Product H", "$80", "Description H"],
        ]

        # Thiết lập chiều rộng cố định cho các cột
        column_widths = [50, 150, 50, 200, 120]  # Danh sách kích thước cố định của từng cột

        # Tải icon cho các nút
        edit_icon = ctk.CTkImage(light_image=Image.open("images/edit.png"), size=(20, 20))  # Icon chỉnh sửa
        delete_icon = ctk.CTkImage(light_image=Image.open("images/remove.png"), size=(20, 20))  # Icon xóa

        for index, product in enumerate(self.products):
            for j, value in enumerate(product):
                label = ctk.CTkLabel(
                    self.scrollable_frame,
                    text=value,
                    width=column_widths[j],  # Đặt kích thước cố định cho mỗi cột
                    anchor="w",  # Căn văn bản về phía trái
                    wraplength=0  # Tắt ngắt dòng, đặt giá trị lớn hơn nếu cần
                )
                label.grid(row=index + 1, column=j, padx=10, pady=5)

            # Nút sửa sản phẩm
            edit_button = ctk.CTkButton(
                self.scrollable_frame,
                text="",
                image=edit_icon,  # Thêm icon chỉnh sửa
                width=60,  # Kích thước rộng hơn để nhìn cân đối
                height=40,  # Chiều cao lớn hơn
                fg_color="#5A9BD5",  # Màu nền xanh dịu mắt
                hover_color="#41729F",  # Màu khi hover (sáng hơn một chút)
                text_color="white",  # Màu chữ trắng
                corner_radius=10,  # Bo tròn góc nút
                font=("Arial", 12, "bold"),  # Font chữ đậm và lớn
                command=lambda idx=index: self.edit_product(idx)
            )
            edit_button.grid(row=index + 1, column=len(product), padx=10, pady=5)

            # Nút xóa sản phẩm
            delete_button = ctk.CTkButton(
                self.scrollable_frame,
                text="",
                image=delete_icon,  # Thêm icon xóa
                width=60,  # Kích thước rộng hơn
                height=40,  # Chiều cao lớn hơn
                fg_color="#D9534F",  # Màu nền đỏ cho nút xóa
                hover_color="#C9302C",  # Màu khi hover đỏ đậm hơn
                text_color="white",  # Màu chữ trắng
                corner_radius=10,  # Bo tròn góc nút
                font=("Arial", 12, "bold"),  # Font chữ đậm và lớn
                command=lambda idx=index: self.delete_product(idx)
            )
            delete_button.grid(row=index + 1, column=len(product) + 1, padx=10, pady=5)

    def create_form(self):
        # Cột cho thông tin sản phẩm
        info_column = ctk.CTkFrame(self.form_frame)
        info_column.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Cột cho nút
        button_column = ctk.CTkFrame(self.form_frame)
        button_column.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Cấu hình tỷ lệ cột
        self.form_frame.grid_columnconfigure(0, weight=7)  # Cột thông tin sản phẩm chiếm 7 phần
        self.form_frame.grid_columnconfigure(1, weight=3)  # Cột nút chiếm 3 phần

        # Trường ID sản phẩm (chỉ để xem)
        self.label_id = ctk.CTkLabel(info_column, text="Product ID:")
        self.label_id.grid(row=0, column=0, padx=10, pady=5, sticky="e")  # Căn phải

        self.entry_id = ctk.CTkEntry(info_column, state="readonly")  # Bỏ width để tự động mở rộng
        self.entry_id.grid(row=0, column=1, padx=10, pady=5, sticky="ew")  # Căn giữa

        # Trường tên sản phẩm
        self.label_name = ctk.CTkLabel(info_column, text="Product Name:")
        self.label_name.grid(row=1, column=0, padx=10, pady=5, sticky="e")  # Căn phải

        self.entry_name = ctk.CTkEntry(info_column, placeholder_text="Product Name")  # Bỏ width
        self.entry_name.grid(row=1, column=1, padx=10, pady=5, sticky="ew")  # Căn giữa

        # Trường giá sản phẩm
        self.label_price = ctk.CTkLabel(info_column, text="Product Price:")
        self.label_price.grid(row=2, column=0, padx=10, pady=5, sticky="e")  # Căn phải

        self.entry_price = ctk.CTkEntry(info_column, placeholder_text="Product Price")  # Bỏ width
        self.entry_price.grid(row=2, column=1, padx=10, pady=5, sticky="ew")  # Căn giữa

        # Trường mô tả sản phẩm
        self.label_desc = ctk.CTkLabel(info_column, text="Product Desc:")
        self.label_desc.grid(row=3, column=0, padx=10, pady=5, sticky="e")  # Căn phải

        self.entry_desc = ctk.CTkEntry(info_column, placeholder_text="Product Desc")  # Bỏ width
        self.entry_desc.grid(row=3, column=1, padx=10, pady=5, sticky="ew")  # Căn giữa

        # Thêm Combobox để chọn danh mục sản phẩm
        self.label_category = ctk.CTkLabel(info_column, text="Product Category:")
        self.label_category.grid(row=4, column=0, padx=10, pady=5, sticky="e")  # Căn phải

        # Danh sách các category (danh mục sản phẩm)
        self.category_options = ["Category A", "Category B", "Category C", "Category D", "Category E"]
        self.combobox_category = ctk.CTkComboBox(info_column, values=self.category_options)
        self.combobox_category.grid(row=4, column=1, padx=10, pady=5, sticky="ew")  # Căn giữa

        # Nút thêm sản phẩm
        self.button_add = ctk.CTkButton(
            master=button_column,
            text="Add Product",
            font=("yu gothic ui", 16, "bold"),
            fg_color="#43CD80",  # Màu nền đỏ cam nổi bật
            hover_color="#2E8B57",  # Màu khi di chuột qua
            corner_radius=15,  # Bo góc cho nút
            width=150,  # Đặt chiều rộng nút
            height=40,  # Đặt chiều cao nút
            command=self.add_product
        )
        self.button_add.grid(row=0, column=0, pady=10, padx=10, sticky="ew")  # Thêm padx

        # Nút sửa sản phẩm
        self.button_edit = ctk.CTkButton(
            master=button_column,
            text="Update Product",
            font=("yu gothic ui", 16, "bold"),
            fg_color="#FF4040",
            hover_color="#CD3333",
            corner_radius=15,  # Bo góc cho nút
            width=150,  # Đặt chiều rộng nút
            height=40,  # Đặt chiều cao nút
            command=lambda: self.edit_product
        )
        self.button_edit.grid(row=1, column=0, pady=5, padx=10, sticky="ew")  # Thêm padx

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