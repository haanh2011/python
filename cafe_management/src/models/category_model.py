class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def update_id(self, id):
        self.id = id
    def getinfo(self):
        print("Mã loại: ", self.id)
        print("Tên loại: ", self.name)

# import os
# import sys
#
# current_dir = os.path.dirname(os.path.abspath(__file__))
# connect_dir = os.path.join(current_dir, '..')
# sys.path.append(connect_dir)
# import connectdb
#
# TYPE_NAME = "cagteories"
#
#
# class Category:
#     def __init__(self, cate_id, name):
#         self.cate_id = cate_id
#         self.name = name
#
#     @property
#     def id(self):
#         return self.__cate_id
#
#     @id.setter
#     def name(self, value):
#         self.__cate_id = value
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     def get_data(self):
#         return connectdb.get_data(TYPE_NAME)
#
#     def insert(self):
#         self.id(connectdb.generate_id(TYPE_NAME))
#         return connectdb.insert_data(TYPE_NAME, self)
#
#     def update(self):
#         return connectdb.update_data(TYPE_NAME, self)
#
#     def delete(self):
#         return connectdb.delete_data(TYPE_NAME, self.cate_id)
