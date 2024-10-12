from customtkinter import *

class PrimaryLabel(CTkLabel):
    def __init__(self, master, width = 0, height = 28, corner_radius = None, bg_color = "transparent", fg_color = None, text_color = "#fd6a36", text_color_disabled = None, text = "CTkLabel", font = ('yu gothic ui', 24, 'bold'), image = None, compound = "center", anchor = "center", wraplength = 0, **kwargs):
        super().__init__(master, width, height, corner_radius, bg_color, fg_color, text_color, text_color_disabled, text, font, image, compound, anchor, wraplength, **kwargs)
        self.master.configure(text_color = "#fd6a36")
