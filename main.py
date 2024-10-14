import sys
from PyQt6.QtWidgets import QApplication
from main_application import MainApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApplication()
    ex.show()
    sys.exit(app.exec())
