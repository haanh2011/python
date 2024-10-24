import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox

current_dir = os.path.dirname(os.path.abspath(__file__))
views_dir = os.path.join(current_dir, '../')
sys.path.append(views_dir)

import styles
import window


def show_dialog(controller, frame_parent, dict_cols, name, display_name, data, staff_id, on_success=None):
    if frame_parent is None:
        messagebox.showerror("Error", "Parent frame is not valid.")
        return

    # Thiết lập chiều rộng
    width = 450
    print("show update", staff_id)
    # Tạo và hiển thị dialog
    dialog_update = window.create_dialog(frame_parent, f"Form cập nhật {name} ", width)

    # Gọi hàm dialog từ file styles.py để áp dụng style
    styles.dialog()

    # Tạo frame chứa các phần tử của form
    window.create_frame_in_dialog(controller=controller, dialog_frame=dialog_update, width=width,
                                  parent_frame=frame_parent, dict_cols=dict_cols, name=name, display_name=display_name,
                                  on_success=on_success, staff_id=staff_id, data=data, is_add=False)
