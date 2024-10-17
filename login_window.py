from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, 
                             QGraphicsDropShadowEffect, QMessageBox, QHBoxLayout)
from PyQt6.QtGui import QFont, QColor, QIcon, QPixmap
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QSize

class LoginWindow(QWidget):
    def __init__(self, switch_to_main):
        super().__init__()
        self.switch_to_main = switch_to_main
        self.initUI()

    def initUI(self):
        self.setFixedSize(400, 500)  # Set fixed window size
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            QLabel#title {
                color: #2c3e50;
                font-size: 28px;
                font-weight: bold;
            }
            QLineEdit {
                padding: 10px;
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Add a spacer at the top to push content down
        main_layout.addSpacing(100)

        # Create a container widget to hold the content
        container = QWidget()
        container.setFixedSize(350, 400)
        container_layout = QVBoxLayout(container)
        container_layout.setSpacing(20)
        container_layout.setContentsMargins(20, 50, 20, 20)
        
        # Title bar with image
        title_layout = QHBoxLayout()
        logo = QLabel()
        pixmap = QPixmap("images/code.png")  # Make sure this file exists in your project directory
        logo.setPixmap(pixmap.scaled(QSize(40, 40), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        title_layout.addWidget(logo)
        
        title = QLabel("TechnoBD")
        title.setObjectName("title")
        title_layout.addWidget(title)
        title_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        container_layout.addLayout(title_layout)

        # Spacer
        container_layout.addSpacing(20)

        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")
        self.add_shadow(self.username)
        container_layout.addWidget(self.username)

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.add_shadow(self.password)
        container_layout.addWidget(self.password)

        login_btn = QPushButton("Login")
        login_btn.clicked.connect(self.login)
        login_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.add_shadow(login_btn)
        container_layout.addWidget(login_btn)

        # Add stretch to push everything to the top within the container
        container_layout.addStretch()

        # Center the container horizontally in the main layout
        main_layout.addWidget(container, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Add another spacer at the bottom for balance
        main_layout.addSpacing(50)

    def add_shadow(self, widget):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(0, 0, 0, 60))
        widget.setGraphicsEffect(shadow)

    def login(self):
        username = self.username.text()
        password = self.password.text()

        if username == "limon" and password == "limon":
            print("Login successful!")
            self.animate_login()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def animate_login(self):
        self.anim = QPropertyAnimation(self, b"windowOpacity")
        self.anim.setDuration(500)
        self.anim.setStartValue(1)
        self.anim.setEndValue(0)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.anim.finished.connect(self.switch_to_main)
        self.anim.start()

    def showEvent(self, event):
        self.animate_appearance()

    def animate_appearance(self):
        self.anim = QPropertyAnimation(self, b"windowOpacity")
        self.anim.setDuration(500)
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.anim.start()