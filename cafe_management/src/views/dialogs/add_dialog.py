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


def show_dialog(controller, frame_parent, dict_cols, type_name):
    if frame_parent is NoneType:
        messagebox.showerror("Error", "Parent frame is not valid.")
        return
    width = 450
    height = 40 + len(dict_cols["columns_name_display"]) * 40
    dialog_add = window.create_dialog(frame_parent, "Add Data Form", width, height)
    # Gọi hàm dialog từ file styles.py để áp dụng style
    styles.dialog()

    # Tạo frame chứa các phần tử của form
    form_frame = ttk.Frame(dialog_add, padding=(10, 10))
    form_frame.pack(fill="both", expand=True)
    add_len = 0
    widgets = {}  # Dictionary to hold label-entry pairs
    # Tạo các trường nhập liệu dựa trên fields
    for idx, (col_name) in enumerate(dict_cols["columns_name"]):
        print(col_name)
        label = ttk.Label(form_frame, text=f"{dict_cols["columns_name_display"][idx]}:")
        if idx > 0:
            label.grid(row=idx, column=0, sticky="w", pady=5)
        # Tạo widget tương ứng
        match str(dict_cols["widget_type"][idx]):
            case "Combobox":
                # Ví dụ: Tạo combobox với các giá trị mẫu
                values = dict_cols["data_init"][col_name]["combobox_values"]
                # create a combobox
                selected_data = tk.StringVar()
                combobox = ttk.Combobox(form_frame, textvariable=selected_data ,values=values, width=35, name=col_name)
                widgets[col_name] = combobox
            case "Entry":
                entry = tk.Entry(form_frame, width=35, name=col_name)
                widgets[col_name] = entry
            case "Text":
                text = tk.Text(form_frame, width=35, height=8, name=col_name)
                add_len += 3
                widgets[col_name] = text

        if idx > 0:
            widgets[col_name].grid(row=idx, column=1, sticky="ew", pady=5)
            # các loại widget khác nếu có

    # Tạo nút lưu
    btn_save = tk.Button(form_frame, text="Save", command=lambda: on_save())
    btn_save.grid(row=len(dict_cols["columns_name"]), column=0, sticky="ew", pady=10)

    # Tạo nút hủy
    btn_cancel = tk.Button(form_frame, text="Cancel", command=lambda: on_cancel())
    btn_cancel.grid(row=len(dict_cols["columns_name"]), column=1, sticky="ew", pady=10)

    window.set_width_height_top_level(dialog_add, width, 40 + (add_len + len(dict_cols["columns_name"])) * 40)

    def on_save():
        data = window.get_widget_values(widgets)
        print("data add", data)
        controller.insert(data)
        dialog_add.destroy()
        messagebox.showinfo("Success", "Data added successfully!")

    def on_cancel():
        dialog_add.destroy()
