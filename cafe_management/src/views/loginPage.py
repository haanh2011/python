# src/pages/loginPage.py
import os

import sqlite3  # Thêm thư viện sqlite3

from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image

from templates import WindowBase
from themes import CusEntry
from utilities import setTheme

setTheme()

PAGE_CONFIGS = {
    'background': '#ffffff'
}
PAGE_ATTRIBUTES = {
    'title': 'Login Page',
    'width': 500,
    'height': 450
}

class LoginPage(WindowBase):
    Username = ''
    Password = ''
    def __init__(self, attributes={}, configs={}):
        self.window = CTk()
        self.window.resizable(False, False)
        super().__init__(self.window, attributes, configs)

        # ====== LOGO ==========
        logoIconPath = os.path.join('src', 'assets', 'images', 'CoffeeShop-brand-logo.png')# Đường dẫn Unix-style (khả dụng cho đa hệ điều hành)
        logoIcon = Image.open(logoIconPath)
        photo = CTkImage(light_image=logoIcon, size=(30, 30))
        logo = CTkLabel(self.window, image=photo, text='')
        logo.place(x=300, y=48)
        # ========================================================================
        # ============================Page Title==================================
        # ========================================================================
        heading = Label(self.window, text="Sign In", font=('',24,'bold'), bg='#ffffff')
        heading.place(x=170, y=40)
        # ========================================================================
        # ============================Username====================================
        # ========================================================================
        username_label = CTkLabel(self.window, text='Username: ')
        username_label.place(x=100, y=130)
        username_entry = CusEntry(self.window, width=290, height=34, textvariable=self.Username, placeholder_text='Tên đăng nhập')
        username_entry.place(x=120, y=160)
        # ========================================================================
        # ============================Password====================================
        # ========================================================================
        password_label = CTkLabel(self.window, text='Password: ')
        password_label.place(x=100, y=220)
        password_entry = CusEntry(self.window, width=290, height=34, show="•", textvariable=self.Password, placeholder_text='Mật khẩu')
        password_entry.place(x=120, y=250)
        # ========================================================================
        # ============================LOGIN BTN====================================
        # ========================================================================
        loginButton = CTkButton(self.window, text='Login', font=("", 12, "bold"),
                            cursor='hand2', command=self.handleLogin, width=290, height=40)
        loginButton.place(x=120, y=370)
    def handleLogin(self):
        # ========================================================================
        # ============================HANDLE WHEN CLICK LOGIN BTN=================
        # ========================================================================
        print('Handle Login')
        # # Admin
        # conn1 = sqlite3.connect("./Database/CoffeeShop.db")
        # cursor1 = conn1.cursor()
        # find_user1 = 'SELECT * FROM Admin_Account WHERE admin_username = ? and admin_password = ?'
        # cursor1.execute(find_user1, (username_entry.get(), password_entry.get()))

        # # Guest
        # conn2 = sqlite3.connect("./Database/CoffeeShop.db")
        # cursor2 = conn2.cursor()
        # find_user2 = 'SELECT * FROM Guest_Account WHERE guest_username = ? and guest_password = ?'
        # cursor2.execute(find_user2, (username_entry.get(), password_entry.get()))

        # # Employee
        # conn3 = sqlite3.connect("./Database/CoffeeShop.db")
        # cursor3 = conn3.cursor()
        # find_user3 = 'SELECT * FROM Employee_Account WHERE employee_username = ? and employee_password = ?'
        # cursor3.execute(find_user3, (username_entry.get(), password_entry.get()))

        # result3 = cursor3.fetchall()
        # result2 = cursor2.fetchall()
        # result1 = cursor1.fetchall()

        # if result2:
        #     messagebox.showinfo("Success", 'Logged in Successfully,\n\nClick "OK" to continue.')
        #     open_guest()
        # elif result1:
        #     messagebox.showinfo("Success", 'Logged in Successfully,\n\nClick "OK" to continue.')
        #     open_admin()
        # elif result3:
        #     messagebox.showinfo("Success", 'Logged in Successfully,\n\nClick "OK" to continue.')
        #     open_employee()
        # else:
        #     messagebox.showerror("Failed", "Wrong Login details, please try again.")

def main():
    # logoIconPath = os.path.join('src', 'assets', 'images', 'CoffeeShop-brand-logo.png')# Đường dẫn Unix-style (khả dụng cho đa hệ điều hành)
    loginPage = LoginPage(attributes=PAGE_ATTRIBUTES, configs=PAGE_CONFIGS)
    loginPage.Render()

if __name__ == "__main__":
    main()