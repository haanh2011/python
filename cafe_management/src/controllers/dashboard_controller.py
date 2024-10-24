import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.join(current_dir, '../models')
connect_dir = os.path.join(current_dir, '..')
sys.path.append(models_dir)

sys.path.append(connect_dir)
import connectdb


# Lấy dữ liệu cho biểu đồ

def get_data_monthly_sale():
    # Doanh số hàng tháng
    return connectdb.get_data_from_db_for_chart(
        "SELECT MONTH(order_date) as Month, SUM(total_price) as Sales FROM orders GROUP BY Month")


def get_data_new_customers_per_month():
    # Khách hàng mới mỗi tháng
    return connectdb.get_data_from_db_for_chart(
        "SELECT MONTH(order_date) as Month, COUNT(DISTINCT customer_id) as New_Customers FROM orders GROUP BY Month")


def get_data_top_selling_products():
    # Sản phẩm bán chạy nhất
    return connectdb.get_data_from_db_for_chart(
        "SELECT order_details.product_name as name, SUM(order_details.quantity) as Quantity_Sold FROM products JOIN order_details ON products.name = order_details.product_name GROUP BY name")


def get_data_staff_performance():
    # Hiệu suất của nhân viên
    return connectdb.get_data_from_db_for_chart(
        "SELECT staffs.name, COUNT(orders.id) as Orders_Handled FROM staffs JOIN orders ON staffs.id = orders.staff_id GROUP BY staffs.name")
