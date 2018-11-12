# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/aarav/Documents/QtWorkspace/generate_invoice.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from database_connector import Database
import xlsxwriter
import datetime


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

    def clear_form(self):
        self.textEditFileName.setText("")
        self.textEditSubmitName.setText("")
        self.labelError.setText("")
        self.textEditFileName_2.setText("")
        self.labelError_2.setText("")
        self.lineEditRate.setText("")

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

    def retranslateUi(self, AddShipper):
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddShipper = QtWidgets.QMainWindow()
    ui = Ui_AddShipper()
    ui.setupUi(AddShipper)
    AddShipper.show()
    sys.exit(app.exec_())

