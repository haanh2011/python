import tkinter as tk
from tkinter import ttk, messagebox
import os
import sys
from types import NoneType

current_dir = os.path.dirname(os.path.abspath(__file__))
views_dir = os.path.join(current_dir, '../')
sys.path.append(views_dir)

import styles
import window

def show_dialog(controller, frame_parent, dict_cols, name, display_name, on_success=None):
    """
    Hiển thị hộp thoại thêm dữ liệu.
        :param controller: Controller quản lý việc thêm dữ liệu.
        :param frame_parent: Khung cha chứa dialog.
        :param dict_cols: Từ điển chứa tên cột, loại widget và dữ liệu khởi tạo.
        :param type_name: Loại dữ liệu được thêm.
        :param on_success: Hàm callback để cập nhật Treeview.
    """

    if frame_parent is NoneType:
        messagebox.showerror("Error", "Parent frame is not valid.")
        return

    # Lấy kích thước màn hình và tính toán chiều cao dialog
    screen_height = frame_parent.winfo_screenheight()
    width = 430
    height = len(dict_cols["columns_name"]) * 50
    max_height = int(screen_height * 0.6)
    height = min(height, max_height)

    dialog_add = window.create_dialog(frame_parent, f"Form thêm {display_name}")

    # Gọi hàm dialog từ file styles.py để áp dụng style
    styles.dialog()
    window.create_frame_in_dialog(controller, dialog_add, width, frame_parent, dict_cols, name, display_name, on_success)
