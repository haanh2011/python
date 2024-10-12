from customtkinter import *
from .color import *

def setFont(fontSize = 16, fontWeight = None): return ('yu gothic ui', fontSize, fontWeight) 

PrimaryTextAttr = {
    'text_color': MAIN_COLOR,
}

PrimaryButtonAttr = {
    'text_color': 'white',
    'fg_color': MAIN_COLOR
}
class H3Label(CTkLabel):
    def __init__(self, master, width = 0, height = 28, corner_radius = None, bg_color = "transparent", fg_color = None, text_color = MAIN_COLOR, text_color_disabled = None, text = "CTkLabel", font = setFont(24,'bold'), image = None, compound = "center", anchor = "center", wraplength = 0, **kwargs):
        super().__init__(master, width, height, corner_radius, bg_color, fg_color, text_color, text_color_disabled, text, font, image, compound, anchor, wraplength, **kwargs)
        self.configure(**PrimaryTextAttr)

class PrimaryButton(CTkButton):
    def __init__(self, master, width = 140, height = 28, corner_radius = None, border_width = None, border_spacing = 2, bg_color = "transparent", fg_color = None, hover_color = None, border_color = None, text_color = None, text_color_disabled = None, background_corner_colors = None, round_width_to_even_numbers = True, round_height_to_even_numbers = True, text = "CTkButton", font = None, textvariable = None, image = None, state = "normal", hover = True, command = None, compound = "left", anchor = "center", **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, border_spacing, bg_color, fg_color, hover_color, border_color, text_color, text_color_disabled, background_corner_colors, round_width_to_even_numbers, round_height_to_even_numbers, text, font, textvariable, image, state, hover, command, compound, anchor, **kwargs)
        self.configure(**PrimaryButtonAttr)