import tkinter as tk

class Tooltip:
    def __init__(self, widget, text_func, delay=500):
        """
        :param widget: Widget cần áp dụng tooltip.
        :param text_func: Hàm trả về nội dung tooltip.
        :param delay: Thời gian chờ trước khi hiển thị tooltip.
        """
        self.widget = widget
        self.text_func = text_func  # Hàm trả về nội dung của tooltip
        self.delay = delay
        self.tooltip_window = None
        self.id = None
        self.widget.bind("<Enter>", self.on_enter)
        self.widget.bind("<Leave>", self.on_leave)
        self.widget.bind("<Motion>", self.on_motion)

    def on_enter(self, event=None):
        self.schedule_tooltip()

    def on_leave(self, event=None):
        self.unschedule_tooltip()
        self.hide_tooltip()

    def on_motion(self, event):
        """Handle the motion event to get current mouse coordinates"""
        self.mouse_x = event.x_root
        self.mouse_y = event.y_root

    def schedule_tooltip(self):
        self.unschedule_tooltip()
        self.id = self.widget.after(self.delay, self.show_tooltip)

    def unschedule_tooltip(self):
        if self.id:
            self.widget.after_cancel(self.id)
            self.id = None

    def show_tooltip(self):
        if self.tooltip_window:
            return

        # Lấy nội dung tooltip từ hàm text_func
        tooltip_text = self.text_func()
        if not tooltip_text:
            return  # Không hiển thị nếu không có nội dung

        # Tọa độ để hiển thị tooltip
        x = self.mouse_x + 10
        y = self.mouse_y + 10

        self.tooltip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(tw, text=tooltip_text, background="lightyellow", borderwidth=1, relief="solid")
        label.pack()

    def hide_tooltip(self):
        tw = self.tooltip_window
        self.tooltip_window = None
        if tw:
            tw.destroy()
