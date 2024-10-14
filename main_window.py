from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QScrollArea, QFrame
)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt, QTimer, QTime

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("TechnoBD Time Tracker")
        self.setFixedSize(400, 600)
        self.setStyleSheet("""
            QWidget {
                background-color: #F5F6F7;
                color: #333333;
                font-family: Arial, sans-serif;
            }
            QPushButton {
                border: none;
                border-radius: 4px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton#tab {
                background-color: transparent;
                color: #777777;
            }
            QPushButton#tab:checked {
                color: #6E5BDE;
                font-weight: bold;
            }
            QPushButton#action {
                background-color: #6E5BDE;
                color: white;
            }
            QPushButton#action:disabled {
                background-color: #D3D3D3;
            }
            QLabel {
                font-size: 14px;
            }
            QScrollArea {
                border: none;
            }
            QScrollBar:vertical {
                border: none;
                background: #E0E0E0;
                width: 12px;
                margin: 0px 0px 0px 0px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical {
                background-color: #6E5BDE;
                min-height: 20px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical:hover {
                background-color: #5B4DD6;
            }
            QScrollBar::sub-line:vertical,
            QScrollBar::add-line:vertical {
                background: none;
                height: 0px;
            }
            QScrollBar::up-arrow:vertical,
            QScrollBar::down-arrow:vertical {
                background: none;
            }
        """)

        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # Header with logo and user image
        header_layout = QHBoxLayout()
        logo_label = QLabel("Limon")
        logo_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #6E5BDE;")
        header_layout.addWidget(logo_label)
        header_layout.addStretch()

        # Replace user icon with an image
        user_image = QLabel()
        user_image.setPixmap(QPixmap("code.png").scaled(30, 30, Qt.AspectRatioMode.KeepAspectRatio))  # Adjust the path
        header_layout.addWidget(user_image)
        layout.addLayout(header_layout)


        # Tab-like buttons
        tab_layout = QHBoxLayout()
        attendance_btn = QPushButton("Attendance")
        time_tracking_btn = QPushButton("Time Tracking")
        for btn in [attendance_btn, time_tracking_btn]:
            btn.setObjectName("tab")
            btn.setCheckable(True)
            tab_layout.addWidget(btn)

        attendance_btn.setChecked(True)  # Set Attendance as the initially selected button
        layout.addLayout(tab_layout)
        # Date
        date_label = QLabel(f"December 12, 2020")
        date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(date_label)

        # Timer
        self.timer_label = QLabel("00:00:00 h")
        self.timer_label.setFont(QFont('Arial', 36, QFont.Weight.Bold))
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.timer_label)

        # Action buttons
        action_layout = QHBoxLayout()
        clock_in_btn = QPushButton("Clock In")
        take_break_btn = QPushButton("Take a Break")
        for btn in [clock_in_btn, take_break_btn]:
            btn.setObjectName("action")
            action_layout.addWidget(btn)
        layout.addLayout(action_layout)

        # Break time left
        break_label = QLabel("Break time left: 30 min")
        break_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(break_label)

        # Fixed header for today's logs
        log_header_layout = QVBoxLayout()
        
        # Title
        title_label = QLabel("Today's Logs")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; background-color: #6E5BDE; color: white; padding: 10px; border-radius: 4px;")
        log_header_layout.addWidget(title_label)

        # Headers for the table
        headers_layout = QHBoxLayout()
        for header in ["Clock in", "Clock out", "Total time"]:
            label = QLabel(header)
            label.setStyleSheet("color: #FFFFFF; background-color: #4C4B6D; padding: 5px; border-radius: 4px;")
            headers_layout.addWidget(label)
        log_header_layout.addLayout(headers_layout)
        layout.addLayout(log_header_layout)  # Add the fixed header to the main layout

        # Add scrollable log entries only
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedHeight(120)  # Adjust height so only two entries show at a time

        # Widget that holds the log entries
        log_container = QWidget()
        log_layout = QVBoxLayout(log_container)
        log_layout.setSpacing(10)

        # Add time logs to the scrollable area
        self.add_time_log_entries(log_layout, [
            ("13:57", "16:32", "2:35:08 h"),
            ("07:11", "11:03", "3:52:27 h"),
            ("08:11", "11:03", "3:52:27 h"),
            ("09:11", "11:03", "3:52:27 h"),
            ("09:11", "11:03", "3:52:27 h"),
            ("09:11", "11:03", "3:52:27 h")
        ])

        scroll_area.setWidget(log_container)  # Set the widget with logs inside the scroll area
        layout.addWidget(scroll_area)

        # Bottom buttons
        bottom_layout = QHBoxLayout()
        open_dashboard_btn = QPushButton("Open Dashboard")
        open_dashboard_btn.setStyleSheet("background-color: transparent; color: #6E5BDE;")
        bottom_layout.addWidget(open_dashboard_btn)
        layout.addLayout(bottom_layout)

        self.setLayout(layout)

        # Start the timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTimer)
        self.timer.start(1000)
        self.time = QTime(0, 0, 0)

    def add_time_log_entries(self, layout, entries):
        for entry in entries:
            entry_layout = QHBoxLayout()
            for item in entry:
                label = QLabel(item)
                label.setStyleSheet("background-color: #F2F2F2; padding: 5px; border-radius: 4px;")
                entry_layout.addWidget(label)
            layout.addLayout(entry_layout)

    def updateTimer(self):
        self.time = self.time.addSecs(1)
        self.timer_label.setText(self.time.toString("hh:mm:ss") + " h")
