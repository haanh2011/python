import os
import platform

def run_with_custom_path(script_path, custom_path = 'src'):
    # Xác định hệ điều hành
    current_os = platform.system()
    
    # Tạo lệnh để chạy script
    if current_os == "Windows":
        # Dùng set PYTHONPATH cho Windows
        command = f"set PYTHONPATH={custom_path} && python {script_path}"
    else:
        # Dùng PYTHONPATH cho Linux và macOS
        command = f"PYTHONPATH={custom_path} python {script_path}"
    
    # Chạy lệnh
    os.system(command)