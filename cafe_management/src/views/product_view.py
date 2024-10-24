import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
controllers_dir = os.path.join(current_dir, '../controllers')
sys.path.append(controllers_dir)
import window
import product_controller
import category_view

name = "products"
display_name = "Sản Phẩm"
columns = {
    "widget_type": ["Entry", "Combobox", "Entry", "Entry", "Text"],
    "columns_name_display": ["Mã", "Loại sản phẩm", "Tên sản phẩm", "Giá tiền", "Mô tả"],
    "columns_name": ["id", "category_id", "name", "price", "description"],
    "data_init": {"id": "", "category_id": {"value_default": "", "combobox_value": []}, "name": "", "price": 0,
                  "description": ""},
    "validates": ["string", "string", "string", "float", "text"]
}


def set_data_init():
    categories = category_view.get_all_data()
    columns["data_init"]["category_id"]["combobox_values"] = [(f"{item[0]} - {item[1]}") for item in categories]


def get_all_data():
    return product_controller.get_data(name)


def create_frame(frame_parent):
    rows = product_controller.get_data(name)
    set_data_init()
    frame = window.create_frame_actions_treeview(product_controller, frame_parent, name, display_name, columns, rows)
    return frame


def create_button_menu(dashboard_frame, frame, buttons, frames):
    btn = window.create_button_menu(dashboard_frame, frame, display_name, buttons, frames, set_data_init)
    return btn
