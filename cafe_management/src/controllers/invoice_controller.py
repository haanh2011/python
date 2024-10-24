import os
import sys

from src.controllers import order_controller

current_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.join(current_dir, '../models')
connect_dir = os.path.join(current_dir, '..')
sys.path.append(models_dir)
import invoice_model

sys.path.append(connect_dir)
import connectdb


def get_data(name):
    return connectdb.get_data(name)


def insert(name, data):
    item = invoice_model.Invoice(**data)
    order = connectdb.get_data_order_by_id(item.order_id)
    print(order,"order")
    if order:
        item.update_total_amount(order[0][4])
        print(item.total_amount,"item")
        item.update_id(connectdb.generate_id(name))
        return connectdb.insert_data(name, item)


def update(name, data):
    item = invoice_model.Invoice(**data)
    return connectdb.update_data(name, item, item.id)


def delete(name, data_id):
    return connectdb.delete_data(name, data_id)
