from src.models.person_model import Person

class Customer(Person):
    def __init__(self, ho_ten, dia_chi, sdt, id_cus, diem):
        super().__init__(ho_ten, dia_chi, sdt)
        self.id_cus = id_cus
        self.diem = diem

    def getinfo(self):
        super().getinfo()
        print("Mã khách hàng: ", self.id_cus)
        print("Điểm: ", self.diem)
