import customtkinter as ctk
from PIL import Image

class CustomerView(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Customer Management")
        window_width = 800  # Chiều rộng cửa sổ
        window_height = 600  # Chiều cao cửa sổ

        # Tính toán để căn giữa cửa sổ
        screen_width = self.winfo_screenwidth()  # Lấy chiều rộng màn hình
        screen_height = self.winfo_screenheight()  # Lấy chiều cao màn hình
        x_cordinate = int((screen_width - window_width) / 2)  # Tính toán tọa độ x
        y_cordinate = int((screen_height - window_height) / 2)  # Tính toán tọa độ y

        # Thiết lập vị trí và kích thước cửa sổ
        self.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

        # Tạo tiêu đề cho CategoryView
        self.label_title = ctk.CTkLabel(
            master=self,
            text="Customer Management",
            font=("yu gothic ui", 28, "bold"),  # Tăng kích thước chữ
            text_color="#FF6F61",  # Sử dụng màu nổi bật hơn
            fg_color="#FFFFFF",  # Màu nền trắng cho tiêu đề
            padx=10,  # Thêm khoảng cách padding xung quanh chữ
            pady=10  # Thêm khoảng cách padding xung quanh chữ
        )
        self.label_title.pack(pady=10, padx=10)  # Giữ khoảng cách với các thành phần khác

        # Khung cuộn chứa customer
        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=780, height=200)  # Giới hạn chiều cao khung
        self.scrollable_frame.pack(pady=10, fill='both', expand=False)  # Không để khung expand

        self.table_headers = ["ID", "Name", "Address", "Phone", "Point"]
        self.customers = []  # Danh sách lưu trữ customer

        self.create_table()

        # Form để thêm/sửa customer
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.pack(pady=10)

        # Chia cột cho thông tin customer và nút
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

        # Thêm một số khách hàng mẫu vào danh sách
        self.customers = [
            ["1", "John Doe", "123 Main St", "555-1234", "120"],
            ["2", "Jane Smith", "456 Oak St", "555-5678", "150"],
            ["3", "Alice Johnson", "789 Pine St", "555-9876", "100"],
            ["4", "Bob Brown", "321 Maple St", "555-6543", "200"],
            ["5", "Charlie Green", "654 Cedar St", "555-4321", "180"],
            ["6", "David Black", "987 Birch St", "555-8765", "220"],
            ["7", "Eve White", "111 Elm St", "555-3456", "160"],
            ["8", "Frank Gray", "222 Spruce St", "555-2345", "140"],
        ]

        # Thiết lập chiều rộng cố định cho các cột
        column_widths = [25, 50, 100, 25, 25]  # Danh sách kích thước cố định của từng cột

        for index, customer in enumerate(self.customers):
            for j, value in enumerate(customer):
                label = ctk.CTkLabel(
                    self.scrollable_frame,
                    text=value,
                    width=column_widths[j],  # Đặt kích thước cố định cho mỗi cột
                    anchor="w",  # Căn văn bản về phía trái
                    wraplength=0  # Tắt ngắt dòng, đặt giá trị lớn hơn nếu cần
                )
                label.grid(row=index + 1, column=j, padx=10, pady=5)

            # Nút sửa customer
            edit_button = ctk.CTkButton(self.scrollable_frame, text="Edit", width=60,  # Kích thước cố định cho nút
                                        command=lambda idx=index: self.edit_customer(idx))
            edit_button.grid(row=index + 1, column=len(customer), padx=10, pady=5)

            # Nút xóa customer
            delete_button = ctk.CTkButton(self.scrollable_frame, text="Delete", width=60,  # Kích thước cố định cho nút
                                          command=lambda idx=index: self.delete_customer(idx))
            delete_button.grid(row=index + 1, column=len(customer) + 1, padx=10, pady=5)

    def create_form(self):
        # Hàm kiểm tra đầu vào (chỉ cho phép số)
        def only_numbers(char):
            return char.isdigit() or char == ""  # Cho phép số hoặc chuỗi rỗng (khi xóa)

        # Tạo validatecommand cho Phone và Point
        vcmd = (self.register(only_numbers), '%P')  # '%P' là giá trị nhập vào

        # Cột cho thông tin
        info_column = ctk.CTkFrame(self.form_frame)
        info_column.grid(row=0, column=0, padx=10, pady=10)

        # Cột cho nút
        button_column = ctk.CTkFrame(self.form_frame)
        button_column.grid(row=0, column=1, padx=10, pady=10)

        # Trường ID customer (chỉ để xem)
        self.label_id = ctk.CTkLabel(info_column, text="Customer ID:")
        self.label_id.grid(row=0, column=0, padx=10, pady=5)

        self.entry_id = ctk.CTkEntry(info_column, state="readonly", width=200)  # Chỉ đọc
        self.entry_id.grid(row=0, column=1, padx=10, pady=5)

        # Trường tên customer
        self.label_name = ctk.CTkLabel(info_column, text="Customer Name:")
        self.label_name.grid(row=1, column=0, padx=10, pady=5)

        self.entry_name = ctk.CTkEntry(info_column, placeholder_text="Customer Name", width=200)
        self.entry_name.grid(row=1, column=1, padx=10, pady=5)

        # Trường địa chỉ
        self.label_address = ctk.CTkLabel(info_column, text="Address: ")
        self.label_address.grid(row=2, column=0, padx=10, pady=5)

        self.entry_address = ctk.CTkEntry(info_column, placeholder_text="Address", width=200)  # Tăng chiều rộng
        self.entry_address.grid(row=2, column=1, padx=10, pady=5)

        # Trường Phone (chỉ cho phép nhập số)
        self.label_phone = ctk.CTkLabel(info_column, text="Phone:")
        self.label_phone.grid(row=3, column=0, padx=10, pady=5)

        self.entry_phone = ctk.CTkEntry(info_column, placeholder_text="Phone", width=200, validate="key",
                                        validatecommand=vcmd)
        self.entry_phone.grid(row=3, column=1, padx=10, pady=5)

        # Trường Point (chỉ cho phép nhập số)
        self.label_point = ctk.CTkLabel(info_column, text="Point:")
        self.label_point.grid(row=4, column=0, padx=10, pady=5)

        self.entry_point = ctk.CTkEntry(info_column, placeholder_text="Point", width=200, validate="key",
                                        validatecommand=vcmd)
        self.entry_point.grid(row=4, column=1, padx=10, pady=5)

        # Nút thêm Customer
        self.button_add = ctk.CTkButton(master=button_column, text="Add Customer", command=self.add_customer)
        self.button_add.grid(row=0, column=0, pady=10)

        # Nút sửa Customer
        self.button_edit = ctk.CTkButton(master=button_column, text="Update Customer", command=lambda: self.edit_customer)
        self.button_edit.grid(row=1, column=0, pady=5)

    def add_customer(self):
        # Logic cho việc thêm loại sản phẩm
        print("Thêm custome mới!")

    def edit_customer(self, index=None):
        # Logic cho việc sửa loại sản phẩm
        if index is not None:
            print(f"Sửa customer tại chỉ số {index}!")
        else:
            print("Sửa customer!")

    def delete_customer(self, index):
        print(f"Xóa customer tại chỉ số {index}!")

    def back_to_main(self):
        # Hiển thị lại cửa sổ chính và đóng cửa sổ hiện tại
        self.master.deiconify()  # Hiển thị lại MainApplication
        self.destroy()  # Đóng cửa sổ ProductView