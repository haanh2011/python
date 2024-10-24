import sys, os
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from src.views import styles, order_view
from styles import *
from src.helper.clock_frame import *

from PIL.ImageOps import expand
from numpy.ma.core import filled
from pandas.io.formats.info import frame_examples_sub

current_dir = os.path.dirname(os.path.abspath(__file__))
utilities_dir = os.path.join(current_dir, '../utilities')
sys.path.append(utilities_dir)
import validate
from login_view import create_login_frame

from src.helper import button_image

from dialogs import add_dialog, update_dialog, delete_dialog


def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_position = (screen_width - width) // 2
    y_position = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x_position}+{y_position}")


def create_root_window(title, width, height):
    root = tk.Tk()
    root.title(title)
    # root.iconbitmap("images/logo.ico")  # Thay đổi đường dẫn đến file icon của bạn
    # Đặt icon bằng hình ảnh
    img = Image.open("images/logo.png")  # Thay đổi đường dẫn đến file hình ảnh của bạn
    icon = ImageTk.PhotoImage(img)
    root.iconphoto(False, icon)

    center_window(root, width, height)
    return root


def create_header(frame_parent):
    header_frame = tk.Frame(frame_parent, bg=BACKGROUND_COLOR)
    header_frame.pack(side="top", fill="x")
    header_logo_label = tk.Label(header_frame, text="QUẢN LÝ QUÁN CÀ PHÊ", font=("Arial", 21, "bold"),
                                 fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR, anchor="center", justify="center")
    header_logo_label.pack(side="left", padx=20, pady=10)

    clock_frame = ClockFrame(header_frame)

    # Create a logout button
    btn_logout = button_image.create_image_button(
        header_frame, "btn_logout", "Đăng xuất", "images/logout.png",
        command=lambda: confirm_logout(frame_parent, clock_frame),
        tooltip_text="",
        bg="#f0f0f0",  # Màu nền tùy chỉnh
        fg=BACKGROUND_COLOR  # Màu chữ tùy chỉnh
    )
    btn_logout.pack(side="right", padx=10, pady=5)

    clock_frame.pack(side="right", padx=20, pady=5)


def confirm_logout(root, clock_frame):
    if messagebox.askokcancel("Xác nhận đăng xuất", "Bạn có chắc chắn muốn đăng xuất?"):
        clock_frame.stop_clock()  # Stop the clock updates
        clock_frame.destroy()  # Destroy the clock frame
        root.destroy()  # Close the main window
        show_login_form()  # Show the login form


def show_login_form(root):
    login_window = tk.Tk()
    login_window.title("Login")
    create_login_frame(login_window)
    center_window(login_window, 400, 200)
    return login_window


def create_frame(frame_parent, name, **kwargs):
    return tk.Frame(frame_parent, name=name, **kwargs)


def create_dialog(frame_parent, title):
    """
    Tạo một dialog và căn giữa nó trên màn hình.

    :param frame_parent: Cửa sổ cha (parent window) của dialog.
    :param title: Tiêu đề của dialog.
    :param width: Chiều rộng của dialog.
    :param height: Chiều cao của dialog.
    :return: Đối tượng dialog được tạo.
    """
    # Tạo dialog
    dialog_toplv = tk.Toplevel(frame_parent)
    dialog_toplv.grab_set()  # Đặt dialog ở chế độ modal
    dialog_toplv.title(title)

    # Cài đặt một số thuộc tính cho dialog (tuỳ chọn)
    dialog_toplv.resizable(False, False)  # Không cho phép thay đổi kích thước

    return dialog_toplv


