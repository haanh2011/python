import tkinter as tk
from tkinter import ttk, messagebox
import bcrypt

import os
import sys

from src.views import main_view
from src.helper import button_image

current_dir = os.path.dirname(os.path.abspath(__file__))
controllers_dir = os.path.join(current_dir, '../controllers')
sys.path.append(controllers_dir)

import login_controller
import window
import styles

# Function to create the main application window after login success
def show_main_app(staff_id = "admin"):
    # Tạo cửa sổ chính
    main_app_root = main_view.create_root_window(1280, 720)
    # Đảm bảo cửa sổ luôn căn giữa khi khởi động lại
    main_app_root.update_idletasks()  # Cập nhật cửa sổ trước khi lấy kích thước
    main_view.frame_main(main_app_root, staff_id)

    main_app_root.mainloop()


def create_login_form(parent, login_command):
    styles.configure_style_login()

    form_frame = ttk.Frame(parent, padding=(20, 10))
    form_frame.pack(fill="both", expand=True)

    title_label = ttk.Label(
        form_frame,
        text="Đăng Nhập",
        font=("Helvetica", 16, "bold"),  # Font chữ cho tiêu đề
        foreground="#000000",  # Màu chữ
        background="#f0f0f0",  # Màu nền
        padding=[10, 5]  # Padding cho label
    )
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    username_label = ttk.Label(form_frame, text="Tên đăng nhập:", style="TLabel")
    username_label.grid(row=1, column=0, sticky="w", pady=(5, 0))
    username_entry = ttk.Entry(form_frame, style="TEntry")
    username_entry.grid(row=1, column=1, sticky="ew", pady=(5, 0))

    password_label = ttk.Label(form_frame, text="Mật khẩu:", style="TLabel")
    password_label.grid(row=2, column=0, sticky="w", pady=(5, 0))
    password_entry = ttk.Entry(form_frame, show="*", style="TEntry")
    password_entry.grid(row=2, column=1, sticky="ew", pady=(5, 10))

    login_button = button_image.create_image_button(
        parent=form_frame,
        name="login_button",
        text="Đăng Nhập",
        command=login_command,
        tooltip_text="Nhấn để đăng nhập"
    )
    login_button.grid(row=3, column=0, columnspan=2, pady=10)

    form_frame.columnconfigure(1, weight=1)
    return username_entry, password_entry  # Trả về các Entry để sử dụng sau này

def create_login_frame():

    login_root = window.create_root_window("Đăng nhập", 400,  240)
    login_root.resizable(False, False)  # Ngăn không cho thay đổi kích thước cửa sổ

    login_controller.add_user_admin()

    def login(event=None): # Sử dụng event=None để có thể gọi hàm từ sự kiện hoặc trực tiếp
        username = username_entry.get()
        password = password_entry.get()
        result = login_controller.get_user(username)

        if result:
            stored_password = result[1]  # Get the stored hashed password# Check if the provided password matches the hashed password
            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                # messagebox.showinfo("Success", "Đăng nhập thành công!")
                login_root.destroy()  # Close login window on success
                show_main_app(result[0])  # Show main application window after login success
                return True
            messagebox.showerror("Error", "Tên đăng nhập hoặc mật khẩu không đúng!")
        else:
            messagebox.showerror("Error", "Tên đăng nhập hoặc mật khẩu không đúng!")

    username_entry, password_entry = create_login_form(login_root, login)

    # Bind phím Enter để kích hoạt nút Đăng Nhập
    login_root.bind('<Return>', login)  # 'Return' là sự kiện nhấn Enter

    login_root.mainloop()
    return  login_root