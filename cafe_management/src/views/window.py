import sys, os
import tkinter as tk
from tkinter import ttk

from styles import *

current_dir = os.path.dirname(os.path.abspath(__file__))
utilities_dir = os.path.join(current_dir, '../utilities')
sys.path.append(utilities_dir)
import validate

from src.helper import button_image

from dialogs import add_dialog, update_dialog, delete_dialog


def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    root.geometry(f"{width}x{height}+{x}+{y}")


def create_root_window(width, height):
    root = tk.Tk()
    root.title("Ứng dụng Quản Lý Quán Cà Phê")
    center_window(root, width, height)
    return root


def create_header(frame_parent):
    header_frame = tk.Frame(frame_parent, bg=BACKGROUND_COLOR)
    header_frame.pack(side="top", fill="x")
    header_logo_label = tk.Label(header_frame, text="QUẢN LÝ QUÁN CÀ PHÊ", font=("Arial", 16, "bold"),
                                 fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR, anchor="center", justify="center")
    header_logo_label.pack(side="left", padx=20, pady=10)
    #
    # # Create a language combobox
    # language_var = tk.StringVar()
    # language_combobox = ttk.Combobox(header_frame, textvariable=language_var, values=["English", "Vietnamese"],
    #                                  state="readonly")
    # language_combobox.pack(side="right", padx=20, pady=10)
    #
    # # Handle language selection (optional)
    # def language_selected(event=None):
    #     selected_language = language_var.get()
    #     # Perform language-specific actions here (e.g., update labels, change translations)


def create_frame(frame_parent, name):
    return tk.Frame(frame_parent, name=name)


def create_dialog(frame_parent, title, width, height):
    # Tạo dialog và căn giữa nó trên màn hình
    dialog = tk.Toplevel(frame_parent)
    dialog.grab_set()  # Đặt dialog ở chế độ modal
    dialog.title(title)
    set_width_height_top_level(dialog, width, height)
    return dialog


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


def create_frame_actions_treeview(controller, frame_parent, display_name, dict_cols, rows):
    """
        Hàm tạo nội dung cho khung (frame) với bảng và các nút hành động.
        :param frame_parent: Frame gốc để đặt khung mới vào.
        :param display_name: Tên của khung nội dung (vd: 'category', 'product', ...)
        :param dict_cols: Từ điển các cột của bảng (vd: {"widget_type": ["Entry", "Entry"],"display_name": ["Mã","Tên loại sản phẩm"],"columns_name": ["id","name"]}).
        :return: Trả về đối tượng frame đã tạo.
    """

    frame_root = tk.Frame(frame_parent, name=f"fr_{display_name}")
    frame_root.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

    # Tạo frame chứa các actions của grid
    frame_action = tk.Frame(frame_root, name=f"fr_action_{display_name}")
    frame_action.grid(row=0, column=0, sticky="sew")

    # Tạo một frame phụ để chứa treeview
    frame_treeview = ttk.Frame(frame_root, name=f"fr_tv_{display_name}")
    frame_treeview.grid(row=1, column=0, sticky="sew")

    # Tạo treeview
    tree = create_tree_view(frame_treeview, dict_cols, rows)

    for idx in range(0, len(dict_cols)):
        frame_action.grid_columnconfigure(idx, weight=1)

    def add_item():
        # Kiểm tra frame_parent
        print("add_item")
        if frame_parent is None:
            print("Error", "Parent frame is not initialized.")
            return

        add_dialog.show_dialog(controller=controller, frame_parent=frame_parent, dict_cols=dict_cols,
                               type_name=display_name)  # Gọi hàm show với frame hợp lệ

    def update_item():
        selected_item_id = tree.selection()[0]
        item_data = tree.item(selected_item_id)
        print("update_item", item_data)
        update_dialog.show_dialog(controller, frame_parent, dict_cols, item_data)

    def delete_item():
        selected_item_id = tree.selection()[0]
        print("delete_item", selected_item_id)
        delete_dialog.show_dialog(controller, frame_parent, selected_item_id)

    widgets = create_actions(frame_action=frame_action, type_name=display_name, add_item=add_item,
                             update_item=update_item,
                             delete_item=delete_item)

    # Bind the click outside event to the root window
    def on_select(event):
        # Get the selected item
        selected_item = tree.selection()[0]

        # Enable the button if an item is selected
        widgets["update_button"].configure(state=tk.NORMAL if selected_item else tk.DISABLED)
        widgets["delete_button"].configure(state=tk.NORMAL if selected_item else tk.DISABLED)

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


