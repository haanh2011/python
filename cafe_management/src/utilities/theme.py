from customtkinter import *
from pathlib import Path

def setTheme(themeType = 'main'):
    # Lấy đường dẫn đến thư mục hiện tại của file đang chạy
    current_dir = Path(__file__).parent.resolve()
    
    # Lấy đường dẫn đến thư mục theme cùng cấp với thư mục hiện tại
    theme_dir = current_dir.parent / 'themes'

    mainThemeDir = theme_dir / f'{themeType}.json'
    set_default_color_theme(mainThemeDir)