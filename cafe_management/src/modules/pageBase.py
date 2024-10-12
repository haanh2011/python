from customtkinter import *

class PageBase:
    attributes = {
        # 'title': "Widget's title",
        'height': None,
        'width': None,
        'x': 0,
        'y': 0,
    }
    configs = {}
    renderFunc = None
    def __init__(self, root, renderFunc, attributes = {}, configs= {}):
        self.root = root
        self.renderFunc = renderFunc
        self.configs.update(configs)
        # Ghi đè các thuộc tính mặc định của attribute vào
        self.attributes.update(attributes)

        self._setAttributes()
        self._setConfigs()

        
    def _setConfigs(self):
        self.root.config(**self.configs)

    def _setAttributes(self):
        if 'title' in self.attributes:
            self.root.title(self.attributes['title'])  # Thiết lập tiêu đề cho cửa sổ

        # *** Chỉnh các thuộc tính cho page
        # Nếu không truyền height and width thì mặc định set full màn hình
        if self.attributes['height'] is None and self.attributes['width'] is None:
            self.root.state('zoomed')
        else:
            self.attributes['x'] = (self.root.winfo_screenwidth() // 2) - (self.attributes['width'] // 2)
            self.attributes['y'] = (self.root.winfo_screenheight() // 2) - (self.attributes['height'] // 2)
            self.root.geometry(f"{self.attributes['width']}x{self.attributes['height']}+{self.attributes['x']}+{self.attributes['y']}")

    def render(self):
        if self.renderFunc is not None:
            self.renderFunc()
        self.root.mainloop()  # Bắt đầu vòng lặp sự kiện Tkinter

    def Exit(self):
        self.root.destroy()  # Đóng Widget
