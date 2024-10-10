import customtkinter

# Khởi tạo CustomTkinter
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

class MainApplication(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Main Application")
        self.geometry("600x400")

        # Nhãn tiêu đề
        self.label_main = customtkinter.CTkLabel(master=self, text="Welcome to the Main Application", font=("yu gothic ui", 24, "bold"))
        self.label_main.pack(pady=20)

        # Nút đăng xuất
        self.button_logout = customtkinter.CTkButton(master=self, text="Logout", command=self.logout)
        self.button_logout.pack(pady=10)

    def logout(self):
        self.destroy()  # Đóng cửa sổ chính
        print("Đã đăng xuất!")
