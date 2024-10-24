import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
controllers_dir = os.path.join(current_dir, '../controllers')
sys.path.append(controllers_dir)

import dashboard_controller
import window

display_name = "Thống Kê"


def create_frame(frame_parent):
    orders_data = dashboard_controller.get_data_monthly_sale()
    customers_data = dashboard_controller.get_data_new_customers_per_month()
    products_data = dashboard_controller.get_data_top_selling_products()
    staffs_data = dashboard_controller.get_data_staff_performance()

    frame = window.create_frame_dashboard(frame_parent, orders_data, customers_data, products_data, staffs_data)
    return frame


def create_button_menu(dashboard_frame, frame, buttons, frames):
    btn = window.create_button_menu(dashboard_frame, frame, display_name, buttons, frames)
    return btn
