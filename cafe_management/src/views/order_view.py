import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
controllers_dir = os.path.join(current_dir, '../controllers')
sys.path.append(controllers_dir)
import window
import src.controllers.order_controller as order_controller

display_name = "Orders"
display_name_detail = "Order Details"

column_orders = {
    "widget_type": ["Entry", "Combobox", "Entry", "Combobox"],
    "columns_name_display": ["Mã", "Khách hàng", "Ngày tạo"],
    "columns_name": ["id", "order_id", "invoice_date"],
    "data_init": {"id": "", "order_id": "", "invoice_date": ""},
    "validates": ["", "", "datetime"]
}

column_order_details = {
    "widget_type": ["Entry", "Combobox", "Combobox", "Entry", "Entry"],
    "columns_name_display": ["Mã", "Mã đơn hàng", "Tên sản phẩm", "Số lượng", "Giá tiền"],
    "columns_name": ["id", "order_id", "product_id", "quality", "price"],
    "data_init": {"id": {}, "order_id": {}, "product_id": {}, "quality": {}, "price": {}},
    "validates": ["string", "string", "string", "integer", "decimal"]
}


def get_all_data():
    return order_controller.get_data()


def get_all_data_details():
    return order_controller.get_data_detailsget_data_details()


def set_data_init():
    data_orders = get_all_data()
    column_orders["data_init"]["id"] = ""
    column_orders["data_init"]["name"] = ""
    column_orders["data_init"]["name"] = ""
    column_orders["data_init"]["name"] = ""


def create_frame(frame_parent):
    order_rows = get_all_data()
    set_data_init()

    # Merge the data into a list of tuples
    rows = []
    for order in order_rows:
        order_details = [detail for detail in order_rows if detail[1] == order[0]]

        # Tạo hàng con cho mỗi chi tiết
        for detail in order_details:
            child_row = order + detail  # Assuming columns 2-5 are detail data
            rows.append(detail)
    print(rows)

    frame = window.create_frame_actions_treeview(order_controller, frame_parent, display_name, column_order_details,
                                                 rows)
    return frame


def create_button_menu(dashboard_frame, frame, buttons, frames):
    btn = window.create_button_menu(dashboard_frame, frame, display_name, buttons, frames)
    return btn
