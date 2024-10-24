import tkinter as tk
from tkinter import messagebox

def validate_integer_input(new_value):
    """Validate integer input."""
    if new_value == "":
        return True  # Allow empty input
    return new_value.isdigit() or (new_value.startswith('-') and new_value[1:].isdigit())

def validate_float_input(new_value):
    """Validate float input."""
    if new_value == "":
        return True  # Allow empty input
    try:
        float(new_value)  # Try to convert to float
        return True
    except ValueError:
        return False  # Not a valid float

def validate_length_input(new_value):
    """Validate input length."""
    max_length = 10
    return len(new_value) <= max_length  # Accept input if within the limit

# Function to update validation message
def update_validation_message(entry, message_label, validation_function):
    """Update validation message based on input."""
    new_value = entry.get()
    if validation_function(new_value):
        message_label.config(text="", fg="green")  # Clear message if valid
    else:
        message_label.config(text="Invalid input", fg="red")  # Show error message

# Main application code
root = tk.Tk()
root.title("Input Validation Example")

# Register validation functions
validate_integer_cmd = root.register(validate_integer_input)
validate_float_cmd = root.register(validate_float_input)
validate_length_cmd = root.register(validate_length_input)

# Create Entry for Integer Input
int_frame = tk.Frame(root)
int_frame.pack(padx=20, pady=5)
int_entry = tk.Entry(int_frame, validate="key", validatecommand=(validate_integer_cmd, "%P"))
int_entry.pack(side="top")
int_message = tk.Label(int_frame, text="")
int_message.pack(side="bottom")
int_entry.bind("<KeyRelease>", lambda e: update_validation_message(int_entry, int_message, validate_integer_input))

# Create Entry for Float Input
float_frame = tk.Frame(root)
float_frame.pack(padx=20, pady=5)
float_entry = tk.Entry(float_frame, validate="key", validatecommand=(validate_float_cmd, "%P"))
float_entry.pack(side="top")
float_message = tk.Label(float_frame, text="")
float_message.pack(side="bottom")
float_entry.bind("<KeyRelease>", lambda e: update_validation_message(float_entry, float_message, validate_float_input))

# Create Entry for Length Input
length_frame = tk.Frame(root)
length_frame.pack(padx=20, pady=5)
length_entry = tk.Entry(length_frame, validate="key", validatecommand=(validate_length_cmd, "%P"))
length_entry.pack(side="top")
length_message = tk.Label(length_frame, text="")
length_message.pack(side="bottom")
length_entry.bind("<KeyRelease>", lambda e: update_validation_message(length_entry, length_message, validate_length_input))

# Button to show entered values
def show_values():
    int_value = int_entry.get()
    float_value = float_entry.get()
    length_value = length_entry.get()

    # Check if all entries are valid before showing values
    if (validate_integer_input(int_value) and
        validate_float_input(float_value) and
        validate_length_input(length_value)):
        messagebox.showinfo("Entered Values", f"Integer: {int_value}\nFloat: {float_value}\nLength: {length_value}")
    else:
        messagebox.showerror("Error", "Please correct the invalid inputs before submitting.")

submit_button = tk.Button(root, text="Submit", command=show_values)
submit_button.pack(pady=10)

root.mainloop()
