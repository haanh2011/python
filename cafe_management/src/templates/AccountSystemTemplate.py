from modules import Template
from tkinter import *

root = Tk()
TEMPLATE_CONFIGS = {
    'background': '#fd6a36'
}
TEMPLATE_ATTRIBUTES = {
    'title': '',
    'width':700,
    'height':650
}
TEMPLATE_WM_ATTRIBUTES = {
    '-topmost': True
}

AccountSystem = Template(**{
    'root': root,
    'configs': TEMPLATE_CONFIGS,
    'attributes': TEMPLATE_ATTRIBUTES,
    'wm_attributes': TEMPLATE_WM_ATTRIBUTES,
    'resizable': (0,0)
})