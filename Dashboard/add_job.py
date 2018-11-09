# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/aarav/Documents/QtWorkspace/add_job.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from database_connector import Database
from current_jobs import Current_job

class Ui_AddJob(object):

    database = Database()

    def setupUi(self, AddJob):
        AddJob.setObjectName("AddJob")
        AddJob.resize(809, 633)
        AddJob.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(AddJob)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 10, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet('QLabel {color: #124E78;}')

        self.listWidgetJobs = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetJobs.setGeometry(QtCore.QRect(40, 80, 261, 451))
        self.listWidgetJobs.setEditTriggers(
            QtWidgets.QAbstractItemView.DoubleClicked | QtWidgets.QAbstractItemView.EditKeyPressed | QtWidgets.QAbstractItemView.SelectedClicked)
        self.listWidgetJobs.setObjectName("listWidgetJobs")
        self.listWidgetJobs.itemSelectionChanged.connect(self.change_data)

        self.update_jobs_list()
        self.selected_job = None

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(310, 90, 451, 441))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 101, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 81, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 111, 16))
        self.label_4.setObjectName("label_4")
        self.textEditOriginAddress = QtWidgets.QTextEdit(self.groupBox)
        self.textEditOriginAddress.setGeometry(QtCore.QRect(10, 180, 441, 41))
        self.textEditOriginAddress.setObjectName("textEditOriginAddress")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 220, 141, 16))
        self.label_5.setObjectName("label_5")
        self.textEditDestinationAddress = QtWidgets.QTextEdit(self.groupBox)
        self.textEditDestinationAddress.setGeometry(QtCore.QRect(10, 240, 441, 41))
        self.textEditDestinationAddress.setObjectName("textEditDestinationAddress")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 280, 141, 16))
        self.label_6.setObjectName("label_6")
        self.textEditComments = QtWidgets.QTextEdit(self.groupBox)
        self.textEditComments.setGeometry(QtCore.QRect(10, 300, 441, 91))
        self.textEditComments.setObjectName("textEditComments")
        self.pushButtonAddJob = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonAddJob.setGeometry(QtCore.QRect(330, 400, 114, 32))
        self.pushButtonAddJob.setStyleSheet("background-color: rgb(40, 195, 50);")
        self.pushButtonAddJob.setObjectName("pushButtonAddJob")
        self.pushButtonAddJob.clicked.connect(self.add_job)

        self.pushButtonEditJob = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonEditJob.setGeometry(QtCore.QRect(210, 400, 114, 32))
        self.pushButtonEditJob.setStyleSheet("background-color: rgb(255, 193, 44);")
        self.pushButtonEditJob.setObjectName("pushButtonEditJob")
        self.pushButtonEditJob.clicked.connect(self.edit_job)

        self.pushButtonDeleteJob = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonDeleteJob.setGeometry(QtCore.QRect(90, 400, 114, 32))
        self.pushButtonDeleteJob.setStyleSheet("background-color: rgb(253, 70, 70);")
        self.pushButtonDeleteJob.clicked.connect(self.delete_job)
        self.pushButtonDeleteJob.setObjectName("pushButtonDeleteJob")

        self.spinBoxShipper = QtWidgets.QComboBox(self.groupBox)
        self.spinBoxShipper.setGeometry(QtCore.QRect(110, 10, 341, 22))
        self.spinBoxShipper.setObjectName("spinBoxShipper")

        self.shipername_list = self.database.get_shippernames()
        self.spinBoxShipper.setStyleSheet("background-color: rgb(255, 255, 255); selection-background-color: #4199D8; text-align: left; color: rgb(0, 0, 0);")

        self.spinBoxShipper.addItems(self.shipername_list)

        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(110, 70, 110, 22))
        self.dateEdit.setObjectName("dateEdit")

        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 71, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 100, 71, 21))
        self.label_8.setObjectName("label_8")
        self.timeEditStartTime = QtWidgets.QTimeEdit(self.groupBox)
        self.timeEditStartTime.setGeometry(QtCore.QRect(110, 100, 111, 22))
        self.timeEditStartTime.setObjectName("timeEditStartTime")
        self.label_10 = QtWidgets.QLabel(self.groupBox)


        self.label_10.setGeometry(QtCore.QRect(10, 130, 71, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(100, 130, 16, 21))
        self.label_11.setObjectName("label_11")
        self.lineEditRate = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditRate.setGeometry(QtCore.QRect(110, 130, 91, 21))
        self.lineEditRate.setObjectName("lineEdit")

        self.spinBoxUsername = QtWidgets.QComboBox(self.groupBox)
        self.spinBoxUsername.setGeometry(QtCore.QRect(110, 40, 341, 22))
        self.spinBoxUsername.setObjectName("spinBoxUsername")

        self.username_list = self.database.get_usernames()

        self.spinBoxUsername.addItems(self.username_list)

        self.spinBoxUsername.setStyleSheet("background-color: rgb(255, 255, 255); selection-background-color: #4199D8; text-align: left; color: rgb(0, 0, 0);")


        self.spinBoxRate = QtWidgets.QComboBox(self.groupBox)
        self.spinBoxRate.setGeometry(QtCore.QRect(210, 130, 101, 22))
        self.spinBoxRate.setObjectName("spinBoxRate")
        self.spinBoxRate.setStyleSheet("background-color: rgb(255, 255, 255); selection-background-color: #4199D8; text-align: left; color: rgb(0, 0, 0);")
        self.spinBoxRate.addItem("Per Hour")
        self.spinBoxRate.addItem("Per Load")


        self.labelError = QtWidgets.QLabel(self.centralwidget)
        self.labelError.setGeometry(QtCore.QRect(340, 520, 421, 21))
        self.labelError.setText("")
        self.labelError.setObjectName("labelError")
        self.labelError.setStyleSheet('QLabel {color: #990000;}')

        self.pushButtonHome = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonHome.setGeometry(QtCore.QRect(720, 20, 50, 50))
        self.pushButtonHome.setIcon(
            QtGui.QIcon("/Users/aarav/Documents/Github/truckerTracker/Dashboard/venv/imgs/144x144.png"))
        self.pushButtonHome.setStyleSheet("border-radius: 3px;")
        self.pushButtonHome.setIconSize(QtCore.QSize(45, 45))
        self.pushButtonHome.setText("")
        self.pushButtonHome.setObjectName("pushButtonHome")
        AddJob.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddJob)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 22))
        self.menubar.setObjectName("menubar")
        AddJob.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddJob)
        self.statusbar.setObjectName("statusbar")
        AddJob.setStatusBar(self.statusbar)

        self.retranslateUi(AddJob)
        QtCore.QMetaObject.connectSlotsByName(AddJob)

    def retranslateUi(self, AddJob):
        _translate = QtCore.QCoreApplication.translate
        AddJob.setWindowTitle(_translate("AddJob", "MainWindow"))
        self.label.setText(_translate("AddJob", "ADD JOB"))
        self.label_2.setText(_translate("AddJob", "Shipper Name:"))
        self.label_3.setText(_translate("AddJob", "Username:"))
        self.label_4.setText(_translate("AddJob", "Origin Address:"))
        self.label_5.setText(_translate("AddJob", "Destination Address:"))
        self.label_6.setText(_translate("AddJob", "Comments:"))
        self.pushButtonAddJob.setText(_translate("AddJob", "Add Job"))
        self.pushButtonEditJob.setText(_translate("AddJob", "Edit Job"))
        self.pushButtonDeleteJob.setText(_translate("AddJob", "Delete Job"))
        self.label_7.setText(_translate("AddJob", "Date:"))
        self.label_8.setText(_translate("AddJob", "Start Time:"))
        self.label_10.setText(_translate("AddJob", "Rate:"))
        self.label_11.setText(_translate("AddJob", "$"))


    def update_jobs_list(self):
        self.listWidgetJobs.clear()
        jobs_list = self.database.get_current_jobs()
        for job in jobs_list:
            job_description = "{} - {} on {} at {}".format(job.job_id, job.username, job.start_date, job.shipper_name)
            self.listWidgetJobs.addItem(job_description)


    def change_data(self):
        item = self.listWidgetJobs.selectedItems()
        if len(item) == 0:
            return
        else:
            list = item[0].text().split()
            index = self.spinBoxShipper.findText(list[6], QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.spinBoxShipper.setCurrentIndex(index)

            index = self.spinBoxUsername.findText(list[2], QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.spinBoxUsername.setCurrentIndex(index)

            self.selected_job = self.database.get_current_job_by_id(list[0])
            self.lineEditRate.setText(str(self.selected_job.rate))
            self.textEditOriginAddress.setText(self.selected_job.origin)
            self.textEditDestinationAddress.setText(self.selected_job.destination)
            self.textEditComments.setText(self.selected_job.comments)
            self.dateEdit.setDate(QtCore.QDate(self.selected_job.start_date))
            time = str(self.selected_job.start_time).split(':')
            self.timeEditStartTime.setTime(QtCore.QTime(float(time[0]), float(time[1])))

            index = self.spinBoxRate.findText(self.selected_job.pay_type, QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.spinBoxRate.setCurrentIndex(index)

    def clear_form(self):
        self.lineEditRate.setText("")
        self.textEditOriginAddress.setText("")
        self.textEditDestinationAddress.setText("")
        self.textEditComments.setText("")
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.listWidgetJobs.clearSelection()
        self.labelError.setText("")

    def add_job(self):
        temp = self.dateEdit.date()
        date = temp.toPyDate()
        temp_2 = self.timeEditStartTime.time()
        time = temp_2.toPyTime()
        shipper_name = self.spinBoxShipper.currentText()
        username = self.spinBoxUsername.currentText()
        rate = self.lineEditRate.text()
        rate_type = self.spinBoxRate.currentText()
        origin = self.textEditOriginAddress.toPlainText()
        destination = self.textEditDestinationAddress.toPlainText()
        comments = self.textEditComments.toPlainText()

        self.database.add_job(shipper_name, username, date, time, rate_type, rate, origin, destination, comments)
        self.update_jobs_list()
        self.clear_form()

    def delete_job(self):
        item = self.listWidgetJobs.selectedItems()
        if len(item) == 0:
            self.labelError.setText("ERROR PLEASE SELECT JOB TO DELETE!")
        else:
            confirm = self.showdialog()
            if confirm:
                self.database.delete_job(self.selected_job.job_id)
                self.clear_form()
                self.update_jobs_list()
                return
            else:
                return

    def edit_job(self):
        item = self.listWidgetJobs.selectedItems()
        if len(item) == 0:
            self.labelError.setText("ERROR PLEASE SELECT JOB TO EDIT!")
        else:
            confirm = self.showdialog()
            if confirm:
                temp = self.dateEdit.date()
                date = temp.toPyDate()
                temp_2 = self.timeEditStartTime.time()
                time = temp_2.toPyTime()
                shipper_name = self.spinBoxShipper.currentText()
                username = self.spinBoxUsername.currentText()
                rate = self.lineEditRate.text()
                rate_type = self.spinBoxRate.currentText()
                origin = self.textEditOriginAddress.toPlainText()
                destination = self.textEditDestinationAddress.toPlainText()
                comments = self.textEditComments.toPlainText()

                self.database.edit_job(shipper_name, username, date, time, rate_type, rate, origin, destination,
                                      comments, self.selected_job.job_id)
                self.update_jobs_list()
                self.clear_form()
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



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddJob = QtWidgets.QMainWindow()
    ui = Ui_AddJob()
    ui.setupUi(AddJob)
    AddJob.show()
    sys.exit(app.exec_())

