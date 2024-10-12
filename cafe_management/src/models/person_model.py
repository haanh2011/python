class Person:
    def __init__(self, ho_ten, dia_chi, sdt):
        self.ho_ten = ho_ten
        self.dia_chi = dia_chi
        self.sdt = sdt
    def getinfo(self):
        print("Họ tên: ", self.ho_ten)
        print("Địa chỉ: ", self.dia_chi)
        print("SĐT: ", self.sdt)
    def __del__(self):
        print('Class Person được hủy')