def create_button_menu(frame_parent, frame_to_show, label, buttons, frames):
    """
    Tạo nút menu trong frame cha và gán hành động hiển thị frame tương ứng khi nhấn.
    :param frame_parent: Frame chứa nút menu.
    :param frame_to_show: Frame cần hiển thị khi nhấn nút.
    :param label: Nhãn của nút.
    :param buttons: Danh sách các nút.
    :param frames: Danh sách các frame.
    :return: Đối tượng nút đã tạo.
    """
    btn = tk.Button(frame_parent, text=label, command=lambda: show_frame(frame_to_show, frames, buttons, btn),
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


def create_tree_view(frame_treeview, dict_cols, rows):
    """
    Tạo Treeview với số lượng cột không xác định.
    :param frame_treeview: Frame cha chứa Treeview.
    :param dict_cols: Dictionary chứa thông tin các cột.
    :param rows: Thông tin data hiển thị trong treeview.
    """
    configure_treeview_style()  # Gọi hàm để cấu hình style

    # Tạo Treeview và đặt nó bên dưới nút "Add"
    tr = ttk.Treeview(frame_treeview, style="Custom.Treeview", columns=dict_cols["columns_name_display"],
                      show='headings',
                      height=15)

    # Đặt tiêu đề cột, căn giữa, và đặt chiều rộng cho mỗi cột

    # Tính toán chiều rộng dựa trên số lượng cột
    total_width = 700  # Tổng chiều rộng của Treeview (có thể tùy chỉnh)
    num_columns = max(1, len(dict_cols["columns_name_display"]))  # Đảm bảo ít nhất là 1 cột
    column_width = total_width // num_columns  # Chiều rộng của mỗi cột

    # Vòng lặp để tạo các widget
    for col_name in dict_cols["columns_name_display"]:
        tr.heading(col_name, text=col_name, anchor="center")  # Căn giữa tiêu đề
        tr.column(col_name, anchor="center", width=column_width)  # Căn giữa dữ liệu và set chiều rộng

    # Thêm data từ DB vào treeview
    if rows:
        for i in rows:
            tr.insert('', 'end', iid=i[0], values=i)

    # Đặt Treeview vào sub_frame, bên dưới nút "Add"
    tr.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=5, pady=5)

    return tr


def create_actions(frame_action, type_name, add_item, update_item, delete_item):
    index_columns = 0
    if type_name == "Orders":
        index_columns = 1
        frame_order = create_frame_order(frame_action)
        frame_order.grid(row=0, column=0, sticky="nsw", padx=5, pady=5)

    # Tạo nút 'Add' và đặt nó ở phía trên, bên phải của sub_frame
    add_button = button_image.create_image_button(
        frame_action, "add_btn", "Thêm", "images/add.png",
        command=lambda: add_item(),
        tooltip_text="Add Item"
    )
    add_button.grid(row=0, column=index_columns + 1, sticky='we', padx=5, pady=5)  # Đặt nút ở góc trên bên phải

    update_button = button_image.create_image_button(
        frame_action,
        "add_btn",
        "Sửa",
        "images/add.png",
        command=lambda: update_item(),
        tooltip_text="Update Item",
        state=tk.DISABLED
    )
    update_button.grid(row=0, column=index_columns + 2, sticky='we', padx=5, pady=5)  # Đặt nút ở góc trên bên phải
    delete_button = button_image.create_image_button(
        frame_action,
        "add_btn",
        "Xoá",
        "images/add.png",
        command=lambda: delete_item(),
        tooltip_text="Delete Item",
        state=tk.DISABLED
    )
    delete_button.grid(row=0, column=index_columns + 3, sticky='we', padx=5, pady=5)  # Đặt nút ở góc trên bên phải
    widgets = {"add_button": add_button, "update_button": update_button, "delete_button": delete_button}
    return widgets


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
            value = widget.get('1.0','end')
            print("value Text", value)
        elif isinstance(widget, ttk.Combobox):
            value = widget.get().split("-")[0].strip()
            print("value Combobox", value)
        elif isinstance(widget, tk.Entry):
            value = widget.get()
            print("value Entry", value)
        else:
            value = None  # Handle unsupported widget types
        print(widget.winfo_name())
        data[widget.winfo_name()] = value
    return data