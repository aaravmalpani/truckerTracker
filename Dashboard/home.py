# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/aarav/Documents/QtWorkspace/TTD_main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from add_shipper import Ui_AddShipper

class Ui_FleetConsole(object):
    def setupUi(self, FleetConsole):
        FleetConsole.setObjectName("FleetConsole")
        FleetConsole.resize(800, 600)
        FleetConsole.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(FleetConsole)
        self.centralwidget.setObjectName("centralwidget")
        self.labelLogo = QtWidgets.QLabel(self.centralwidget)
        self.labelLogo.setGeometry(QtCore.QRect(290, 50, 251, 201))
        self.labelLogo.setText("")
        pixmap = QtGui.QPixmap("/Users/aarav/Documents/Github/truckerTracker/Dashboard/venv/imgs/truck-blue.png")
        self.labelLogo.setPixmap(pixmap)
        self.labelLogo.setObjectName("labelLogo")
        self.pushButtonShipper = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonShipper.setGeometry(QtCore.QRect(250, 300, 151, 81))
        self.pushButtonShipper.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(3, 38, 75);\n"
"selection-background-color: rgb(3, 38, 75);")


        self.pushButtonShipper.setObjectName("pushButtonShipper")
        self.pushButtonJobs = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonJobs.setGeometry(QtCore.QRect(430, 300, 151, 81))
        self.pushButtonJobs.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(3, 38, 75);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-color: rgb(3, 38, 75);")
        self.pushButtonShipper.clicked.connect(self.show_shipper_manager)

        self.pushButtonJobs.setObjectName("pushButtonJobs")
        self.pushButtonGenerateInvoice = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGenerateInvoice.setGeometry(QtCore.QRect(540, 420, 151, 81))
        self.pushButtonGenerateInvoice.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(3, 38, 75);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-color: rgb(3, 38, 75);")
        self.pushButtonGenerateInvoice.setObjectName("pushButtonGenerateInvoice")
        self.pushButtonBol = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBol.setGeometry(QtCore.QRect(160, 420, 151, 81))
        self.pushButtonBol.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(3, 38, 75);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-color: rgb(3, 38, 75);")
        self.pushButtonBol.setObjectName("pushButtonBol")
        self.pushButtonDriverLogs = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDriverLogs.setGeometry(QtCore.QRect(350, 420, 151, 81))
        self.pushButtonDriverLogs.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(3, 38, 75);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-color: rgb(3, 38, 75);")
        self.pushButtonDriverLogs.setObjectName("pushButtonDriverLogs")
        FleetConsole.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FleetConsole)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFLEET_MANAGER_CONSOLE = QtWidgets.QMenu(self.menubar)
        self.menuFLEET_MANAGER_CONSOLE.setObjectName("menuFLEET_MANAGER_CONSOLE")
        FleetConsole.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FleetConsole)
        self.statusbar.setObjectName("statusbar")
        FleetConsole.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFLEET_MANAGER_CONSOLE.menuAction())

        self.retranslateUi(FleetConsole)
        QtCore.QMetaObject.connectSlotsByName(FleetConsole)

    def retranslateUi(self, FleetConsole):
        _translate = QtCore.QCoreApplication.translate
        FleetConsole.setWindowTitle(_translate("FleetConsole", "MainWindow"))
        self.pushButtonShipper.setText(_translate("FleetConsole", "Shipper Manager"))
        self.pushButtonJobs.setText(_translate("FleetConsole", "Jobs Manager"))
        self.pushButtonGenerateInvoice.setText(_translate("FleetConsole", "Generate Invoice"))
        self.pushButtonBol.setText(_translate("FleetConsole", "View Bill of Ladings"))
        self.pushButtonDriverLogs.setText(_translate("FleetConsole", "Driver Logs"))
        self.menuFLEET_MANAGER_CONSOLE.setTitle(_translate("FleetConsole", "FLEET MANAGER CONSOLE"))

    def show_shipper_manager(self):
        pass



def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FleetConsole = QtWidgets.QMainWindow()
    ui = Ui_FleetConsole()
    ui.setupUi(FleetConsole)
    FleetConsole.show()
    sys.exit(app.exec_())

main()