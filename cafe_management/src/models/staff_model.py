from person_model import Person

class Staff(Person):
    def __init__(self, id,name,username,password,phone,address):
        super().__init__(name, phone, address)
        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.phone = phone
        self.address = address

    def update_id(self, id):
        self.id = id