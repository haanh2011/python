import tkinter as tk
from datetime import datetime
import tkinter.font as font

class ClockFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.running = True  # Flag to control clock updates
        self.after_id = None  # To store the after ID for cancellation
        self.create_widgets()
        self.update_clock()

    def create_widgets(self):
        # Thiết lập font chữ
        self.clock_font = font.Font(family="Helvetica", size=16, weight="bold")

        # Tạo label đồng hồ
        self.clock_label = tk.Label(self, font=self.clock_font, fg="white", bg="#CD6600", padx=10, pady=5)
        self.clock_label.pack()


    def update_clock(self):
        if self.running:
            # Lấy thời gian hiện tại
            current_time = datetime.now().strftime("%H:%M:%S")

            # Cập nhật văn bản của label
            self.clock_label.config(text=current_time)

            # Gọi lại phương thức sau 1 giây
            self.after_id = self.after(1000, self.update_clock)  # Store the after ID

    def stop_clock(self):
        if self.after_id:
            self.after_cancel(self.after_id)  # Cancel the scheduled after call
            self.after_id = None