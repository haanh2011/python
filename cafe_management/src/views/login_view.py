import tkinter as tk
from tkinter import ttk, messagebox


def login():
    username = username_entry.get()
    password = password_entry.get()

    # Thay thế đoạn này bằng logic xác thực thực tế của bạn
    if username == "1" and password == "1":
        messagebox.showinfo("Success", "Đăng nhập thành công!")
    else:
        messagebox.showerror("Error", "Tên đăng nhập hoặc mật khẩu không đúng!")


def create_login_frame(root_frame):
    # Tạo frame để chứa các phần tử của form đăng nhập
    form_frame = ttk.Frame(root_frame, padding=(20, 10))
    form_frame.pack(fill="both", expand=True)

    # Tạo nhãn tiêu đề
    title_label = ttk.Label(form_frame, text="Đăng Nhập", font=("Helvetica", 16, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    # Tạo nhãn và trường nhập cho tên đăng nhập và mật khẩu
    username_label = ttk.Label(form_frame, text="Tên đăng nhập:")
    username_label.grid(row=1, column=0, sticky="w", pady=(5, 0))
    username_entry = ttk.Entry(form_frame)
    username_entry.grid(row=1, column=1, sticky="ew", pady=(5, 0))

    password_label = ttk.Label(form_frame, text="Mật khẩu:")
    password_label.grid(row=2, column=0, sticky="w", pady=(5, 0))
    password_entry = ttk.Entry(form_frame, show="*")  # Ẩn mật khẩu
    password_entry.grid(row=2, column=1, sticky="ew", pady=(5, 10))

    # Tạo nút đăng nhập
    login_button = ttk.Button(form_frame, text="Đăng Nhập", command=login)
    login_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Thay đổi màu nền cho button
    login_button.configure(style="TButton")

    # Tạo kiểu cho button
    style = ttk.Style()
    style.configure("TButton", padding=6, relief="flat", background="#4CAF50", foreground="black",
                    font=("Helvetica", 10, "bold"))
    style.map("TButton", background=[("active", "#45a049")])  # Màu nền khi nhấn

    # Điều chỉnh trọng số cột để làm cho form phản hồi tốt hơn
    form_frame.columnconfigure(1, weight=1)

    return form_frame
