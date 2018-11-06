# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/aarav/Documents/QtWorkspace/add_shipper.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from database_connector import Database
from shipper import Shipper

class Ui_AddShipper(object):

    database = Database()

    def setupUi(self, AddShipper):
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
        self.listWidgetShippers.itemSelectionChanged.connect(self.change_data)

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
        self.pushButtonClearForm.clicked.connect(self.clear_data)

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
        self.pushButtonHome.setGeometry(QtCore.QRect(720, 20, 41, 41))
        self.pushButtonHome.setStyleSheet("background-image: url(:/Users/aarav/Documents/Github/truckerTracker/Dashboard/venv/imgs/truck-blue.png);")
        self.pushButtonHome.setText("")
        self.pushButtonHome.setObjectName("pushButtonHome")
        AddShipper.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddShipper)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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

    def change_data(self):
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

    def clear_data(self):
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
                self.clear_data()
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
                self.clear_data()
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
        self.clear_data()
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
    AddShipper = QtWidgets.QMainWindow()
    ui = Ui_AddShipper()
    ui.setupUi(AddShipper)
    AddShipper.show()
    sys.exit(app.exec_())

