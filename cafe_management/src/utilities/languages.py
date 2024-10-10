gt = 'Module thao tác với languages'
languages = {
    "vi": {
        "FORMAT_DATE": "d/M/yyyy",
        "FORMAT_DATETIME": "d/M/yyyy hh:mm",
        "TITLE_PROJECT": "QUẢN LÝ QUÁN CÀ PHÊ",
        "MANAGE_X": "quản lý {0}",
        "CATEGORY": "Loại Sản Phẩm",
        "PRODUCT": "Sản Phẩm",
        "ORDER": "Đơn Hàng",
        "INVOICE": "Hóa Đơn",
        "CUSTOMER": "Khách Hàng",
        "TOTAL_AMOUNT": "Thành tiền"
    }
}

def get_text(language, key):
    return languages[language][key]
