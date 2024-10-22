import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
utilities_dir = os.path.join(current_dir, '../utilities')
sys.path.append(utilities_dir)

views_dir = os.path.join(current_dir, '../views')
sys.path.append(views_dir)

import window
import category_view
import customer_view
import invoice_view
import order_view
import product_view
import staff_view

# utilities_dir = os.path.join(current_dir, '../utilities')
# sys.path.append(utilities_dir)
#
# import languages
#
#
# def combobox_lang():
#     # Duyệt qua các biến trong module 'languages' và lọc ra các từ điển ngôn ngữ, bỏ qua __builtins__
#     language_dictionaries = {name: value for name, value in vars(languages).items() if
#                              isinstance(value, dict) and name != "__builtins__"}
#
#     # In ra số lượng và tên các ngôn ngữ
#     print(f"Found {len(language_dictionaries)} languages: {list(language_dictionaries.keys())}")
#

def create_root_window(width, height):
    return window.create_root_window(width, height)

def frame_main(frame_root):
    window.create_header(frame_root)

    # Create frame for the left menu
    dashboard_frame = window.create_frame(frame_root, "dashboard_frame")
    dashboard_frame.pack(side="left", fill="y", padx=(10, 10))

    # Create the content frame
    fr_category = category_view.create_frame(frame_root)
    fr_product = product_view.create_frame(frame_root)
    fr_order = order_view.create_frame(frame_root)
    fr_invoice = invoice_view.create_frame(frame_root)
    fr_customer = customer_view.create_frame(frame_root)
    fr_staff = staff_view.create_frame(frame_root)

    # List of frames and buttons
    frames = [fr_category, fr_product, fr_order, fr_invoice, fr_customer, fr_staff]
    buttons = []

    # Create buttons for the menu
    btn_category = category_view.create_button_menu(dashboard_frame, fr_category,  buttons, frames)
    btn_product = product_view.create_button_menu(dashboard_frame, fr_product, buttons, frames)
    btn_order = order_view.create_button_menu(dashboard_frame, fr_order, buttons, frames)
    btn_invoice = invoice_view.create_button_menu(dashboard_frame, fr_invoice,  buttons, frames)
    btn_customer = customer_view.create_button_menu(dashboard_frame, fr_customer,  buttons, frames)
    btn_staff = staff_view.create_button_menu(dashboard_frame, fr_staff,  buttons, frames)

    #Set hiển thị mặc định là order
    window.show_frame(fr_order, frames, buttons, btn_order)