import pandas as pd
import os


def read_data_sheet(sheet_name):
    '''
    Đọc sheet cụ thể từ file Excel.

    Args:
        sheet_name: Tên sheet cần đọc.

    Returns:
        df: Pandas DataFrame chứa dữ liệu từ sheet.
    '''
    try:
        # Sử dụng đường dẫn tuyệt đối
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'dataTemplate.xlsx'))

        # Đọc dữ liệu từ file Excel vào DataFrame
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        return df

    except FileNotFoundError:
        print(f"File không tồn tại: {file_path}")
        return None

    except Exception as e:
        print(f"Đã có lỗi xảy ra khi đọc file Excel: {e}")
        return None