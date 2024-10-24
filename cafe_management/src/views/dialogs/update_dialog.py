import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox

current_dir = os.path.dirname(os.path.abspath(__file__))
views_dir = os.path.join(current_dir, '../')
sys.path.append(views_dir)

import styles
import window


def show_dialog(controller, frame_parent, dict_cols, name, display_name, data, on_success=None):
    if frame_parent is None:
        messagebox.showerror("Error", "Parent frame is not valid.")
        return

    # Thiết lập chiều rộng
    width = 450

    # Tạo và hiển thị dialog
    dialog_update = window.create_dialog(frame_parent, f"Form cập nhật {name} ", width)

    # Gọi hàm dialog từ file styles.py để áp dụng style
    styles.dialog()

    # Tạo frame chứa các phần tử của form
    window.create_frame_in_dialog(controller, dialog_update, width, frame_parent, dict_cols, name, display_name, on_success,data, False)
