import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
views_dir = os.path.join(current_dir, '../')
sys.path.append(views_dir)

import styles
import window


def show_dialog(controller, frame_parent, data_id):
    # Create and show the dialog
    width = 400
    height = 200

    # Create and show the dialog
    dialog_delete = window.create_dialog(frame_parent, "Delete Data Form", width, height)
    # Create a frame to hold the form elements
    form_frame = ttk.Frame(dialog_delete, padding=(20, 10))
    form_frame.pack(fill="both", expand=True)

    # Create labels and entry fields
    name_label = ttk.Label(form_frame, text="Bạn có muốn delete")
    name_label.grid(row=0, column=0, sticky="w")

    # Create labels and entry fields
    btn_ok = tk.Button(form_frame, text="Save", command=lambda: on_save(data_id))
    btn_ok.grid(row=1, column=0, sticky="ew")
    btn_cancel = tk.Button(form_frame, text="Cancel", command=lambda: on_cancel())
    btn_cancel.grid(row=1, column=1, sticky="ew")

    def on_save(data_id):
        controller.delete(data_id)
        dialog_delete.destroy()
        messagebox.showinfo("Success", "Xoá dữ liệu thành công!")

    def on_cancel():
        dialog_delete.destroy()
