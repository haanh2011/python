from src.models.person_model import Person

class Staff(Person):
    def __init__(self, ho_ten, dia_chi, sdt, id_staff, username, password):
        super().__init__(ho_ten, dia_chi, sdt)
        self.id_staff = id_staff
        self.username = username
        self.password = password

    def getinfo(self):
        super().getinfo()
        print("Mã nhân viên: ", self.id_staff)
        print("Username: ", self.username)
        print("Password: ", self.password)
