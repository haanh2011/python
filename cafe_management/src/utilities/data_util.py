import pandas as pd

def read_data_sheet(file_path, sheet_name):
  """
  Đọc dữ liệu từ sheet "Product" trong file Excel và trả về một DataFrame.

  Args:
    file_path: Đường dẫn đến file Excel.
    sheet_name: Tên sheet cần đọc.

  Returns:
    Một DataFrame chứa dữ liệu từ sheet "Product".
  """

  # Đọc dữ liệu từ file Excel vào DataFrame
  df = pd.read_excel(file_path, sheet_name=sheet_name)

  return df
