import customtkinter

class CategoryManagement(customtkinter.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title = 'Category Management'
        self.geometry("700x600")

        # Nút để quay lại cửa sổ chính
        btn_back = customtkinter.CTkButton(self, text="Back", command=self.back_to_main)
        btn_back.pack(pady=20)

    def back_to_main(self):
        # Đóng cửa sổ con và hiển thị lại cửa sổ chính
        self.destroy()
        self.master.deiconify()