from .person_model import Person

class Staff(Person):
    def __init__(self, full_name, sex, address, phone_number, username, password):
        self.id = id
        Person.__init__(full_name, sex, address, phone_number)
        self.username = username
        self.password = password
