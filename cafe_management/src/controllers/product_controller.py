import os
import sys

from unicodedata import category

current_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.join(current_dir, '../models')
connect_dir = os.path.join(current_dir, '..')
sys.path.append(models_dir)
import product_model, category_model

sys.path.append(connect_dir)
import connectdb

TYPE_NAME = "products"


def get_data():
    return connectdb.get_data(TYPE_NAME)


def insert(data):
    item = product_model.Product(**data)
    print(item, "item")
    item.update_id(connectdb.generate_id(TYPE_NAME))
    return connectdb.insert_data(TYPE_NAME, item)


def update(data):
    item = product_model.Product(**data)
    return connectdb.update_data(TYPE_NAME, item, item.id)


def delete(data_id):
    return connectdb.delete_data(TYPE_NAME, data_id)
