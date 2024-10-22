import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox

current_dir = os.path.dirname(os.path.abspath(__file__))
views_dir = os.path.join(current_dir, '../')
sys.path.append(views_dir)

import styles
import window


def show_dialog(controller, frame_parent, dict_cols, data):
    if frame_parent is None:
        messagebox.showerror("Error", "Parent frame is not valid.")
        return

    width = 400
    height = 40 + len(dict_cols["columns_name_display"]) * 40
    # Create and show the dialog
    dialog_update = window.create_dialog(frame_parent, "Update Data Form",width,  height)

    # Gọi hàm dialog từ file styles.py để áp dụng style
    styles.dialog()

    # Tạo frame chứa các phần tử của form
    form_frame = ttk.Frame(dialog_update, padding=(10, 10))
    form_frame.pack(fill="both", expand=True)

    widgets = {}  # Dictionary to hold label-entry pairs
    row_index = 0
    # Tạo các trường nhập liệu dựa trên fields
    for idx, (col_name) in enumerate(dict_cols["columns_name"]):
        label = ttk.Label(form_frame, text=f"{dict_cols["columns_name_display"][idx]}:")
        label.grid(row=idx, column=0, sticky="w", pady=5)
        # Tạo widget tương ứng
        match str(dict_cols["widget_type"][idx]):
            case "Combobox":
                # Ví dụ: Tạo combobox với các giá trị mẫu
                values = dict_cols["data_init"][col_name]["combobox_values"]
                combobox = ttk.Combobox(form_frame, values=values, width=3, name=col_name)
                combobox.grid(row=idx, column=1, sticky="ew", pady=5)
                widgets[col_name] = combobox
            case "Entry":
                entry = tk.Entry(form_frame, width=35, name=col_name)
                entry.insert(tk.END, data["values"][idx])  # Set the default text to data["values"][idx]
                entry.grid(row=idx, column=1, sticky="ew", pady=5)
                widgets[col_name] = entry
            # các loại widget khác nếu có
        row_index +=1
    # Tạo nút lưu
    btn_save = tk.Button(form_frame, text="Save", command=lambda: on_save())
    btn_save.grid(row=row_index, column=0, sticky="ew", pady=10)

    # Tạo nút hủy
    btn_cancel = tk.Button(form_frame, text="Cancel", command=lambda: on_cancel())
    btn_cancel.grid(row=row_index, column=1, sticky="ew", pady=10)

    window.set_width_height_top_level(dialog_update, width, 40 + row_index * 40)
    def on_save():
        data = window.get_widget_values(widgets)
        controller.update(data)
        dialog_update.destroy()
        messagebox.showinfo("Success", "Thay đổi dữ liệu thành công!")

    def on_cancel():
        dialog_update.destroy()
