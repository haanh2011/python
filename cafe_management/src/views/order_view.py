import customtkinter as ctk
from PIL import Image

class OrderView(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Order Management")
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
            text="Order Management",
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

        self.table_headers = ["ID", "Staff", "Customer", "Date", "Detail", "Actions"]
        self.orders = []  # Danh sách lưu trữ thông tin order

        self.create_table()

        # Form để thêm/sửa sản phẩm
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.pack(pady=10)

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

        # Thêm một số đơn hàng mẫu vào danh sách
        self.orders = [
            ["1", "John Smith", "Alice Johnson", "2024-10-12", "3 x Item A, 2 x Item B"],
            ["2", "Jane Doe", "Bob Brown", "2024-10-11", "1 x Item C, 4 x Item D"],
            ["3", "Mark Johnson", "Eve White", "2024-10-10", "5 x Item E, 2 x Item F"],
            ["4", "Lucy Adams", "Charlie Green", "2024-10-09", "2 x Item G, 3 x Item H"],
            ["5", "Peter Parker", "David Black", "2024-10-08", "6 x Item I, 1 x Item J"],
            ["6", "Tony Stark", "Frank Gray", "2024-10-07", "3 x Item K, 5 x Item L"],
            ["7", "Bruce Wayne", "John Doe", "2024-10-06", "4 x Item M, 2 x Item N"],
            ["8", "Clark Kent", "Jane Smith", "2024-10-05", "2 x Item O, 6 x Item P"],
        ]

        # Thiết lập chiều rộng cố định cho các cột
        column_widths = [25, 50, 50, 50, 150, 120]  # Danh sách kích thước cố định của từng cột

        # Tải icon cho các nút
        edit_icon = ctk.CTkImage(light_image=Image.open("images/edit.png"), size=(20, 20))  # Icon chỉnh sửa
        delete_icon = ctk.CTkImage(light_image=Image.open("images/remove.png"), size=(20, 20))  # Icon xóa

        for index, order in enumerate(self.orders):
            for j, value in enumerate(order):
                label = ctk.CTkLabel(
                    self.scrollable_frame,
                    text=value,
                    width=column_widths[j],  # Đặt kích thước cố định cho mỗi cột
                    anchor="w",  # Căn văn bản về phía trái
                    wraplength=0  # Tắt ngắt dòng, đặt giá trị lớn hơn nếu cần
                )
                label.grid(row=index + 1, column=j, padx=10, pady=5)

            # Nút sửa order
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
                command=lambda idx=index: self.edit_order(idx)
            )
            edit_button.grid(row=index + 1, column=len(order), padx=10, pady=5)

            # Nút xóa order
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
                command=lambda idx=index: self.delete_order(idx)
            )
            delete_button.grid(row=index + 1, column=len(order) + 1, padx=10, pady=5)

    def create_form(self):
        # Cột cho thông tin
        info_column = ctk.CTkFrame(self.form_frame)
        info_column.grid(row=0, column=0, padx=10, pady=10)

        # Cột cho nút
        button_column = ctk.CTkFrame(self.form_frame)
        button_column.grid(row=0, column=1, padx=10, pady=10)

        # Trường ID order (chỉ để xem)
        self.label_id = ctk.CTkLabel(info_column, text="Order ID:")
        self.label_id.grid(row=0, column=0, padx=10, pady=5)

        self.entry_id = ctk.CTkEntry(info_column, state="readonly", width=200)  # Chỉ đọc
        self.entry_id.grid(row=0, column=1, padx=10, pady=5)

        # Trường Staff
        self.label_staff = ctk.CTkLabel(info_column, text="Staff:")
        self.label_staff.grid(row=1, column=0, padx=10, pady=5)

        self.entry_staff = ctk.CTkEntry(info_column, placeholder_text="Staff", width=200)
        self.entry_staff.grid(row=1, column=1, padx=10, pady=5)

        # Trường customer
        self.label_customer = ctk.CTkLabel(info_column, text="Customer: ")
        self.label_customer.grid(row=2, column=0, padx=10, pady=5)

        self.entry_customer = ctk.CTkEntry(info_column, placeholder_text="Customer", width=200)  # Tăng chiều rộng
        self.entry_customer.grid(row=2, column=1, padx=10, pady=5)

        # Trường Date
        self.label_date = ctk.CTkLabel(info_column, text="Date:")
        self.label_date.grid(row=3, column=0, padx=10, pady=5)

        self.entry_date = ctk.CTkEntry(info_column, placeholder_text="Date", width=200, validate="key")
        self.entry_date.grid(row=3, column=1, padx=10, pady=5)

        # Trường Detail
        self.label_detail = ctk.CTkLabel(info_column, text="Detail:")
        self.label_detail.grid(row=4, column=0, padx=10, pady=5)

        self.entry_detail = ctk.CTkEntry(info_column, placeholder_text="Detail", width=200, validate="key")
        self.entry_detail.grid(row=4, column=1, padx=10, pady=5)

        # Nút thêm Order
        self.button_add = ctk.CTkButton(
            master=button_column,
            text="Add Order",
            font=("yu gothic ui", 16, "bold"),
            fg_color="#43CD80",  # Màu nền đỏ cam nổi bật
            hover_color="#2E8B57",  # Màu khi di chuột qua
            corner_radius=15,  # Bo góc cho nút
            width=150,  # Đặt chiều rộng nút
            height=40,  # Đặt chiều cao nút
            command=self.add_order
        )
        self.button_add.grid(row=0, column=0, pady=10)

        # Nút sửa Order
        self.button_edit = ctk.CTkButton(
            master=button_column,
            text="Update Order",
            font=("yu gothic ui", 16, "bold"),
            fg_color="#FF4040",
            hover_color="#CD3333",
            corner_radius=15,  # Bo góc cho nút
            width=150,  # Đặt chiều rộng nút
            height=40,  # Đặt chiều cao nút
            command=lambda: self.edit_order
        )
        self.button_edit.grid(row=1, column=0, pady=5)

    def add_order(self):
        # Logic cho việc thêm order
        print("Thêm order mới!")

    def edit_order(self, index=None):
        # Logic cho việc sửa order
        if index is not None:
            print(f"Sửa order tại chỉ số {index}!")
        else:
            print("Sửa order!")

    def delete_order(self, index):
        print(f"Xóa order tại chỉ số {index}!")

    def back_to_main(self):
        # Hiển thị lại cửa sổ chính và đóng cửa sổ hiện tại
        self.master.deiconify()  # Hiển thị lại MainApplication
        self.destroy()  # Đóng cửa sổ ProductView