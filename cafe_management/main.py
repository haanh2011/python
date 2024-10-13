from src.utilities import run_with_custom_path

def main():
    run_with_custom_path("src/themes/buildThemeToJson.py") #file build custom theme
    # Chạy loadingPage.py với PYTHONPATH
    run_with_custom_path("src/views/managementPage.py")

if __name__ == "__main__":
    main()