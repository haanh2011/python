from datetime import datetime
import re

def validate_date(value, format):
    """Validates the entered date against the specified format.

    Args:
        value: The entered date value.
        format: The desired format for the date input.

    Returns:
        True if the date is valid, False otherwise.
    """

    try:
        datetime.strptime(value, format)
        return True
    except ValueError:
        return False


def validate_price(value, isNone=False):
    if isNone and value == "":
        return True  # Cho phép nhập rỗng
    return re.match(r"^\d{1,4}\.\d{2}0,00VND", value) is not None
