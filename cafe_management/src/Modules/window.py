from customtkinter import *
from PIL import Image
from matplotlib.backend_tools import cursors

PRIMARY_COLOR = '#FFA24C'
PRIMARY_HOVER_COLOR = '#FF6500'
TEXT_PRIMARY_COLOR = '#243642'

class DataTable:
    table = None #CTkFrame()
    table_header = [] #['header1', 'header2', 'header3']
    table_header_type = {
        'id': 'float'
    } #{'header': 'float', 'header2': 'string'}
    table_data = [] #[
    # ['dataRow1_1','dataRow1_2','dataRow1_3'],
    # ['dataRow2_1','dataRow2_2','dataRow2_3']
    # ]
    table_column_width = [] # [50,100,150]
    table_header_frame = None
    table_data_frame = None
    edit_icon = CTkImage(light_image=Image.open("images/edit.png"), size=(20, 20))
    delete_icon = CTkImage(light_image=Image.open("images/remove.png"), size=(20, 20))
    def __init__(self, table, table_header, table_data, table_column_width):
        self.table = table
        self.table_header_frame = CTkFrame(self.table, fg_color=PRIMARY_COLOR)
        self.table_data_frame = CTkScrollableFrame(self.table)
        self.table_headers = table_header
        self.table_data = table_data
        self.table_column_width = table_column_width

    def draw(self):
            self.table.pack(fill='both', expand=True, padx=5, pady=5)
            #Tạo Header
            self.draw_table_header()
            # Tạo Data
            self.draw_table_data()
    def draw_table_header(self):
        self.table_header_frame.pack(fill='x', expand=False, padx=5)
        # Tạo Table Header
        for header in self.table_headers:
            column = self.table_headers.index(header)
            width = self.table_column_width[column] if len(self.table_column_width) != 0 else 0
            table_header = CTkButton(self.table_header_frame,
                                    text=header + '▼',
                                    anchor="center",  # Căn giữa tiêu đề
                                    width=width,  # Đặt kích thước cố định cho tiêu đề nếu cần
                                    # wraplength=0,
                                    font=('', 16, 'bold'),
                                    text_color=TEXT_PRIMARY_COLOR,
                                    fg_color='transparent', bg_color='transparent',
                                    hover_color=PRIMARY_HOVER_COLOR,
                                    cursor = 'hand2'
                                    )
            table_header.value = header
            table_header.configure(command=lambda btn=table_header: self.handle_on_click_table_header(btn))# Truyền nút vào hàm xử lý)
            table_header.grid(row=0, column=column, sticky="nsew", padx=10, pady=5)

        self.table_header_frame.grid_columnconfigure(1, weight=1)

    def handle_on_click_table_header(self, btn):
        current_text = btn.cget('text')  # Lấy văn bản hiện tại của nút
        table_header = btn.value
        isDesc = False if '▼' in current_text else True
        # TODO: Đã sắp xếp cho cột ID
        if table_header.lower() in self.table_header_type: # Xác định các kiểu dữ liệu để tiến hành sort cho đúng
            index = self.table_headers.index(table_header)
            sorted_category = sorted(self.table_data, key=lambda x: int(x[index]), reverse=isDesc)
            print(sorted_category)

        # Kiểm tra xem văn bản có chứa "▲" hay không và thay đổi
        if '▲' in current_text:
            btn.configure(text=current_text.replace('▲', '▼'))
        else:
            btn.configure(text=current_text.replace('▼', '▲'))
    def draw_table_data(self):
        self.table_data_frame.pack(fill='both', expand=True)

        # Tạo Table Data
        for index, cate in enumerate(self.table_data):
            row = index + 1
            for j, value in enumerate(cate):
                column = j
                column_width = self.table_column_width[column] if len(self.table_column_width) != 0 else 0
                label = CTkLabel(
                    self.table_data_frame,
                    text=value,
                    width=column_width,  # Đặt kích thước cố định cho mỗi cột
                    anchor="center",  # Căn văn bản về phía trái
                    wraplength=0  # Tắt ngắt dòng, đặt giá trị lớn hơn nếu cần
                )
                label.grid(row=row, column=column, sticky="nsew", padx=10, pady=5)

            action_frame = CTkFrame(self.table_data_frame)
            action_frame.grid(row=row, column=len(cate), padx=15, pady=5)

            # Nút sửa loại sản phẩm
            edit_button = CTkButton(
                action_frame,
                text="",
                image=self.edit_icon,  # Thêm icon chỉnh sửa
                width=60,  # Kích thước rộng hơn để nhìn cân đối
                height=40,  # Chiều cao lớn hơn
                fg_color="#5A9BD5",  # Màu nền xanh dịu mắt
                hover_color="#41729F",  # Màu khi hover (sáng hơn một chút)
                text_color="white",  # Màu chữ trắng
                corner_radius=10,  # Bo tròn góc nút
                font=("Arial", 12, "bold"),  # Font chữ đậm và lớn
                command=lambda idx=index: self.edit_cate(idx)
            )
            edit_button.grid(row=0, column=0, padx=10)

            # Nút xóa loại sản phẩm
            delete_button = CTkButton(
                action_frame,
                text="",
                image=self.delete_icon,  # Thêm icon xóa
                width=60,  # Kích thước rộng hơn
                height=40,  # Chiều cao lớn hơn
                fg_color="#D9534F",  # Màu nền đỏ cho nút xóa
                hover_color="#C9302C",  # Màu khi hover đỏ đậm hơn
                text_color="white",  # Màu chữ trắng
                corner_radius=10,  # Bo tròn góc nút
                font=("Arial", 12, "bold"),  # Font chữ đậm và lớn
                command=lambda idx=index: self.delete_cate(idx)
            )
            delete_button.grid(row=0, column=1, padx=10)

            # actionFrame.grid_columnconfigure('all', weight=1)

            self.table_data_frame.grid_columnconfigure(1, weight=1)
    def delete_cate(self, index):
        print(index)
    def edit_cate(self, index):
        print(index)