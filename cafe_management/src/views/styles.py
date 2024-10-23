# styles.py
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def get_font():
    return ("Arial", 14)


def get_button_menu_font():
    return ("Arial", 16, "bold")


def get_button_actions_font():
    return ("Arial", 12, "bold")


BUTTON_ACTIVE_COLOR = "#000000"  # Black
BUTTON_NORMAL_COLOR = "#CD6600"
BUTTON_FOREGROUND_COLOR = "#FFFFFF"  # White
FOREGROUND_COLOR = "#FFFFFF"  # White

BACKGROUND_COLOR = "#CD6600"
BACKGROUND_TREEVIEW="#FFFFE0"
BACKGROUND_DIALOG="#FFFFE0"

DISABLED_FOREGROUND = "#1C1C1C"
TEXT_COLOR_BLACK = "#000000"  # Black

FONT = ("Arial", 10)  # Kiểu chữ cho ô dữ liệu
FONT_HEADING = ("Arial", 12, "bold")  # Kiểu chữ cho tiêu đề
TEXT_COLOR_GREY = "#333333"  # Màu chữ ô dữ liệu
TEXT_COLOR_WHITE = "#FFFFFF"
FONT_SELECTED = ("Arial", 10, "bold")  # Kiểu chữ cho ô khi chọn


BTN_MENU = {
    "font": get_button_menu_font(),
    "bg": BACKGROUND_COLOR,
    "fg": FOREGROUND_COLOR,
    "activebackground": BUTTON_ACTIVE_COLOR,
    "activeforeground": BUTTON_FOREGROUND_COLOR,
    "padx": 10,
    "pady": 10,
    "relief": tk.FLAT,
    "borderwidth": 0,
    "highlightthickness": 0,
    "width": 15,  # Đặt chiều rộng cho nút
    "disabledforeground": DISABLED_FOREGROUND  # Màu chữ khi button bị disable
}

BTN_ADD = {
    "bg": "#4CAF50",
    "fg": FOREGROUND_COLOR,
    "font": get_button_actions_font(),
    "activebackground": "#3E8E41",
    "activeforeground": BUTTON_FOREGROUND_COLOR,
    "padx": 8,
    "pady": 4,
    "relief": tk.FLAT,
    "borderwidth": 0,
    "highlightthickness": 0
}


# Hàm để trả về đối tượng BTN_ADD khi có root window
def get_btn_add():
    # Lấy đường dẫn tương đối của thư mục dự án
    project_dir = os.path.dirname(os.path.dirname(__file__))
    # Đường dẫn đến hình ảnh
    add_icon_path = os.path.join(project_dir, "images", "add.png")

    add_icon = Image.open(add_icon_path)
    add_icon = add_icon.resize((20, 20), Image.LANCZOS)
    add_photo = ImageTk.PhotoImage(add_icon)  # Tạo ảnh sau khi root window có sẵn

    BTN_ADD = {
        "bg": "#4CAF50",
        "fg": FOREGROUND_COLOR,
        "font": get_button_actions_font(),
        "activebackground": "#3E8E41",
        "activeforeground": BUTTON_FOREGROUND_COLOR,
        "padx": 8,
        "pady": 4,
        "relief": tk.FLAT,
        "borderwidth": 0,
        "highlightthickness": 0,
        "image": add_photo,
        "compound": "left"
    }

    return BTN_ADD


BTN_UPDATE = {
    "bg": "#2196F3",
    "fg": FOREGROUND_COLOR,
    "font": get_button_actions_font(),
    "activebackground": "#1976D2",
    "activeforeground": BUTTON_FOREGROUND_COLOR,
    "padx": 8,
    "pady": 4,
    "relief": tk.FLAT,
    "borderwidth": 0,
    "highlightthickness": 0
}

BTN_DELETE = {
    "bg": "#F44336",
    "fg": FOREGROUND_COLOR,
    "font": get_button_actions_font(),
    "activebackground": "#C62828",
    "activeforeground": BUTTON_FOREGROUND_COLOR,
    "padx": 8,
    "pady": 4,
    "relief": tk.FLAT,
    "borderwidth": 0,
    "highlightthickness": 0
}

