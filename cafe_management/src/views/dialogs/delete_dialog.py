import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
views_dir = os.path.join(current_dir, '../')
sys.path.append(views_dir)

import styles
import window

def show_dialog(controller, frame_parent, data_id, on_success=None):

    # Thiết lập kích thước dialog
    width, height = 400, 100
    dialog_delete = window.create_dialog(frame_parent, "Delete Data Form", width, height)

    # Tạo frame để chứa các phần tử của form
    form_frame = ttk.Frame(dialog_delete, padding=(20, 10))
    form_frame.pack(fill="both", expand=True)

    # Tạo nhãn xác nhận với dữ liệu động
    name_label = ttk.Label(form_frame, text=f"Bạn có muốn xóa {data_id}?")
    name_label.grid(row=0, column=0, columnspan=2, sticky="w")

    # Tạo nút "Save" và "Cancel"
    btn_ok = ttk.Button(form_frame, text="Save", command=lambda: on_save(), style="Save.TButton")
    btn_ok.grid(row=1, column=0, sticky="ew", pady=10)

    btn_cancel = ttk.Button(form_frame, text="Cancel", command=dialog_delete.destroy, style="Cancel.TButton")
    btn_cancel.grid(row=1, column=1, sticky="ew", pady=10)

    def on_save():
        controller.delete(data_id)  # Gọi controller để xóa dữ liệu
        dialog_delete.destroy()  # Đóng dialog
        messagebox.showinfo("Success", "Xoá dữ liệu thành công!")  # Thông báo thành công

        if on_success:
            on_success()  # Gọi callback để cập nhật Treeview