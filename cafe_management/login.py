import pandas as pd
from main import MainApplication
import customtkinter

# Khởi tạo CustomTkinter
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

# Đọc dữ liệu từ tệp Excel
excel_file = 'src/data/dataTemplate.xlsx'
# Đọc tất cả các sheet trong tệp Excel vào một dictionary
sheets_dict = pd.read_excel(excel_file, sheet_name=None)
# Truy cập từng sheet bằng tên của nó
users_df = sheets_dict['Users']  # Bảng Users
# Kiểm tra nội dung
print(users_df.head())
class LoginApplication(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("400x300")

        # Nhãn tiêu đề
        self.label_title = customtkinter.CTkLabel(master=self, text="Login", font=("yu gothic ui", 24, "bold"))
        self.label_title.pack(pady=20) #pack: phương thức dùng để thêm đối tượng vào trong cửa sổ (hoặc khung) của ứng dụng, pady=20: padding trên dưới

        # Nhãn và ô nhập tên người dùng
        self.label_username = customtkinter.CTkLabel(master=self, text="Username")
        self.label_username.pack(pady=(10, 0))
        self.entry_username = customtkinter.CTkEntry(master=self, placeholder_text="Enter your username")
        self.entry_username.pack(pady=(0, 10))

        # Nhãn và ô nhập mật khẩu
        self.label_password = customtkinter.CTkLabel(master=self, text="Password")
        self.label_password.pack(pady=(10, 0))
        self.entry_password = customtkinter.CTkEntry(master=self, placeholder_text="Enter your password", show='*')
        self.entry_password.pack(pady=(0, 20))

        # Nút đăng nhập
        self.button_login = customtkinter.CTkButton(master=self, text="Login", command=self.login)
        self.button_login.pack(pady=10)

    # Hàm xử lý khi nhấn nút đăng nhập
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        print(f"Username: {username}, Password: {password}")
        if any((users_df['Username'] == username) & (users_df['Password'] == password)):
            print("Đăng nhập thành công!")
            self.destroy() # Đóng cửa sổ login
            app = MainApplication() # Khởi động ứng dụng chính
            app.mainloop()
        else:
            print("Sai tên đăng nhập hoặc mật khẩu.")

if __name__ == "__main__":
    app = LoginApplication()
    app.mainloop()
