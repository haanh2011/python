import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from src.views import styles

def load_image_button(image_path, size=(20, 20)):
    """
    Tải và thay đổi kích thước hình ảnh từ đường dẫn, trả về đối tượng PhotoImage để sử dụng trong nút.

    :param image_path: Đường dẫn đến file ảnh.
    :param size: Bộ đôi (width, height) để thay đổi kích thước hình ảnh.
    :return: Đối tượng ImageTk.PhotoImage đã được thay đổi kích thước.
    """
    if not os.path.exists(image_path):
        messagebox.showerror("Error", f"Image file not found: {image_path}")
        return None

    try:
        # Mở và thay đổi kích thước hình ảnh
        image = Image.open(image_path)
        image = image.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(image)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load image: {str(e)}")
        return None

def create_image_button(parent, name, text="", image_path=None, command=None, size=(20, 20), tooltip_text=None,
                        compound="left",state=tk.NORMAL, **kwargs):
    """
    Tạo một nút với hình ảnh và thêm vào cha của nó (parent), với khả năng tùy chỉnh cao.

    :param parent: Đối tượng cha (frame, window, etc.) nơi nút sẽ được đặt.
    :param name: Tên cho nút, dùng để dễ dàng tham chiếu sau này.
    :param text: Văn bản hiển thị trên nút.
    :param image_path: Đường dẫn đến file hình ảnh (nếu có).
    :param command: Hàm sẽ được gọi khi nhấn nút.
    :param size: Bộ đôi (width, height) để thay đổi kích thước hình ảnh.
    :param tooltip_text: Văn bản tooltip sẽ xuất hiện khi di chuột qua nút (nếu có).
    :param compound: Vị trí của hình ảnh so với văn bản ("left", "right", "top", "bottom").
    :param kwargs: Các tham số bổ sung để định dạng nút (bg, fg, etc.).
    :return: Đối tượng nút đã tạo.
    """
    # Thiết lập các thuộc tính mặc định cho nút
    default_button_styles = {
        "bg": "#4CAF50",
        "fg": styles.FOREGROUND_COLOR,
        "font": styles.get_button_actions_font(),
        "activebackground": "#3E8E41",
        "activeforeground": styles.BUTTON_FOREGROUND_COLOR,
        "padx": 8,
        "pady": 4,
        "relief": tk.FLAT,
        "borderwidth": 0,
        "highlightthickness": 0
    }

    # Kết hợp các giá trị mặc định với kwargs do người dùng cung cấp
    button_styles = {**default_button_styles, **kwargs}

    photo = None

    if image_path:
        # Tải ảnh và kiểm tra lỗi nếu có
        photo = load_image_button(image_path, size)
        if photo is None:
            return None

    # Tạo đối tượng Button với hình ảnh và văn bản
    btn = tk.Button(parent, text=text, command=command, image=photo, compound=compound, **button_styles, state=state)

    if photo:
        btn.image = photo  # Giữ tham chiếu ảnh để nó không bị xóa bởi garbage collector
    btn._name = name  # Đặt tên cho nút để tham chiếu sau

    # Nếu có tooltip text, tạo tooltip cho nút
    if tooltip_text:
        create_tooltip(btn, tooltip_text)

    return btn


def create_tooltip(widget, text):
    """
    Tạo tooltip hiển thị khi người dùng di chuột qua một widget.

    :param widget: Widget mà tooltip sẽ gắn vào (nút, label, etc.).
    :param text: Văn bản sẽ hiển thị trong tooltip.
    """
    tooltip = tk.Toplevel(widget, bg='yellow', padx=1, pady=1)
    tooltip.wm_overrideredirect(True)  # Loại bỏ thanh tiêu đề
    tooltip_label = tk.Label(tooltip, text=text, bg='yellow', fg='black', relief='solid', borderwidth=1)
    tooltip_label.pack()

    def on_enter(event):
        tooltip.geometry(f"+{widget.winfo_rootx() + 20}+{widget.winfo_rooty() + 20}")
        tooltip.deiconify()

    def on_leave(event):
        tooltip.withdraw()

    widget.bind("<Enter>", on_enter)
    widget.bind("<Leave>", on_leave)

    tooltip.withdraw()  # Ẩn tooltip ban đầu
