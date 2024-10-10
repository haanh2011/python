from .person_model import Person

class Customer(Person):
    def __init__(self, full_name, sex, address, phone_number, point):
        self.id = id
        Person.__init__(full_name, sex, address, phone_number)
        self.point = point
