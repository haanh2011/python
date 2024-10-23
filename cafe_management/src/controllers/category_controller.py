import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.join(current_dir, '../models')
connect_dir = os.path.join(current_dir, '../utilities')
sys.path.append(models_dir)
import category_model

sys.path.append(connect_dir)
import connectdb

TYPE_NAME = "categories"

def get_data():
    return connectdb.get_data(TYPE_NAME)


def insert(data):
    item = category_model.Category(**data)
    item.update_id(connectdb.generate_id(TYPE_NAME))
    # return item.insert()
    return connectdb.insert_data(TYPE_NAME, item)


def update(data):
    item = category_model.Category(**data)
    # return item.update()
    return connectdb.update_data(TYPE_NAME, item, item.id)


def delete(data_id):
    # return item.update()
    return connectdb.delete_data(TYPE_NAME, data_id)
