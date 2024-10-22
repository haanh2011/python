class Person:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address
    def getinfo(self):
        print("Họ tên: ", self.name)
        print("Địa chỉ: ", self.address)
        print("SĐT: ", self.phone)
    def __del__(self):
        print('Class Person được hủy')
