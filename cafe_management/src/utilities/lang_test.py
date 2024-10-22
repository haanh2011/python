import tkinter as tk
from tkinter import ttk
# from languages import all_languages

def create_header(frame_parent):
    header_frame = tk.Frame(frame_parent)
    header_frame.pack(side="top", fill="x")
    #
    # languages_list = []  # Empty list to store titles
    #
    # # Depending on the structure inside 'all_languages'
    # if isinstance(all_languages, dict):  # Assuming it's a dictionary
    #     for code, language_data in all_languages.items():
    #         languages_list.append(language_data["title_languages"])
    # else:
    #     # Handle other structures (list, etc.) if needed
    #     pass
    # # Create a language combobox
    # language_var = tk.StringVar()
    # language_combobox = ttk.Combobox(header_frame, textvariable=language_var, values=languages_list, state="readonly")
    # language_combobox.pack(side="right", padx=20, pady=10)
    #
    # # Handle language selection
    # def language_selected(event=None):
    #     selected_language = language_var.get()
    #     update_ui(selected_language)
    #
    # language_combobox.bind("<<ComboboxSelected>>", language_selected)
    #
    # # ... (other header elements)

def update_ui(language):
    # Get the dictionary for the selected language
    selected_language_dict = next((lang for lang in all_languages.values() if lang["title_languages"] == language), None)

    # Update all elements in the root window using the selected language dictionary
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(text=selected_language_dict.get(widget.config("text")[0], widget.config("text")[0]))
        elif isinstance(widget, tk.Button):
            widget.config(text=selected_language_dict.get(widget.config("text")[0], widget.config("text")[0]))
        # Add more conditions for other widget types if needed

def create_main_frame(root):
    main_frame = tk.Frame(root)
    main_frame.pack(side="top", fill="both", expand=True)

    # Create labels, buttons, and other elements here
    label1 = tk.Label(main_frame, text="Welcome")
    label1.pack()
    button1 = tk.Button(main_frame, text="Click me")
    button1.pack()

    # ... (other elements)

# Main function
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Language Selection")

    create_header(root)
    create_main_frame(root)

    root.mainloop()
