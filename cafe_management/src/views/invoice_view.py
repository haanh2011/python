import customtkinter as ctk
from PIL import Image

class InvoiceView(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Invoice Management")
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
            text="Invoice Management",
            font=("yu gothic ui", 28, "bold"),  # Tăng kích thước chữ
            text_color="#FF6F61",  # Sử dụng màu nổi bật hơn
            fg_color="#FFFFFF",  # Màu nền trắng cho tiêu đề
            padx=10,  # Thêm khoảng cách padding xung quanh chữ
            pady=10  # Thêm khoảng cách padding xung quanh chữ
        )
        self.label_title.pack(pady=10, padx=10)  # Giữ khoảng cách với các thành phần khác

        # Khung cuộn chứa bảng sản phẩm
        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=780, height=250)  # Giới hạn chiều cao khung
        self.scrollable_frame.pack(pady=10, fill='both', expand=False)  # Không để khung expand

        self.table_headers = ["ID", "ID Order", "Date", "Desc"]
        self.invoices = []  # Danh sách lưu trữ thông tin invoice

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

        # Thêm một số hóa đơn (invoice) mẫu vào danh sách
        self.invoices = [
            ["1", "101", "2024-10-12", "Invoice for order 101 - Paid"],
            ["2", "102", "2024-10-11", "Invoice for order 102 - Pending payment"],
            ["3", "103", "2024-10-10", "Invoice for order 103 - Paid"],
            ["4", "104", "2024-10-09", "Invoice for order 104 - Overdue"],
            ["5", "105", "2024-10-08", "Invoice for order 105 - Paid"],
            ["6", "106", "2024-10-07", "Invoice for order 106 - Pending payment"],
            ["7", "107", "2024-10-06", "Invoice for order 107 - Paid"],
            ["8", "108", "2024-10-05", "Invoice for order 108 - Cancelled"],
        ]

        # Thiết lập chiều rộng cố định cho các cột
        column_widths = [25, 25, 25, 150]  # Danh sách kích thước cố định của từng cột

        for index, invoice in enumerate(self.invoices):
            for j, value in enumerate(invoice):
                label = ctk.CTkLabel(
                    self.scrollable_frame,
                    text=value,
                    width=column_widths[j],  # Đặt kích thước cố định cho mỗi cột
                    anchor="w",  # Căn văn bản về phía trái
                    wraplength=0  # Tắt ngắt dòng, đặt giá trị lớn hơn nếu cần
                )
                label.grid(row=index + 1, column=j, padx=10, pady=5)

            # Nút sửa invoice
            edit_button = ctk.CTkButton(self.scrollable_frame, text="Edit", width=60,  # Kích thước cố định cho nút
                                        command=lambda idx=index: self.edit_invoice(idx))
            edit_button.grid(row=index + 1, column=len(invoice), padx=10, pady=5)

            # Nút xóa invoice
            delete_button = ctk.CTkButton(self.scrollable_frame, text="Delete", width=60,  # Kích thước cố định cho nút
                                          command=lambda idx=index: self.delete_invoice(idx))
            delete_button.grid(row=index + 1, column=len(invoice) + 1, padx=10, pady=5)

    def create_form(self):
        # Cột cho thông tin
        info_column = ctk.CTkFrame(self.form_frame)
        info_column.grid(row=0, column=0, padx=10, pady=10)

        # Cột cho nút
        button_column = ctk.CTkFrame(self.form_frame)
        button_column.grid(row=0, column=1, padx=10, pady=10)

        # Trường ID Invoice (chỉ để xem)
        self.label_id = ctk.CTkLabel(info_column, text="Invoice ID:")
        self.label_id.grid(row=0, column=0, padx=10, pady=5)

        self.entry_id = ctk.CTkEntry(info_column, state="readonly", width=200)  # Chỉ đọc
        self.entry_id.grid(row=0, column=1, padx=10, pady=5)

        # Trường ID Order
        self.label_id_order = ctk.CTkLabel(info_column, text="ID Order:")
        self.label_id_order.grid(row=1, column=0, padx=10, pady=5)

        self.entry_id_order = ctk.CTkEntry(info_column, placeholder_text="ID Order", width=200)
        self.entry_id_order.grid(row=1, column=1, padx=10, pady=5)

        # Trường Date
        self.label_date = ctk.CTkLabel(info_column, text="Date: ")
        self.label_date.grid(row=2, column=0, padx=10, pady=5)

        self.entry_date = ctk.CTkEntry(info_column, placeholder_text="Date", width=200)  # Tăng chiều rộng
        self.entry_date.grid(row=2, column=1, padx=10, pady=5)

        # Trường Desc
        self.label_desc = ctk.CTkLabel(info_column, text="Desc:")
        self.label_desc.grid(row=3, column=0, padx=10, pady=5)

        self.entry_desc = ctk.CTkEntry(info_column, placeholder_text="Desc", width=200, validate="key")
        self.entry_desc.grid(row=3, column=1, padx=10, pady=5)

        # Nút thêm Invoice
        self.button_add = ctk.CTkButton(master=button_column, text="Add Invoice", command=self.add_invoice)
        self.button_add.grid(row=0, column=0, pady=10)

        # Nút sửa Invoice
        self.button_edit = ctk.CTkButton(master=button_column, text="Update Invoice", command=lambda: self.edit_invoice)
        self.button_edit.grid(row=1, column=0, pady=5)

    def add_invoice(self):
        # Logic cho việc thêm invoice
        print("Thêm invoice mới!")

    def edit_invoice(self, index=None):
        # Logic cho việc sửa invoice
        if index is not None:
            print(f"Sửa invoice tại chỉ số {index}!")
        else:
            print("Sửa invoice!")

    def delete_invoice(self, index):
        print(f"Xóa invoice tại chỉ số {index}!")

    def back_to_main(self):
        # Hiển thị lại cửa sổ chính và đóng cửa sổ hiện tại
        self.master.deiconify()  # Hiển thị lại MainApplication
        self.destroy()  # Đóng cửa sổ ProductView