# src/pages/loadingPage.py
import sys

from utilities import run_with_custom_path
from modules import PageBase
from tkinter import *
from tkinter.ttk import Progressbar

PAGE_CONFIGS = {
    'background': '#fd6a36'
}
PAGE_ATTRIBUTES = {
    'width':530,'height':430
}

root = Tk()
image = PhotoImage(file='src/assets/images/coffeeShop-ico.png')

def handleExit():
    sys.exit(root.destroy())

i = 0

def loadingPageRender ():
    root.overrideredirect(1)
    root.wm_attributes('-topmost', True)

    welcome_label = Label(text='Welcome to Coffee Manager System', bg='#fd6a36', font=("yu gothic ui", 15, "bold"), fg='black')
    welcome_label.place(x=85, y=25)

    bg_label = Label(root, image=image, bg='#fd6a36')
    bg_label.place(x=130, y=65)

    progress_label = Label(root, text="Please Wait...", font=('yu gothic ui', 13, 'bold'), fg='black', bg='#fd6a36')
    progress_label.place(x=190, y=350)
    progress = Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')
    progress.place(x=15, y=390)

    exit_btn = Button(text='x', bg='#fd6a36', command=lambda: handleExit(), bd=0, font=("yu gothic ui", 16, "bold"),
                    activebackground='#fd6a36', fg='white')
    exit_btn.place(x=490, y=0)

    def load():
        global i
        if i <= 10:
            txt = 'Please Wait...  ' + (str(10*i)+'%')
            progress_label.config(text=txt)
            progress_label.after(500, load) # 500 (ms) = Time to load 10%
            progress['value'] = 10*i
            i += 1
        else:
            root.withdraw()
            # Chạy loadingPage.py với PYTHONPATH chỉ định cho Windows
            run_with_custom_path("src/pages/loginPage.py")
            root.destroy()
            # print('Load Completed!!!')
    
    load()
    load()

loadingPage = PageBase(root, loadingPageRender,PAGE_ATTRIBUTES, PAGE_CONFIGS)


def main():
    loadingPage.render();

if __name__ == "__main__":
    main()