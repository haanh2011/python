import sys
import os

# Thêm thư mục src vào sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from pages import loadingPage

def main():
    loadingPage.render()

if __name__ == "__main__":
    main()