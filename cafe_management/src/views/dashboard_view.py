import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
controllers_dir = os.path.join(current_dir, '../controllers')
sys.path.append(controllers_dir)

import window
display_name = "Thống Kê"

def create_frame(frame_parent):
    frame = window.create_frame_dashboard(frame_parent)
    return frame

def create_button_menu(dashboard_frame, frame, buttons, frames):
    btn = window.create_button_menu(dashboard_frame, frame, display_name, buttons, frames)
    return btn