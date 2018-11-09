# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/aarav/Documents/QtWorkspace/generate_invoice.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from database_connector import Database
import xlsxwriter

class Ui_AddShipper(object):

    database = Database()

    def setupUi(self, AddShipper):
        AddShipper.setObjectName("AddShipper")
        AddShipper.resize(809, 633)
        AddShipper.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(AddShipper)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 20, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(False)
        font.setWeight(50)

        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet('QLabel {color: #124E78;}')

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(170, 160, 461, 261))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 101, 21))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 110, 141, 21))
        self.label_6.setObjectName("label_6")
        self.lineEditSubmitName = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditSubmitName.setGeometry(QtCore.QRect(110, 110, 341, 21))
        self.lineEditSubmitName.setObjectName("lineEditSubmitName")

        self.pushButtonGenerate = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonGenerate.setGeometry(QtCore.QRect(170, 210, 114, 32))
        self.pushButtonGenerate.setStyleSheet("background-color: rgb(40, 195, 50);")
        self.pushButtonGenerate.setObjectName("pushButtonGenerate")
        self.pushButtonGenerate.clicked.connect(self.generate)

        self.spinBoxShipper = QtWidgets.QComboBox(self.groupBox)
        self.spinBoxShipper.setGeometry(QtCore.QRect(110, 10, 341, 22))
        self.spinBoxShipper.setObjectName("spinBoxShipper")
        self.shipername_list = self.database.get_shippernames()
        self.spinBoxShipper.setStyleSheet(
            "background-color: rgb(255, 255, 255); selection-background-color: #4199D8; text-align: left; color: rgb(0, 0, 0);")
        self.spinBoxShipper.addItems(self.shipername_list)

        self.dateEditTo = QtWidgets.QDateEdit(self.groupBox)
        self.dateEditTo.setGeometry(QtCore.QRect(110, 70, 110, 22))
        self.dateEditTo.setObjectName("dateEditTo")
        self.dateEditTo.setDateTime(QtCore.QDateTime.currentDateTime())

        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 71, 21))
        self.label_7.setObjectName("label_7")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(10, 40, 71, 21))
        self.label_13.setObjectName("label_13")

        self.dateEditFrom = QtWidgets.QDateEdit(self.groupBox)
        self.dateEditFrom.setGeometry(QtCore.QRect(110, 40, 110, 22))
        self.dateEditFrom.setObjectName("dateEditFrom")
        self.dateEditFrom.setDateTime(QtCore.QDateTime.currentDateTime())

        self.label_23 = QtWidgets.QLabel(self.groupBox)
        self.label_23.setGeometry(QtCore.QRect(10, 140, 141, 21))
        self.label_23.setObjectName("label_23")
        self.lineEditFileName = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditFileName.setGeometry(QtCore.QRect(110, 140, 341, 21))
        self.lineEditFileName.setObjectName("lineEditFileName")

        self.labelError = QtWidgets.QLabel(self.groupBox)
        self.labelError.setGeometry(QtCore.QRect(20, 180, 421, 21))
        self.labelError.setText("")
        self.labelError.setObjectName("labelError")
        self.labelError.setStyleSheet('QLabel {color: #990000;}')
        self.labelError.setAlignment(QtCore.Qt.AlignCenter)

        self.pushButtonHome = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonHome.setGeometry(QtCore.QRect(720, 20, 50, 50))
        self.pushButtonHome.setIcon(
            QtGui.QIcon("/Users/aarav/Documents/Github/truckerTracker/Dashboard/venv/imgs/144x144.png"))
        self.pushButtonHome.setStyleSheet("border-radius: 3px;")
        self.pushButtonHome.setIconSize(QtCore.QSize(45, 45))
        self.pushButtonHome.setText("")
        self.pushButtonHome.setObjectName("pushButtonHome")
        AddShipper.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddShipper)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 22))
        self.menubar.setObjectName("menubar")
        AddShipper.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddShipper)
        self.statusbar.setObjectName("statusbar")
        AddShipper.setStatusBar(self.statusbar)

        self.retranslateUi(AddShipper)
        QtCore.QMetaObject.connectSlotsByName(AddShipper)

    def retranslateUi(self, AddShipper):
        _translate = QtCore.QCoreApplication.translate
        AddShipper.setWindowTitle(_translate("AddShipper", "MainWindow"))
        self.label.setText(_translate("AddShipper", "GENERATE INVOICE"))
        self.label_2.setText(_translate("AddShipper", "Shipper Name:"))
        self.label_6.setText(_translate("AddShipper", "Submitted By:"))
        self.pushButtonGenerate.setText(_translate("AddShipper", "Generate"))
        self.label_7.setText(_translate("AddShipper", "To Date:"))
        self.label_13.setText(_translate("AddShipper", "From Date:"))
        self.label_23.setText(_translate("AddShipper", "File Name:"))

    def clear_form(self):
        self.lineEditFileName.setText("")
        self.lineEditSubmitName.setText("")
        self.labelError.setText("")

    def generate(self):
        filename = self.lineEditFileName.text()
        submitter = self.lineEditSubmitName.text()

        print(filename, submitter)

        if filename == "" or submitter == "":
            self.labelError.setText("Error: Please fill out all fields")
        else:
            filename += ".xlsx"
            workbook = xlsxwriter.Workbook(filename)
            worksheet = workbook.add_worksheet()
            expenses = (
                ['Rent', 1000],
                ['Gas', 100],
                ['Food', 300],
                ['Gym', 50],
            )

            # Start from the first cell. Rows and columns are zero indexed.
            row = 0
            col = 0

            # Iterate over the data and write it out row by row.
            for item, cost in (expenses):
                worksheet.write(row, col, item)
                worksheet.write(row, col + 1, cost)
                row += 1

            # Write a total using a formula.
            worksheet.write(row, 0, 'Total')
            worksheet.write(row, 1, '=SUM(B1:B4)')

            workbook.close()
            self.clear_form()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddShipper = QtWidgets.QMainWindow()
    ui = Ui_AddShipper()
    ui.setupUi(AddShipper)
    AddShipper.show()
    sys.exit(app.exec_())

