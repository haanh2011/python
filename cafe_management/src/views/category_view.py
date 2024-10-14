import customtkinter as ctk
from PIL import Image

class CategoryView(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Category Management")
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
            text="Category Management",
            font=("yu gothic ui", 28, "bold"),  # Tăng kích thước chữ
            text_color="#FF6F61",  # Sử dụng màu nổi bật hơn
            fg_color="#FFFFFF",  # Màu nền trắng cho tiêu đề
            padx=10,  # Thêm khoảng cách padding xung quanh chữ
            pady=10  # Thêm khoảng cách padding xung quanh chữ
        )
        self.label_title.pack(pady=10, padx=10)  # Giữ khoảng cách với các thành phần khác

        # Khung cuộn chứa bảng sản phẩm
        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=780, height=300)  # Giới hạn chiều cao khung
        self.scrollable_frame.pack(pady=10, fill='both', expand=False)  # Không để khung expand

        self.table_headers = ["ID", "Name", "Actions"]
        self.category = []  # Danh sách lưu trữ thông tin loại sản phẩm

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
        # Tạo tiêu đề cho bảng và căn lề trái
        for header in self.table_headers:
            label = ctk.CTkLabel(
                self.scrollable_frame,
                text=header,
                anchor="center",  # Căn giữa tiêu đề
                width=100  # Đặt kích thước cố định cho tiêu đề nếu cần
            )
            label.grid(row=0, column=self.table_headers.index(header), padx=10, pady=5, sticky="w")

        # Thêm cột cho các nút (Edit và Delete)
        self.scrollable_frame.grid_columnconfigure(len(self.table_headers) - 2, weight=1)  # Cột Edit
        self.scrollable_frame.grid_columnconfigure(len(self.table_headers) - 1, weight=1)  # Cột Delete

        # Cập nhật danh sách headers để có thể hiển thị tên cột cho nút
        self.table_headers.append("Edit")
        self.table_headers.append("Delete")

        # Thêm một số sản phẩm mẫu vào danh sách
        self.category = [
            ["1", "Category A"],
            ["2", "Category B"],
            ["3", "Category C"],
            ["4", "Category D"],
            ["5", "Category E"],
            ["6", "Category F"],
            ["7", "Category G"],
            ["8", "Category H"],
        ]

        # Thiết lập chiều rộng cố định cho các cột
        column_widths = [50, 150, 120]  # Danh sách kích thước cố định của từng cột

        # Tải icon cho các nút
        edit_icon = ctk.CTkImage(light_image=Image.open("images/edit.png"), size=(20, 20))  # Icon chỉnh sửa
        delete_icon = ctk.CTkImage(light_image=Image.open("images/remove.png"), size=(20, 20))  # Icon xóa

        for index, cate in enumerate(self.category):
            for j, value in enumerate(cate):
                label = ctk.CTkLabel(
                    self.scrollable_frame,
                    text=value,
                    width=column_widths[j],  # Đặt kích thước cố định cho mỗi cột
                    anchor="w",  # Căn văn bản về phía trái
                    wraplength=0  # Tắt ngắt dòng, đặt giá trị lớn hơn nếu cần
                )
                label.grid(row=index + 1, column=j, padx=10, pady=5)

            # Nút sửa loại sản phẩm
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
                command=lambda idx=index: self.edit_cate(idx)
            )
            edit_button.grid(row=index + 1, column=len(cate), padx=10, pady=5)

            # Nút xóa loại sản phẩm
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
                command=lambda idx=index: self.delete_cate(idx)
            )
            delete_button.grid(row=index + 1, column=len(cate) + 1, padx=10, pady=5)

    def create_form(self):
        # Cột cho thông tin loại sản phẩm
        info_column = ctk.CTkFrame(self.form_frame)
        info_column.grid(row=0, column=0, padx=10, pady=10)

        # Cột cho nút
        button_column = ctk.CTkFrame(self.form_frame)
        button_column.grid(row=0, column=1, padx=10, pady=10)

        # Trường ID loại sản phẩm (chỉ để xem)
        self.label_id = ctk.CTkLabel(info_column, text="Category ID:")
        self.label_id.grid(row=0, column=0, padx=10, pady=5)

        self.entry_id = ctk.CTkEntry(info_column, state="readonly", width=200)  # Chỉ đọc
        self.entry_id.grid(row=0, column=1, padx=10, pady=5)

        # Trường tên sản phẩm
        self.label_name = ctk.CTkLabel(info_column, text="Category Name:")
        self.label_name.grid(row=1, column=0, padx=10, pady=5)

        self.entry_name = ctk.CTkEntry(info_column, placeholder_text="Category Name", width=200)
        self.entry_name.grid(row=1, column=1, padx=10, pady=5)

        # Nút thêm loại sản phẩm
        self.button_add = ctk.CTkButton(
            master=button_column,
            text="Add Category",
            font=("yu gothic ui", 16, "bold"),
            fg_color="#43CD80",  # Màu nền đỏ cam nổi bật
            hover_color="#2E8B57",  # Màu khi di chuột qua
            corner_radius=15,  # Bo góc cho nút
            width=150,  # Đặt chiều rộng nút
            height=40,  # Đặt chiều cao nút
            command=self.add_cate
        )
        self.button_add.grid(row=0, column=0, pady=10)

        # Nút sửa loại sản phẩm
        self.button_edit = ctk.CTkButton(
            master=button_column,
            text="Update Category",
            font=("yu gothic ui", 16, "bold"),
            fg_color="#FF4040",
            hover_color="#CD3333",
            corner_radius=15,  # Bo góc cho nút
            width=150,  # Đặt chiều rộng nút
            height=40,  # Đặt chiều cao nút
            command=lambda: self.edit_cate
        )
        self.button_edit.grid(row=1, column=0, pady=5)

    def add_cate(self):
        # Logic cho việc thêm loại sản phẩm
        print("Thêm loại sản phẩm mới!")

    def edit_cate(self, index=None):
        # Logic cho việc sửa loại sản phẩm
        if index is not None:
            print(f"Sửa loại sản phẩm tại chỉ số {index}!")
        else:
            print("Sửa loại sản phẩm!")

    def delete_cate(self, index):
        print(f"Xóa loại sản phẩm tại chỉ số {index}!")

    def back_to_main(self):
        # Hiển thị lại cửa sổ chính và đóng cửa sổ hiện tại
        self.master.deiconify()  # Hiển thị lại MainApplication
        self.destroy()  # Đóng cửa sổ CategoryView