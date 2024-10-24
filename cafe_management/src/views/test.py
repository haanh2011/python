import mysql.connector
from datetime import datetime, timedelta
import random

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abc123",
    database="ql_bancaphe"
)
cursor = connection.cursor()

# Function to insert data
def insert_data(query, values):
    cursor.execute(query, values)
    connection.commit()

# Insert sample data for multiple months and larger volume
def insert_large_sample_data():
    current_date = datetime.now()

    # Categories
    categories = [
        ("C001", "Coffee"),
        ("C002", "Tea"),
        ("C003", "Pastries"),
        ("C004", "Juices"),
        ("C005", "Smoothies")
    ]
    for category in categories:
        insert_data("INSERT INTO categories (id, name) VALUES (%s, %s)", category)

    # Products
    products = [
        ("P001", "C001", "Espresso", 2.50, "Strong coffee shot"),
        ("P002", "C001", "Americano", 3.00, "Diluted espresso"),
        ("P003", "C002", "Green Tea", 2.00, "Refreshing green tea"),
        ("P004", "C003", "Croissant", 1.50, "Buttery pastry"),
        ("P005", "C004", "Orange Juice", 3.00, "Freshly squeezed orange juice"),
        ("P006", "C005", "Berry Smoothie", 4.50, "Mixed berry smoothie")
    ]
    for product in products:
        insert_data("INSERT INTO products (id, category_id, name, price, description) VALUES (%s, %s, %s, %s, %s)", product)

    # Customers
    customers = [
        ("CU001", "John Doe", "0987654321", "123 Main St", 10),
        ("CU002", "Jane Smith", "0981234567", "456 Oak St", 20),
        ("CU003", "Jim Beam", "0976543210", "789 Maple St", 15),
        ("CU004", "Lisa Ray", "0965432109", "123 Pine St", 25),
        ("CU005", "Emily Stone", "0954321098", "987 Cedar St", 30)
    ]
    for customer in customers:
        insert_data("INSERT INTO customers (id, name, phone, address, point) VALUES (%s, %s, %s, %s, %s)", customer)

    # Staff
    staff = [
        ("S001", "Alice Brown", "alice_b", "encrypted_password1", "0987654321", "789 Maple St"),
        ("S002", "Bob White", "bob_w", "encrypted_password2", "0976543210", "456 Pine St")
    ]
    for s in staff:
        insert_data("INSERT INTO staffs (id, name, username, password, phone, address) VALUES (%s, %s, %s, %s, %s, %s)", s)

    # Insert orders and order details for each day in the last 6 months
    for i in range(180):  # 180 days (~6 months)
        order_date = current_date - timedelta(days=i)  # Create orders daily
        order_id = f"O{i+1000}"
        customer_id = random.choice(["CU001", "CU002", "CU003", "CU004", "CU005"])
        staff_id = random.choice(["S001", "S002"])
        total_price = random.uniform(10.00, 100.00)  # Random total price between 10 and 100

        # Insert order
        insert_data("INSERT INTO orders (id, customer_id, staff_id, order_date, total_price) VALUES (%s, %s, %s, %s, %s)",
                    (order_id, customer_id, staff_id, order_date, total_price))

        # Insert multiple order details for each order
        num_items = random.randint(1, 5)  # 1 to 5 items per order
        for j in range(num_items):
            product = random.choice(products)
            quantity = random.randint(1, 3)
            price = product[3]
            order_detail_id = f"OD{i+1000}{j}"
            insert_data("INSERT INTO order_details (id, order_id, product_name, quantity, price) VALUES (%s, %s, %s, %s, %s)",
                        (order_detail_id, order_id, product[2], quantity, price * quantity))

    # Insert invoices linked to orders
    for i in range(180):
        order_id = f"O{i+1000}"
        invoice_id = f"IN{i+1000}"
        invoice_date = current_date - timedelta(days=i)
        total_amount = random.uniform(50.00, 200.00)
        payment_status = random.choice([0, 1])  # 0 for unpaid, 1 for paid
        insert_data("INSERT INTO invoices (id, order_id, invoice_date, total_amount, payment_status) VALUES (%s, %s, %s, %s, %s)",
                    (invoice_id, order_id, invoice_date, total_amount, payment_status))

# Run the data insertion function
insert_large_sample_data()

# Close the database connection
cursor.close()
connection.close()
