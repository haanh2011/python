import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
controllers_dir = os.path.join(current_dir, '../controllers')
sys.path.append(controllers_dir)
import window
import order_controller, customer_view, product_view

display_name = "Orders"
display_name_detail = "Order Details"

column_orders = {
    "widget_type": ["Entry", "Combobox", "Product_list"],
    "columns_name_display": ["Mã", "Khách hàng", "Ngày tạo"],
    "columns_name": ["id", "customer_id", "products_info"],
    "data_init": {"id": "", "customer_id": {"value_default": "", "combobox_value": []},
                  "products_info": {"value_default": "", "combobox_value": []}},
    "validates": ["string", "string", "list"]
}

column_order_details = {
    "widget_type": ["Entry", "Entry", "Product_list", "Entry", "Entry", "Entry"],
    "columns_name_display": ["Mã", "Mã đơn hàng", "Tên sản phẩm", "Số lượng", "Giá tiền"],
    "columns_name": ["id", "order_id", "product_name", "quality", "price"],
    "data_init": {"id": "", "order_id": "", "product_name": "", "quality": 0, "price": 0},
    "validates": ["string", "string", list, "integer", "decimal"]
}


def get_all_data():
    return order_controller.get_data()


def get_all_data_details():
    return order_controller.get_data_detailsget_data_details()


def set_data_init():
    customers = customer_view.get_all_data()
    column_orders["data_init"]["customer_id"]["combobox_values"] = [(f"{item[0]} - {item[1]}") for item in customers]
    products = product_view.get_all_data()
    column_orders["data_init"]["products_info"]["combobox_values"] = [(f"{item[0]} - {item[2]} - {item[3]}") for item in products]


def create_frame(frame_parent):
    rows = get_all_data()
    set_data_init()
    frame = window.create_frame_actions_treeview(order_controller, frame_parent, display_name, column_orders, rows)
    return frame


def create_frame_details(frame_parent):
    rows = get_all_data_details()
    frame = window.create_frame_actions_treeview(order_controller, frame_parent, display_name, column_order_details,
                                                 rows)
    return frame


def create_button_menu(dashboard_frame, frame, buttons, frames):
    btn = window.create_button_menu(dashboard_frame, frame, display_name, buttons, frames)
    return btn
