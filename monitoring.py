import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, 
                             QHBoxLayout, QLineEdit, QStackedWidget, QMainWindow)
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt, QTimer, QTime, QDate

class LoginWindow(QWidget):
    def __init__(self, switch_to_main):
        super().__init__()
        self.switch_to_main = switch_to_main
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        title = QLabel("Insightful")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont('Arial', 20))
        layout.addWidget(title)

        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")
        layout.addWidget(self.username)

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password)

        login_btn = QPushButton("Login")
        login_btn.clicked.connect(self.login)
        layout.addWidget(login_btn)

        self.setLayout(layout)

    def login(self):
        # Here you would typically verify credentials
        # For this example, we'll just switch to the main window
        self.switch_to_main()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Tab-like buttons
        tab_layout = QHBoxLayout()
        attendance_btn = QPushButton("Attendance")
        time_tracking_btn = QPushButton("Time Tracking")
        tab_layout.addWidget(attendance_btn)
        tab_layout.addWidget(time_tracking_btn)
        layout.addLayout(tab_layout)

        # Date and timer
        date_label = QLabel(f"Started at {QTime.currentTime().toString('hh:mm')} {QDate.currentDate().toString('MMMM dd, yyyy')}")
        layout.addWidget(date_label)

        self.timer_label = QLabel("00:00:00 h")
        self.timer_label.setFont(QFont('Arial', 24))
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.timer_label)

        # Action buttons
        action_layout = QHBoxLayout()
        clock_out_btn = QPushButton("Clock Out")
        take_break_btn = QPushButton("Take a Break")
        action_layout.addWidget(clock_out_btn)
        action_layout.addWidget(take_break_btn)
        layout.addLayout(action_layout)

        # Break time left
        break_label = QLabel("Break time left 30 min")
        layout.addWidget(break_label)

        # Today's time log
        today_label = QLabel("Today")
        layout.addWidget(today_label)

        time_log = QLabel("Clock in\t\tClock out\t\tTotal time\n13:57\t\t16:32\t\t2:35:08 h\n07:11\t\t11:03\t\t3:52:27 h")
        layout.addWidget(time_log)

        # Yesterday's time log
        yesterday_label = QLabel("Yesterday")
        layout.addWidget(yesterday_label)

        yesterday_log = QLabel("Clock in\t\tClock out\t\tTotal time\n09:54\t\t\t\t\t2:08:11 h")
        layout.addWidget(yesterday_log)

        # Bottom buttons
        bottom_layout = QHBoxLayout()
        last_sync_btn = QPushButton("Last synth\nDec 12, 2020 at 19:36")
        open_dashboard_btn = QPushButton("Open Dashboard")
        bottom_layout.addWidget(last_sync_btn)
        bottom_layout.addWidget(open_dashboard_btn)
        layout.addLayout(bottom_layout)

        self.setLayout(layout)

        # Start the timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTimer)
        self.timer.start(1000)
        self.time = QTime(0, 0, 0)

    def updateTimer(self):
        self.time = self.time.addSecs(1)
        self.timer_label.setText(self.time.toString("hh:mm:ss") + " h")

class MainApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.login_window = LoginWindow(self.switch_to_main)
        self.main_window = MainWindow()

        self.stacked_widget.addWidget(self.login_window)
        self.stacked_widget.addWidget(self.main_window)

        self.setWindowTitle('Insightful Time Tracker')
        self.setGeometry(100, 100, 300, 500)

    def switch_to_main(self):
        self.stacked_widget.setCurrentIndex(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApplication()
    ex.show()
    sys.exit(app.exec())