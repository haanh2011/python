import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.join(current_dir, '../models')
connect_dir = os.path.join(current_dir, '..')
sys.path.append(models_dir)
import staff_model

sys.path.append(connect_dir)
import connectdb


def get_data(name):
    return connectdb.get_data(name)


def insert(name, data):
    item = staff_model.Staff(**data)
    item.update_id(connectdb.generate_id(name))
    return connectdb.insert_data(name, item)


def update(name, data):
    item = staff_model.Staff(**data)
    return connectdb.update_data(name, item, item.id)


def delete(name, data_id):
    return connectdb.delete_data(name, data_id)

def get_user(username, password):
    return connectdb.get_user(username, password)