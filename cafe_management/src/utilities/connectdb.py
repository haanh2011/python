import mysql.connector
import pandas as pd
import configparser
import bcrypt

HOST = 'localhost'
USER = 'root'
PASSWORD = 'Abc123'
DB_NAME = 'ql_bancaphe'


def connect_mysql():
    # config = configparser.ConfigParser()
    # config.read('./config.ini')
    # print(config)
    # Connect to MySQL server
    # db = mysql.connector.connect(
    #     host = config['Database']['host'],
    #     user = config['Database']['user'],
    #     password = config['Database']['password'],
    #     database = config['Database']['database'],
    # )
    db = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD
    )
    return db


def connect_db():
    # config = configparser.ConfigParser()
    # config.read('config.ini')
    # print(config)
    # Connect to MySQL server
    db = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DB_NAME
    )
    # db = mysql.connector.connect(
    #     host=config['database']['host'],
    #     user=config['database']['user'],
    #     password=config['database']['password'],
    #     database=config['database']['name']
    # )
    return db


def check_and_create_database():
    """Checks if the specified database exists and creates it if not.

    Args:
        database_name (str): The name of the database to check.
    """
    db = connect_mysql()
    # Create a cursor object
    cursor = db.cursor()
    try:
        # Check if the database exists
        cursor.execute(f"SHOW DATABASES LIKE '{DB_NAME}'")
        result = cursor.fetchone()

        if not result:
            # Create the database if it doesn't exist
            cursor.execute(f"CREATE DATABASE {DB_NAME}")
            print(f"Database '{DB_NAME}' created successfully.")
        else:
            print(f"Database '{DB_NAME}' already exists.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        db.close()


def check_and_create_table(table_name, create_table_query):
    """Checks if the specified table exists and creates it if not.

    Args:
        table_name (str): The name of the table to check.
        column_definitions (list): A list of tuples containing column names and their data types.
        foreign_key_constraints (list): A list of tuples containing foreign key constraints.
    """

    # Connect to MySQL server
    db = connect_db()

    # Create a cursor object
    cursor = db.cursor()
    try:

        # Check if the table exists
        cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        result = cursor.fetchone()

        if not result:
            cursor.execute(create_table_query)
            print(f"Table '{table_name}' created successfully.")
        else:
            print(f"Table '{table_name}' already exists.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        db.close()


def check_and_create_tables_in_db():
    check_and_create_table("categories",
                           "CREATE TABLE categories ("
                           + " id CHAR(20) PRIMARY KEY,"
                           + " name VARCHAR(150) NOT NULL,"
                           + " is_delete tinyint(1) NOT NULL DEFAULT '0'"
                           + " );"
                           )
    check_and_create_table("products",
                           "CREATE TABLE products ("
                           + " id CHAR(20) PRIMARY KEY,"
                           + " category_id CHAR(20),"
                           + " name VARCHAR(150) NOT NULL,"
                           + " price DECIMAL(10,2) NOT NULL,"
                           + " description CHAR(250),"
                           + " is_delete tinyint(1) NOT NULL DEFAULT '0',"
                           + " FOREIGN KEY (category_id) REFERENCES categories(id)"
                           + " );"
                           )
    check_and_create_table("customers",
                           "CREATE TABLE customers ("
                           + " id CHAR(20) PRIMARY KEY,"
                           + " name VARCHAR(150) NOT NULL,"
                           + " phone VARCHAR(10),"
                           + " address VARCHAR(255),"
                           + " point int DEFAULT 0,"
                           + " is_delete tinyint(1) NOT NULL DEFAULT '0'"
                           + " );"
                           )
    check_and_create_table("staffs",
                           "CREATE TABLE staffs ("
                           + " id CHAR(20) PRIMARY KEY,"
                           + " name VARCHAR(150) NOT NULL,"
                           + " username VARCHAR(100) NOT NULL,"
                           + " password VARCHAR(255) NOT NULL,"
                           + " phone VARCHAR(10),"
                           + " address VARCHAR(255),"
                           + " is_delete tinyint(1) NOT NULL DEFAULT '0'"
                           + " );"
                           )

    check_and_create_table("orders",
                           "CREATE TABLE orders ("
                           + " id CHAR(20) PRIMARY KEY,"
                           + " customer_id CHAR(20),"
                           + " staff_id CHAR(20),"
                           + " order_date DATETIME DEFAULT CURRENT_TIMESTAMP,"
                           + " total_price DECIMAL(10,2),"
                           + " is_delete tinyint(1) NOT NULL DEFAULT '0',"
                           + " FOREIGN KEY (customer_id) REFERENCES customers(id),"
                           + " FOREIGN KEY (staff_id) REFERENCES staffs(id)"
                           + " );"
                           )
    check_and_create_table("order_details",
                           "CREATE TABLE order_details ("
                           + " id CHAR(20) PRIMARY KEY,"
                           + " order_id CHAR(20),"
                           + " product_name VARCHAR(150),"
                           + " quantity INT,"
                           + " price DECIMAL(10,2),"
                           + " is_delete tinyint(1) NOT NULL DEFAULT '0',"
                           + " FOREIGN KEY (order_id) REFERENCES orders(id)"
                           + " );"
                           )

    check_and_create_table("invoices",
                           "CREATE TABLE invoices ("
                           + " id CHAR(20) PRIMARY KEY,"
                           + " order_id CHAR(20),"
                           + " invoice_date DATETIME DEFAULT CURRENT_TIMESTAMP,"
                           + " total_amount INT,"
                           + " payment_status DECIMAL(10,2),"
                           + " is_delete tinyint(1) NOT NULL DEFAULT '0',"
                           + " FOREIGN KEY (order_id) REFERENCES orders(id)"
                           + " );"
                           )


def get_data_by_value(type_name, col_name, value):
    db = connect_db()
    cursor = db.cursor()
    try:
        cursor.execute(f"SELECT * FROM {DB_NAME}.{type_name} WHERE is_delete = 0 AND {col_name} = '{value}'")
        data = cursor.fetchall()
        return data

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        db.close()


def get_data(type_name):
    db = connect_db()
    cursor = db.cursor()
    try:
        cursor.execute(f"SELECT * FROM `{DB_NAME}`.`{type_name}` WHERE is_delete = 0")
        data = cursor.fetchall()
        return data

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        db.close()


PREFIXES = {
    "categories": "CAT",
    "customers": "CUST",
    "staffs": "STAFF",
    "orders": "ORDER",
    "order_details": "OD",
    "invoices": "INV",
    "products": "PROD"
}


def generate_id(table_name):
    """Hàm tự động sinh mã ID

    Args:
        prefix (str): Tiền tố của mã ID.
        table_name (str): Tên table

    Returns:
        str: Mã ID mới.
    """
    # Kết nối đến cơ sở dữ liệu
    mydb = connect_db()
    mycursor = mydb.cursor()
    try:
        prefix = PREFIXES[table_name]

        # Truy vấn lấy ID lớn nhất có cùng tiền tố
        sql = f"SELECT MAX(id) FROM `{DB_NAME}`.`{table_name}` WHERE id LIKE '{prefix}%'"
        mycursor.execute(sql)

        # Lấy kết quả
        result = mycursor.fetchone()
        last_id = result[0] if result else None

        # Tăng số thứ tự và định dạng lại
        if last_id:
            last_num = int(last_id[len(prefix):])
            new_num = str(last_num + 1).zfill(4)  # Đảm bảo 4 chữ số
        else:
            new_num = "0001"

        new_id = prefix + new_num
        return new_id

    except mysql.connector.Error as error:
        print(f"Error: {error}")
        return None
    finally:
        # Đóng kết nối
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()


def insert_data(table_name, data):
    """Chèn dữ liệu đã cho vào cơ sở dữ liệu MySQL.

    Đối số:
    data (dict): Một từ điển chứa dữ liệu cần chèn.
    """

    # Connect to the MySQL database
    cnx = connect_db()

    # Create a cursor object
    cursor = cnx.cursor()
    print("insert_data")
    try:
        # Lấy tất cả các thuộc tính của đối tượng
        attributes = vars(data)

        # Chuẩn bị câu lệnh SQL
        columns = ', '.join(attributes.keys())
        placeholders = ', '.join(['%s'] * len(attributes))
        sql = f"INSERT INTO `{DB_NAME}`.`{table_name}` ({columns}) VALUES ({placeholders})"

        # Chuẩn bị giá trị cho câu lệnh SQL
        values = tuple(attributes.values())
        print("values", sql % values)
        # Thực hiện câu lệnh INSERT với các giá trị dữ liệu
        cursor.execute(sql, values)

        # Commit thay đổi vào cơ sở dữ liệu
        cnx.commit()

        print("Data inserted successfully!")
        return ""
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return err
    finally:
        # Close the cursor and connection  

        if cursor:
            cursor.close()
        if cnx:
            cnx.close()


def update_data(table_name, data, data_id):
    """Cập nhật dữ liệu trong cơ sở dữ liệu MySQL.

    Đối số:
    table_name (str): Tên bảng.
    data (dict): Một từ điển chứa dữ liệu cần cập nhật.
    where_clause (str): Điều kiện WHERE để xác định hàng cần cập nhật.
    """

    # Connect to the MySQL database
    cnx = connect_db()

    # Create a cursor object
    cursor = cnx.cursor()
    try:
        # Lấy tất cả các thuộc tính của đối tượng

        # Lấy tất cả các thuộc tính của đối tượng, bỏ qua 'id'
        attributes = {k: v for k, v in vars(data).items() if k != 'id'}

        # Chuẩn bị câu lệnh SQL
        set_clause = ', '.join([f"{key} = %s" for key in attributes])
        sql = f"UPDATE `{DB_NAME}`.`{table_name}` SET {set_clause} WHERE id = '{data_id}'"
        # Chuẩn bị giá trị cho câu lệnh SQL
        values = tuple(attributes.values())
        # Thực hiện câu lệnh UPDATE với các giá trị dữ liệu
        cursor.execute(sql, values)

        # Commit thay đổi vào cơ sở dữ liệu
        cnx.commit()

        print("Data updated successfully!")
        return ""

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the cursor and connection

        if cursor:
            cursor.close()
        if cnx:
            cnx.close()


# Delete row Action
def delete_data(table_name, id_data):
    db = connect_db()
    cursor = db.cursor()
    try:
        cursor.execute(f"UPDATE {table_name} SET is_delete = 1 WHERE id='{id_data}'")
        db.commit()
        return ""
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return err
    finally:
        # Close the cursor and connection
        cursor.close()
        db.close()


def get_user(username):
    db = connect_db()
    cursor = db.cursor()
    try:

        # Check if the user exists
        query = f"SELECT id, password FROM {DB_NAME}.staffs WHERE username = '{username}'"
        print("query", query)
        cursor.execute(query)

        # Fetch the result
        result = cursor.fetchone()

        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        db.close()


def insert_user_admin(data):
    db = connect_db()
    cursor = db.cursor()
    try:
        cursor.execute(f"SELECT * FROM {DB_NAME}.staffs WHERE id = 'admin' AND is_delete = 0")
        result = cursor.fetchall()
        if not result or len(result) == 0:
            insert_data("staffs", data)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the cursor and connection
        cursor.close()
        db.close()


def update_point_of_customer(customer_id, point_to_add, is_add = True):
    db = connect_db()
    cursor = db.cursor()
    try:
        if is_add:
            cursor.execute(
                f"UPDATE {DB_NAME}.customers SET point = point + {point_to_add} WHERE id = '{customer_id}'")
        else:
            cursor.execute(
                f"UPDATE {DB_NAME}.customers SET point = point - {point_to_add} WHERE id = '{customer_id}'")

        # Commit thay đổi vào cơ sở dữ liệu
        db.commit()

        print("Data updated successfully!")
        return ""
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return err
    finally:
        # Close the cursor and connection
        cursor.close()
        db.close()

# Lấy dữ liệu từ các bảng
def get_data_from_db_for_chart(query):
    db = connect_db()
    cursor = db.cursor(dictionary=True)  # Sử dụng dictionary=True để lấy kết quả dưới dạng dict
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        return pd.DataFrame(data)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return err
    finally:
        # Close the cursor and connection
        cursor.close()
        db.close()

def get_data_order_by_id(order_id):
    db = connect_db()
    cursor = db.cursor()
    try:
        cursor.execute(f"SELECT * FROM {DB_NAME}.orders WHERE id = '{order_id}'")
        data = cursor.fetchall()

        print("Data updated successfully!")
        return data

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the cursor and connection
        cursor.close()
        db.close()