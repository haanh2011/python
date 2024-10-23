import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.join(current_dir, '../models')
connect_dir = os.path.join(current_dir, '..')

sys.path.append(models_dir)
import order_model

sys.path.append(connect_dir)
import connectdb

TYPE_NAME = "orders"
TYPE_NAME_DETAIL = "order_details"


def generate_id():
    new_id = connectdb.generate_id(TYPE_NAME)
    return new_id


def get_data():
    return connectdb.get_data(TYPE_NAME)

def get_data_detail(order_id):
    return connectdb.get_data_by_value(TYPE_NAME_DETAIL, "order_id", order_id)

def insert(data):
    print("data order", data)
    # item = order_model.Order(**data)
    # item.update_id(connectdb.generate_id(TYPE_NAME))
    # return connectdb.insert_data(TYPE_NAME, item)


def insert_details(data):
    item = order_model.OrderDetail(**data)
    item.update_id(connectdb.generate_id(TYPE_NAME_DETAIL))
    return connectdb.insert_data(TYPE_NAME_DETAIL, item)


def update(data):
    item = order_model.Order(**data)
    return connectdb.update_data(TYPE_NAME, item, item.id)


def update_details(data):
    item = order_model.OrderDetail(**data)
    return connectdb.update_data(TYPE_NAME_DETAIL, item, item.id)


def delete(data_id):
    return connectdb.delete_data(TYPE_NAME, data_id)

def delete_details(data_id):
    return connectdb.delete_data(TYPE_NAME_DETAIL, data_id)
