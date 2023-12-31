# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compiler.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(475, 659)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.year = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Marcellus SC")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.year.setFont(font)
        self.year.setAlignment(QtCore.Qt.AlignCenter)
        self.year.setObjectName("year")
        self.horizontalLayout.addWidget(self.year)
        self.month = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Marcellus SC")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.month.setFont(font)
        self.month.setAlignment(QtCore.Qt.AlignCenter)
        self.month.setObjectName("month")
        self.horizontalLayout.addWidget(self.month)
        self.week = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Marcellus SC")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.week.setFont(font)
        self.week.setAlignment(QtCore.Qt.AlignCenter)
        self.week.setObjectName("week")
        self.horizontalLayout.addWidget(self.week)
        self.day = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Marcellus SC")
        font.setPointSize(10)
        self.day.setFont(font)
        self.day.setAlignment(QtCore.Qt.AlignCenter)
        self.day.setObjectName("day")
        self.horizontalLayout.addWidget(self.day)
        self.hour = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Marcellus SC")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.hour.setFont(font)
        self.hour.setAlignment(QtCore.Qt.AlignCenter)
        self.hour.setObjectName("hour")
        self.horizontalLayout.addWidget(self.hour)
        self.minute = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Marcellus SC")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.minute.setFont(font)
        self.minute.setAlignment(QtCore.Qt.AlignCenter)
        self.minute.setObjectName("minute")
        self.horizontalLayout.addWidget(self.minute)
        self.second = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Marcellus SC")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.second.setFont(font)
        self.second.setAlignment(QtCore.Qt.AlignCenter)
        self.second.setObjectName("second")
        self.horizontalLayout.addWidget(self.second)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.valueY = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Marcellus SC")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.valueY.setFont(font)
        self.valueY.setAlignment(QtCore.Qt.AlignCenter)
        self.valueY.setObjectName("valueY")
        self.horizontalLayout_2.addWidget(self.valueY)
        self.valueM = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Marcellus SC")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.valueM.setFont(font)
        self.valueM.setAlignment(QtCore.Qt.AlignCenter)
        self.valueM.setObjectName("valueM")
        self.horizontalLayout_2.addWidget(self.valueM)
        self.valueW = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Marcellus SC")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.valueW.setFont(font)
        self.valueW.setAlignment(QtCore.Qt.AlignCenter)
        self.valueW.setObjectName("valueW")
        self.horizontalLayout_2.addWidget(self.valueW)
        self.valueD = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Marcellus SC")
        font.setPointSize(10)
        self.valueD.setFont(font)
        self.valueD.setAlignment(QtCore.Qt.AlignCenter)
        self.valueD.setObjectName("valueD")
        self.horizontalLayout_2.addWidget(self.valueD)
        self.valueH = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Marcellus SC")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.valueH.setFont(font)
        self.valueH.setAlignment(QtCore.Qt.AlignCenter)
        self.valueH.setObjectName("valueH")
        self.horizontalLayout_2.addWidget(self.valueH)
        self.valueMi = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Marcellus SC")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.valueMi.setFont(font)
        self.valueMi.setAlignment(QtCore.Qt.AlignCenter)
        self.valueMi.setObjectName("valueMi")
        self.horizontalLayout_2.addWidget(self.valueMi)
        self.valueS = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Marcellus SC")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.valueS.setFont(font)
        self.valueS.setAlignment(QtCore.Qt.AlignCenter)
        self.valueS.setObjectName("valueS")
        self.horizontalLayout_2.addWidget(self.valueS)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 475, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.year.setText(_translate("MainWindow", "Year"))
        self.month.setText(_translate("MainWindow", "Month"))
        self.week.setText(_translate("MainWindow", "Week"))
        self.day.setText(_translate("MainWindow", "Day"))
        self.hour.setText(_translate("MainWindow", "Hour"))
        self.minute.setText(_translate("MainWindow", "Minute"))
        self.second.setText(_translate("MainWindow", "Second"))
        self.valueY.setText(_translate("MainWindow", "0"))
        self.valueM.setText(_translate("MainWindow", "0"))
        self.valueW.setText(_translate("MainWindow", "0"))
        self.valueD.setText(_translate("MainWindow", "0"))
        self.valueH.setText(_translate("MainWindow", "0"))
        self.valueMi.setText(_translate("MainWindow", "0"))
        self.valueS.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
