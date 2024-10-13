# src/pages/loadingPage.py

from utilities import run_with_custom_path,setTheme
from templates import WindowBase
from themes import H3Label

from tkinter import PhotoImage
from PIL import Image
from customtkinter import *

setTheme()

PAGE_ATTRIBUTES = {
    'width':530,'height':430
}

class LoadingPage(WindowBase):
    def __init__(self, attributes={}, configs={}):
        self.window = CTk()
        super().__init__(self.window, attributes, configs)

        logo_path = 'src/assets/images/coffeeShop-ico.png'
        image_open = Image.open(logo_path)
        image = CTkImage(light_image=image_open,dark_image=image_open, size=(225,225))

        self.window.overrideredirect(1)
        self.window.wm_attributes('-topmost', True)

        welcome_label = H3Label(self.window, text='Welcome to Coffee Manager System')
        welcome_label.place(x=75, y=35)

        bg_label = CTkLabel(self.window, image=image, text=None)
        bg_label.place(x=150, y=100)

        self.progress_label = CTkLabel(self.window, text="Please Wait...")
        self.progress_label.place(x=195, y=350)
        self.progress = CTkProgressBar(self.window, orientation=HORIZONTAL, width=500, mode='determinate')
        self.progress.place(x=15, y=380)

        exit_btn = CTkButton(self.window, text='X', command=lambda: self.Exit(), border_width=0, font=("yu gothic ui", 16, "bold"), width= 50)
        exit_btn.place(x=480, y=0)

        self.load()
        self.load()

    def load(self):
        global i
        if i <= 10:
            txt = 'Please Wait...  ' + (str(10*i)+'%')
            self.progress_label.configure(text=txt)
            self.progress_label.after(500, self.load) # 500 (ms) = Time to load 10%
            self.progress.set(0.1*i)
            i += 1
        else:
            self.window.withdraw()
            # Chạy loadingPage.py với PYTHONPATH chỉ định cho Windows
            run_with_custom_path("src/views/loginPage.py")
            self.window.destroy()
            # print('Load Completed!!!')

i = 0

def main():
    loadingPage = LoadingPage(attributes=PAGE_ATTRIBUTES)
    loadingPage.Render()

if __name__ == "__main__":
    main()