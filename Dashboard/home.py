# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/aarav/Documents/QtWorkspace/TTD_main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import xlsxwriter
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from add_shipper import Ui_AddShipper
from database_connector import Database

class Ui_FleetConsole(object):

    database = Database()

    def setupUi(self, FleetConsole):
        FleetConsole.setObjectName("FleetConsole")
        FleetConsole.resize(800, 600)
        FleetConsole.setStyleSheet("background-color: #124E78;")
        self.centralwidget = QtWidgets.QWidget(FleetConsole)
        self.centralwidget.setObjectName("centralwidget")
        self.labelLogo = QtWidgets.QLabel(self.centralwidget)
        self.labelLogo.setGeometry(QtCore.QRect(290, 50, 251, 201))
        self.labelLogo.setText("")

        pixmap = QtGui.QPixmap("/Users/aarav/Documents/Github/truckerTracker/Dashboard/venv/imgs/truck-blue.png")
        pixmap = pixmap.scaled(971/4,780/4)
        self.labelLogo.setPixmap(pixmap)
        self.labelLogo.setObjectName("labelLogo")

        self.pushButtonShipper = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonShipper.setGeometry(QtCore.QRect(250, 300, 151, 81))
        self.pushButtonShipper.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(3, 38, 75);\n"
"selection-background-color: rgb(3, 38, 75);")
        self.pushButtonShipper.setObjectName("pushButtonShipper")
        self.pushButtonShipper.clicked.connect(self.show_shipper_manager)

        self.pushButtonJobs = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonJobs.setGeometry(QtCore.QRect(430, 300, 151, 81))
        self.pushButtonJobs.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(3, 38, 75);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-color: rgb(3, 38, 75);")
        self.pushButtonJobs.setObjectName("pushButtonJobs")
        self.pushButtonJobs.clicked.connect(self.show_add_job)

        self.pushButtonGenerateInvoice = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGenerateInvoice.setGeometry(QtCore.QRect(540, 420, 151, 81))
        self.pushButtonGenerateInvoice.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(3, 38, 75);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-color: rgb(3, 38, 75);")
        self.pushButtonGenerateInvoice.setObjectName("pushButtonGenerateInvoice")
        self.pushButtonGenerateInvoice.clicked.connect(self.show_generate)

        self.pushButtonBol = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBol.setGeometry(QtCore.QRect(160, 420, 151, 81))
        self.pushButtonBol.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(3, 38, 75);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-color: rgb(3, 38, 75);")
        self.pushButtonBol.setObjectName("pushButtonBol")
        self.pushButtonBol.clicked.connect(self.show_BOL)

        self.pushButtonDriverLogs = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDriverLogs.setGeometry(QtCore.QRect(350, 420, 151, 81))
        self.pushButtonDriverLogs.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(3, 38, 75);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-color: rgb(3, 38, 75);")
        self.pushButtonDriverLogs.setObjectName("pushButtonDriverLogs")
        self.pushButtonDriverLogs.clicked.connect(self.show_driver_log)

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
        self.pushButtonGenerateInvoice.setText(_translate("FleetConsole", "Generate Logs"))
        self.pushButtonBol.setText(_translate("FleetConsole", "View Bill of Ladings"))
        self.pushButtonDriverLogs.setText(_translate("FleetConsole", "Driver Info"))
        self.menuFLEET_MANAGER_CONSOLE.setTitle(_translate("FleetConsole", "FLEET MANAGER CONSOLE"))

    def show_shipper_manager(self):
        self.ui.setupUiAddShipper(self.FleetConsole)

    def show_generate(self):
        self.ui.setupUiGenerate(self.FleetConsole)

    def show_add_job(self):
        self.ui.setupUiAddJob(self.FleetConsole)

    def show_home(self):
        self.ui.setupUi(self.FleetConsole)

    def show_BOL(self):
        self.ui.setupUiBOL(self.FleetConsole)

    def show_driver_log(self):
        self.ui.setupUiDriverLog(self.FleetConsole)

    def setupUiAddJob(self, AddJob):
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
        self.labelError.setGeometry(QtCore.QRect(330, 530, 421, 21))
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
        self.pushButtonHome.clicked.connect(self.show_home)

        AddJob.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddJob)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 22))
        self.menubar.setObjectName("menubar")
        AddJob.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddJob)
        self.statusbar.setObjectName("statusbar")
        AddJob.setStatusBar(self.statusbar)

        self.retranslateUiAddJob(AddJob)
        QtCore.QMetaObject.connectSlotsByName(AddJob)

    def retranslateUiAddJob(self, AddJob):
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

    def clear_form_add_job(self):
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
        self.clear_form_add_job()

    def delete_job(self):
        item = self.listWidgetJobs.selectedItems()
        if len(item) == 0:
            self.labelError.setText("ERROR PLEASE SELECT JOB TO DELETE!")
        else:
            confirm = self.showdialog()
            if confirm:
                self.database.delete_job(self.selected_job.job_id)
                self.clear_form_add_job()
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
                self.clear_form_add_job()
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

    def setupUiGenerate(self, AddShipper):
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
        self.groupBox.setGeometry(QtCore.QRect(170, 80, 461, 491))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 101, 21))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 141, 21))
        self.label_6.setObjectName("label_6")

        self.textEditSubmitName = QtWidgets.QLineEdit(self.groupBox)
        self.textEditSubmitName.setGeometry(QtCore.QRect(110, 130, 341, 21))
        self.textEditSubmitName.setObjectName("textEditSubmitName")

        self.pushButtonGenerateInvoice = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonGenerateInvoice.setGeometry(QtCore.QRect(160, 230, 131, 32))
        self.pushButtonGenerateInvoice.setStyleSheet("background-color: rgb(40, 195, 50);")
        self.pushButtonGenerateInvoice.setObjectName("pushButtonGenerateInvoice")
        self.pushButtonGenerateInvoice.clicked.connect(self.generate_invoice)

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
        self.label_23.setGeometry(QtCore.QRect(10, 160, 141, 21))
        self.label_23.setObjectName("label_23")

        self.textEditFileName = QtWidgets.QLineEdit(self.groupBox)
        self.textEditFileName.setGeometry(QtCore.QRect(110, 160, 341, 21))
        self.textEditFileName.setObjectName("textEditFileName")

        self.labelError = QtWidgets.QLabel(self.groupBox)
        self.labelError.setGeometry(QtCore.QRect(20, 200, 421, 21))
        self.labelError.setText("")
        self.labelError.setObjectName("labelError")
        self.labelError.setStyleSheet('QLabel {color: #990000;}')
        self.labelError.setAlignment(QtCore.Qt.AlignCenter)

        self.dateEditTo_2 = QtWidgets.QDateEdit(self.groupBox)
        self.dateEditTo_2.setGeometry(QtCore.QRect(110, 350, 110, 22))
        self.dateEditTo_2.setObjectName("dateEditTo_2")
        self.dateEditTo_2.setDateTime(QtCore.QDateTime.currentDateTime())

        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(10, 320, 71, 21))
        self.label_14.setObjectName("label_14")

        self.spinBoxDriverName = QtWidgets.QComboBox(self.groupBox)
        self.spinBoxDriverName.setGeometry(QtCore.QRect(110, 290, 341, 22))
        self.spinBoxDriverName.setObjectName("spinBoxDriverName")
        self.drivername_list = self.database.get_usernames()
        self.spinBoxDriverName.setStyleSheet(
            "background-color: rgb(255, 255, 255); selection-background-color: #4199D8; text-align: left; color: rgb(0, 0, 0);")
        self.spinBoxDriverName.addItems(self.drivername_list)

        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 290, 91, 21))
        self.label_3.setObjectName("label_3")

        self.textEditFileName_2 = QtWidgets.QLineEdit(self.groupBox)
        self.textEditFileName_2.setGeometry(QtCore.QRect(110, 380, 341, 21))
        self.textEditFileName_2.setObjectName("textEditFileName_2")

        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 350, 71, 21))
        self.label_8.setObjectName("label_8")

        self.label_24 = QtWidgets.QLabel(self.groupBox)
        self.label_24.setGeometry(QtCore.QRect(10, 380, 91, 21))
        self.label_24.setObjectName("label_24")

        self.dateEditFrom_2 = QtWidgets.QDateEdit(self.groupBox)
        self.dateEditFrom_2.setGeometry(QtCore.QRect(110, 320, 110, 22))
        self.dateEditFrom_2.setObjectName("dateEditFrom_2")
        self.dateEditFrom_2.setDateTime(QtCore.QDateTime.currentDateTime())

        self.labelError_2 = QtWidgets.QLabel(self.groupBox)
        self.labelError_2.setGeometry(QtCore.QRect(20, 420, 421, 21))
        self.labelError_2.setText("")
        self.labelError_2.setObjectName("labelError_2")
        self.labelError_2.setStyleSheet('QLabel {color: #990000;}')
        self.labelError_2.setAlignment(QtCore.Qt.AlignCenter)

        self.pushButtonGenerateDriver = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonGenerateDriver.setGeometry(QtCore.QRect(160, 450, 131, 32))
        self.pushButtonGenerateDriver.setStyleSheet("background-color: rgb(40, 195, 50);")
        self.pushButtonGenerateDriver.setObjectName("pushButtonGenerateDriver")
        self.pushButtonGenerateDriver.clicked.connect(self.generate_driver_log)

        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 91, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(110, 100, 16, 21))
        self.label_5.setObjectName("label_5")
        self.lineEditRate = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditRate.setGeometry(QtCore.QRect(130, 100, 71, 21))
        self.lineEditRate.setObjectName("lineEditRate")

        self.pushButtonHome = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonHome.setGeometry(QtCore.QRect(720, 20, 50, 50))
        self.pushButtonHome.setIcon(
            QtGui.QIcon("/Users/aarav/Documents/Github/truckerTracker/Dashboard/venv/imgs/144x144.png"))
        self.pushButtonHome.setStyleSheet("border-radius: 3px;")
        self.pushButtonHome.setIconSize(QtCore.QSize(45, 45))
        self.pushButtonHome.setText("")
        self.pushButtonHome.setObjectName("pushButtonHome")
        self.pushButtonHome.clicked.connect(self.show_home)


        AddShipper.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddShipper)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 22))
        self.menubar.setObjectName("menubar")
        AddShipper.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddShipper)
        self.statusbar.setObjectName("statusbar")
        AddShipper.setStatusBar(self.statusbar)

        self.retranslateUiGenerate(AddShipper)
        QtCore.QMetaObject.connectSlotsByName(AddShipper)

    def clear_form(self):
        self.textEditFileName.setText("")
        self.textEditSubmitName.setText("")
        self.labelError.setText("")
        self.textEditFileName_2.setText("")
        self.labelError_2.setText("")
        self.lineEditRate.setText("")

    def generate_driver_log(self):
        filename = self.textEditFileName_2.text()
        if filename == "":
            self.labelError_2.setText("Error: Please enter file name")
        else:
            temp = self.dateEditFrom_2.date()
            date_from = temp.toPyDate()
            temp2 = self.dateEditTo_2.date()
            date_to = temp2.toPyDate()
            driver_name = self.spinBoxDriverName.currentText()
            data = self.database.get_driver_logs(driver_name, date_from, date_to)

            filename += ".xlsx"
            workbook = xlsxwriter.Workbook(filename)
            worksheet = workbook.add_worksheet()

            header_format = workbook.add_format()
            header_format.set_bold()
            header_format.set_align('left')
            header_format.set_font_size(21)
            header_format.set_bg_color('#a1a7af')

            money = workbook.add_format({'num_format': '$0.00'})

            worksheet.merge_range('A1:E1', 'Pullin\' Freight, LLC', header_format)

            title_format = workbook.add_format()
            title_format.set_bold()
            title_format.set_align('left')
            title_format.set_font_size(15)

            worksheet.write('A2:C2', 'Driver Log For:  {}'.format(driver_name.capitalize()), title_format)
            worksheet.write('A3:C3', 'Rate:', title_format)
            worksheet.write('B3', 20, money)

            title_format_2 = workbook.add_format()
            title_format_2.set_bold()
            title_format_2.set_align('right')
            title_format_2.set_font_size(13)
            title_format_2.set_bg_color('#a1a7af')

            worksheet.merge_range('F1:J1', 'Log from: {} to: {}'.format(str(date_from), str(date_to)),
                                  title_format_2)

            row = 3
            col = 0

            table_title_format = workbook.add_format()
            table_title_format.set_bold()
            table_title_format.set_color('#6d6d6d')
            table_title_format.set_align('center')
            table_title_format.set_font_size(13)

            worksheet.write(row, col, 'Date', table_title_format)
            worksheet.write(row, col + 1, 'Invoice #', table_title_format)
            worksheet.write(row, col + 2, 'Shipper', table_title_format)
            worksheet.write(row, col + 3, 'Origin', table_title_format)
            worksheet.write(row, col + 4, 'Destination', table_title_format)
            worksheet.write(row, col + 5, 'Hours', table_title_format)
            worksheet.write(row, col + 6, 'Sub-Total', table_title_format)

            table_content_even = workbook.add_format()
            table_content_even.set_bg_color('#dbdbdb')
            table_content_even.set_font_size(11)

            table_content_odd = workbook.add_format()
            table_content_odd.set_bg_color('#ffffff')
            table_content_odd.set_font_size(11)

            table_content_even_money = workbook.add_format()
            table_content_even_money.set_bg_color('#dbdbdb')
            table_content_even_money.set_font_size(11)
            table_content_even_money.set_num_format('$0.00')

            table_content_odd_money = workbook.add_format()
            table_content_odd_money.set_bg_color('#ffffff')
            table_content_odd_money.set_font_size(11)
            table_content_odd_money.set_num_format('$0.00')

            row = 4
            theme = table_content_even
            money = table_content_even_money

            for bol in data:
                if row %2 == 0:
                    theme = table_content_even
                    money = table_content_even_money
                else:
                    theme = table_content_odd
                    money = table_content_odd_money
                if bol.loads == 0:
                    selected_payment = bol.hours_worked
                if bol.hours_worked == 0:
                    selected_payment = bol.loads

                row_excel = row+1

                worksheet.write(row, col, str(bol.date), theme)
                print(str(bol.date))
                worksheet.write(row, col + 1, bol.bill_number, theme)
                worksheet.write(row, col + 2, bol.shipper_name, theme)
                worksheet.write(row, col + 3, bol.origin, theme)
                worksheet.write(row, col + 4, bol.destination, theme)
                worksheet.write(row, col + 5, selected_payment, theme)
                worksheet.write(row, col + 6, '=B3*F{}'.format(row_excel), money)
                row += 1

            total = workbook.add_format()
            total.set_bold()
            total.set_num_format('$0.00')
            total.set_font_size(12)
            row_excel = row + 1
            worksheet.write(row, 6, '=SUM(G5:G{})'.format(row),total)
            worksheet.write(row, 5, '=SUM(F5:F{})'.format(row))
            worksheet.write(row,3, 'Grand Total:',total)

            end = workbook.add_format()
            end.set_bg_color('#319e3b')
            row += 1
            row_excel = row + 1
            worksheet.merge_range('A{}:G{}'.format(row_excel, row_excel), '', end)

            workbook.close()
            self.clear_form()

    def generate_invoice(self):
        filename = self.textEditFileName.text()
        submitter = self.textEditSubmitName.text()
        rate = self.lineEditRate.text()

        print(filename, submitter)

        if filename == "" or submitter == "" or rate == "":
            self.labelError.setText("Error: Please fill out all fields")
        else:
            temp = self.dateEditFrom.date()
            date_from = temp.toPyDate()
            temp2 = self.dateEditTo.date()
            date_to = temp2.toPyDate()
            shipper_name = self.spinBoxShipper.currentText()
            data = self.database.get_bol_invoiced(shipper_name, date_from, date_to)
            rate = float(rate)/100

            print(data)

            filename += ".xlsx"
            workbook = xlsxwriter.Workbook(filename)
            worksheet = workbook.add_worksheet()

            money = workbook.add_format({'num_format': '$#,###.#0'})

            header_format = workbook.add_format()
            header_format.set_bold()
            header_format.set_align('left')
            header_format.set_font_size(21)
            header_format.set_bg_color('#a1a7af')

            worksheet.merge_range('A1:E1', 'Pullin\' Freight, LLC', header_format)


            title_format = workbook.add_format()
            title_format.set_bold()
            title_format.set_align('left')
            title_format.set_font_size(15)

            worksheet.write('A2:C2','Billed to:', title_format)
            worksheet.write('A3:C3', 'Address:', title_format)

            title_format_2 = workbook.add_format()
            title_format_2.set_bold()
            title_format_2.set_align('right')
            title_format_2.set_font_size(13)
            title_format_2.set_bg_color('#a1a7af')

            worksheet.merge_range('F1:J1', 'Invoice from: {} to: {}'.format(str(date_from), str(date_to)), title_format_2)

            row = 3
            col = 0

            table_title_format = workbook.add_format()
            table_title_format.set_bold()
            table_title_format.set_color('#6d6d6d')
            table_title_format.set_align('center')
            table_title_format.set_font_size(13)

            worksheet.write(row, col, 'Date',table_title_format)
            worksheet.write(row, col + 1, 'Invoice #',table_title_format)
            worksheet.write(row, col + 2, 'Shipper',table_title_format)
            worksheet.write(row, col + 3, 'Origin',table_title_format)
            worksheet.write(row, col + 4, 'Destination',table_title_format)
            worksheet.write(row, col + 5, 'Loads/Hours',table_title_format)
            worksheet.write(row, col + 6, 'Rate',table_title_format)
            worksheet.write(row, col + 7, 'Sub-Total',table_title_format)
            worksheet.write(row, col + 8, '-{}% Broker Fee'.format(rate*100),table_title_format)
            worksheet.write(row, col + 9, 'Total',table_title_format)

            table_content_even = workbook.add_format()
            table_content_even.set_bg_color('#dbdbdb')
            table_content_even.set_font_size(11)

            table_content_odd = workbook.add_format()
            table_content_odd.set_bg_color('#ffffff')
            table_content_odd.set_font_size(11)

            table_content_even_money = workbook.add_format()
            table_content_even_money.set_bg_color('#dbdbdb')
            table_content_even_money.set_font_size(11)
            table_content_even_money.set_num_format('$0.00')

            table_content_odd_money = workbook.add_format()
            table_content_odd_money.set_bg_color('#ffffff')
            table_content_odd_money.set_font_size(11)
            table_content_odd_money.set_num_format('$0.00')

            row = 4
            theme = table_content_even
            money = table_content_even_money
            # Iterate over the data and write it out row by row.
            for bol in data:
                if row %2 == 0:
                    theme = table_content_even
                    money = table_content_even_money
                else:
                    theme = table_content_odd
                    money = table_content_odd_money
                if bol.loads == 0:
                    selected_payment = bol.hours_worked
                if bol.hours_worked == 0:
                    selected_payment = bol.loads

                row_excel = row+1

                worksheet.write(row, col, str(bol.date), theme)
                print(str(bol.date))
                worksheet.write(row, col + 1, bol.bill_number, theme)
                worksheet.write(row, col + 2, bol.shipper_name, theme)
                worksheet.write(row, col + 3, bol.origin, theme)
                worksheet.write(row, col + 4, bol.destination, theme)
                worksheet.write(row, col + 5, selected_payment, theme)
                worksheet.write(row, col + 6, bol.rate, money)
                worksheet.write(row, col + 7, '=F{}*G{}'.format(row_excel, row_excel),money)
                worksheet.write(row, col+8, '=H{}*{}'.format(row_excel, rate),money)
                worksheet.write(row, col + 9, '=H{}-I{}'.format(row_excel, row_excel),money)
                row += 1

            total = workbook.add_format()
            total.set_bold()
            total.set_num_format('$0.00')
            total.set_font_size(12)
            row_excel = row + 1
            worksheet.write(row, 9, '=SUM(J5:J{})'.format(row),total)
            worksheet.write(row,8, 'Grand Total:',total)

            row += 2
            row_excel = row + 1
            worksheet.merge_range('A{}:J{}'.format(row_excel, row_excel), 'Submitted: {} by {}'.format(str(datetime.date.today()), submitter))

            end = workbook.add_format()
            end.set_bg_color('#319e3b')
            row += 1
            row_excel = row + 1
            worksheet.merge_range('A{}:J{}'.format(row_excel, row_excel), '', end)

            workbook.close()
            self.clear_form()

    def retranslateUiGenerate(self, AddShipper):
        _translate = QtCore.QCoreApplication.translate
        AddShipper.setWindowTitle(_translate("AddShipper", "MainWindow"))
        self.label.setText(_translate("AddShipper", "GENERATE LOGS"))
        self.label_2.setText(_translate("AddShipper", "Shipper Name:"))
        self.label_6.setText(_translate("AddShipper", "Submitted By:"))
        self.pushButtonGenerateInvoice.setText(_translate("AddShipper", "Generate Invoice"))
        self.label_7.setText(_translate("AddShipper", "To Date:"))
        self.label_13.setText(_translate("AddShipper", "From Date:"))
        self.label_23.setText(_translate("AddShipper", "File Name:"))
        self.label_14.setText(_translate("AddShipper", "From Date:"))
        self.label_3.setText(_translate("AddShipper", "Driver Name:"))
        self.label_8.setText(_translate("AddShipper", "To Date:"))
        self.label_24.setText(_translate("AddShipper", "File Name:"))
        self.pushButtonGenerateDriver.setText(_translate("AddShipper", "Generate Driver Log"))
        self.label_4.setText(_translate("AddShipper", "Brokerage"))
        self.label_5.setText(_translate("AddShipper", "%"))

    def setupUiAddShipper(self, AddShipper):
        AddShipper.setObjectName("AddShipper")
        AddShipper.resize(800, 600)
        AddShipper.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(AddShipper)
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

        self.listWidgetShippers = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetShippers.setGeometry(QtCore.QRect(40, 80, 261, 451))
        self.listWidgetShippers.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.listWidgetShippers.setObjectName("listWidgetShippers")
        self.listWidgetShippers.itemSelectionChanged.connect(self.change_data_add_shipper)

        self.update_shipper_list()

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(320, 80, 451, 441))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lineEditShipperName = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditShipperName.setGeometry(QtCore.QRect(10, 30, 441, 21))
        self.lineEditShipperName.setObjectName("lineEditShipperName")

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 111, 16))
        self.label_3.setObjectName("label_3")

        self.textEditShipperAddress = QtWidgets.QTextEdit(self.groupBox)
        self.textEditShipperAddress.setGeometry(QtCore.QRect(10, 130, 441, 51))
        self.textEditShipperAddress.setObjectName("textEditShipperAddress")

        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 111, 16))
        self.label_4.setObjectName("label_4")

        self.textEditOriginAddress = QtWidgets.QTextEdit(self.groupBox)
        self.textEditOriginAddress.setGeometry(QtCore.QRect(10, 200, 441, 51))
        self.textEditOriginAddress.setObjectName("textEditOriginAddress")

        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 250, 141, 16))
        self.label_5.setObjectName("label_5")

        self.textEditDestinationAddress = QtWidgets.QTextEdit(self.groupBox)
        self.textEditDestinationAddress.setGeometry(QtCore.QRect(10, 270, 441, 51))
        self.textEditDestinationAddress.setObjectName("textEditDestinationAddress")

        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 320, 141, 16))
        self.label_6.setObjectName("label_6")

        self.textEditComments = QtWidgets.QTextEdit(self.groupBox)
        self.textEditComments.setGeometry(QtCore.QRect(10, 340, 441, 51))
        self.textEditComments.setObjectName("textEditComments")

        self.pushButtonAddShipper = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonAddShipper.setGeometry(QtCore.QRect(353, 400, 101, 32))
        self.pushButtonAddShipper.setStyleSheet("background-color: rgb(40, 195, 50);")
        self.pushButtonAddShipper.setObjectName("pushButtonAddShipper")
        self.pushButtonAddShipper.clicked.connect(self.add_shipper)

        self.pushButtonEditShipper = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonEditShipper.setGeometry(QtCore.QRect(243, 400, 101, 32))
        self.pushButtonEditShipper.setStyleSheet("background-color: rgb(255, 193, 44);")
        self.pushButtonEditShipper.setObjectName("pushButtonEditShipper")
        self.pushButtonEditShipper.clicked.connect(self.edit_shipper)

        self.pushButtonDeleteShipper = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonDeleteShipper.setGeometry(QtCore.QRect(130, 400, 101, 32))
        self.pushButtonDeleteShipper.setStyleSheet("background-color: rgb(253, 70, 70);")
        self.pushButtonDeleteShipper.setObjectName("pushButtonDeleteShipper")
        self.pushButtonDeleteShipper.clicked.connect(self.delete_shipper)

        self.pushButtonClearForm = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonClearForm.setGeometry(QtCore.QRect(10, 400, 101, 32))
        self.pushButtonClearForm.setStyleSheet("background-color: rgb(122, 122, 122);")
        self.pushButtonClearForm.setObjectName("pushButtonClearForm")
        self.pushButtonClearForm.clicked.connect(self.clear_data_add_shipper)

        self.lineEditBrokerName = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditBrokerName.setGeometry(QtCore.QRect(10, 80, 441, 21))
        self.lineEditBrokerName.setObjectName("lineEditBrokerName")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 55, 101, 21))

        self.label_7.setObjectName("label_7")
        self.labelError = QtWidgets.QLabel(self.centralwidget)
        self.labelError.setGeometry(QtCore.QRect(340, 520, 421, 21))
        self.labelError.setText("")

        self.labelError.setObjectName("labelError")
        self.labelError.setStyleSheet('QLabel {color: #990000;}')

        self.pushButtonHome = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonHome.setGeometry(QtCore.QRect(720, 20, 50, 50))
        self.pushButtonHome.setIcon(QtGui.QIcon("/Users/aarav/Documents/Github/truckerTracker/Dashboard/venv/imgs/144x144.png"))
        self.pushButtonHome.setStyleSheet("border-radius: 3px;")
        self.pushButtonHome.setIconSize(QtCore.QSize(45,45))
        self.pushButtonHome.setText("")
        self.pushButtonHome.setObjectName("pushButtonHome")
        self.pushButtonHome.clicked.connect(self.show_home)

        AddShipper.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddShipper)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        AddShipper.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddShipper)
        self.statusbar.setObjectName("statusbar")
        AddShipper.setStatusBar(self.statusbar)

        self.retranslateUiAddShipper(AddShipper)
        QtCore.QMetaObject.connectSlotsByName(AddShipper)

    def retranslateUiAddShipper(self, AddShipper):
        _translate = QtCore.QCoreApplication.translate
        AddShipper.setWindowTitle(_translate("AddShipper", "MainWindow"))
        self.label.setText(_translate("AddShipper", "ADD SHIPPER"))
        self.label_2.setText(_translate("AddShipper", "Shipper Name:"))
        self.label_3.setText(_translate("AddShipper", "Shipper Address:"))
        self.label_4.setText(_translate("AddShipper", "Origin Address:"))
        self.label_5.setText(_translate("AddShipper", "Destination Address:"))
        self.label_6.setText(_translate("AddShipper", "Comments:"))
        self.pushButtonAddShipper.setText(_translate("AddShipper", "Add Shipper"))
        self.pushButtonEditShipper.setText(_translate("AddShipper", "Edit Shipper"))
        self.pushButtonDeleteShipper.setText(_translate("AddShipper", "Delete Shipper"))
        self.pushButtonClearForm.setText(_translate("AddShipper","Clear Form"))
        self.label_7.setText(_translate("AddShipper", "Broker Name:"))

    def update_shipper_list(self):
        self.listWidgetShippers.clear()
        shipper_list = self.database.get_shippers()
        for shipper in shipper_list:
            shipper_description = "{} - {} - {}".format(shipper.shipper_id, shipper.name, shipper.address)
            self.listWidgetShippers.addItem(shipper_description)

    def change_data_add_shipper(self):
        item = self.listWidgetShippers.selectedItems()
        if len(item) == 0:
            return
        else:
            list = item[0].text().split()
            shipper = self.database.get_shipper(list[0])
            self.lineEditShipperName.setText(shipper.name)
            self.lineEditBrokerName.setText(shipper.broker_name)
            self.textEditShipperAddress.setText(shipper.address)
            self.textEditOriginAddress.setText(shipper.origin)
            self.textEditDestinationAddress.setText(shipper.destination)
            self.textEditComments.setText(shipper.comments)

    def clear_data_add_shipper(self):
        self.listWidgetShippers.clearSelection()
        self.lineEditShipperName.setText("")
        self.lineEditBrokerName.setText("")
        self.textEditShipperAddress.setText("")
        self.textEditOriginAddress.setText("")
        self.textEditDestinationAddress.setText("")
        self.textEditComments.setText("")
        self.labelError.setText("")

    def edit_shipper(self):
        item = self.listWidgetShippers.selectedItems()
        if len(item) == 0:
            self.labelError.setText("ERROR PLEASE SELECT SHIPPER TO EDIT!")
        else:
            confirm = self.showdialog()
            if confirm:
                list = item[0].text().split()
                shipper_id = list[0]

                name = self.lineEditShipperName.text()
                broker_name = self.lineEditBrokerName.text()
                address = str(self.textEditShipperAddress.toPlainText())
                origin = str(self.textEditOriginAddress.toPlainText())
                destination = str(self.textEditDestinationAddress.toPlainText())
                comments = str(self.textEditComments.toPlainText())
                self.database.update_shipper(shipper_id,name, broker_name, address,origin,destination,comments)
                self.update_shipper_list()
                self.clear_data_add_shipper()
                return
            else:
                return

    def delete_shipper(self):
        item = self.listWidgetShippers.selectedItems()
        if len(item) == 0:
            self.labelError.setText("ERROR PLEASE SELECT SHIPPER TO DELETE!")
        else:
            confirm = self.showdialog()
            if confirm:
                list = item[0].text().split()
                shipper_id = list[0]

                self.database.delete_shipper(shipper_id)
                self.update_shipper_list()
                self.clear_data_add_shipper()
                return
            else:
                return

    def add_shipper(self):
        name = self.lineEditShipperName.text()
        broker_name = self.lineEditBrokerName.text()
        address = str(self.textEditShipperAddress.toPlainText())
        origin = str(self.textEditOriginAddress.toPlainText())
        destination = str(self.textEditDestinationAddress.toPlainText())
        comments = str(self.textEditComments.toPlainText())

        if (name == ""):
            self.labelError.setText("Error: Name Cannot be blank!")
            return
        if (address == ""):
            self.labelError.setText("Error: Address Cannot be blank")
            return

        self.database.add_shipper(name, broker_name, address,origin,destination,comments)
        self.update_shipper_list()
        self.clear_data_add_shipper()
        return


    def setupUiBOL(self, Bill_of_Lading):
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
        self.pushButtonClearJob.clicked.connect(self.clear_form_BOL)

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
        self.pushButtonHome.setGeometry(QtCore.QRect(720, 20, 50, 50))
        self.pushButtonHome.setIcon(
            QtGui.QIcon("/Users/aarav/Documents/Github/truckerTracker/Dashboard/venv/imgs/144x144.png"))
        self.pushButtonHome.setStyleSheet("border-radius: 3px;")
        self.pushButtonHome.setIconSize(QtCore.QSize(45, 45))
        self.pushButtonHome.setText("")
        self.pushButtonHome.setObjectName("pushButtonHome")
        self.pushButtonHome.clicked.connect(self.show_home)

        self.tableWidgetBills = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetBills.setGeometry(QtCore.QRect(20, 70, 771, 251))
        self.tableWidgetBills.setObjectName("tableWidgetBills")
        self.tableWidgetBills.setColumnCount(13)
        self.tableWidgetBills.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.tableWidgetBills.itemSelectionChanged.connect(self.change_data_BOL)
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

        self.retranslateUiBOL(Bill_of_Lading)
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

    def change_data_BOL(self):
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
                self.clear_form_BOL()

    def clear_form_BOL(self):
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
        self.clear_form_BOL()

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
                self.clear_form_BOL()
                return


    def retranslateUiBOL(self, Bill_of_Lading):
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

    def setupUiDriverLog(self, DriverLog):
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
        self.pushButtonHome.setGeometry(QtCore.QRect(720, 20, 50, 50))
        self.pushButtonHome.setIcon(
            QtGui.QIcon("/Users/aarav/Documents/Github/truckerTracker/Dashboard/venv/imgs/144x144.png"))
        self.pushButtonHome.setStyleSheet("border-radius: 3px;")
        self.pushButtonHome.setIconSize(QtCore.QSize(45, 45))
        self.pushButtonHome.setText("")
        self.pushButtonHome.setObjectName("pushButtonHome")
        self.pushButtonHome.clicked.connect(self.show_home)

        self.tableWidgetUsers = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetUsers.setGeometry(QtCore.QRect(20, 70, 771, 261))
        self.tableWidgetUsers.setObjectName("tableWidgetUsers")
        self.tableWidgetUsers.setColumnCount(9)
        self.tableWidgetUsers.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.tableWidgetUsers.itemSelectionChanged.connect(self.change_data_driver_log)
        column_titles = ['id', 'first name', 'last name','username','phone number', 'email', 'address', 'license no.', 'license exp.']
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

        self.retranslateUiDriverLog(DriverLog)
        QtCore.QMetaObject.connectSlotsByName(DriverLog)

    def retranslateUiDriverLog(self, DriverLog):
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

    def change_data_driver_log(self):
        item = self.tableWidgetUsers.selectedItems()
        if len(item) == 0:
            return
        else:
            #time = str(self.selected_job.start_time).split(':')
            #self.timeEditStartTime.setTime(QtCore.QTime(int(time[0]), int(time[1])))
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
                self.database.update_user(user_id, first_name, last_name, phone_number, email, address)
                self.update_user_list()
                self.clear_data_driver_log()
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
                self.database.delete_user(user_id)
                self.update_user_list()
                self.clear_data_driver_log()
                return
            else:
                return

    def clear_data_driver_log(self):
        self.lineEditFirstName.setText("")
        self.lineEditLastName.setText("")
        self.labelUsername.setText("")
        self.lineEditPhoneNumber.setText("")
        self.lineEditEmail.setText("")
        self.textEditAddress.setText("")
        self.labelLicenseNumber.setText("")
        self.labelLicenseExpiration.setText("")


    def set_layout(self, ui, FleetConsole):
        self.ui = ui
        self.FleetConsole = FleetConsole

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FleetConsole = QtWidgets.QMainWindow()
    ui = Ui_FleetConsole()
    ui.setupUi(FleetConsole)
    ui.set_layout(ui, FleetConsole)
    FleetConsole.show()
    sys.exit(app.exec_())