# styles.py
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def get_font():
    return ("Arial", 12)


def get_button_menu_font():
    return ("Arial", 12, "bold")


def get_button_actions_font():
    return ("Arial", 10)


BUTTON_ACTIVE_COLOR = "#000000"  # Black
BUTTON_NORMAL_COLOR = "#CD6600"
BUTTON_FOREGROUND_COLOR = "#FFFFFF"  # White
FOREGROUND_COLOR = "#FFFFFF"  # White
BACKGROUND_COLOR = "#CD6600"
DISABLED_FOREGROUND = "#1C1C1C"
TEXT_COLOR_BLACK = "#000000"  # Black

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
    "width": 12,  # Đặt chiều rộng cho nút
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

    style.configure("Custom.Treeview",
                    background="#FFFFE0",  # Màu nền
                    foreground="#333333",  # Màu chữ
                    rowheight=25,  # Chiều cao hàng
                    fieldbackground="#FFFFE0")  # Màu nền cho ô dữ liệu

    style.configure("Custom.Treeview.Heading",
                    background=BACKGROUND_COLOR,  # Màu nền tiêu đề
                    foreground=TEXT_COLOR_BLACK,  # Màu chữ tiêu đề
                    font=get_font(),  # Kiểu chữ tiêu đề
                    borderwidth=0)  # Đường viền tiêu đề


def dialog():
    # Tạo style tùy chỉnh
    style = ttk.Style()

    # Cấu hình style cho Label
    style.configure("TLabel", font=("Helvetica", 12), foreground="black", padding=10)

    # Cấu hình style cho Entry
    style.configure("TEntry", padding=5, relief="flat", foreground="blue")

    # Cấu hình style cho Button
    style.configure("TButton", font=("Helvetica", 10, "bold"), padding=5, relief="raised", background="#4CAF50",
                    foreground="white")
