import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
connect_dir = os.path.join(current_dir, '../utilities')
sys.path.append(connect_dir)
import connectdb
import matplotlib.pyplot as plt
import seaborn as sns

# Lấy dữ liệu cho biểu đồ
orders_data = connectdb.get_data_from_db_for_chart("SELECT MONTH(order_date) as Month, SUM(total_price) as Sales FROM orders GROUP BY Month")
customers_data =  connectdb.get_data_from_db_for_chart("SELECT MONTH(order_date) as Month, COUNT(DISTINCT customer_id) as New_Customers FROM orders GROUP BY Month")
products_data =  connectdb.get_data_from_db_for_chart("SELECT name, SUM(order_details.quantity) as Quantity_Sold FROM products JOIN order_details ON products.id = order_details.product_name GROUP BY name")
staffs_data =  connectdb.get_data_from_db_for_chart("SELECT staffs.name, COUNT(orders.id) as Orders_Handled FROM staffs JOIN orders ON staffs.id = orders.customer_id GROUP BY staffs.name")

# Tạo figure để chứa 4 biểu đồ
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Biểu đồ 1: Doanh thu theo tháng
sns.barplot(x='Month', y='Sales', data=orders_data, ax=axs[0, 0])
axs[0, 0].set_title('Monthly Sales')
axs[0, 0].set_ylabel('Total Sales')
axs[0, 0].set_xlabel('Month')

# Biểu đồ 2: Khách hàng mới theo tháng
sns.lineplot(x='Month', y='New_Customers', data=customers_data, marker='o', ax=axs[0, 1])
axs[0, 1].set_title('New Customers per Month')
axs[0, 1].set_ylabel('New Customers')
axs[0, 1].set_xlabel('Month')

# Biểu đồ 3: Sản phẩm bán chạy
sns.barplot(x='name', y='Quantity_Sold', data=products_data, ax=axs[1, 0])
axs[1, 0].set_title('Top Selling Products')
axs[1, 0].set_ylabel('Quantity Sold')
axs[1, 0].set_xlabel('Product')

# Biểu đồ 4: Nhân viên xử lý đơn hàng
sns.barplot(x='name', y='Orders_Handled', data=staffs_data, ax=axs[1, 1])
axs[1, 1].set_title('Staff Performance')
axs[1, 1].set_ylabel('Orders Handled')
axs[1, 1].set_xlabel('Staff')

# Hiển thị tất cả biểu đồ
plt.tight_layout()
plt.show()