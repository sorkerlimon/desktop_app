from PyQt6.QtCore import QTime, QTimer, QDateTime

def get_current_datetime(self):
    return QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")

def print_action(self, action):
    print(f"{action}: {self.get_current_datetime()}")
    
def toggle_clock(self):
    if not self.is_clocked_in: 
        self.is_clocked_in = True
        self.clock_btn.setText("Clock Out")
        self.clock_btn.setObjectName("clock_out")
        self.break_btn.setEnabled(True)
        self.timer.start(1000)
        self.print_action("Clock In")
    else:
        self.is_clocked_in = False
        self.clock_btn.setText("Clock In")
        self.clock_btn.setObjectName("action")
        self.break_btn.setEnabled(False)
        self.timer.stop()
        self.time = QTime(0, 0, 0)
        self.timer_label.setText("00:00:00 h")
        self.print_action("Clock out")
    self.clock_btn.setStyle(self.clock_btn.style())

def toggle_break(self):
    if not self.is_on_break:
        self.is_on_break = True
        self.break_btn.setText("Break Out")
        self.break_btn.setObjectName("break_out")
        self.clock_btn.setEnabled(False)
        self.timer.stop()
        self.print_action("Break In")
    else:
        self.is_on_break = False
        self.break_btn.setText("Take a Break")
        self.break_btn.setObjectName("action")
        self.clock_btn.setEnabled(True)
        self.timer.start(1000)
        self.print_action("Break Out")
    self.break_btn.setStyle(self.break_btn.style())
