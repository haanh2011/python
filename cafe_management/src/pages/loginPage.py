# src/pages/loginPage.py
import os

import sqlite3  # Thêm thư viện sqlite3

from tkinter import *
from tkinter import messagebox
from customtkinter import *
from PIL import ImageTk, Image
from modules import PageBase
from themes import *

PAGE_CONFIGS = {
    'background': '#ffffff'
}
PAGE_ATTRIBUTES = {
    'title': 'Login Page',
    'width': 700,
    'height': 650
}

root = CTk()

def renderLoginPage():
    # ====== LOGO ==========
    logoIcon = Image.open(os.path.join('src', 'assets', 'images', 'CoffeeShop-brand-logo.png'))  # Đường dẫn Unix-style (khả dụng cho đa hệ điều hành)
    photo = ImageTk.PhotoImage(logoIcon)
    logo = Label(root, image=photo, bg='#ffffff')
    logo.image = photo
    logo.place(x=20, y=45)

    brand_name = Label(root, text='GIDEONS COFFEE SHOP', bg='#ffffff', fg='#ff6c38', font=("", 15, "bold"))
    brand_name.place(x=90, y=60)

    text = Label(root, text="FDA APPROVED", bg='#ffffff', font=("", 12, "bold"))
    text.place(x=20, y=140)

    txt2 = "• We produce hygienic and healthy coffee \nby all standards\t\t\t \n\n• Very Affordable and best Coffee in " \
           "town \nfor the past two and half years\t"
    text2 = Label(root, text=txt2, fg="#6b6a69", bg='#ffffff', font=("", 11, "bold"))
    text2.place(x=20, y=180)

    # ====== COFFEE IMAGE ==========
    coffeeImage = Image.open('src/assets/images/coffee3.gif')  # Sửa đường dẫn
    photo = ImageTk.PhotoImage(coffeeImage)
    coffee_image = Label(root, image=photo, bg='#ffffff')
    coffee_image.image = photo
    coffee_image.place(x=30, y=370)

    # Page Divider Line
    pageDivide_line = Canvas(root, width=1.5, height=900, bg="#e6e6e6", highlightthickness=0)
    pageDivide_line.place(x=350, y=0)

    heading = Label(root, text="Sign In", font=("", 13, "bold"), bg='#ffffff')
    heading.place(x=490, y=50)

    Username = StringVar()
    Password = StringVar()

    def login_all():
        # Admin
        conn1 = sqlite3.connect("./Database/CoffeeShop.db")
        cursor1 = conn1.cursor()
        find_user1 = 'SELECT * FROM Admin_Account WHERE admin_username = ? and admin_password = ?'
        cursor1.execute(find_user1, (username_entry.get(), password_entry.get()))

        # Guest
        conn2 = sqlite3.connect("./Database/CoffeeShop.db")
        cursor2 = conn2.cursor()
        find_user2 = 'SELECT * FROM Guest_Account WHERE guest_username = ? and guest_password = ?'
        cursor2.execute(find_user2, (username_entry.get(), password_entry.get()))

        # Employee
        conn3 = sqlite3.connect("./Database/CoffeeShop.db")
        cursor3 = conn3.cursor()
        find_user3 = 'SELECT * FROM Employee_Account WHERE employee_username = ? and employee_password = ?'
        cursor3.execute(find_user3, (username_entry.get(), password_entry.get()))

        result3 = cursor3.fetchall()
        result2 = cursor2.fetchall()
        result1 = cursor1.fetchall()

        if result2:
            messagebox.showinfo("Success", 'Logged in Successfully,\n\nClick "OK" to continue.')
            open_guest()
        elif result1:
            messagebox.showinfo("Success", 'Logged in Successfully,\n\nClick "OK" to continue.')
            open_admin()
        elif result3:
            messagebox.showinfo("Success", 'Logged in Successfully,\n\nClick "OK" to continue.')
            open_employee()
        else:
            messagebox.showerror("Failed", "Wrong Login details, please try again.")

    # ========================================================================
    # ============================Username====================================
    # ========================================================================
    username_label = Label(root, text='Username', fg="#27221c", bg='#ffffff', font=("", 12, "bold"))
    username_label.place(x=380, y=150)
    username_entry = Entry(root, highlightthickness=2, relief=FLAT, bg="#fafafa", fg="#6b6a69",
                           font=("", 12, 'bold'), textvariable=Username)
    username_entry.place(x=380, y=182, width=290, height=34)
    username_entry.config(highlightbackground="#6b6a69", highlightcolor="black")

    # ========================================================================
    # ============================Password====================================
    # ========================================================================
    password_label = Label(root, text='Password', fg="#27221c", bg='#ffffff', font=("", 12, "bold"))
    password_label.place(x=380, y=250)
    password_entry = Entry(root, highlightthickness=2, relief=FLAT, bg="#fafafa", fg="#6b6a69", font=("", 12), show="•",
                           textvariable=Password)
    password_entry.place(x=380, y=282, width=290, height=34)
    password_entry.config(highlightbackground="#6b6a69", highlightcolor="black")

    loginButton = Button(root, fg='#f8f8f8', text='Login', bg='#ff6c38', font=("", 12, "bold"),
                         cursor='hand2', activebackground='#ff6c38', command=login_all)
    loginButton.place(x=380, y=370, width=290, height=40)

    line = Canvas(root, width=286, height=1.5, bg="#e6e6e6", highlightthickness=0)
    line.place(x=380, y=440)
    # label = Label(root, text='No Account Yet', bg='#ffffff')
    # label.place(x=480, y=430)

    # createButton = Button(root, fg='#f8f8f8', text='Create New Account', bg='#4286f5', font=("", 12, "bold"),
    #                       cursor='hand2', activebackground='#4286f5', command=lambda: show_frame(sign_up))
    # createButton.place(x=380, y=470, width=290, height=40)

loginPage = PageBase(root, renderLoginPage, PAGE_ATTRIBUTES, PAGE_CONFIGS)
loginPage.render()
