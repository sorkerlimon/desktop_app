# File: main_application.py
from PyQt6.QtWidgets import QMainWindow, QStackedWidget
from PyQt6.QtGui import QIcon
from login_window import LoginWindow
from main_window import MainWindow
from PyQt6.QtWidgets import QApplication
import sys

class MainApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.login_window = LoginWindow(self.switch_to_main)
        self.main_window = MainWindow(self.switch_to_login)

        self.stacked_widget.addWidget(self.login_window)
        self.stacked_widget.addWidget(self.main_window)

        self.setWindowTitle('TechnoBD Time Tracker')
        self.setGeometry(100, 100, 400, 600)
        self.setFixedSize(400, 600)
        self.setWindowIcon(QIcon('code.png')) 

    def switch_to_main(self):
        self.stacked_widget.setCurrentIndex(1)

    def switch_to_login(self):
        self.stacked_widget.setCurrentIndex(0)  # Switch back to the login window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApplication()
    ex.show()
    sys.exit(app.exec())
