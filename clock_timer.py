from PyQt6.QtCore import QObject, QTime, QTimer, QDateTime
from PyQt6.QtWidgets import QPushButton
import pyautogui
import os
from datetime import datetime


class ClockTimer(QObject):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time = QTime(0, 0, 0)
        self.is_clocked_in = False
        self.is_on_break = False
            

        self.screenshot_timer = QTimer()
        self.screenshot_timer.timeout.connect(self.take_screenshot)

        self.screenshot_dir = "screenshots"
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

    def take_screenshot(self):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{timestamp}.png"
        filepath = os.path.join(self.screenshot_dir, filename)
        
        try:
            # Take screenshot of entire screen
            screenshot = pyautogui.screenshot()
            screenshot.save(filepath)
            print(f"Screenshot saved: {filepath}")
        except Exception as e:
            print(f"Error taking screenshot: {str(e)}")

    def update_timer(self):
        if self.is_clocked_in and not self.is_on_break:
            self.time = self.time.addSecs(1)
            self.main_window.timer_label.setText(self.time.toString("hh:mm:ss") + " h")

    def get_current_datetime(self):
        return QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")

    def print_action(self, action):
        print(f"{action}: {self.get_current_datetime()}")
    
    def toggle_clock(self):
        if not self.is_clocked_in: 
            self.is_clocked_in = True
            self.main_window.clock_btn.setText("Clock Out")
            self.main_window.clock_btn.setObjectName("clock_out")
            self.main_window.break_btn.setEnabled(True)
            self.timer.start(1000)
            self.screenshot_timer.start(20000)
            self.print_action("Clock In")
            self.take_screenshot()
        else:
            self.is_clocked_in = False
            self.main_window.clock_btn.setText("Clock In")
            self.main_window.clock_btn.setObjectName("action")
            self.main_window.break_btn.setEnabled(False)
            self.timer.stop()
            self.time = QTime(0, 0, 0)
            self.main_window.timer_label.setText("00:00:00 h")
            self.print_action("Clock out")
            # Take screenshot when clocking out
        self.main_window.clock_btn.setStyle(self.main_window.clock_btn.style())

    def toggle_break(self):
        if not self.is_on_break:
            self.is_on_break = True
            self.main_window.break_btn.setText("Break Out")
            self.main_window.break_btn.setObjectName("break_out")
            self.main_window.clock_btn.setEnabled(False)
            self.timer.stop()
            self.print_action("Break In")
        else:
            self.is_on_break = False
            self.main_window.break_btn.setText("Take a Break")
            self.main_window.break_btn.setObjectName("action")
            self.main_window.clock_btn.setEnabled(True)
            self.timer.start(1000)
            self.print_action("Break Out")
        self.main_window.break_btn.setStyle(self.main_window.break_btn.style())