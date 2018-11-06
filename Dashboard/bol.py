# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/aarav/Documents/QtWorkspace/bol.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from database_connector import Database
from bill_of_lading import BOL

class Ui_Bill_of_Lading(object):

    database = Database()

    def setupUi(self, Bill_of_Lading):
        Bill_of_Lading.setObjectName("Bill_of_Lading")
        Bill_of_Lading.resize(809, 633)
        Bill_of_Lading.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Bill_of_Lading)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 10, 281, 51))

        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet('QLabel {color: #124E78;}')
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 320, 741, 261))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 101, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 81, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(310, 130, 101, 16))
        self.label_4.setObjectName("label_4")
        self.textEditOriginAddress = QtWidgets.QTextEdit(self.groupBox)
        self.textEditOriginAddress.setGeometry(QtCore.QRect(420, 130, 301, 21))
        self.textEditOriginAddress.setObjectName("textEditOriginAddress")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(310, 160, 101, 16))
        self.label_5.setObjectName("label_5")
        self.textEditDestinationAddress = QtWidgets.QTextEdit(self.groupBox)
        self.textEditDestinationAddress.setGeometry(QtCore.QRect(420, 160, 301, 21))
        self.textEditDestinationAddress.setObjectName("textEditDestinationAddress")

        self.pushButtonAddJob = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonAddJob.setGeometry(QtCore.QRect(500, 220, 114, 32))
        self.pushButtonAddJob.setStyleSheet("background-color: rgb(40, 195, 50);")
        self.pushButtonAddJob.setObjectName("pushButtonAddJob")
        self.pushButtonAddJob.clicked.connect(self.add_bol)

        self.pushButtonEditJob = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonEditJob.setGeometry(QtCore.QRect(380, 220, 114, 32))
        self.pushButtonEditJob.setStyleSheet("background-color: rgb(255, 193, 44);")
        self.pushButtonEditJob.setObjectName("pushButtonEditJob")
        self.pushButtonEditJob.clicked.connect(self.edit_bol)

        self.pushButtonDeleteJob = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonDeleteJob.setGeometry(QtCore.QRect(260, 220, 114, 32))
        self.pushButtonDeleteJob.setStyleSheet("background-color: rgb(253, 70, 70);")
        self.pushButtonDeleteJob.setObjectName("pushButtonDeleteJob")
        self.pushButtonDeleteJob.clicked.connect(self.delete_bol)

        self.spinBoxShipper = QtWidgets.QComboBox(self.groupBox)
        self.spinBoxShipper.setGeometry(QtCore.QRect(120, 10, 181, 22))
        self.spinBoxShipper.setObjectName("spinBoxShipper")
        self.shipername_list = self.database.get_shippernames()

        self.spinBoxShipper.setStyleSheet(
            "background-color: rgb(255, 255, 255); selection-background-color: #4199D8; text-align: left; color: rgb(0, 0, 0);")

        self.spinBoxShipper.addItems(self.shipername_list)

        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(120, 70, 110, 22))
        self.dateEdit.setObjectName("dateEdit")

        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 70, 71, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 100, 71, 21))
        self.label_8.setObjectName("label_8")

        self.timeEditStartTime = QtWidgets.QTimeEdit(self.groupBox)
        self.timeEditStartTime.setGeometry(QtCore.QRect(120, 100, 111, 22))
        self.timeEditStartTime.setObjectName("timeEditStartTime")


        self.timeEditEndTime = QtWidgets.QTimeEdit(self.groupBox)
        self.timeEditEndTime.setGeometry(QtCore.QRect(120, 130, 111, 22))
        self.timeEditEndTime.setObjectName("timeEditEndTime")


        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(20, 130, 71, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(310, 40, 71, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(420, 40, 16, 21))
        self.label_11.setObjectName("label_11")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(430, 40, 111, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(310, 100, 101, 21))
        self.label_12.setObjectName("label_12")
        self.lineEditBillNumber = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditBillNumber.setGeometry(QtCore.QRect(120, 40, 171, 21))
        self.lineEditBillNumber.setObjectName("lineEditBillNumber")
        self.lineEditLoads = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditLoads.setGeometry(QtCore.QRect(420, 100, 113, 21))
        self.lineEditLoads.setObjectName("lineEditLoads")

        self.labelError = QtWidgets.QLabel(self.groupBox)
        self.labelError.setGeometry(QtCore.QRect(180, 190, 421, 21))
        self.labelError.setText("")
        self.labelError.setObjectName("labelError")
        self.labelError.setStyleSheet('QLabel {color: #990000;}')

        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(310, 10, 81, 21))
        self.label_6.setObjectName("label_6")

        self.spinBoxUsername = QtWidgets.QComboBox(self.groupBox)
        self.spinBoxUsername.setGeometry(QtCore.QRect(420, 10, 301, 22))
        self.spinBoxUsername.setObjectName("spinBoxUsername")

        self.username_list = self.database.get_usernames()

        self.spinBoxUsername.addItems(self.username_list)

        self.spinBoxUsername.setStyleSheet(
            "background-color: rgb(255, 255, 255); selection-background-color: #4199D8; text-align: left; color: rgb(0, 0, 0);")

        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(20, 160, 91, 21))
        self.label_13.setObjectName("label_13")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 160, 101, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButtonClearJob = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonClearJob.setGeometry(QtCore.QRect(140, 220, 114, 32))
        self.pushButtonClearJob.setStyleSheet("background-color: rgb(122, 122, 122);")
        self.pushButtonClearJob.setObjectName("pushButtonClearJob")
        self.pushButtonClearJob.clicked.connect(self.clear_form)

        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(310, 70, 71, 21))
        self.label_14.setObjectName("label_14")

        self.spinBoxRate = QtWidgets.QComboBox(self.groupBox)
        self.spinBoxRate.setGeometry(QtCore.QRect(420, 70, 111, 22))
        self.spinBoxRate.setObjectName("spinBoxRate")
        self.spinBoxRate.setObjectName("spinBoxRate")
        self.spinBoxRate.setStyleSheet(
            "background-color: rgb(255, 255, 255); selection-background-color: #4199D8; text-align: left; color: rgb(0, 0, 0);")
        self.spinBoxRate.addItem("Per Hour")
        self.spinBoxRate.addItem("Per Load")

        self.pushButtonHome = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonHome.setGeometry(QtCore.QRect(720, 20, 41, 41))
        self.pushButtonHome.setStyleSheet("background-image: url(:/home/baseline_home_black_18dp.png);")
        self.pushButtonHome.setText("")
        self.pushButtonHome.setObjectName("pushButtonHome")

        self.tableWidgetBills = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetBills.setGeometry(QtCore.QRect(20, 70, 771, 251))
        self.tableWidgetBills.setObjectName("tableWidgetBills")
        self.tableWidgetBills.setColumnCount(13)
        self.tableWidgetBills.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.tableWidgetBills.itemSelectionChanged.connect(self.change_data)
        column_titles = ['id', 'date', 'bill_number', 'shipper_name', 'username', 'rate', 'rate_type', 'origin', 'destination', 'loads',
                         'start_time', 'end_time', 'hours_worked']
        counter = 0
        for title in column_titles:
            item = QtWidgets.QTableWidgetItem(title)
            item.setBackground(QtGui.QColor(211, 211, 211))
            self.tableWidgetBills.setHorizontalHeaderItem(counter, item)
            counter += 1
        self.update_bol_table()


        header = self.tableWidgetBills.resizeColumnToContents(0)

        Bill_of_Lading.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Bill_of_Lading)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 22))
        self.menubar.setObjectName("menubar")
        Bill_of_Lading.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Bill_of_Lading)
        self.statusbar.setObjectName("statusbar")
        Bill_of_Lading.setStatusBar(self.statusbar)

        self.retranslateUi(Bill_of_Lading)
        QtCore.QMetaObject.connectSlotsByName(Bill_of_Lading)

    def update_bol_table(self):
        for i in reversed(range(self.tableWidgetBills.rowCount())):
            self.tableWidgetBills.removeRow(i)

        bills_list = self.database.get_bols()

        for row_number in range(len(bills_list)):
            self.tableWidgetBills.insertRow(row_number)
            bill = bills_list[row_number]
            self.tableWidgetBills.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(bill.bill_id)))
            self.tableWidgetBills.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(bill.date)))
            self.tableWidgetBills.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(bill.bill_number)))
            self.tableWidgetBills.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(bill.shipper_name)))
            self.tableWidgetBills.setItem(row_number, 4, QtWidgets.QTableWidgetItem(str(bill.user_name)))
            self.tableWidgetBills.setItem(row_number, 5, QtWidgets.QTableWidgetItem(str(bill.rate)))
            self.tableWidgetBills.setItem(row_number, 6, QtWidgets.QTableWidgetItem(str(bill.rate_type)))
            self.tableWidgetBills.setItem(row_number, 7, QtWidgets.QTableWidgetItem(str(bill.origin)))
            self.tableWidgetBills.setItem(row_number, 8, QtWidgets.QTableWidgetItem(str(bill.destination)))
            self.tableWidgetBills.setItem(row_number, 9, QtWidgets.QTableWidgetItem(str(bill.loads)))
            self.tableWidgetBills.setItem(row_number, 10, QtWidgets.QTableWidgetItem(str(bill.start_time)))
            self.tableWidgetBills.setItem(row_number, 11, QtWidgets.QTableWidgetItem(str(bill.end_time)))
            self.tableWidgetBills.setItem(row_number, 12, QtWidgets.QTableWidgetItem(str(bill.hours_worked)))
        return

    def change_data(self):
        item = self.tableWidgetBills.selectedItems()
        if len(item) == 0:
            return
        else:
            temp = (str(item[1].text())).split('-')
            self.dateEdit.setDate(QtCore.QDate(int(temp[0]), int(temp[1]), int(temp[2])))
            self.lineEditBillNumber.setText(str(item[2].text()))

            index = self.spinBoxShipper.findText(str(item[3].text()), QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.spinBoxShipper.setCurrentIndex(index)

            index = self.spinBoxUsername.findText(str(item[4].text()), QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.spinBoxUsername.setCurrentIndex(index)

            self.lineEdit.setText(str(item[5].text()))

            index = self.spinBoxRate.findText(str(item[6].text()), QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.spinBoxRate.setCurrentIndex(index)

            self.textEditOriginAddress.setText(str(item[7].text()))
            self.textEditDestinationAddress.setText(str(item[8].text()))
            self.lineEditLoads.setText(str(item[9].text()))

            time = str(item[10].text()).split(':')
            self.timeEditStartTime.setTime(QtCore.QTime(float(time[0]), float(time[1])))

            time = str(item[11].text()).split(':')
            self.timeEditEndTime.setTime(QtCore.QTime(float(time[0]), float(time[1])))

            self.lineEdit_2.setText(str(item[12].text()))
            return

    def edit_bol(self):
        item = self.tableWidgetBills.selectedItems()
        if len(item) == 0:
            self.labelError.setText("ERROR PLEASE SELECT JOB TO EDIT!")
        else:
            confirm = self.showdialog()
            if confirm:
                temp = self.dateEdit.date()
                date = temp.toPyDate()
                temp_2 = self.timeEditStartTime.time()
                start_time = temp_2.toPyTime()
                temp_3 = self.timeEditEndTime.time()
                end_time = temp_3.toPyTime()
                shipper_name = self.spinBoxShipper.currentText()
                username = self.spinBoxUsername.currentText()
                rate_type = self.spinBoxRate.currentText()
                rate = self.lineEdit.text()
                hours_worked = self.lineEdit_2.text()
                loads = self.lineEditLoads.text()
                origin = self.textEditOriginAddress.toPlainText()
                destination = self.textEditDestinationAddress.toPlainText()
                bill_number = self.lineEditBillNumber.text()
                bill_id = item[0].text()

                self.database.edit_bol(bill_id, date, bill_number,shipper_name, username, rate, rate_type, origin, destination, loads, start_time, end_time, hours_worked)
                self.update_bol_table()
                self.clear_form()

    def clear_form(self):
        self.tableWidgetBills.clearSelection()
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.lineEditBillNumber.setText("")
        self.lineEdit.setText("")
        self.textEditOriginAddress.setText("")
        self.textEditDestinationAddress.setText("")
        self.lineEditLoads.setText("")
        self.timeEditStartTime.setTime(QtCore.QTime.currentTime())
        self.timeEditEndTime.setTime(QtCore.QTime.currentTime())
        self.lineEdit_2.setText("")
        self.labelError.setText("")

    def showdialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)

        msg.setText("Make Changes?")
        msg.setInformativeText("The action CANNOT be undone!")
        msg.setWindowTitle("Confirmation")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        retval = msg.exec_()

        if retval == QMessageBox.Yes:
            return True
        else:
            return False

    def add_bol(self):
        temp = self.dateEdit.date()
        date = temp.toPyDate()
        temp_2 = self.timeEditStartTime.time()
        start_time = temp_2.toPyTime()
        temp_3 = self.timeEditEndTime.time()
        end_time = temp_3.toPyTime()
        shipper_name = self.spinBoxShipper.currentText()
        username = self.spinBoxUsername.currentText()
        rate_type = self.spinBoxRate.currentText()
        rate = self.lineEdit.text()
        hours_worked = self.lineEdit_2.text()
        loads = self.lineEditLoads.text()
        origin = self.textEditOriginAddress.toPlainText()
        destination = self.textEditDestinationAddress.toPlainText()
        bill_number = self.lineEditBillNumber.text()
        self.database.add_bol(date, bill_number, shipper_name, username, rate, rate_type, origin, destination,
                               loads, start_time, end_time, hours_worked)
        self.update_bol_table()
        self.clear_form()

    def delete_bol(self):
        item = self.tableWidgetBills.selectedItems()
        if len(item) == 0:
            self.labelError.setText("ERROR PLEASE SELECT JOB TO EDIT!")
        else:
            confirm = self.showdialog()
            if confirm:
                bill_id = item[0].text()
                self.database.delete_bol(bill_id)
                self.update_bol_table()
                self.clear_form()
                return


    def retranslateUi(self, Bill_of_Lading):
        _translate = QtCore.QCoreApplication.translate
        Bill_of_Lading.setWindowTitle(_translate("Bill_of_Lading", "MainWindow"))
        self.label.setText(_translate("Bill_of_Lading", "BILL OF LADINGS"))
        self.label_2.setText(_translate("Bill_of_Lading", "Shipper Name:"))
        self.label_3.setText(_translate("Bill_of_Lading", "Bill Number:"))
        self.label_4.setText(_translate("Bill_of_Lading", "Origin:"))
        self.label_5.setText(_translate("Bill_of_Lading", "Destination:"))
        self.pushButtonAddJob.setText(_translate("Bill_of_Lading", "Add BOL"))
        self.pushButtonEditJob.setText(_translate("Bill_of_Lading", "Edit BOL"))
        self.pushButtonDeleteJob.setText(_translate("Bill_of_Lading", "Delete BOL"))
        self.label_7.setText(_translate("Bill_of_Lading", "Date:"))
        self.label_8.setText(_translate("Bill_of_Lading", "Start Time:"))
        self.label_9.setText(_translate("Bill_of_Lading", "End Time:"))
        self.label_10.setText(_translate("Bill_of_Lading", "Rate:"))
        self.label_11.setText(_translate("Bill_of_Lading", "$"))
        self.label_12.setText(_translate("Bill_of_Lading", "Loads:"))
        self.label_6.setText(_translate("Bill_of_Lading", " Username:"))
        self.label_13.setText(_translate("Bill_of_Lading", "Hours Worked:"))
        self.pushButtonClearJob.setText(_translate("Bill_of_Lading", "Clear BOL"))
        self.label_14.setText(_translate("Bill_of_Lading", "Rate Type:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Bill_of_Lading = QtWidgets.QMainWindow()
    ui = Ui_Bill_of_Lading()
    ui.setupUi(Bill_of_Lading)
    Bill_of_Lading.show()
    sys.exit(app.exec_())

