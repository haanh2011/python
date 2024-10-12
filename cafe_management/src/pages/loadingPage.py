# src/pages/loadingPage.py
import sys

from utilities import run_with_custom_path, setTheme
from modules import PageBase
from tkinter import PhotoImage
from customtkinter import *
from themes import *

PAGE_CONFIGS = {
    # 'background': '#fd6a36'
}
PAGE_ATTRIBUTES = {
    'width':530,'height':430
}

setTheme()

root = CTk()
image = PhotoImage(file='src/assets/images/coffeeShop-ico.png')

def handleExit():
    sys.exit(root.destroy())

i = 0

def loadingPageRender ():
    root.overrideredirect(1)
    root.wm_attributes('-topmost', True)

    welcome_label = H3Label(root, text='Welcome to Coffee Manager System')
    welcome_label.place(x=75, y=35)

    bg_label = CTkLabel(root, image=image, fg_color='#fd6a36', text=None)
    bg_label.place(x=170, y=110)

    progress_label = CTkLabel(root, text="Please Wait...")
    progress_label.place(x=195, y=350)
    progress = CTkProgressBar(root, orientation=HORIZONTAL, width=500, mode='determinate')
    progress.place(x=15, y=380)

    exit_btn = PrimaryButton(root, text='X', command=lambda: handleExit(), border_width=0, font=("yu gothic ui", 16, "bold"), width= 50)
    exit_btn.place(x=480, y=0)

    def load():
        global i
        if i <= 10:
            txt = 'Please Wait...  ' + (str(10*i)+'%')
            progress_label.configure(text=txt)
            progress_label.after(500, load) # 500 (ms) = Time to load 10%
            progress.set(0.1*i)
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