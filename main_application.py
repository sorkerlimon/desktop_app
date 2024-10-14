# File: main_application.py
from PyQt6.QtWidgets import QMainWindow, QStackedWidget
from PyQt6.QtGui import QIcon
from login_window import LoginWindow
from main_window import MainWindow

class MainApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.login_window = LoginWindow(self.switch_to_main)
        self.main_window = MainWindow()

        self.stacked_widget.addWidget(self.login_window)
        self.stacked_widget.addWidget(self.main_window)

        self.setWindowTitle('TechnoBD Time Tracker')
        self.setGeometry(100, 100, 400, 600)
        self.setFixedSize(400, 600)


        # Set window icon (logo)
        self.setWindowIcon(QIcon('code.png'))  # Update with the path to your logo file

    def switch_to_main(self):
        self.stacked_widget.setCurrentIndex(1)




