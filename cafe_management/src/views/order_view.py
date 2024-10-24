import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
controllers_dir = os.path.join(current_dir, '../controllers')
sys.path.append(controllers_dir)
import window
import order_controller, customer_view, product_view

name = "orders"
name_details = "order_details"
display_name = "Đơn Hàng"
display_name_detail = "Chi Tiết Đơn Hàng"
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
    "validates": ["string", "string", "list", "int", "float"],
    "maxvalues": ["string", "string", "list", "int", "float"]
}


def get_all_data():
    return order_controller.get_data(name)


def get_all_data_details(order_id):
    return order_controller.get_data_details(name_details, order_id)


def set_data_init():
    customers = customer_view.get_all_data()
    column_orders["data_init"]["customer_id"]["combobox_values"] = [(f"{item[0]} - {item[1]}") for item in customers]
    products = product_view.get_all_data()
    column_orders["data_init"]["products_info"]["combobox_values"] = [(f"{item[0]} - {item[2]} - {item[3]}") for item in
                                                                      products]
    print("customers", customers)
    print("products", products)


def create_frame(frame_parent):
    data = get_all_data()
    set_data_init()
    frame = window.create_frame_actions_treeview(order_controller, frame_parent, name, display_name, column_orders,
                                                 data)
    return frame


def create_frame_details(frame_parent, order_id):
    rows = get_all_data_details(order_id)
    frame = window.create_frame_treeview_details(order_controller, frame_parent, name_details, display_name,
                                                 column_order_details, rows)
    return frame


def create_button_menu(dashboard_frame, frame, buttons, frames):
    btn = window.create_button_menu(dashboard_frame, frame, display_name, buttons, frames, set_data_init)
    return btn
