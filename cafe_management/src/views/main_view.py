import os
import sys
from tkinter import Tk, Label
from PIL import Image, ImageTk
current_dir = os.path.dirname(os.path.abspath(__file__))
utilities_dir = os.path.join(current_dir, '../utilities')
sys.path.append(utilities_dir)
import validate
views_dir = os.path.join(current_dir, '../views')
sys.path.append(views_dir)

import window
import category_view
import customer_view
import invoice_view
import order_view
import product_view
import staff_view
import dashboard_view

def create_root_window(width, height):
    return window.create_root_window("Ứng dụng Quản Lý Quán Cà Phê", width, height)

def frame_main(frame_root, staff_id):
    window.create_header(frame_root)

    # Register the validation function with tkinter

    # Register validation functions
    validate_integer_cmd = frame_root.register(validate.validate_integer_input)
    validate_float_cmd = frame_root.register(validate.validate_float_input)
    validate_length_cmd = frame_root.register(validate.validate_length_input)


    # Create frame for the left menu
    dashboard_frame = window.create_frame(frame_root, "dashboard_frame", bg="")
    dashboard_frame.pack(side="left", fill="y", padx=(10, 10))

    # Tải hình ảnh
    image_logo_path = "images/home_bg.jpg"
    image_logo = Image.open(image_logo_path)
    image_bg_path = "images/bg.jpg"
    image_bg = Image.open(image_bg_path)

    # Đặt kích thước cho hình ảnh
    new_size = (180, 100)  # Kích thước mới (width, height)
    image_resized = image_logo.resize(new_size, Image.LANCZOS)  # Resize hình ảnh

    # Chuyển đổi hình ảnh đã thay đổi kích thước thành PhotoImage
    logo = ImageTk.PhotoImage(image_resized)
    bg = ImageTk.PhotoImage(image_bg)

    # Thêm hình ảnh vào dashboard_frame
    # Thêm hình nền trước
    image_label_bg = Label(dashboard_frame, image=bg)
    image_label_bg.place(relwidth=1, relheight=1)  # Đặt hình nền lấp đầy khung

    # Thêm logo lên trên hình nền
    image_label_logo = Label(dashboard_frame, image=logo)
    image_label_logo.pack(padx=5, pady=10)  # Đặt khoảng cách cho hình ảnh

    # Giữ tham chiếu đến photo để tránh garbage collection
    image_label_logo.image = logo  # Lưu giữ tham chiếu đến PhotoImage
    image_label_bg.image = bg  # Lưu giữ tham chiếu đến PhotoImage
    if staff_id == "admin":
        # Create the content frame
        fr_dashboard = dashboard_view.create_frame(frame_root)
        fr_category = category_view.create_frame(frame_root)
        fr_product = product_view.create_frame(frame_root)
        fr_order = order_view.create_frame(frame_root)
        fr_invoice = invoice_view.create_frame(frame_root)
        fr_customer = customer_view.create_frame(frame_root)
        fr_staff = staff_view.create_frame(frame_root)

        # List of frames and buttons
        frames = [fr_dashboard, fr_category, fr_product, fr_order, fr_invoice, fr_customer, fr_staff]
        buttons = []

        # Create buttons for the menu
        btn_dashboard = dashboard_view.create_button_menu(dashboard_frame, fr_dashboard,  buttons, frames)
        btn_category = category_view.create_button_menu(dashboard_frame, fr_category,  buttons, frames)
        btn_product = product_view.create_button_menu(dashboard_frame, fr_product, buttons, frames)
        btn_order = order_view.create_button_menu(dashboard_frame, fr_order, buttons, frames)
        btn_invoice = invoice_view.create_button_menu(dashboard_frame, fr_invoice,  buttons, frames)
        btn_customer = customer_view.create_button_menu(dashboard_frame, fr_customer,  buttons, frames)
        btn_staff = staff_view.create_button_menu(dashboard_frame, fr_staff,  buttons, frames)

        #Set hiển thị mặc định là order
        window.show_frame(fr_order, frames, buttons, btn_order)
    else:
        # Create the content frame
        fr_dashboard = dashboard_view.create_frame(frame_root)
        fr_order = order_view.create_frame(frame_root)
        fr_invoice = invoice_view.create_frame(frame_root)
        fr_customer = customer_view.create_frame(frame_root)

        # List of frames and buttons
        frames = [fr_dashboard,  fr_order, fr_invoice, fr_customer]
        buttons = []

        # Create buttons for the menu
        btn_dashboard = dashboard_view.create_button_menu(dashboard_frame, fr_dashboard, buttons, frames)
        btn_order = order_view.create_button_menu(dashboard_frame, fr_order, buttons, frames)
        btn_invoice = invoice_view.create_button_menu(dashboard_frame, fr_invoice, buttons, frames)
        btn_customer = customer_view.create_button_menu(dashboard_frame, fr_customer,  buttons, frames)

        # Set hiển thị mặc định là order
        window.show_frame(fr_order, frames, buttons, btn_order)