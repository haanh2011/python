import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
controllers_dir = os.path.join(current_dir, '../controllers')
sys.path.append(controllers_dir)

import category_controller
import window

name = "categories"
display_name = "Loại Sản Phẩm"
columns = {
    "widget_type": ["Entry", "Entry"],
    "columns_name_display": ["Mã loại", "Tên loại sản phẩm"],  # Tên column hiển thị trên grid view
    "columns_name": ["id", "name"],  # sử dụng để thao tác insert, update delete data
    "data_init": {"id": "", "name": ""},  # sử dụng để set data init
    "validates": ["string", "string"],  # sử dụng để check valid data
    "max_values": [20, 150]  # sử dụng để check max length or max value
}


def get_all_data():
    return category_controller.get_data(name)


def create_frame(frame_parent, staff_id):
    rows = get_all_data()
    frame = window.create_frame_actions_treeview(category_controller, frame_parent, name, display_name, columns, rows,
                                                 staff_id)
    return frame


def create_button_menu(dashboard_frame, frame, buttons, frames):
    btn = window.create_button_menu(dashboard_frame, frame, display_name, buttons, frames)
    return btn