def set_centered_geometry(root, top_level):
    # Cập nhật giao diện để lấy kích thước thực tế của dialog
    top_level.update_idletasks()

    # Lấy kích thước của màn hình
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Lấy kích thước thực tế của dialog sau khi cập nhật
    dialog_width = top_level.winfo_reqwidth()  # Chiều rộng
    dialog_height = top_level.winfo_reqheight()  # Chiều cao

    # Tính toán vị trí để đặt dialog ở giữa màn hình
    x_position = (screen_width // 2) - (dialog_width // 2)
    y_position = (screen_height // 2) - (dialog_height // 2)

    # Đặt kích thước và vị trí của dialog
    top_level.geometry(f"{dialog_width}x{dialog_height}+{x_position}+{y_position}")


def create_tree_view(frame_treeview, dict_cols, rows):
    """
    Tạo Treeview với số lượng cột không xác định.
    :param frame_treeview: Frame cha chứa Treeview.
    :param dict_cols: Dictionary chứa thông tin các cột.
    :param rows: Thông tin data hiển thị trong treeview.
    """
    configure_treeview_style()  # Gọi hàm để cấu hình style

    # Đảm bảo frame_treeview chiếm đầy khung
    frame_treeview.grid_rowconfigure(0, weight=1)
    frame_treeview.grid_columnconfigure(0, weight=1)  # Cấu hình để cột chiếm toàn bộ không gian

    # Tạo Treeview và đặt nó vào frame
    tr = ttk.Treeview(frame_treeview, style="Custom.Treeview", columns=dict_cols["columns_name_display"],
                      show='headings')

    # Tính toán chiều rộng dựa trên số lượng cột
    total_width = 1000  # Tổng chiều rộng của Treeview (có thể tùy chỉnh)
    num_columns = max(1, len(dict_cols["columns_name_display"]))  # Đảm bảo ít nhất là 1 cột
    column_width = total_width // num_columns  # Chiều rộng của mỗi cột

    # Vòng lặp để tạo các widget, đặt tiêu đề cột, căn giữa, và đặt chiều rộng cho mỗi cột
    for col_name in dict_cols["columns_name_display"]:
        tr.heading(col_name, text=col_name, anchor="center")  # Căn giữa tiêu đề
        tr.column(col_name, anchor="center", width=column_width)  # Căn giữa dữ liệu và set chiều rộng

    # Thêm data từ DB vào treeview
    if rows:
        for i in rows:
            tr.insert('', 'end', iid=i[0], values=i)

    # Đặt Treeview vào lưới và để nó mở rộng toàn bộ không gian còn lại
    tr.grid(row=0, column=0, sticky='nsew')

    # Thêm thanh cuộn
    scrollbar_y = ttk.Scrollbar(frame_treeview, orient="vertical", command=tr.yview)
    scrollbar_y.grid(row=0, column=1, sticky='ns')

    scrollbar_x = ttk.Scrollbar(frame_treeview, orient="horizontal", command=tr.xview)
    scrollbar_x.grid(row=1, column=0, sticky='ew')

    tr.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

    return tr


def create_actions(frame_action, name, show_details_item, add_item, update_item, delete_item):
    # Tạo nút 'Add' và đặt nó ở phía trên, bên phải của sub_frame
    add_button = button_image.create_image_button(
        frame_action, "add_btn", "Thêm", "images/add.png",
        command=lambda: add_item(),
        tooltip_text="Thêm",
        bg="#4CAF50",  # Màu nền tùy chỉnh
        fg="white"  # Màu chữ tùy chỉnh
    )
    add_button.grid(row=0, column=0, sticky='we', padx=5, pady=5)  # Đặt nút ở góc trên bên phải

    update_button = button_image.create_image_button(
        frame_action,
        "add_btn",
        "Sửa",
        "images/edit.png",
        command=lambda: update_item(),
        tooltip_text="Sửa",
        bg="#FFC107",  # Màu nền tùy chỉnh
        fg="white",  # Màu chữ tùy chỉnh
        state=tk.DISABLED
    )
    update_button.grid(row=0, column=1, sticky='we', padx=5, pady=5)  # Đặt nút ở góc trên bên phải

    delete_button = button_image.create_image_button(
        frame_action,
        "add_btn",
        "Xoá",
        "images/delete.png",
        command=lambda: delete_item(),
        tooltip_text="Xoá",
        bg="#CD5555",  # Màu nền tùy chỉnh
        fg="white",  # Màu chữ tùy chỉnh
        state=tk.DISABLED
    )
    delete_button.grid(row=0, column=2, sticky='we', padx=5, pady=5)  # Đặt nút ở góc trên bên phải

    widgets = {"add_button": add_button, "update_button": update_button, "delete_button": delete_button}
    if name == "orders":
        show_details_button = button_image.create_image_button(
            frame_action, "add_btn", "Chi tiết", "images/order.png",
            command=lambda: show_details_item(),
            tooltip_text="Chi tiết ",
            bg="#3b5998",  # Màu nền tùy chỉnh
            fg="white",  # Màu chữ tùy chỉnh
            state=tk.DISABLED
        )
        show_details_button.grid(row=0, column=3, sticky='we', padx=5, pady=5)  # Đặt nút ở góc trên bên phải
        widgets["show_details_button"] = show_details_button
    return widgets


def create_frame_actions_treeview(controller, frame_parent, name, display_name, dict_cols, rows):
    """
        Hàm tạo nội dung cho khung (frame) với bảng và các nút hành động.
        :param controller: Bộ điều khiển để lấy dữ liệu và thực hiện các thao tác.
        :param frame_parent: Frame gốc để đặt khung mới vào.
        :param display_name: Tên của khung nội dung (vd: 'category', 'product', ...).
        :param dict_cols: Từ điển các cột của bảng (vd: {"columns_name_display": ["Mã", "Tên loại sản phẩm"], ...}).
        :param rows: Dữ liệu ban đầu cho Treeview.
        :return: Trả về đối tượng frame đã tạo.
    """
    # Tạo frame chứa toàn bộ
    frame_root = tk.Frame(frame_parent, name=f"fr_{name}", bg="#f0f0f0")
    frame_root.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

    # Cấu hình để frame_root mở rộng đầy đủ
    frame_root.grid_rowconfigure(1, weight=1)  # Đảm bảo row 1 (chứa Treeview) mở rộng theo chiều dọc
    frame_root.grid_columnconfigure(0, weight=1)  # Đảm bảo cột chứa Treeview mở rộng theo chiều ngang

    # Tạo frame chứa các actions của grid
    frame_action = tk.Frame(frame_root, name=f"fr_action_{name}")
    frame_action.grid(row=0, column=0, sticky="ne", padx=10, pady=10)

    # Cấu hình các cột của frame_action để căn đều các nút
    for idx in range(len(dict_cols["columns_name_display"])):
        frame_action.grid_columnconfigure(idx, weight=1)

    # Tạo frame phụ chứa Treeview
    frame_treeview = ttk.Frame(frame_root, name=f"fr_tv_{name}")
    frame_treeview.grid(row=1, column=0, sticky="nsew")  # Đảm bảo nó mở rộng full

    # Đảm bảo frame_treeview chiếm toàn bộ không gian còn lại
    frame_treeview.grid_rowconfigure(0, weight=1)
    frame_treeview.grid_columnconfigure(0, weight=1)

    # Tạo treeview
    tree = create_tree_view(frame_treeview, dict_cols, rows)

    def update_tree_view():
        """
        Cập nhật Treeview với dữ liệu mới từ controller.
        """
        # Xóa dữ liệu cũ trong Treeview
        for item in tree.get_children():
            tree.delete(item)

        # Lấy dữ liệu mới và thêm vào Treeview
        new_rows = controller.get_data(name)
        for row in new_rows:
            tree.insert('', 'end', iid=row[0], values=row)

        print("Treeview updated successfully!")

    def show_details_item():
        # Kiểm tra frame_parent
        print("show_details_item")
        if frame_parent is None:
            print("Error: Parent frame is not initialized.")
            return
        selected_item = tree.selection()
        if not selected_item:
            print("Error: No item selected.")
            return
        selected_item_id = selected_item[0]
        order_view.create_frame_details(frame_parent, selected_item_id)

    def add_item():
        print("Add item")
        if frame_parent is None:
            print("Error: Parent frame is not initialized.")
            return

        # Hiển thị dialog thêm dữ liệu mới
        add_dialog.show_dialog(controller=controller, frame_parent=frame_parent, dict_cols=dict_cols,
                               name=name, display_name=display_name, on_success=update_tree_view)

    def update_item():
        selected_item = tree.selection()
        if not selected_item:
            print("Error: No item selected.")
            return
        selected_item_id = selected_item[0]
        item_data = tree.item(selected_item_id)
        print("update_item", item_data)
        update_dialog.show_dialog(controller=controller, frame_parent=frame_parent, dict_cols=dict_cols,
                                  name=name, display_name=display_name, data=item_data, on_success=update_tree_view)

    def delete_item():
        selected_item_id = tree.selection()[0]
        print("delete_item", selected_item_id)
        delete_dialog.show_dialog(controller=controller, frame_parent=frame_parent, name=name, data_id=selected_item_id,
                                  on_success=update_tree_view)

    widgets = create_actions(frame_action=frame_action, name=name, show_details_item=show_details_item,
                             add_item=add_item,
                             update_item=update_item,
                             delete_item=delete_item)

    # Bind the click outside event to the root window
    def on_select(event):
        selected_items = tree.selection()

        # Kiểm tra nếu không có mục nào được chọn
        if not selected_items:
            print("No item selected.")
            widgets["update_button"].configure(state=tk.DISABLED)
            widgets["delete_button"].configure(state=tk.DISABLED)
            if name == "orders":
                widgets["show_details_button"].configure(state=tk.DISABLED)
            return

        selected_item_id = selected_items[0]

        # Enable the button if an item is selected
        widgets["update_button"].configure(state=tk.NORMAL if selected_item_id else tk.DISABLED)
        widgets["delete_button"].configure(state=tk.NORMAL if selected_item_id else tk.DISABLED)
        if name == "orders":
            widgets["show_details_button"].configure(state=tk.NORMAL if selected_item_id else tk.DISABLED)

    # Bind the selection event to the Treeview
    tree.bind('<<TreeviewSelect>>', on_select)

    # frame_treeview.grid(row=1, column=0, sticky="new")

    def on_click_outside(event):
        # Clear the selection if clicked outside the Treeview
        print("click outside", event)
        tree.selection_set()

    frame_root.bind('<Button-1>', on_click_outside)
    return frame_root


def create_button(frame_parent, name, command, state="disabled"):
    """
    Tạo một nút trong frame cha với tên và lệnh chỉ định.

    Args:
        frame_parent (tk.Frame): Frame cha nơi nút sẽ được thêm vào.
        name (str): Tên hiển thị của nút.
        command (callable): Lệnh được gọi khi nút được nhấn.
        state (str): Trạng thái của nút ('normal', 'disabled'). Mặc định là 'disabled'.

    Returns:
        tk.Button: Đối tượng nút đã được tạo.
    """
    btn = tk.Button(frame_parent, text=name, command=command)
    btn.pack(pady=5, state=state)  # Thêm khoảng cách cho nút (tuỳ chọn)
    return btn


def pack_forget_all_frames(frames):
    """
    Ẩn tất cả các frame.
    :param frames: Danh sách các frame cần ẩn.
    """
    for frame in frames:
        frame.pack_forget()


def enable_all_buttons(buttons):
    """
    Kích hoạt lại tất cả các nút trong danh sách nút.
    :param buttons: Danh sách các nút cần kích hoạt.
    """
    for btn in buttons:
        btn.config(state=tk.NORMAL)


def show_frame(selected_frame, frames, buttons, selected_button):
    """
    Hiển thị frame được chọn và vô hiệu hóa nút tương ứng.
    :param selected_frame: Frame cần hiển thị.
    :param frames: Danh sách các frame.
    :param buttons: Danh sách các nút.
    :param selected_button: Nút cần vô hiệu hóa.
    """
    # Ẩn tất cả các frame
    pack_forget_all_frames(frames)

    # Kích hoạt lại tất cả các nút
    enable_all_buttons(buttons)

    # Hiển thị frame được chọn và vô hiệu hóa nút tương ứng
    selected_frame.pack(fill="both", expand=True)
    selected_button.config(state="disabled")


def create_button_menu(frame_parent, frame_to_show, display_name, buttons, frames, func_set_data_init=None):
    """
    Tạo nút menu trong frame cha và gán hành động hiển thị frame tương ứng khi nhấn.
    :param frame_parent: Frame chứa nút menu.
    :param frame_to_show: Frame cần hiển thị khi nhấn nút.
    :param display_name: Nhãn của nút.
    :param buttons: Danh sách các nút.
    :param frames: Danh sách các frame.
    :return: Đối tượng nút đã tạo.
    """

    def show_frame_and_set_init():
        if func_set_data_init != None:
            func_set_data_init()
        show_frame(frame_to_show, frames, buttons, btn)

    btn = tk.Button(frame_parent, text=display_name, command=lambda: show_frame_and_set_init(),
                    **BTN_MENU)
    btn.pack(fill="x", padx=5, pady=5)
    buttons.append(btn)
    return btn


def create_frame_order(frame_actions):
    height_widget = 40
    frame_order = ttk.Frame(frame_actions, height=height_widget * 3)

    # Tạo entry order id
    entry_customer_label = ttk.Label(frame_order, width=20,
                                     text="Tên khách hàng")  # Điều chỉnh width của entry để dài hơn
    entry_customer_label.grid(row=0, column=0, sticky="ns", pady=5)
    combobox_customer = ttk.Combobox(frame_order, width=25,
                                     height=height_widget)  # Điều chỉnh width của entry để dài hơn
    combobox_customer.grid(row=0, column=1, sticky="ns", pady=5)
    # Tạo entry order id
    entry_create_date_label = ttk.Label(frame_order, width=20, text="Ngày tạo")  # Điều chỉnh width của entry để dài hơn
    entry_create_date_label.grid(row=1, column=0, sticky="ns", pady=5)
    combobox_create_date = ttk.Combobox(frame_order, width=25,
                                        height=height_widget)  # Điều chỉnh width của entry để dài hơn
    combobox_create_date.grid(row=1, column=1, sticky="ns", pady=5)

    entry_id_label = ttk.Label(frame_order, width=20, text="Mã đơn hàng")  # Điều chỉnh width của entry để dài hơn
    entry_id_label.grid(row=2, column=0, sticky="ns", pady=5)
    combobox_id = ttk.Combobox(frame_order, width=25, height=height_widget)  # Điều chỉnh width của entry để dài hơn
    combobox_id.grid(row=2, column=1, sticky="ns", pady=5)
    return frame_order


def create_date_entry(parent, format="%Y-%m-%d"):
    """Creates an entry field for date input with the specified format.

    Args:
        parent: The parent widget for the entry field.
        format: The desired format for the date input (default: "%Y-%m-%d").

    Returns:
        The created entry field widget.
    """

    entry = ttk.Entry(parent)
    entry.pack()

    # Bind the entry field to a validation function
    entry.configure(validate="key", validatecommand=(entry.register(validate.validate_date), "%P", format))

    return entry


# Hàm để lấy dữ liệu từ Treeview và chuyển thành danh sách các dicts
def get_treeview_data_to_dict(treeview):
    treeview_data = []

    # Lấy header (columns)
    columns = treeview["columns"]

    # Lấy tất cả các hàng trong Treeview
    for row_id in treeview.get_children():
        row_values = treeview.item(row_id)['values']

        # Kết hợp header với giá trị của hàng
        row_dict = {columns[i]: row_values[i] for i in range(len(columns))}
        treeview_data.append(row_dict)

    return treeview_data


def get_widget_values(widgets):
    """Retrieves values from various widget types in a dictionary.

    Args:
        widgets (dict): A dictionary mapping widget labels to their corresponding tkinter widgets.

    Returns:
        dict: A dictionary containing widget labels as keys and their respective values as values.
    """

    data = {}
    for label, widget in widgets.items():
        if isinstance(widget, tk.Text):
            value = widget.get('1.0', 'end')
            print("value Text", value)
        elif isinstance(widget, ttk.Combobox):
            value = widget.get().split("-")[0].strip()
            print("value Combobox", value)
        elif isinstance(widget, ttk.Treeview):
            # Get all items from Treeview
            value = get_treeview_data_to_dict(widget)
            print(value, "value treeview")
        elif isinstance(widget, tk.Entry):
            value = widget.get()
            print("value Entry", value)
        else:
            value = None  # Handle unsupported widget types
        print(widget.winfo_name())
        data[widget.winfo_name()] = value
    return data


def set_width_height_top_level(top_level, width, height):
    # Lấy kích thước màn hình và tính toán vị trí giữa
    screen_width = top_level.winfo_screenwidth()
    screen_height = top_level.winfo_screenheight()
    dialog_width = width
    dialog_height = height
    x_position = (screen_width // 2) - (dialog_width // 2)
    y_position = (screen_height // 2) - (dialog_height // 2)

    # Căn giữa dialog trên màn hình
    top_level.geometry(f"{dialog_width}x{dialog_height}+{x_position}+{y_position}")  # Set kích thước và vị trí


# Tạo hàm chứa add list product cho order
def create_entry_add_list_product(form_frame, product_values, idx, col_name, widgets, data_id, total_price):
    print("data_id", data_id)
    data_details = {}
    if data_id != "":
        data_details = order_view.get_all_data_details(data_id)
    print("data_details", data_details)
    product_label = tk.Label(form_frame, text="Sản phẩm:",
                             font=("Helvetica", 12),
                             foreground="#000000",
                             padx=10, pady=10)
    product_label.grid(row=idx + 1, column=0, sticky="ew")

    # Combobox để nhập tên sản phẩm
    selected_data = tk.StringVar()
    product_combobox = ttk.Combobox(form_frame, textvariable=selected_data, values=product_values, width=35,
                                    state="readonly",
                                    font=("Helvetica", 12),
                                    justify='center')
    product_combobox.grid(row=idx + 1, column=1, sticky="ew")

    # Entry để nhập số lượng
    quantity_label = tk.Label(form_frame, text="Số lượng:",
                              font=("Helvetica", 12),
                              foreground="#000000",
                              padx=10, pady=10)
    quantity_label.grid(row=idx + 2, column=0, sticky="ew")
    quantity_entry = tk.Entry(form_frame)
    quantity_entry.grid(row=idx + 2, column=1, sticky="ew")

    def add_product():
        """Handle the Add button press."""
        data_product = product_combobox.get().split("-")
        product_name = data_product[1].strip()
        product_price = data_product[2].strip()
        quantity = quantity_entry.get().strip()

        if not product_name or not quantity:
            messagebox.showwarning("Input Error", "Both product name and quantity are required.")
            return

        try:
            quantity = int(quantity)
        except ValueError:
            messagebox.showwarning("Input Error", "Quantity must be a number.")
            return

        # Check if the product ID already exists in the Treeview
        existing_item = None
        for item in tree.get_children():
            values = tree.item(item, 'values')
            if values[1] == product_name:  # Compare product ID
                existing_item = item
                break
        total = float(entry_total.get()) + float(product_price) * float(quantity)
        update_entry_value(total)
        if existing_item:  # If product ID exists, update the quantity
            existing_quantity = int(tree.item(existing_item, 'values')[2])  # Get current quantity
            new_quantity = existing_quantity + quantity  # Calculate new quantity
            tree.item(existing_item, values=(product_name, product_price, new_quantity))  # Update the item
        else:  # If product ID does not exist, add a new row
            tree.insert("", "end", values=(product_name, product_price, quantity))

        # Clear the input fields
        product_combobox.set('')
        quantity_entry.delete(0, tk.END)

    def delete_product():
        """Handle the Delete button press."""
        selected_idx = tree.selection()
        selected_item = tree.item(selected_idx)
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a product to delete.")
            return
        tree.delete(selected_idx)
        total = float(entry_total.get()) - float(selected_item["values"][1]) * float(selected_item["values"][2])
        update_entry_value(total)
        print(selected_item, "selected_item")

    def on_tree_select(event):
        """Enable or disable the delete button based on selection."""
        selected_item = tree.selection()
        if selected_item:
            delete_button.config(state="normal")  # Enable delete button
        else:
            delete_button.config(state="disabled")  # Disable delete button

    # Hàm để cập nhật giá trị của Entry từ code
    def update_entry_value(new_value):
        entry_total.config(state="normal")  # Chuyển state về 'normal' để có thể thay đổi
        entry_total_value.set(new_value)  # Cập nhật giá trị của Entry
        entry_total.config(state="readonly")  # Đặt lại state về 'readonly' để khóa

    # Nút để thêm sản phẩm
    add_button = tk.Button(form_frame, text="Thêm", command=lambda: add_product(), bg="#2196F3", fg="white")
    add_button.grid(row=idx + 3, column=0, sticky="ew")

    # Button to delete products
    delete_button = tk.Button(form_frame, text="Xoá", command=delete_product, state="disabled", bg="#FF9800",
                              fg="white")
    delete_button.grid(row=idx + 3, column=1, sticky="ew")

    # Treeview để hiển thị danh sách sản phẩm
    tree = ttk.Treeview(form_frame, columns=("product_name", "price", "quantity"), show="headings", name=col_name)
    tree.bind("<<TreeviewSelect>>", on_tree_select)

    # Thiết lập tiêu đề cho các cột
    tree.heading("product_name", text="Tên")
    tree.heading("price", text="Giá")
    tree.heading("quantity", text="Số lượng")

    # Thiết lập cột (anchor để căn lề và width để thiết lập chiều rộng)
    tree.column(column="product_name", anchor="w", width=120)  # Left align Name, adjust width
    tree.column(column="price", anchor="e", width=70)  # Left align Name, adjust width
    tree.column(column="quantity", anchor="e", width=100)  # Center align Quantity, adjust width

    tree.grid(row=idx + 4, column=0, columnspan=2, sticky="ew")
    if data_details:
        for detail in data_details:
            tree.insert('', 'end', iid=detail[0], values=(detail[2], detail[3], detail[4]))
    total_label = tk.Label(form_frame, text="Tổng tiền:",
                           font=("Helvetica", 12),
                           foreground="#000000",
                           padx=10, pady=10)
    total_label.grid(row=idx + 5, column=0, sticky="ew")

    # Tạo StringVar để lưu giá trị của Entry
    entry_total_value = tk.StringVar()
    entry_total = tk.Entry(form_frame, textvariable=entry_total_value, width=35, name="total_price", state="readonly")

    if total_price and total_price != "" and float(total_price) > 0:
        update_entry_value(total_price)
    else:
        update_entry_value(0)
    entry_total.grid(row=idx + 5, column=1, sticky="ew")

    widgets[col_name] = tree
    widgets["total_price"] = entry_total


# Tạo frame chứa các phần tử của dialog add, update
def create_frame_in_dialog(controller, dialog_frame, width, parent_frame, dict_cols, name, display_name,
                           on_success, data=[], is_add=True):
    # Tạo frame chứa các phần tử của form
    form_frame = ttk.Frame(dialog_frame)
    form_frame.pack(padx=10, pady=10, fill="both", expand=True)
    # Tạo style cho buttons
    styles.create_button_style()
    create_widgets_in_dialog(form_frame, dict_cols, is_add, controller, dialog_frame,
                             name, display_name, on_success, data)

    # Cập nhật lại kích thước của dialog
    dialog_frame.update_idletasks()  # Cập nhật để có kích thước chính xác sau khi thêm phần tử

    # Cài đặt cấu hình để cho phép tự mở rộng chiều cao theo nội dung
    dialog_frame.geometry(f"{dialog_frame.winfo_reqwidth()}x{dialog_frame.winfo_reqheight()}")
    set_centered_geometry(parent_frame, dialog_frame)

    return form_frame


def create_btn_save_cancel(form_frame, dict_cols, num_widget_add, on_save, on_cancel):
    # Tạo nút "Save" và "Cancel"
    for i, (text, command) in enumerate([
        ("Save", lambda: on_save()),
        ("Cancel", lambda: on_cancel())
    ]):
        btn = ttk.Button(form_frame, text=text, command=command, style=f"{text}.TButton")
        btn.grid(row=len(dict_cols["columns_name"]) + num_widget_add + 1, column=i, pady=4, sticky="ew")


# Hàm để kiểm tra và đặt giá trị mặc định dựa trên id
def set_combobox_selected_by_id_prefix(data, id_prefix):
    for idx, (item) in enumerate(data):
        if item.startswith(id_prefix):  # Kiểm tra chuỗi bắt đầu bằng id_prefix
            return item
    print(f"Không tìm thấy mục bắt đầu với {id_prefix}")


def create_widgets_in_dialog(form_frame, dict_cols, is_add, controller, dialog_frame,
                             name, display_name, on_success, data):
    widgets = {}  # Dictionary to hold label-entry pairs

    num_widget_add = 0  # Tạo các trường nhập liệu dựa trên fields

    for idx, (col_name) in enumerate(dict_cols["columns_name"]):
        index = num_widget_add + idx
        # Tạo widget tương ứng
        match str(dict_cols["widget_type"][idx]):
            case "Combobox":
                values = dict_cols["data_init"][col_name]["combobox_values"]
                # selected_data = tk.StringVar()
                combobox = ttk.Combobox(form_frame, values=values, width=35, name=col_name,
                                        state="readonly")
                if not is_add:
                    dt = set_combobox_selected_by_id_prefix(values, data["values"][idx])
                    combobox.set(dt)
                widgets[col_name] = combobox
            case "Entry":
                # Tạo Entry với padding để tăng chiều cao
                entry = tk.Entry(form_frame, width=35, name=col_name)
                if dict_cols["validates"][idx] == "password":
                    entry.config(show='*')
                if not is_add:
                    entry.insert(tk.END, data["values"][idx])  # Set the default text to data["values"][idx]
                widgets[col_name] = entry
            case "Text":
                text = tk.Text(form_frame, width=35, height=6, name=col_name)
                if not is_add:
                    text.insert('1.0', data["values"][idx])
                    widgets[col_name] = text
            case "Product_list":
                product_values = dict_cols["data_init"][col_name]["combobox_values"]
                if not is_add:
                    create_entry_add_list_product(form_frame, product_values, idx, col_name, widgets, data["values"][0],
                                                  data["values"][3])
                else:
                    create_entry_add_list_product(form_frame, product_values, idx, col_name, widgets, "", 0)
                num_widget_add = 5
            # các loại widget khác nếu có

        # Trường hợp add thì không hiển thị item ID do id được generate tự động khi add
        # Trường hợp data date thì không hiển thị do date sẽ được add date.now
        if not (is_add and idx == 0) and str(dict_cols["widget_type"][idx]) != "Date" and str(
                dict_cols["widget_type"][idx]) != "Product_list":
            label = ttk.Label(form_frame, text=f"{dict_cols["columns_name_display"][idx]}:")
            label.grid(row=index, column=0, sticky="w")
            widgets[col_name].grid(row=index, column=1, sticky="ew")

    def on_save():
        """
        Lưu dữ liệu khi nhấn nút "Save".
        """
        data = get_widget_values(widgets)
        if is_add:
            controller.insert(name, data)  # Thêm dữ liệu vào cơ sở dữ liệu
        else:
            controller.update(name, data)  # Update dữ liệu vào cơ sở dữ liệu
        dialog_frame.destroy()  # Đóng dialog
        messagebox.showinfo("Success", f"{display_name} added successfully!")  # Thông báo thành công
        if on_success:
            on_success()  # Cập nhật Treeview

    def on_cancel():
        dialog_frame.destroy()

    # Tạo nút "Save" và "Cancel"
    create_btn_save_cancel(form_frame, dict_cols, num_widget_add, on_save, on_cancel)
    return widgets


def create_frame_treeview_details(controller, frame_parent, name, display_name, dict_cols, rows):
    """
        Hàm tạo nội dung cho khung (frame) với bảng và các nút hành động.
        :param controller: Bộ điều khiển để lấy dữ liệu và thực hiện các thao tác.
        :param frame_parent: Frame gốc để đặt khung mới vào.
        :param display_name: Tên của khung nội dung (vd: 'category', 'product', ...).
        :param dict_cols: Từ điển các cột của bảng (vd: {"columns_name_display": ["Mã", "Tên loại sản phẩm"], ...}).
        :param rows: Dữ liệu ban đầu cho Treeview.
        :return: Trả về đối tượng frame đã tạo.
    """
    # Tạo frame chứa toàn bộ
    frame_root = tk.Toplevel(frame_parent, name=f"fr_{name}", bg="#f0f0f0")

    # Tạo frame phụ chứa Treeview
    frame_treeview = ttk.Frame(frame_root, name=f"fr_tv_details_{name}")
    frame_treeview.pack(fill=tk.BOTH, expand=True)  # Đảm bảo nó mở rộng full

    # Tạo treeview
    tree = create_tree_view(frame_treeview, dict_cols, rows)


def create_frame_dashboard(frame_parent):
    # Tạo frame dashboard
    frame_dashboard = tk.Frame(frame_parent, padx=20, pady=10, bg="#f0f0f0")
    frame_dashboard.pack(fill="both", expand=True)

    # Cấu hình mở rộng cột để căn giữa nội dung
    frame_dashboard.columnconfigure(0, weight=1)

    # Tạo tiêu đề
    lbl_title = tk.Label(frame_dashboard, text="Bảng Thống Kê Doanh Thu", font=("Arial", 18, "bold"), bg="#f0f0f0")
    lbl_title.grid(row=0, column=0, pady=10, sticky="ew")

    # Dữ liệu doanh thu giả theo tháng
    data = {
        "months": ["Tháng 1", "Tháng 2", "Tháng 3", "Tháng 4", "Tháng 5", "Tháng 6"],
        "revenues": [10000000, 15000000, 12000000, 18000000, 20000000, 25000000]
    }

    # Tạo vùng biểu đồ doanh thu
    fig, ax = plt.subplots(figsize=(6, 4))
    canvas = FigureCanvasTkAgg(fig, master=frame_dashboard)
    canvas.get_tk_widget().grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # Vẽ biểu đồ doanh thu theo tháng
    months = data["months"]
    revenues = data["revenues"]
    ax.bar(months, revenues, color="blue")
    ax.set_title("Doanh thu theo tháng")
    ax.set_xlabel("Tháng")
    ax.set_ylabel("Doanh thu (VND)")

    # Cập nhật biểu đồ
    canvas.draw()

    # Tính tổng doanh thu
    total_revenue = sum(revenues)

    # Hiển thị tổng doanh thu
    lbl_total = tk.Label(frame_dashboard, text=f"Tổng Doanh Thu: {total_revenue:,} VND", font=("Arial", 14),
                         bg="#f0f0f0")
    lbl_total.grid(row=2, column=0, columnspan=2, pady=10)

    return frame_dashboard
