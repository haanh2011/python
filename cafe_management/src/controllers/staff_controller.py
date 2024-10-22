import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.join(current_dir, '../models')
connect_dir = os.path.join(current_dir, '..')
sys.path.append(models_dir)
import staff_model

sys.path.append(connect_dir)
import connectdb

TYPE_NAME = "staffs"


def get_data():
    return connectdb.get_data(TYPE_NAME)


def insert(data):
    item = staff_model.Staff(**data)
    item.update_id(connectdb.generate_id(TYPE_NAME))
    return connectdb.insert_data(TYPE_NAME, item)


def update(data):
    item = staff_model.Staff(**data)
    return connectdb.update_data(TYPE_NAME, item, item.id)


def delete(data_id):
    return connectdb.delete_data(TYPE_NAME, data_id)
