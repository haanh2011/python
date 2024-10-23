import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
controllers_dir = os.path.join(current_dir, '../controllers')
sys.path.append(controllers_dir)
import window
import staff_controller

display_name = "Staffs"

columns = {
    "widget_type": ["Entry", "Entry", "Entry", "Entry", "Entry", "Entry"],
    "columns_name_display": ["Mã", "Tên", "Username", "Password", "Điện thoại", "Địa chỉ"],
    "columns_name": ["id","name","username","password","phone","address"],
    "data_init": {"id":"","name":"","username":"","password":"","phone":"","address":""},
    "validates": ["string", "string", "string", "password", "string", "string"]
}

def set_data_init():
    print("set data init")
    for i in range(len(columns["columns_name"])):
        print("col", columns["columns_name"][i])


def get_all_data():
    return staff_controller.get_data()


def create_frame(frame_parent):
    rows = get_all_data()
    frame = window.create_frame_actions_treeview(staff_controller, frame_parent, display_name, columns, rows)
    return frame


def create_button_menu(dashboard_frame, frame, buttons, frames):
    btn = window.create_button_menu(dashboard_frame, frame, display_name, buttons, frames)
    return btn