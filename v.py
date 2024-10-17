import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QCheckBox
)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setFixedSize(300, 550)

        # Main layout
        layout = QVBoxLayout()

        # Background color and rounded corners for window
        self.setStyleSheet("""
            background-color: #E0F7FA;
            border-radius: 20px;
        """)

        # Top banner (simulating the blue wave)
        banner_label = QLabel(self)
        banner_label.setFixedHeight(150)
        banner_label.setStyleSheet("""
            background-color: #0099FF;
            border-top-left-radius: 20px;
            border-top-right-radius: 20px;
        """)
        layout.addWidget(banner_label)

        # Title and description
        title_label = QLabel("Hello,\nLogin to Your Account", self)
        title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: white; margin-top: -100px;")
        layout.addWidget(title_label)

        # Username input field
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        self.username_input.setFixedHeight(40)
        self.username_input.setStyleSheet("""
            background-color: #F5FFFA;
            border: 2px solid #D0D0D0;
            border-radius: 20px;
            padding-left: 15px;
        """)
        layout.addWidget(self.username_input)

        # Password input field
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setFixedHeight(40)
        self.password_input.setStyleSheet("""
            background-color: #F5FFFA;
            border: 2px solid #D0D0D0;
            border-radius: 20px;
            padding-left: 15px;
        """)
        layout.addWidget(self.password_input)

        # Remember me checkbox
        self.remember_me = QCheckBox("I accept terms and policy", self)
        layout.addWidget(self.remember_me)

        # Login button
        login_button = QPushButton("LOGIN", self)
        login_button.setStyleSheet("""
            background-color: #0099FF;
            color: white;
            font-size: 14px;
            border-radius: 20px;
            padding: 10px;
        """)
        login_button.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        layout.addWidget(login_button)

        # Set layout
        self.setLayout(layout)

# Run the application
app = QApplication(sys.argv)
window = LoginWindow()
window.show()
sys.exit(app.exec())
