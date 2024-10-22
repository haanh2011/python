def convert_to_int(value):
    """Converts a value to an integer, handling empty strings, None, and other falsy values.

    Args:
        value (str or int): The value to be converted.

    Returns:
        int: The converted integer value or 0 if the value is falsy.
    """

    if not value:
        return 0
    else:
        return int(value)