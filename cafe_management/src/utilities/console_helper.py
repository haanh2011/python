# import datetime
# from cafe_management.src.localizeds import *
# from cafe_management.src.utilities import FormatHelper

class ConsoleHelper:
    @staticmethod
    def get_int_input(prompt):
        """
        Prompts the user to input an integer. Repeats until a valid integer >= 0 is provided.
        """
        # while True:
        #     try:
        #         input_value = int(input(prompt))
        #         if input_value >= 0:
        #             return input_value
        #         else:
        #             print("Please enter an integer greater than or equal to 0.")
        #     except ValueError:
        #         print("Invalid input. Please enter an integer.")

    @staticmethod
    def get_double_input(prompt):
        """
        Prompts the user to input a double (float). Repeats until a valid float >= 0 is provided.
        """
        # while True:
        #     try:
        #         input_value = float(input(prompt))
        #         if input_value >= 0:
        #             return input_value
        #         else:
        #             print("Please enter a number greater than or equal to 0.")
        #     except ValueError:
        #         print("Invalid input. Please enter a valid number.")

    @staticmethod
    def get_datetime_input(prompt):
        """
        Prompts the user to input a date in the format defined by get_localized_string(FORMAT_DATE).
        Repeats until a valid date is provided.
        """
        # while True:
        #     try:
        #         input_value = input(prompt)
        #         date = datetime.datetime.strptime(
        #             input_value, get_localized_string(FORMAT_DATE)
        #         )
        #         return date
        #     except ValueError:
        #         print(
        #             f"Invalid date format. Please enter the date in the format {get_localized_string(FORMAT_DATE)}."
        #         )

    @staticmethod
    def get_string_input(prompt):
        """
        Prompts the user to input a non-empty string. Repeats until a valid string is provided.
        """
        # while True:
        #     input_value = input(prompt).strip()
        #     if input_value:
        #         return input_value
        #     else:
        #         print("Input cannot be empty. Please try again.")

    @staticmethod
    def get_yn_input(prompt):
        """
        Prompts the user to input either 'Y' or 'N'. Repeats until a valid input is provided.
        """
        # while True:
        #     input_value = input(prompt).strip().upper()
        #     if input_value in ["Y", "N"]:
        #         return input_value
        #     else:
        #         print("Please enter 'Y' or 'N'.")

    @staticmethod
    def print_title_menu(title, is_clear_console=True):
        """
        Prints a formatted title for a menu. Optionally clears the console.
        """
        # if is_clear_console:
        #     ConsoleHelper.clear_console()
        # print(f"===== {title} =====")

    @staticmethod
    def clear_console():
        """
        Clears the console.
        """
        print("\033c", end="")

    @staticmethod
    def print_header_table(title):
        """
        Prints a table header based on the provided title.
        """
        # ConsoleHelper.print_horizontal_line_of_table(title)
        # if title == get_localized_string(CATEGORY:
        #     print(f"| {'ID':-5} | {'Tên loại sản phẩm':-25} |")
        # elif title == get_localized_string(PRODUCT:
        #     print(f"| {'ID':-5} | {'Tên sản phẩm':-25} | {'Giá':-15} |")
        # elif title == get_localized_string(ORDER:
        #     print(
        #         f"| {'STT':-5} | {'ID':-5} | {'Tên sản phẩm':-25} | {'Giá':15} | {'Số lượng':10} | {'Thành tiền':-15} |"
        #     )
        # elif title == get_localized_string(CUSTOMER:
        #     print(
        #         f"| {'Mã':-5} | {'Tên':-25} | {'Ngày sinh':-10} | {'SĐT':-10} | {'Email':-25} | {'Điểm':10} |"
        #     )
        # elif title == get_localized_string(INVOICE:
        #     print(f"| {'Mã':-5} | {'Mã đơn hàng':-15} | {'Ngày lập hoá đơn':-20} |")
        # ConsoleHelper.print_horizontal_line_of_table(title)

    @staticmethod
    def print_menu_details(name):
        """
        Prints menu details based on the name parameter.
        """
        # ConsoleHelper.print_title_menu(
        #     f"{get_localized_string(MANAGE_X.format(name).upper()}"
        # )
        # print(
        #     f"1. {FormatHelper.to_title_case(get_localized_string(DISPLAY_LIST_X.format(name))}"
        # )
        # print(f"2. {FormatHelper.to_title_case(get_localized_string(ADD_X.format(name))}")
        # print(f"3. {FormatHelper.to_title_case(get_localized_string(UPDATE_X.format(name))}")
        # print(f"4. {FormatHelper.to_title_case(get_localized_string(DELETE_X.format(name))}")
        # print(f"0. {get_localized_string(BACK}")

    @staticmethod
    def print_horizontal_line_of_table(title):
        """
        Prints a horizontal line based on the table's title.
        """
        # if title == get_localized_string(CATEGORY:
        #     print("-" * 37)
        # elif title == get_localized_string(PRODUCT:
        #     print("-" * 50)
        # elif title == get_localized_string(ORDER:
        #     print("-" * 94)
        # elif title == get_localized_string(CUSTOMER:
        #     print("-" * 104)
        # elif title == get_localized_string(INVOICE:
        #     print("-" * 45)
