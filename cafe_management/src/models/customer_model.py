import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
utilities_dir = os.path.join(current_dir, '../utilities')
sys.path.append(utilities_dir)

import converter

from person_model import Person

class Customer(Person):
    def __init__(self, id, name, phone, address, point = 0):
        super().__init__(name, phone, address)
        self.id = id
        self.point = converter.convert_to_int(point)

    def update_id(self, id):
        self.id = id
    def update_point(self, point):
        self.point = point
    def getinfo(self):
        super().getinfo()
        print("Mã khách hàng: ", self.id)
        print("Điểm: ", self.point)
