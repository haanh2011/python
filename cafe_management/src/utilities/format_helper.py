import locale


class FormatHelper:
    """Hỗ trợ định dạng số và chuỗi cho ứng dụng."""

    @staticmethod
    def format_to_vnd(number):
        """
        Định dạng số theo tiền VNĐ.

        :param number: Số cần định dạng (có thể là int, float, hoặc decimal).
        :return: Chuỗi định dạng tiền VNĐ.
        """
        # Thiết lập định dạng cho tiền tệ Việt Nam
        locale.setlocale(locale.LC_ALL, "vi_VN.UTF-8")  # Cài đặt locale cho Việt Nam
        formatted_number = locale.format_string(
            "%d", number, grouping=True
        )  # Định dạng số với dấu phẩy
        return f"{formatted_number} đ"

    @staticmethod
    def to_title_case(input_string):
        """
        Chuyển đổi chuỗi thành chữ cái đầu tiên của mỗi từ viết hoa.

        :param input_string: Chuỗi đầu vào.
        :return: Chuỗi đã chuyển đổi.
        """
        return input_string.title()