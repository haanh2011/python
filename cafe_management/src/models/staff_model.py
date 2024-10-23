from person_model import Person
import bcrypt


class Staff(Person):

    def __init__(self, id, name, username, password, phone, address):
        super().__init__(name, phone, address)
        salt = bcrypt.gensalt()
        self.id = id
        self.name = name
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'), salt)  # Hàm mã hóa mật khẩu
        self.phone = phone
        self.address = address

    def update_id(self, id):
        self.id = id
