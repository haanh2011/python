import tkinter

from customtkinter import *
from .buildThemeToJson import *

def setFont(fontSize = 16, fontWeight = None): return ('yu gothic ui', fontSize, fontWeight) 

PrimaryTextAttr = {
    'text_color': PRIMARY_COLOR,
}

PrimaryButtonAttr = {
    'text_color': 'white',
    'fg_color': PRIMARY_COLOR
}
class H3Label(CTkLabel):
    def __init__(self, master, width = 0, height = 28, corner_radius = None, bg_color = "transparent", fg_color = None, text_color = PRIMARY_COLOR, text_color_disabled = None, text = "CTkLabel", font = setFont(24,'bold'), image = None, compound = "center", anchor = "center", wraplength = 0, **kwargs):
        super().__init__(master, width, height, corner_radius, bg_color, fg_color, text_color, text_color_disabled, text, font, image, compound, anchor, wraplength, **kwargs)
        self.configure(**PrimaryTextAttr)

class CusEntry(CTkEntry):
    def __init__(self, master, width = 140, height = 28, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, text_color = None, placeholder_text_color = None, textvariable = None, placeholder_text = None, font = None, state = tkinter.NORMAL, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, text_color, placeholder_text_color, textvariable, placeholder_text, font, state, **kwargs)
        
        # Gắn sự kiện focus và unfocus cho Entry
        self.bind("<FocusIn>", self.on_focus)
        self.bind("<FocusOut>", self.on_unfocus)

    # Hàm thay đổi màu khi Entry được focus
    def on_focus(self, event):
        self.configure(border_color=PRIMARY_COLOR)

    # Hàm thay đổi màu khi Entry mất focus
    def on_unfocus(self, event):
        self.configure(border_color="gray")