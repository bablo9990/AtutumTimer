


def update(second, minute, hour, day, week, month, year):
    def render(Year, Mouth, Week, Day, Hour, Minute, Second):
        result = f"""
        "Year": {Year},
        "Mouth": {Mouth},
        "Week": {Week},
        "Day": {Day},
        "Hour": {Hour},
        "Minute": {Minute},
        "Second": {Second}"""
        return str('{'+result+'}')
    with open('data.json', 'w') as f:
        data = {
        "Year": year,
        "Mouth": month,
        "Week": week,
        "Day": day,
        "Hour": hour,
        "Minute": minute,
        "Second": second}
        f.write(render(Second=second, Minute=minute, Hour=hour, Day=day, Week=week, Mouth=month, Year=year))
def read():
    from json import load
    with open('data.json', 'r') as f:
        data = load(f)
    return data

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from compiler import Ui_MainWindow
class GUI(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self, status):
        super().__init__()
        self.setupUi(self)
        self.data = read()
        self.seconds = int(self.data['Second'])
        self.minutes = int(self.data['Minute'])
        self.hours = int(self.data['Hour'])
        self.days = int(self.data['Day'])
        self.weeks = int(self.data['Week'])
        self.mouths = int(self.data['Mouth'])
        self.years = int(self.data['Year'])
        self.valueS.setText(str(self.seconds))
        self.valueH.setText(str(self.hour))
        self.setWindowIcon(QIcon("ico.ico"))
        self.status = status
        self.update_time()
        self.timer = QTimer()
        self.time()

    def time(self):
        self.timer.timeout.connect(self.update_time)
        self.timer.start(999)

    def update_time(self):
        self.seconds += 1
        self.valueS.setText(str(self.seconds))
        self.valueMi.setText(str(self.minutes))
        self.valueH.setText(str(self.hours))
        self.valueD.setText(str(self.days))
        self.valueW.setText(str(self.weeks))
        self.valueM.setText(str(self.mouths))
        self.valueY.setText(str(self.years))
        if self.seconds >= 59:
            self.seconds = 0
            self.minutes += 1
        if self.minutes >= 59:
            self.minutes = 0
            self.hours += 1
        if self.hours >= 24:
            self.hours = 0
            self.days += 1
        if self.days >= 7:
            self.days = 0
            self.weeks += 1
        if self.weeks >= 7:
            self.weeks = 0
            self.mouths += 1
        if self.mouths >= 12:
            self.mouths = 0
            self.years += 1
        update(second=self.seconds, minute=self.minutes, hour=self.hours, day=self.days, week=self.weeks, month=self.mouths, year=self.years)



status = 0
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = GUI(status=status)
    w.show()
    sys.exit(app.exec())