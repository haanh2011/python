import re


def validate_integer_input(new_value):
    # Allow empty input, or a string that represents a valid integer
    return new_value.isdigit() or (not new_value.startswith('-') and new_value[1:].isdigit()) or new_value == ""

def validate_float_input(new_value):
    # Allow empty input, or a string that represents a valid float
    if new_value == "":
        return True  # Allow empty input
    try:
        float(new_value)  # Try to convert to float
        return True  # If successful, it's a valid float
    except ValueError:
        return False  # If it raises ValueError, it's not a valid float

def validate_length_input(new_value):
    # Set the maximum length
    max_length = 10
    if len(new_value) <= max_length:
        return True  # Accept input if it's within the limit
    else:
        return False  # Reject input if it's too long

def validate_phone_input(new_value):
    """Chỉ cho phép chữ số, đảm bảo chữ số đầu tiên là '0' và giới hạn độ dài ở mức 10 chữ số. (ví dụ: 0999999999)."""
    if new_value == "":  # Cho phép nhập dữ liệu rỗng
        return True

    # Kiểm tra xem ký tự đầu tiên có phải là '0' và các ký tự còn lại là chữ số, tối đa 10 ký tự
    if new_value[0] == "0" and new_value.isdigit() and len(new_value) <= 10:
        return True

    return False  # Từ chối bất kỳ đầu vào nào không bắt đầu bằng '0' hoặc vượt quá 10 chữ số
