# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/aarav/Documents/QtWorkspace/driver_log.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from database_connector import Database

class Ui_DriverLog(object):

    database = Database()

    def setupUi(self, DriverLog):
        DriverLog.setObjectName("DriverLog")
        DriverLog.resize(809, 633)
        DriverLog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(DriverLog)
        self.centralwidget.setObjectName("centralwidget")
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(280, 10, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(False)
        font.setWeight(50)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.labelTitle.setStyleSheet('QLabel {color: #124E78;}')

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 330, 761, 251))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.pushButtonEditDriver = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonEditDriver.setGeometry(QtCore.QRect(380, 210, 114, 32))
        self.pushButtonEditDriver.setStyleSheet("background-color: rgb(255, 193, 44);")
        self.pushButtonEditDriver.setObjectName("pushButtonEditDriver")
        self.pushButtonEditDriver.clicked.connect(self.edit_driver)

        self.pushButtonDeleteUser = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonDeleteUser.setGeometry(QtCore.QRect(260, 210, 114, 32))
        self.pushButtonDeleteUser.setStyleSheet("background-color: rgb(253, 70, 70);")
        self.pushButtonDeleteUser.setObjectName("pushButtonDeleteUser")
        self.pushButtonDeleteUser.clicked.connect(self.delete_driver)

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 81, 21))
        self.label_2.setObjectName("label_2")
        self.lineEditFirstName = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditFirstName.setGeometry(QtCore.QRect(150, 30, 171, 21))
        self.lineEditFirstName.setObjectName("lineEditFirstName")
        self.lineEditLastName = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditLastName.setGeometry(QtCore.QRect(510, 30, 211, 21))
        self.lineEditLastName.setText("")
        self.lineEditLastName.setObjectName("lineEditLastName")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(410, 30, 91, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(60, 60, 81, 21))
        self.label_4.setObjectName("label_4")

        self.labelUsername = QtWidgets.QLabel(self.groupBox)
        self.labelUsername.setGeometry(QtCore.QRect(150, 60, 171, 21))
        self.labelUsername.setText("")
        self.labelUsername.setObjectName("labelUsername")

        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(410, 60, 101, 21))
        self.label_5.setObjectName("label_5")
        self.lineEditPhoneNumber = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditPhoneNumber.setGeometry(QtCore.QRect(510, 60, 211, 21))
        self.lineEditPhoneNumber.setObjectName("lineEditPhoneNumber")
        self.lineEditEmail = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditEmail.setGeometry(QtCore.QRect(150, 90, 171, 21))
        self.lineEditEmail.setText("")
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(60, 90, 71, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(410, 90, 91, 21))
        self.label_7.setObjectName("label_7")
        self.textEditAddress = QtWidgets.QTextEdit(self.groupBox)
        self.textEditAddress.setGeometry(QtCore.QRect(510, 90, 211, 74))
        self.textEditAddress.setObjectName("textEditAddress")

        self.labelLicenseNumber = QtWidgets.QLabel(self.groupBox)
        self.labelLicenseNumber.setGeometry(QtCore.QRect(150, 120, 171, 21))
        self.labelLicenseNumber.setText("")
        self.labelLicenseNumber.setObjectName("labelLicenseNumber")

        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(60, 120, 81, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(60, 150, 81, 21))
        self.label_9.setObjectName("label_9")
        self.labelLicenseExpiration = QtWidgets.QLabel(self.groupBox)
        self.labelLicenseExpiration.setGeometry(QtCore.QRect(150, 150, 171, 21))
        self.labelLicenseExpiration.setText("")
        self.labelLicenseExpiration.setObjectName("labelLicenseExpiration")
        self.pushButtonHome = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonHome.setGeometry(QtCore.QRect(720, 20, 41, 41))
        self.pushButtonHome.setStyleSheet("background-image: url(:/home/baseline_home_black_18dp.png);")
        self.pushButtonHome.setText("")
        self.pushButtonHome.setObjectName("pushButtonHome")

        self.tableWidgetUsers = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetUsers.setGeometry(QtCore.QRect(20, 70, 771, 261))
        self.tableWidgetUsers.setObjectName("tableWidgetUsers")
        self.tableWidgetUsers.setColumnCount(9)
        self.tableWidgetUsers.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.tableWidgetUsers.itemSelectionChanged.connect(self.change_data)
        column_titles = ['id', 'first name', 'last name','username','phone number', 'email', 'address', 'license no.', 'license exp.' ]
        counter = 0
        for title in column_titles:
            item = QtWidgets.QTableWidgetItem(title)
            item.setBackground(QtGui.QColor(211,211,211))
            self.tableWidgetUsers.setHorizontalHeaderItem(counter,item)
            counter += 1
        self.update_user_list()

        header = self.tableWidgetUsers.resizeColumnToContents(0)

        DriverLog.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DriverLog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 22))
        self.menubar.setObjectName("menubar")
        DriverLog.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DriverLog)
        self.statusbar.setObjectName("statusbar")
        DriverLog.setStatusBar(self.statusbar)

        self.retranslateUi(DriverLog)
        QtCore.QMetaObject.connectSlotsByName(DriverLog)

    def retranslateUi(self, DriverLog):
        _translate = QtCore.QCoreApplication.translate
        DriverLog.setWindowTitle(_translate("DriverLog", "MainWindow"))
        self.labelTitle.setText(_translate("DriverLog", "DRIVER LOG"))
        self.pushButtonEditDriver.setText(_translate("DriverLog", "Edit User"))
        self.pushButtonDeleteUser.setText(_translate("DriverLog", "Delete User"))
        self.label_2.setText(_translate("DriverLog", "First Name:"))
        self.label_3.setText(_translate("DriverLog", "Last Name:"))
        self.label_4.setText(_translate("DriverLog", "Username:"))
        self.label_5.setText(_translate("DriverLog", "Phone Number:"))
        self.label_6.setText(_translate("DriverLog", "Email:"))
        self.label_7.setText(_translate("DriverLog", "Address:"))
        self.label_8.setText(_translate("DriverLog", "License No.:"))
        self.label_9.setText(_translate("DriverLog", "License Exp.:"))

    def change_data(self):
        item = self.tableWidgetUsers.selectedItems()
        if len(item) == 0:
            return
        else:
            self.lineEditFirstName.setText(str(item[1].text()))
            self.lineEditLastName.setText(str(item[2].text()))
            self.labelUsername.setText(str(item[3].text()))
            self.lineEditPhoneNumber.setText(str(item[4].text()))
            self.lineEditEmail.setText(str(item[5].text()))
            self.textEditAddress.setText(str(item[6].text()))
            self.labelLicenseNumber.setText(str(item[7].text()))
            self.labelLicenseExpiration.setText(str(item[8].text()))
            return

    def update_user_list(self):
        for i in reversed(range(self.tableWidgetUsers.rowCount())):
            self.tableWidgetUsers.removeRow(i)

        users_list = self.database.get_users()

        for row_number in range(len(users_list)):
            self.tableWidgetUsers.insertRow(row_number)
            user = users_list[row_number]
            self.tableWidgetUsers.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(user.user_id)))
            self.tableWidgetUsers.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(user.first_name)))
            self.tableWidgetUsers.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(user.last_name)))
            self.tableWidgetUsers.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(user.username)))
            self.tableWidgetUsers.setItem(row_number, 4, QtWidgets.QTableWidgetItem(str(user.phone_number)))
            self.tableWidgetUsers.setItem(row_number, 5, QtWidgets.QTableWidgetItem(str(user.email)))
            self.tableWidgetUsers.setItem(row_number, 6, QtWidgets.QTableWidgetItem(str(user.address)))
            self.tableWidgetUsers.setItem(row_number, 7, QtWidgets.QTableWidgetItem(str(user.license_number)))
            self.tableWidgetUsers.setItem(row_number, 8, QtWidgets.QTableWidgetItem(str(user.license_expire)))

        return

    def edit_driver(self):
        item = self.tableWidgetUsers.selectedItems()
        if len(item) == 0:
            print("ERROR PLEASE SELECT DRIVER TO EDIT OR ADD NEW DRIVER!")
        else:
            confirm = self.showdialog()
            if confirm:
                user_id = int(item[0].text())
                first_name = self.lineEditFirstName.text()
                last_name = self.lineEditLastName.text()
                phone_number = self.lineEditPhoneNumber.text()
                email = self.lineEditEmail.text()
                address = str(self.textEditAddress.toPlainText())
                self.database.run_update_user(user_id, first_name, last_name, phone_number, email, address)
                self.update_user_list()
                self.clear_data()
                return
            else:
                return

    def delete_driver(self):
        item = self.tableWidgetUsers.selectedItems()
        if len(item) == 0:
            print("ERROR PLEASE SELECT DRIVER TO DELETE OR ADD NEW DRIVER!")
        else:
            confirm = self.showdialog()
            if confirm:
                user_id = int(item[0].text())
                self.database.run_delete_user(user_id)
                self.update_user_list()
                self.clear_data()
                return
            else:
                return

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

    def clear_data(self):
        self.lineEditFirstName.setText("")
        self.lineEditLastName.setText("")
        self.labelUsername.setText("")
        self.lineEditPhoneNumber.setText("")
        self.lineEditEmail.setText("")
        self.textEditAddress.setText("")
        self.labelLicenseNumber.setText("")
        self.labelLicenseExpiration.setText("")

if __name__ == "__main__":
    import sys
    from database_connector import Database

    app = QtWidgets.QApplication(sys.argv)
    DriverLog = QtWidgets.QMainWindow()
    ui = Ui_DriverLog()
    ui.setupUi(DriverLog)
    
    DriverLog.show()
    sys.exit(app.exec_())

