import tkinter as tk
from tkinter import ttk, messagebox


# Tạo hàm chứa add list product cho order
def create_entry_add_list_product(form_frame, product_values, idx, product_list):
    # Label for Product
    product_label = tk.Label(form_frame, text="Product:")
    product_label.grid(row=idx + 1, column=0, sticky="ew")

    # Combobox để nhập tên sản phẩm
    selected_data = tk.StringVar()
    product_combobox = ttk.Combobox(form_frame, textvariable=selected_data, values=product_values, width=35,
                                    state="readonly")
    product_combobox.grid(row=idx + 1, column=1, sticky="ew")

    # Label for Quantity
    quantity_label = tk.Label(form_frame, text="Quantity:")
    quantity_label.grid(row=idx + 2, column=0, sticky="ew")
    quantity_entry = tk.Entry(form_frame)
    quantity_entry.grid(row=idx + 2, column=1, sticky="ew")

    # Treeview to display added products
    tree = ttk.Treeview(form_frame, columns=("Id", "Name", "Quantity"), show="headings")

    # Set up Treeview columns and headers
    tree.heading("Id", text="Id")
    tree.heading("Name", text="Name")
    tree.heading("Quantity", text="Quantity")
    tree.column("Id", anchor="center", width=50)
    tree.column("Name", anchor="w", width=150)
    tree.column("Quantity", anchor="center", width=100)

    tree.grid(row=idx + 4, column=0, columnspan=2, sticky="ew")

    def add_product():
        """Xử lý khi nhấn nút Add."""
        # Get product id and name from the combobox
        product_id = product_combobox.get().split("-")[0].strip()
        product_name = product_combobox.get().split("-")[1].strip()
        quantity = quantity_entry.get().strip()

        if not product_id or not quantity:
            messagebox.showwarning("Input Error", "Both product name and quantity are required.")
            return

        try:
            quantity = int(quantity)
        except ValueError:
            messagebox.showwarning("Input Error", "Quantity must be a number.")
            return

        # Add product data to the passed product_list
        product_list.append((product_id, product_name, quantity))

        # Add product to Treeview
        tree.insert("", "end", values=(product_id, product_name, quantity))

        # Clear input fields
        product_combobox.set('')
        quantity_entry.delete(0, tk.END)

    def save_products():
        """Xử lý khi nhấn nút Save."""
        # Get all items from Treeview
        products_in_tree = []
        for item in tree.get_children():
            product_data = tree.item(item, 'values')
            products_in_tree.append(product_data)

        if not products_in_tree:
            messagebox.showwarning("Save Error", "No products to save.")
        else:
            # Show saved data (You can handle the data however you need here)
            print("Saved Products:", products_in_tree)
            messagebox.showinfo("Success", "Products saved successfully!")
            # Optionally, return or process this data further

    # Button to add product
    add_button = tk.Button(form_frame, text="Add", command=add_product)
    add_button.grid(row=idx + 3, column=0, columnspan=1, sticky="ew")

    # Button to save products
    save_button = tk.Button(form_frame, text="Save", command=save_products)
    save_button.grid(row=idx + 3, column=1, columnspan=1, sticky="ew")


# Sample usage of the function
def main():
    root = tk.Tk()
    root.title("Order Form")

    # Frame for form
    form_frame = tk.Frame(root)
    form_frame.pack(padx=10, pady=10)

    # Sample product data to show in combobox
    product_values = ["1 - Product A", "2 - Product B", "3 - Product C"]

    # Initialize product list data (this will be updated inside the function)
    product_list_data = []

    # Call the function to create product input form
    create_entry_add_list_product(form_frame, product_values, 0, product_list_data)

    root.mainloop()


# Run the example
if __name__ == "__main__":
    main()
