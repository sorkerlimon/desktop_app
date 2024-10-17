from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QScrollArea, QFrame, QApplication, QMessageBox
)
from PyQt6.QtGui import QFont, QPixmap,QDesktopServices
from PyQt6.QtCore import Qt, QTimer, QTime,QUrl,QDateTime
import sys
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt,QDate
from clock_timer import ClockTimer

class ConfirmationDialog(QDialog):
    def __init__(self, message, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Confirmation")
        self.setModal(True)
        

        layout = QVBoxLayout()

        # Message Label
        message_label = QLabel(message)
        message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(message_label)

        # Button Layout
        button_layout = QHBoxLayout()

        # Yes Button
        yes_button = QPushButton("Yes")
        yes_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; border: none; border-radius: 5px;")
        yes_button.clicked.connect(self.accept)  # Accepts the dialog
        button_layout.addWidget(yes_button)

        # No Button
        no_button = QPushButton("No")
        no_button.setStyleSheet("background-color: #f44336; color: white; padding: 10px; border: none; border-radius: 5px;")
        no_button.clicked.connect(self.reject)  # Rejects the dialog
        button_layout.addWidget(no_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.setFixedSize(300, 150)  # Set a fixed size for the dialog

class MainWindow(QWidget):
    def __init__(self, logout_callback):
        super().__init__()
        self.logout_callback = logout_callback 
        self.clock_timer = ClockTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("TechnoBD Time Tracker")
        self.setFixedSize(400, 600)
        with open('styles.css', 'r') as f:
            self.setStyleSheet(f.read())

        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # Header with logo and user image
        header_layout = QHBoxLayout()
        logo_label = QLabel("Limon")
        logo_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #6E5BDE;")
        header_layout.addWidget(logo_label)
        header_layout.addStretch()

        # User image that acts as a logout button
        self.user_image = QLabel()
        self.user_image.setPixmap(QPixmap("images/logout.png").scaled(30, 30, Qt.AspectRatioMode.KeepAspectRatio))
        self.user_image.mousePressEvent = self.on_logout_click  # Connect click event to logout function
        header_layout.addWidget(self.user_image)
        layout.addLayout(header_layout)

        # Timer
        self.timer_label = QLabel("00:00:00 h")
        self.timer_label.setFont(QFont('Arial', 36, QFont.Weight.Bold))
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.timer_label)

        # Action buttons
        self.action_layout = QHBoxLayout()
        self.clock_btn = QPushButton("Clock In")
        self.break_btn = QPushButton("Take a Break")
        for btn in [self.clock_btn, self.break_btn]:
            btn.setObjectName("action")
            self.action_layout.addWidget(btn)
        layout.addLayout(self.action_layout)

        

        # Connect buttons to their respective functions

        self.clock_btn.clicked.connect(self.clock_timer.toggle_clock)
        self.break_btn.clicked.connect(self.clock_timer.toggle_break)

        # Break time left
        self.break_label = QLabel("Break time left: 30 min")
        self.break_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.break_label)

        # Fixed header for today's logs
        log_header_layout = QVBoxLayout()
        
        title_label = QLabel("Today's Logs")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; background-color: #6E5BDE; color: white; padding: 10px; border-radius: 4px;")
        log_header_layout.addWidget(title_label)

        headers_layout = QHBoxLayout()
        for header in ["Clock in", "Clock out", "Total time"]:
            label = QLabel(header)
            label.setStyleSheet("color: #FFFFFF; background-color: #4C4B6D; padding: 5px; border-radius: 4px;")
            headers_layout.addWidget(label)
        log_header_layout.addLayout(headers_layout)
        layout.addLayout(log_header_layout)

        # Add scrollable log entries
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedHeight(120)

        log_container = QWidget()
        log_layout = QVBoxLayout(log_container)
        log_layout.setSpacing(10)

        self.add_time_log_entries(log_layout, [
            ("13:57", "16:32", "3:52:27 h"),
            ("07:11", "11:03", "3:52:27 h"),
            ("08:11", "11:03", "3:52:27 h"),
            ("09:11", "11:03", "3:52:27 h"),
            ("09:11", "11:03", "3:52:27 h"),
            ("09:11", "11:03", "3:52:27 h")
        ])

        scroll_area.setWidget(log_container)
        layout.addWidget(scroll_area)

        # Bottom layout with date and Open Dashboard button
        bottom_layout = QHBoxLayout()
        
        date_label = QLabel(QDate.currentDate().toString("MMMM d, yyyy"))
        date_label.setStyleSheet("color: #777777;")
        bottom_layout.addWidget(date_label)
        
        bottom_layout.addStretch()

        def open_dashboard():
        # Replace this URL with your desired link
            url = "https://www.example.com/dashboard"
            QDesktopServices.openUrl(QUrl(url))
            
        open_dashboard_btn = QPushButton("Open Dashboard")
        # open_dashboard_btn.setStyleSheet("background-color: transparent; color: #6E5BDE;")
        open_dashboard_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent; 
                color: #6E5BDE; 
                border: none; 
                padding: 10px 20px; 
                font-size: 16px; 
                font-weight: bold; 
                border-radius: 10px; 
            }
            QPushButton:hover {
                background-color: rgba(110, 91, 222, 0.1); 
                color: #4A3C9E; 
            }
            QPushButton:pressed {
                background-color: rgba(110, 91, 222, 0.2); 
                color: #3A2E7D; 
            }
        """)

        open_dashboard_btn.clicked.connect(open_dashboard)
        bottom_layout.addWidget(open_dashboard_btn)
        
        layout.addLayout(bottom_layout)

        self.setLayout(layout)

        # Initialize timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.clock_timer.update_timer)
        self.time = QTime(0, 0, 0)
        self.is_clocked_in = False
        self.is_on_break = False
        self.break_btn.setEnabled(False)


    def add_time_log_entries(self, layout, entries):
        for entry in entries:
            entry_layout = QHBoxLayout()
            for item in entry:
                label = QLabel(item)
                label.setStyleSheet("background-color: #F2F2F2; padding: 5px; border-radius: 4px;")
                entry_layout.addWidget(label)
            layout.addLayout(entry_layout)


    def on_logout_click(self, event):
        if self.is_clocked_in:
            dialog = ConfirmationDialog("Clock out before logout?", self)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                self.clock_timer.toggle_clock() 
                self.confirm_logout()
                
        else:
            self.confirm_logout()

    def confirm_logout(self):
        dialog = ConfirmationDialog("Are you sure you want to logout?", self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.logout_callback()  