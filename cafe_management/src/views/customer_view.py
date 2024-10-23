import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
controllers_dir = os.path.join(current_dir, '../controllers')
sys.path.append(controllers_dir)
import window
import customer_controller

name = "customers"
display_name = "Khách Hàng"
columns = {
    "widget_type": ["Entry", "Entry", "Entry", "Entry", "Entry"],
    "columns_name_display": ["Mã", "Tên", "Điện thoại", "Địa chỉ", "Điểm"],
    "columns_name": ["id", "name", "phone", "address", "point"],
    "data_init": {"id": "", "name": "", "phone": "", "address": "", "point": 0},
    "validates": ["string", "string", "string", "string", "int"]
}


def get_all_data():
    return customer_controller.get_data(name)


def create_frame(frame_parent):
    rows = get_all_data()
    frame = window.create_frame_actions_treeview(customer_controller, frame_parent, name, display_name, columns, rows)
    return frame


def create_button_menu(dashboard_frame, frame, buttons, frames):
    btn = window.create_button_menu(dashboard_frame, frame, display_name, buttons, frames)
    return btn