def configure_treeview_style():
    style = ttk.Style()

    style.theme_use("default")  # Đảm bảo sử dụng theme mặc định

    # Cấu hình Treeview
    style.configure("Custom.Treeview",
                    background=BACKGROUND_TREEVIEW,  # Màu nền
                    foreground=TEXT_COLOR_GREY,  # Màu chữ
                    rowheight=30,  # Chiều cao hàng
                    fieldbackground="#FFFFE0",  # Màu nền cho ô dữ liệu
                    font=FONT)  # Kiểu chữ cho ô dữ liệu

    # Cấu hình tiêu đề Treeview
    style.configure("Custom.Treeview.Heading",
                    background=BACKGROUND_COLOR,  # Màu nền tiêu đề
                    foreground=TEXT_COLOR_BLACK,  # Màu chữ tiêu đề
                    font=get_font(),  # Kiểu chữ tiêu đề
                    borderwidth=0)  # Đường viền tiêu đề

    # Tùy chỉnh màu sắc và font khi chọn hàng
    style.map("Custom.Treeview",
              background=[('selected', "#184785")],  # Màu nền khi chọn
              foreground=[('selected', TEXT_COLOR_WHITE)],  # Màu chữ khi chọn
              font=[('selected', FONT_SELECTED)])  # Kiểu chữ khi chọn


def dialog():
    # Tạo style tùy chỉnh
    style = ttk.Style()

    # Cấu hình style cho Label
    style.configure("TLabel",
                    font=("Helvetica", 12),  # Tăng kích thước font cho Label
                    foreground=TEXT_COLOR_BLACK,
                    background="#f0f0f0",  # Màu nền
                    padding=[10, 10])

    # Cấu hình style cho Entry
    style.configure("TEntry",
                    font=("Helvetica", 12),  # Tăng kích thước font cho Entry
                    padding=[10, 10],  # Tăng padding trên và dưới để chiều cao lớn hơn
                    relief="flat",
                    foreground="#1a1a1a",  # Màu chữ tối
                    background="#ffffff")  # Màu nền trắng
    style.map("TEntry",
              background=[('focus', '#e0f7fa'),  # Màu xanh nhạt khi focus
                          ('!focus', '#ffffff')],
              foreground=[('focus', '#1a1a1a'),
                          ('!focus', '#333333')])

    # Cấu hình style cho Button
    style.configure("TButton",
                    font=("Helvetica", 12, "bold"),  # Tăng kích thước font cho Button
                    padding=5,
                    relief="raised",
                    background="#008CBA",  # Màu xanh lam
                    foreground="white")
    style.map("TButton",
              background=[('active', '#005f75')],  # Màu xanh đậm hơn khi active
              relief=[('pressed', 'sunken'), ('!pressed', 'raised')])

    # Cấu hình style cho Combobox
    style.configure("TCombobox",
                    font=("Helvetica", 12),  # Tăng kích thước font cho Combobox
                    padding=5,
                    relief="flat",
                    background="#ffffff")  # Màu nền trắng
    style.map("TCombobox",
              fieldbackground=[('focus', '#e0f7fa'),
                               ('!focus', '#ffffff')],
              background=[('focus', '#e0f7fa'),
                          ('!focus', '#ffffff')])

    # Cấu hình style cho Toplevel (Dialog)
    style.configure("TFrame", background="#f0f0f0")  # Màu nền sáng cho dialog

def create_button_style():
    style = ttk.Style()

    # Cấu hình style cho Button lưu
    style.configure("Save.TButton", font=("Helvetica", 10, "bold"), padding=5, relief="raised",
                    background="#4CAF50", foreground="white")
    style.map("Save.TButton",
              background=[('active', '#45a049')],
              relief=[('pressed', 'sunken'), ('!pressed', 'raised')])

    # Cấu hình style cho Button hủy
    style.configure("Cancel.TButton", font=("Helvetica", 10, "bold"), padding=5, relief="raised",
                    background="#f44336", foreground="white")
    style.map("Cancel.TButton",
              background=[('active', '#e53935')],
              relief=[('pressed', 'sunken'), ('!pressed', 'raised')])
