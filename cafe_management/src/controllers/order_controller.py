import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.join(current_dir, '../models')
connect_dir = os.path.join(current_dir, '..')

sys.path.append(models_dir)
import order_model

sys.path.append(connect_dir)
import connectdb


def generate_id(name):
    new_id = connectdb.generate_id(name)
    return new_id


def get_data(name):
    return connectdb.get_data(name)


def get_data_details(name, order_id):
    return connectdb.get_data_by_value(name, "order_id", order_id)


def insert(name,data):
    products_info = data.pop("products_info")

    item = order_model.Order(**data)
    item.update_id(connectdb.generate_id(name))
    connectdb.insert_data(name, item)
    for product in products_info:
        product["id"] = connectdb.generate_id("order_details")
        product["order_id"] = item.id
        insert_details("order_details",product)


def insert_details(name, data):
    print("data", data)
    item = order_model.OrderDetail(**data)
    return connectdb.insert_data(name, item)


def update(name, data):
    products_info = data.pop("products_info")

    item = order_model.Order(**data)
    connectdb.update_data(name, item, item.id)
    for product in products_info:
        product["id"] = connectdb.generate_id("order_details")
        product["order_id"] = item.id
        update_details("order_details",product)


def update_details(name, data):
    item = order_model.OrderDetail(**data)
    return connectdb.update_data(f"{name}_details", item, item.id)


def delete(name, data_id):
    return connectdb.delete_data(name, data_id)


def delete_details(name, data_id):
    return connectdb.delete_data(f"{name}_details", data_id)
