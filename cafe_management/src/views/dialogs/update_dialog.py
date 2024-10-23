import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox

current_dir = os.path.dirname(os.path.abspath(__file__))
views_dir = os.path.join(current_dir, '../')
sys.path.append(views_dir)

import styles
import window


def show_dialog(controller, frame_parent, dict_cols, type_name, data, on_success=None):
    if frame_parent is None:
        messagebox.showerror("Error", "Parent frame is not valid.")
        return

    # Thiết lập chiều rộng
    width = 430

    # Tính toán chiều cao tùy theo số lượng phần tử
    row_height = 50  # Chiều cao trung bình cho mỗi hàng (có thể điều chỉnh nếu cần)
    row_index = len(dict_cols["columns_name"])  # Số lượng hàng
    height = (row_index + 2) * row_height  # Thêm 2 cho nút lưu và hủy

    # Tạo và hiển thị dialog
    dialog_update = window.create_dialog(frame_parent, "Update Data Form", width, height)

    # Gọi hàm dialog từ file styles.py để áp dụng style
    styles.dialog()

    # Tạo frame chứa các phần tử của form
    window.create_frame_in_dialog(controller, dialog_update, width, frame_parent, dict_cols, type_name, on_success,data, False)
