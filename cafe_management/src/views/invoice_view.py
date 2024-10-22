import os
import sys
import datetime

current_dir = os.path.dirname(os.path.abspath(__file__))
controllers_dir = os.path.join(current_dir, '../controllers')
sys.path.append(controllers_dir)
import window
import invoice_controller

display_name = "Invoices"
columns = {
    "widget_type": ["Entry", "Combobox", "Entry"],
    "columns_name_display": ["Mã", "Mã đơn hàng", "Ngày tạo"],
    "columns_name": ["id", "order_id", "invoice_date"],
    "data_init": {"id": "", "order_id": {}, "invoice_date": datetime.datetime.now()},
    "validates": ["string", "string", "string", "datetime"]
}


def set_data_init():
    print("set data init")


def get_all_data():
    return invoice_controller.get_data()


def create_frame(frame_parent):
    rows = get_all_data()
    set_data_init()
    frame = window.create_frame_actions_treeview(invoice_controller, frame_parent, display_name, columns, rows)
    return frame


def create_button_menu(dashboard_frame, frame, buttons, frames):
    btn = window.create_button_menu(dashboard_frame, frame, display_name, buttons, frames)
    return btn
