class Category:
    def __init__(self, id_cate, name):
        self.id_cate = id_cate
        self.name = name
    def getinfo(self):
        print("Mã loại: ", self.id_cate)
        print("Tên loại: ", self.name)
