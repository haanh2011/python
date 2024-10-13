from customtkinter import *
from PIL import Image, ImageTk
import os
import sys
class WindowBase:
    attributes = {
        # 'title': "Widget's title",
        'height': None,
        'width': None,
        'x': 0,
        'y': 0,
    }
    configs = {}
    def __init__(self, window, attributes = {}, configs= {}):
        self.window = window
        self.configs.update(configs)
        # Ghi đè các thuộc tính mặc định của attribute vào
        self.attributes.update(attributes)

        self._setAttributes()
        self._setConfigs()
        self._setLogo()
        
    def _setLogo(self):
        logoPath = os.path.join('src', 'assets', 'images', 'CoffeeShop-brand-logo.ico')  # Đảm bảo logo có định dạng .ico
        if os.path.exists(logoPath):
            # Đặt biểu tượng cho cửa sổ bằng iconbitmap
            self.window.iconbitmap(logoPath)  # Đặt icon cho cửa sổ
        else:
            print("Logo path not found.")
    def _setConfigs(self):
        self.window.config(**self.configs)
    def _setConfigs(self):
        self.window.config(**self.configs)

    def _setAttributes(self):
        if 'title' in self.attributes:
            self.window.title(self.attributes['title'])  # Thiết lập tiêu đề cho cửa sổ

        # *** Chỉnh các thuộc tính cho page
        # Nếu không truyền height and width thì mặc định set full màn hình
        if self.attributes['height'] is None and self.attributes['width'] is None:
            self.window.state('zoomed')
        else:
            self.attributes['x'] = (self.window.winfo_screenwidth() // 2) - (self.attributes['width'] // 2)
            self.attributes['y'] = (self.window.winfo_screenheight() // 2) - (self.attributes['height'] // 2)
            self.window.geometry(f"{self.attributes['width']}x{self.attributes['height']}+{self.attributes['x']}+{self.attributes['y']}")
    def Render(self):
        self.window.mainloop()

    def Exit(self):
        sys.exit(self.window.destroy())

