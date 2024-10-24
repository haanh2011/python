import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.join(current_dir, '../models')
connect_dir = os.path.join(current_dir, '..')
sys.path.append(models_dir)
import staff_model
sys.path.append(connect_dir)
import connectdb

def get_user(username):
    return connectdb.get_user(username)
def add_user_admin():
    data = {
                "id": "admin",
                "name": "admin",
                "username": "admin",
                "password": "admin",
                "phone": "",
                "address": ""}
    item = staff_model.Staff(**data)

    return connectdb.insert_user_admin(item)