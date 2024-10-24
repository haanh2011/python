import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))
views_dir = os.path.join(current_dir , 'views')
utilities_dir = os.path.join(current_dir, 'utilities')
sys.path.append(views_dir)
sys.path.append(utilities_dir)

from views import login_view
from utilities import connectdb

# Kiểm tra và tạo database
connectdb.check_and_create_database()
connectdb.check_and_create_tables_in_db()
# connectdb.insert_data_ex()
# main_view.combobox_lang()

login_view.create_login_frame()  # Show the login form
