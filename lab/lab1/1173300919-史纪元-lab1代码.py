import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 661)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 901, 621))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 571, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.verticalLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 2, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 3, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(610, 30, 171, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(10, 200, 781, 251))
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 571, 191))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.verticalLayoutWidget_4)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 2, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_2.addWidget(self.lineEdit_7, 1, 1, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_2.addWidget(self.lineEdit_9, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_2.addWidget(self.lineEdit_8, 3, 1, 1, 1)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(610, 30, 171, 131))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 200, 781, 251))
        self.tableWidget_2.setRowCount(5)
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(610, 30, 171, 131))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_4.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_4.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_4.addWidget(self.pushButton_12)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 200, 781, 251))
        self.tableWidget_3.setRowCount(5)
        self.tableWidget_3.setColumnCount(4)
        self.tableWidget_3.setObjectName("tableWidget_3")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(0, 0, 571, 191))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.verticalLayoutWidget_6)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 1, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 2, 0, 1, 1)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout_4.addWidget(self.lineEdit_18, 3, 1, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_4.addWidget(self.lineEdit_16, 2, 1, 1, 1)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.gridLayout_4.addWidget(self.lineEdit_19, 0, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 0, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 3, 0, 1, 1)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout_4.addWidget(self.lineEdit_17, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.tab_4)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(610, 30, 171, 131))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_13 = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_5.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_5.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout_5.addWidget(self.pushButton_15)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 200, 781, 251))
        self.tableWidget_4.setRowCount(5)
        self.tableWidget_4.setColumnCount(5)
        self.tableWidget_4.setObjectName("tableWidget_4")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.tab_4)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(0, 0, 571, 191))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.verticalLayoutWidget_8)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.verticalLayoutWidget_8)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.gridLayout_5.addWidget(self.lineEdit_21, 2, 1, 1, 1)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.verticalLayoutWidget_8)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.gridLayout_5.addWidget(self.lineEdit_22, 1, 1, 1, 1)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.verticalLayoutWidget_8)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.gridLayout_5.addWidget(self.lineEdit_23, 3, 1, 1, 1)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.verticalLayoutWidget_8)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.gridLayout_5.addWidget(self.lineEdit_24, 0, 1, 1, 1)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.verticalLayoutWidget_8)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.gridLayout_5.addWidget(self.lineEdit_25, 4, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_21.setObjectName("label_21")
        self.gridLayout_5.addWidget(self.label_21, 0, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_22.setObjectName("label_22")
        self.gridLayout_5.addWidget(self.label_22, 1, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 2, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_24.setObjectName("label_24")
        self.gridLayout_5.addWidget(self.label_24, 3, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_25.setObjectName("label_25")
        self.gridLayout_5.addWidget(self.label_25, 4, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.tab_5)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(610, 30, 171, 131))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_16 = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.pushButton_16.setObjectName("pushButton_16")
        self.verticalLayout_6.addWidget(self.pushButton_16)
        self.pushButton_17 = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.pushButton_17.setObjectName("pushButton_17")
        self.verticalLayout_6.addWidget(self.pushButton_17)
        self.pushButton_18 = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.pushButton_18.setObjectName("pushButton_18")
        self.verticalLayout_6.addWidget(self.pushButton_18)
        self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_5.setGeometry(QtCore.QRect(0, 200, 781, 251))
        self.tableWidget_5.setRowCount(5)
        self.tableWidget_5.setColumnCount(5)
        self.tableWidget_5.setObjectName("tableWidget_5")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, item)
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.tab_5)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(0, 0, 571, 191))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.verticalLayoutWidget_10)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.verticalLayoutWidget_10)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.gridLayout_6.addWidget(self.lineEdit_26, 2, 1, 1, 1)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.verticalLayoutWidget_10)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.gridLayout_6.addWidget(self.lineEdit_27, 1, 1, 1, 1)
        self.lineEdit_28 = QtWidgets.QLineEdit(self.verticalLayoutWidget_10)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.gridLayout_6.addWidget(self.lineEdit_28, 3, 1, 1, 1)
        self.lineEdit_29 = QtWidgets.QLineEdit(self.verticalLayoutWidget_10)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.gridLayout_6.addWidget(self.lineEdit_29, 0, 1, 1, 1)
        self.lineEdit_30 = QtWidgets.QLineEdit(self.verticalLayoutWidget_10)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.gridLayout_6.addWidget(self.lineEdit_30, 4, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.label_26.setObjectName("label_26")
        self.gridLayout_6.addWidget(self.label_26, 0, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.label_27.setObjectName("label_27")
        self.gridLayout_6.addWidget(self.label_27, 1, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.label_28.setObjectName("label_28")
        self.gridLayout_6.addWidget(self.label_28, 2, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.label_29.setObjectName("label_29")
        self.gridLayout_6.addWidget(self.label_29, 3, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.label_30.setObjectName("label_30")
        self.gridLayout_6.addWidget(self.label_30, 4, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(self.tab_6)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(0, 0, 571, 191))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.verticalLayoutWidget_12)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.verticalLayoutWidget_12)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.gridLayout_7.addWidget(self.lineEdit_31, 2, 1, 1, 1)
        self.lineEdit_32 = QtWidgets.QLineEdit(self.verticalLayoutWidget_12)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.gridLayout_7.addWidget(self.lineEdit_32, 1, 1, 1, 1)
        self.lineEdit_33 = QtWidgets.QLineEdit(self.verticalLayoutWidget_12)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.gridLayout_7.addWidget(self.lineEdit_33, 3, 1, 1, 1)
        self.lineEdit_34 = QtWidgets.QLineEdit(self.verticalLayoutWidget_12)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.gridLayout_7.addWidget(self.lineEdit_34, 0, 1, 1, 1)
        self.lineEdit_35 = QtWidgets.QLineEdit(self.verticalLayoutWidget_12)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.gridLayout_7.addWidget(self.lineEdit_35, 4, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        self.label_31.setObjectName("label_31")
        self.gridLayout_7.addWidget(self.label_31, 0, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        self.label_32.setObjectName("label_32")
        self.gridLayout_7.addWidget(self.label_32, 1, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        self.label_33.setObjectName("label_33")
        self.gridLayout_7.addWidget(self.label_33, 2, 0, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        self.label_34.setObjectName("label_34")
        self.gridLayout_7.addWidget(self.label_34, 3, 0, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        self.label_35.setObjectName("label_35")
        self.gridLayout_7.addWidget(self.label_35, 4, 0, 1, 1)
        self.tableWidget_6 = QtWidgets.QTableWidget(self.tab_6)
        self.tableWidget_6.setGeometry(QtCore.QRect(0, 200, 781, 251))
        self.tableWidget_6.setRowCount(5)
        self.tableWidget_6.setColumnCount(5)
        self.tableWidget_6.setObjectName("tableWidget_6")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, item)
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.tab_6)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(610, 30, 171, 131))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_19 = QtWidgets.QPushButton(self.verticalLayoutWidget_11)
        self.pushButton_19.setObjectName("pushButton_19")
        self.verticalLayout_7.addWidget(self.pushButton_19)
        self.pushButton_20 = QtWidgets.QPushButton(self.verticalLayoutWidget_11)
        self.pushButton_20.setObjectName("pushButton_20")
        self.verticalLayout_7.addWidget(self.pushButton_20)
        self.pushButton_21 = QtWidgets.QPushButton(self.verticalLayoutWidget_11)
        self.pushButton_21.setObjectName("pushButton_21")
        self.verticalLayout_7.addWidget(self.pushButton_21)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.verticalLayoutWidget_13 = QtWidgets.QWidget(self.tab_7)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(610, 30, 171, 131))
        self.verticalLayoutWidget_13.setObjectName("verticalLayoutWidget_13")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButton_22 = QtWidgets.QPushButton(self.verticalLayoutWidget_13)
        self.pushButton_22.setObjectName("pushButton_22")
        self.verticalLayout_8.addWidget(self.pushButton_22)
        self.pushButton_23 = QtWidgets.QPushButton(self.verticalLayoutWidget_13)
        self.pushButton_23.setObjectName("pushButton_23")
        self.verticalLayout_8.addWidget(self.pushButton_23)
        self.pushButton_24 = QtWidgets.QPushButton(self.verticalLayoutWidget_13)
        self.pushButton_24.setObjectName("pushButton_24")
        self.verticalLayout_8.addWidget(self.pushButton_24)
        self.tableWidget_7 = QtWidgets.QTableWidget(self.tab_7)
        self.tableWidget_7.setGeometry(QtCore.QRect(0, 200, 781, 251))
        self.tableWidget_7.setRowCount(5)
        self.tableWidget_7.setColumnCount(4)
        self.tableWidget_7.setObjectName("tableWidget_7")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, item)
        self.verticalLayoutWidget_14 = QtWidgets.QWidget(self.tab_7)
        self.verticalLayoutWidget_14.setGeometry(QtCore.QRect(0, 0, 571, 191))
        self.verticalLayoutWidget_14.setObjectName("verticalLayoutWidget_14")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.verticalLayoutWidget_14)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.lineEdit_37 = QtWidgets.QLineEdit(self.verticalLayoutWidget_14)
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.gridLayout_8.addWidget(self.lineEdit_37, 1, 1, 1, 1)
        self.lineEdit_36 = QtWidgets.QLineEdit(self.verticalLayoutWidget_14)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.gridLayout_8.addWidget(self.lineEdit_36, 2, 1, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.verticalLayoutWidget_14)
        self.label_37.setObjectName("label_37")
        self.gridLayout_8.addWidget(self.label_37, 1, 0, 1, 1)
        self.lineEdit_38 = QtWidgets.QLineEdit(self.verticalLayoutWidget_14)
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.gridLayout_8.addWidget(self.lineEdit_38, 3, 1, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.verticalLayoutWidget_14)
        self.label_39.setObjectName("label_39")
        self.gridLayout_8.addWidget(self.label_39, 3, 0, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.verticalLayoutWidget_14)
        self.label_38.setObjectName("label_38")
        self.gridLayout_8.addWidget(self.label_38, 2, 0, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.verticalLayoutWidget_14)
        self.label_36.setObjectName("label_36")
        self.gridLayout_8.addWidget(self.label_36, 0, 0, 1, 1)
        self.lineEdit_39 = QtWidgets.QLineEdit(self.verticalLayoutWidget_14)
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.gridLayout_8.addWidget(self.lineEdit_39, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.verticalLayoutWidget_15 = QtWidgets.QWidget(self.tab_8)
        self.verticalLayoutWidget_15.setGeometry(QtCore.QRect(610, 30, 171, 131))
        self.verticalLayoutWidget_15.setObjectName("verticalLayoutWidget_15")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_15)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton_25 = QtWidgets.QPushButton(self.verticalLayoutWidget_15)
        self.pushButton_25.setObjectName("pushButton_25")
        self.verticalLayout_9.addWidget(self.pushButton_25)
        self.pushButton_26 = QtWidgets.QPushButton(self.verticalLayoutWidget_15)
        self.pushButton_26.setObjectName("pushButton_26")
        self.verticalLayout_9.addWidget(self.pushButton_26)
        self.pushButton_27 = QtWidgets.QPushButton(self.verticalLayoutWidget_15)
        self.pushButton_27.setObjectName("pushButton_27")
        self.verticalLayout_9.addWidget(self.pushButton_27)
        self.tableWidget_8 = QtWidgets.QTableWidget(self.tab_8)
        self.tableWidget_8.setGeometry(QtCore.QRect(0, 200, 781, 251))
        self.tableWidget_8.setRowCount(5)
        self.tableWidget_8.setColumnCount(4)
        self.tableWidget_8.setObjectName("tableWidget_8")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(3, item)
        self.verticalLayoutWidget_16 = QtWidgets.QWidget(self.tab_8)
        self.verticalLayoutWidget_16.setGeometry(QtCore.QRect(0, 0, 571, 191))
        self.verticalLayoutWidget_16.setObjectName("verticalLayoutWidget_16")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.verticalLayoutWidget_16)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_44 = QtWidgets.QLabel(self.verticalLayoutWidget_16)
        self.label_44.setObjectName("label_44")
        self.gridLayout_9.addWidget(self.label_44, 3, 0, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.verticalLayoutWidget_16)
        self.label_43.setObjectName("label_43")
        self.gridLayout_9.addWidget(self.label_43, 2, 0, 1, 1)
        self.lineEdit_42 = QtWidgets.QLineEdit(self.verticalLayoutWidget_16)
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.gridLayout_9.addWidget(self.lineEdit_42, 1, 1, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.verticalLayoutWidget_16)
        self.label_41.setObjectName("label_41")
        self.gridLayout_9.addWidget(self.label_41, 0, 0, 1, 1)
        self.lineEdit_44 = QtWidgets.QLineEdit(self.verticalLayoutWidget_16)
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.gridLayout_9.addWidget(self.lineEdit_44, 0, 1, 1, 1)
        self.lineEdit_41 = QtWidgets.QLineEdit(self.verticalLayoutWidget_16)
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.gridLayout_9.addWidget(self.lineEdit_41, 2, 1, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.verticalLayoutWidget_16)
        self.label_42.setObjectName("label_42")
        self.gridLayout_9.addWidget(self.label_42, 1, 0, 1, 1)
        self.lineEdit_43 = QtWidgets.QLineEdit(self.verticalLayoutWidget_16)
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.gridLayout_9.addWidget(self.lineEdit_43, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tab_8, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 20, 731, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_3.addWidget(self.label_20)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_14.setText("")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.horizontalLayout_3.addWidget(self.lineEdit_14)
        self.label_40 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_3.addWidget(self.label_40)
        self.label_49 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_49.setText("")
        self.label_49.setObjectName("label_49")
        self.horizontalLayout_3.addWidget(self.label_49)
        self.label_45 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_45.setText("")
        self.label_45.setObjectName("label_45")
        self.horizontalLayout_3.addWidget(self.label_45)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_3.addWidget(self.pushButton_9)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_46 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_46.setObjectName("label_46")
        self.horizontalLayout_5.addWidget(self.label_46)
        self.label_47 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_47.setText("")
        self.label_47.setObjectName("label_47")
        self.horizontalLayout_5.addWidget(self.label_47)
        self.pushButton_28 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_28.setObjectName("pushButton_28")
        self.horizontalLayout_5.addWidget(self.pushButton_28)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout.addWidget(self.lineEdit_10)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout.addWidget(self.lineEdit_11)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.label_51 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_51.setText("")
        self.label_51.setObjectName("label_51")
        self.horizontalLayout.addWidget(self.label_51)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_48 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_48.setObjectName("label_48")
        self.horizontalLayout_6.addWidget(self.label_48)
        self.label_50 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_50.setText("")
        self.label_50.setObjectName("label_50")
        self.horizontalLayout_6.addWidget(self.label_50)
        self.pushButton_29 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_29.setObjectName("pushButton_29")
        self.horizontalLayout_6.addWidget(self.pushButton_29)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        self.tableWidget_9 = QtWidgets.QTableWidget(self.widget)
        self.tableWidget_9.setGeometry(QtCore.QRect(50, 270, 731, 201))
        self.tableWidget_9.setRowCount(3)
        self.tableWidget_9.setColumnCount(1)
        self.tableWidget_9.setObjectName("tableWidget_9")
        self.tabWidget.addTab(self.widget, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 903, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(8)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "公寓号"))
        self.label_2.setText(_translate("MainWindow", "楼层数"))
        self.label_3.setText(_translate("MainWindow", "寝室数"))
        self.label_4.setText(_translate("MainWindow", "是否有澡堂"))
        self.label_5.setText(_translate("MainWindow", "建成年份"))
        self.pushButton.setText(_translate("MainWindow", "查询"))
        self.pushButton_2.setText(_translate("MainWindow", "插入"))
        self.pushButton_3.setText(_translate("MainWindow", "删除"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "公寓号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "楼层数"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "寝室数"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "是否有澡堂"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "建成年份"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "公寓表"))
        self.label_7.setText(_translate("MainWindow", "寝室号"))
        self.label_8.setText(_translate("MainWindow", "床位数"))
        self.label_6.setText(_translate("MainWindow", "公寓号"))
        self.label_9.setText(_translate("MainWindow", "是否有空调"))
        self.pushButton_4.setText(_translate("MainWindow", "查询"))
        self.pushButton_5.setText(_translate("MainWindow", "插入"))
        self.pushButton_6.setText(_translate("MainWindow", "删除"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "公寓号"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "寝室号"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "床位数"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "是否有空调"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "寝室表"))
        self.pushButton_10.setText(_translate("MainWindow", "查询"))
        self.pushButton_11.setText(_translate("MainWindow", "插入"))
        self.pushButton_12.setText(_translate("MainWindow", "删除"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "公寓号"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "寝室号"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "床位号"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "是否加长"))
        self.label_17.setText(_translate("MainWindow", "寝室号"))
        self.label_18.setText(_translate("MainWindow", "床位号"))
        self.label_16.setText(_translate("MainWindow", "公寓号"))
        self.label_19.setText(_translate("MainWindow", "是否加长"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "床位表"))
        self.pushButton_13.setText(_translate("MainWindow", "查询"))
        self.pushButton_14.setText(_translate("MainWindow", "插入"))
        self.pushButton_15.setText(_translate("MainWindow", "删除"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "学号"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "性别"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "年龄"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "专业"))
        self.label_21.setText(_translate("MainWindow", "学号"))
        self.label_22.setText(_translate("MainWindow", "姓名"))
        self.label_23.setText(_translate("MainWindow", "性别"))
        self.label_24.setText(_translate("MainWindow", "年龄"))
        self.label_25.setText(_translate("MainWindow", "专业"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "学生表"))
        self.pushButton_16.setText(_translate("MainWindow", "查询"))
        self.pushButton_17.setText(_translate("MainWindow", "插入"))
        self.pushButton_18.setText(_translate("MainWindow", "删除"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "学期"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "公寓号"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "寝室号"))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "床位号"))
        item = self.tableWidget_5.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "学号"))
        self.label_26.setText(_translate("MainWindow", "学期"))
        self.label_27.setText(_translate("MainWindow", "公寓号"))
        self.label_28.setText(_translate("MainWindow", "寝室号"))
        self.label_29.setText(_translate("MainWindow", "床位号"))
        self.label_30.setText(_translate("MainWindow", "学号"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "学生-床位表"))
        self.label_31.setText(_translate("MainWindow", "职员工号"))
        self.label_32.setText(_translate("MainWindow", "姓名"))
        self.label_33.setText(_translate("MainWindow", "性别"))
        self.label_34.setText(_translate("MainWindow", "年龄"))
        self.label_35.setText(_translate("MainWindow", "手机号"))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "职员工号"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "性别"))
        item = self.tableWidget_6.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "年龄"))
        item = self.tableWidget_6.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "手机号"))
        self.pushButton_19.setText(_translate("MainWindow", "查询"))
        self.pushButton_20.setText(_translate("MainWindow", "插入"))
        self.pushButton_21.setText(_translate("MainWindow", "删除"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "员工表"))
        self.pushButton_22.setText(_translate("MainWindow", "查询"))
        self.pushButton_23.setText(_translate("MainWindow", "插入"))
        self.pushButton_24.setText(_translate("MainWindow", "删除"))
        item = self.tableWidget_7.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "学期"))
        item = self.tableWidget_7.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "职员工号"))
        item = self.tableWidget_7.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "公寓号"))
        item = self.tableWidget_7.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "职务"))
        self.label_37.setText(_translate("MainWindow", "职员工号"))
        self.label_39.setText(_translate("MainWindow", "职务"))
        self.label_38.setText(_translate("MainWindow", "公寓号"))
        self.label_36.setText(_translate("MainWindow", "学期"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "员工-公寓表"))
        self.pushButton_25.setText(_translate("MainWindow", "查询"))
        self.pushButton_26.setText(_translate("MainWindow", "插入"))
        self.pushButton_27.setText(_translate("MainWindow", "删除"))
        item = self.tableWidget_8.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "公寓号"))
        item = self.tableWidget_8.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget_8.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "手机号"))
        item = self.tableWidget_8.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "性别"))
        self.label_44.setText(_translate("MainWindow", "性别"))
        self.label_43.setText(_translate("MainWindow", "手机号"))
        self.label_41.setText(_translate("MainWindow", "公寓号"))
        self.label_42.setText(_translate("MainWindow", "姓名"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "洗衣机维修人员表"))
        self.label_20.setText(_translate("MainWindow", "嵌套查询：查询没有在"))
        self.label_40.setText(_translate("MainWindow", "公寓工作过的员工姓名"))
        self.pushButton_9.setText(_translate("MainWindow", "查询"))
        self.label_46.setText(_translate("MainWindow", "分组查询：查询至少做过两种不同工作的员工姓名"))
        self.pushButton_28.setText(_translate("MainWindow", "查询"))
        self.label_10.setText(_translate("MainWindow", "连接查询：查询住过"))
        self.label_11.setText(_translate("MainWindow", "公寓 和"))
        self.label_12.setText(_translate("MainWindow", "公寓的学生姓名"))
        self.pushButton_7.setText(_translate("MainWindow", "查询"))
        self.label_48.setText(_translate("MainWindow", "对视图的查询：查询计算机系学生住过的公寓号（其中计算机系学生是一个视图）"))
        self.pushButton_29.setText(_translate("MainWindow", "查询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "更多功能"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.query)
        self.pushButton_4.clicked.connect(self.query)
        self.pushButton_10.clicked.connect(self.query)
        self.pushButton_25.clicked.connect(self.query)
        self.pushButton_22.clicked.connect(self.query)
        self.pushButton_19.clicked.connect(self.query)
        self.pushButton_16.clicked.connect(self.query)
        self.pushButton_13.clicked.connect(self.query)

        self.pushButton_2.clicked.connect(self.insert)
        self.pushButton_5.clicked.connect(self.insert)
        self.pushButton_11.clicked.connect(self.insert)
        self.pushButton_14.clicked.connect(self.insert)
        self.pushButton_17.clicked.connect(self.insert)
        self.pushButton_20.clicked.connect(self.insert)
        self.pushButton_23.clicked.connect(self.insert)
        self.pushButton_26.clicked.connect(self.insert)

        self.pushButton_3.clicked.connect(self.delete)
        self.pushButton_6.clicked.connect(self.delete)
        self.pushButton_12.clicked.connect(self.delete)
        self.pushButton_15.clicked.connect(self.delete)
        self.pushButton_18.clicked.connect(self.delete)
        self.pushButton_21.clicked.connect(self.delete)
        self.pushButton_24.clicked.connect(self.delete)
        self.pushButton_27.clicked.connect(self.delete)

        self.pushButton_7.clicked.connect(self.connect_query)
        self.pushButton_9.clicked.connect(self.nested_query)
        self.pushButton_28.clicked.connect(self.group_query)
        self.pushButton_29.clicked.connect(self.view_query)

    def query(self):
        try:
            db = pymysql.connect(host='localhost', user='root', password='1235', database='studentdormitory')
            cursor = db.cursor()
        except pymysql.Error:
            print('连接数据库失败')
        button = ui.sender().objectName()  # 判断是哪个表下的查询
        condition = ''
        if button == 'pushButton':  # 公寓表查询
            if len(self.lineEdit_2.text().split()) != 0:
                condition += 'dorm_id like \'' + self.lineEdit_2.text() + '\' '
            else:
                condition += 'dorm_id like \'%\' '
            if len(self.lineEdit.text().split()) != 0:
                condition += 'and floors like \'' + self.lineEdit.text() + '\' '
            if len(self.lineEdit_4.text().split()) != 0:
                condition += 'and rooms like \'' + self.lineEdit_4.text() + '\' '
            if len(self.lineEdit_3.text().split()) != 0:
                condition += 'and has_bath like \'' + self.lineEdit_3.text() + '\' '
            if len(self.lineEdit_5.text().split()) != 0:
                condition += 'and built_year like \'' + self.lineEdit_5.text() + '\''
            sql = 'select * from dorm where ' + condition
            cursor.execute(sql)
            result = cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_num, row_data in enumerate(result):
                self.tableWidget.insertRow(row_num)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_num, column_number, QtWidgets.QTableWidgetItem(str(data)))
        elif button == 'pushButton_4':
            if len(self.lineEdit_9.text().split()) != 0:
                condition += 'dorm_id like \'' + self.lineEdit_9.text() + '\' '
            else:
                condition += 'dorm_id like \'%\' '
            if len(self.lineEdit_7.text().split()) != 0:
                condition += 'and room_id like \'' + self.lineEdit_7.text() + '\' '
            if len(self.lineEdit_6.text().split()) != 0:
                condition += 'and beds like \'' + self.lineEdit_6.text() + '\' '
            if len(self.lineEdit_8.text().split()) != 0:
                condition += 'and has_ac like \'' + self.lineEdit_8.text() + '\' '
            sql = 'select * from room where ' + condition
            cursor.execute(sql)
            result = cursor.fetchall()
            self.tableWidget_2.setRowCount(0)
            for row_num, row_data in enumerate(result):
                self.tableWidget_2.insertRow(row_num)
                for column_number, data in enumerate(row_data):
                    self.tableWidget_2.setItem(row_num, column_number, QtWidgets.QTableWidgetItem(str(data)))
        elif button == 'pushButton_10':
            if len(self.lineEdit_19.text().split()) != 0:
                condition += 'dorm_id like \'' + self.lineEdit_19.text() + '\' '
            else:
                condition += 'dorm_id like \'%\' '
            if len(self.lineEdit_17.text().split()) != 0:
                condition += 'and room_id like \'' + self.lineEdit_17.text() + '\' '
            if len(self.lineEdit_16.text().split()) != 0:
                condition += 'and bed_id like \'' + self.lineEdit_16.text() + '\' '
            if len(self.lineEdit_18.text().split()) != 0:
                condition += 'and is_long like \'' + self.lineEdit_18.text() + '\' '
            sql = 'select * from bed where ' + condition
            cursor.execute(sql)
            result = cursor.fetchall()
            self.tableWidget_3.setRowCount(0)
            for row_num, row_data in enumerate(result):
                self.tableWidget_3.insertRow(row_num)
                for column_number, data in enumerate(row_data):
                    self.tableWidget_3.setItem(row_num, column_number, QtWidgets.QTableWidgetItem(str(data)))
        elif button == 'pushButton_13':
            if len(self.lineEdit_24.text().split()) != 0:
                condition += 'Sid like \'' + self.lineEdit_24.text() + '\' '
            else:
                condition += 'Sid like \'%\' '
            if len(self.lineEdit_22.text().split()) != 0:
                condition += 'and Sname like \'' + self.lineEdit_22.text() + '\' '
            if len(self.lineEdit_21.text().split()) != 0:
                condition += 'and Sgender like \'' + self.lineEdit_21.text() + '\' '
            if len(self.lineEdit_23.text().split()) != 0:
                condition += 'and Sage like \'' + self.lineEdit_23.text() + '\' '
            if len(self.lineEdit_25.text().split()) != 0:
                condition += 'and Smajor like \'' + self.lineEdit_25.text() + '\' '
            sql = 'select * from student where ' + condition
            cursor.execute(sql)
            result = cursor.fetchall()
            self.tableWidget_4.setRowCount(0)
            for row_num, row_data in enumerate(result):
                self.tableWidget_4.insertRow(row_num)
                for column_number, data in enumerate(row_data):
                    self.tableWidget_4.setItem(row_num, column_number, QtWidgets.QTableWidgetItem(str(data)))
        elif button == 'pushButton_16':
            if len(self.lineEdit_29.text().split()) != 0:
                condition += 'semester like \'' + self.lineEdit_29.text() + '\' '
            else:
                condition += 'semester like \'%\' '
            if len(self.lineEdit_27.text().split()) != 0:
                condition += 'and dorm_id like \'' + self.lineEdit_27.text() + '\' '
            if len(self.lineEdit_26.text().split()) != 0:
                condition += 'and room_id like \'' + self.lineEdit_26.text() + '\' '
            if len(self.lineEdit_28.text().split()) != 0:
                condition += 'and bed_id like \'' + self.lineEdit_28.text() + '\' '
            if len(self.lineEdit_30.text().split()) != 0:
                condition += 'and Sid like \'' + self.lineEdit_30.text() + '\' '
            sql = 'select * from student_bed where ' + condition
            cursor.execute(sql)
            result = cursor.fetchall()
            self.tableWidget_5.setRowCount(0)
            for row_num, row_data in enumerate(result):
                self.tableWidget_5.insertRow(row_num)
                for column_number, data in enumerate(row_data):
                    self.tableWidget_5.setItem(row_num, column_number, QtWidgets.QTableWidgetItem(str(data)))
        elif button == 'pushButton_19':
            if len(self.lineEdit_34.text().split()) != 0:
                condition += 'Eid like \'' + self.lineEdit_34.text() + '\' '
            else:
                condition += 'Eid like \'%\' '
            if len(self.lineEdit_32.text().split()) != 0:
                condition += 'and Ename like \'' + self.lineEdit_32.text() + '\' '
            if len(self.lineEdit_31.text().split()) != 0:
                condition += 'and Egender like \'' + self.lineEdit_31.text() + '\' '
            if len(self.lineEdit_33.text().split()) != 0:
                condition += 'and Eage like \'' + self.lineEdit_33.text() + '\' '
            if len(self.lineEdit_35.text().split()) != 0:
                condition += 'and E_phonenumber like \'' + self.lineEdit_35.text() + '\' '
            sql = 'select * from employee where ' + condition
            cursor.execute(sql)
            result = cursor.fetchall()
            self.tableWidget_6.setRowCount(0)
            for row_num, row_data in enumerate(result):
                self.tableWidget_6.insertRow(row_num)
                for column_number, data in enumerate(row_data):
                    self.tableWidget_6.setItem(row_num, column_number, QtWidgets.QTableWidgetItem(str(data)))
        elif button == 'pushButton_22':
            if len(self.lineEdit_39.text().split()) != 0:
                condition += 'semester like \'' + self.lineEdit_39.text() + '\' '
            else:
                condition += 'semester like \'%\' '
            if len(self.lineEdit_37.text().split()) != 0:
                condition += 'and Eid like \'' + self.lineEdit_37.text() + '\' '
            if len(self.lineEdit_36.text().split()) != 0:
                condition += 'and dorm_id like \'' + self.lineEdit_36.text() + '\' '
            if len(self.lineEdit_38.text().split()) != 0:
                condition += 'and job like \'' + self.lineEdit_38.text() + '\' '
            sql = 'select * from employee_dorm where ' + condition
            cursor.execute(sql)
            result = cursor.fetchall()
            self.tableWidget_7.setRowCount(0)
            for row_num, row_data in enumerate(result):
                self.tableWidget_7.insertRow(row_num)
                for column_number, data in enumerate(row_data):
                    self.tableWidget_7.setItem(row_num, column_number, QtWidgets.QTableWidgetItem(str(data)))
        elif button == 'pushButton_25':
            if len(self.lineEdit_44.text().split()) != 0:
                condition += 'dorm_id like \'' + self.lineEdit_44.text() + '\' '
            else:
                condition += 'dorm_id like \'%\' '
            if len(self.lineEdit_42.text().split()) != 0:
                condition += 'and Mname like \'' + self.lineEdit_42.text() + '\' '
            if len(self.lineEdit_41.text().split()) != 0:
                condition += 'and M_phonenumber like \'' + self.lineEdit_41.text() + '\' '
            if len(self.lineEdit_43.text().split()) != 0:
                condition += 'and Mgender like \'' + self.lineEdit_43.text() + '\' '
            sql = 'select * from maintenance_worker where ' + condition
            cursor.execute(sql)
            result = cursor.fetchall()
            self.tableWidget_8.setRowCount(0)
            for row_num, row_data in enumerate(result):
                self.tableWidget_8.insertRow(row_num)
                for column_number, data in enumerate(row_data):
                    self.tableWidget_8.setItem(row_num, column_number, QtWidgets.QTableWidgetItem(str(data)))

        db.close()

    def insert(self):
        try:
            db = pymysql.connect(host='localhost', user='root', password='1235', database='studentdormitory')
            cursor = db.cursor()
        except pymysql.Error:
            print('连接数据库失败')
        button = ui.sender().objectName()
        if button == 'pushButton_2':
            # 判断是否插入空值
            if len(self.lineEdit.text().split()) * len(self.lineEdit_2.text().split()) * len(self.lineEdit_3.text().split()) * len(self.lineEdit_4.text().split()) * len(self.lineEdit_5.text().split()) == 0:
                QMessageBox.critical(self, 'Error', 'Can\'t insert null value')
                return
            sql = 'insert into dorm(dorm_id, floors, rooms, has_bath, built_year) values ' + \
                  '(\'' + self.lineEdit_2.text() + '\', ' + self.lineEdit.text() + ',' + self.lineEdit_4.text() + ',\'' \
                  + self.lineEdit_3.text() + '\',\'' + self.lineEdit_5.text() + '\');'

        elif button == 'pushButton_5':
            # 判断是否插入空值
            if len(self.lineEdit_9.text().split()) * len(self.lineEdit_7.text().split()) * len(self.lineEdit_6.text().split()) * len(
                    self.lineEdit_8.text().split()) == 0:
                QMessageBox.critical(self, 'Error', 'Can\'t insert null value')
                return
            sql = 'insert into room(dorm_id, room_id, beds, has_ac) values ' + '(\'' + self.lineEdit_9.text() +\
                  '\', \'' + self.lineEdit_7.text() + '\',' + self.lineEdit_6.text() + ',\'' \
                  + self.lineEdit_8.text() + '\');'

        elif button == 'pushButton_11':
            # 判断是否插入空值
            if len(self.lineEdit_19.text().split()) * len(self.lineEdit_17.text().split()) * len(self.lineEdit_16.text().split()) * len(
                    self.lineEdit_18.text().split()) == 0:
                QMessageBox.critical(self, 'Error', 'Can\'t insert null value')
                return
            sql = 'insert into bed(dorm_id, room_id, bed_id, is_long) values ' + '(\'' + self.lineEdit_19.text() + \
                  '\', \'' + self.lineEdit_17.text() + '\',\'' + self.lineEdit_16.text() + '\',\'' \
                  + self.lineEdit_18.text() + '\');'

        elif button == 'pushButton_14':
            # 判断是否插入空值
            if len(self.lineEdit_24.text().split()) * len(self.lineEdit_22.text().split()) * len(self.lineEdit_21.text().split()) * len(
                    self.lineEdit_23.text().split()) * len(self.lineEdit_25.text().split()) == 0:
                QMessageBox.critical(self, 'Error', 'Can\'t insert null value')
                return
            sql = 'insert into student(Sid, Sname, Sgender, Sage, Smajor) values ' + \
                  '(\'' + self.lineEdit_24.text() + '\', \'' + self.lineEdit_22.text() + '\',\'' + self.lineEdit_21.text() + '\',' \
                  + self.lineEdit_23.text() + ',\'' + self.lineEdit_25.text() + '\');'

        elif button == 'pushButton_17':
            # 判断是否插入空值
            if len(self.lineEdit_29.text().split()) * len(self.lineEdit_27.text().split()) * len(self.lineEdit_26.text().split()) * len(
                    self.lineEdit_28.text().split()) * len(self.lineEdit_30.text().split()) == 0:
                QMessageBox.critical(self, 'Error', 'Can\'t insert null value')
                return
            sql = 'insert into student_bed(semester, dorm_id, room_id, bed_id, Sid) values ' + \
                  '(\'' + self.lineEdit_29.text() + '\', \'' + self.lineEdit_27.text() + '\',\'' + self.lineEdit_26.text() + '\',\'' \
                  + self.lineEdit_28.text() + '\',\'' + self.lineEdit_30.text() + '\');'

        elif button == 'pushButton_20':
            # 判断是否插入空值
            if len(self.lineEdit_34.text().split()) * len(self.lineEdit_32.text().split()) * len(self.lineEdit_31.text().split()) * len(
                    self.lineEdit_33.text().split()) * len(self.lineEdit_35.text().split()) == 0:
                QMessageBox.critical(self, 'Error', 'Can\'t insert null value')
                return
            sql = 'insert into employee(Eid, Ename, Egender, Eage, E_phonenumber) values ' + \
                  '(\'' + self.lineEdit_34.text() + '\', \'' + self.lineEdit_32.text() + '\',\'' + self.lineEdit_31.text() + '\',' \
                  + self.lineEdit_33.text() + ',\'' + self.lineEdit_35.text() + '\');'

        elif button == 'pushButton_23':
            # 判断是否插入空值
            if len(self.lineEdit_39.text().split()) * len(self.lineEdit_37.text().split()) * len(self.lineEdit_36.text().split()) * len(
                    self.lineEdit_38.text().split()) == 0:
                QMessageBox.critical(self, 'Error', 'Can\'t insert null value')
                return
            sql = 'insert into employee_dorm(semester, Eid, dorm_id, job) values ' + '(\'' + self.lineEdit_39.text() + \
                  '\', \'' + self.lineEdit_37.text() + '\',\'' + self.lineEdit_36.text() + '\',\'' \
                  + self.lineEdit_38.text() + '\');'

        elif button == 'pushButton_26':
            # 判断是否插入空值
            if len(self.lineEdit_44.text().split()) * len(self.lineEdit_42.text().split()) * len(self.lineEdit_41.text().split()) * len(
                    self.lineEdit_43.text().split()) == 0:
                QMessageBox.critical(self, 'Error', 'Can\'t insert null value')
                return
            sql = 'insert into maintenance_worker(dorm_id, Mname, M_phonenumber, Mgender) values ' + \
                  '(\'' + self.lineEdit_44.text() + '\', \'' + self.lineEdit_42.text() + '\',\'' + \
                  self.lineEdit_41.text() + '\',\'' + self.lineEdit_43.text() + '\');'

        try:
            cursor.execute(sql)
            db.commit()
            QMessageBox.information(self, '提示', '插入成功')
        except pymysql.Error as err:
            QMessageBox.critical(self, 'Error', str(err))
        db.close()

    def delete(self):
        try:
            db = pymysql.connect(host='localhost', user='root', password='1235', database='studentdormitory')
            cursor = db.cursor()
        except pymysql.Error:
            print('连接数据库失败')
        button = ui.sender().objectName()  # 判断是哪个表下的删除
        condition = ''

        if button == 'pushButton_3':  # 公寓表查询
            if self.lineEdit_2.text() != '':
                condition += 'dorm_id like \'' + self.lineEdit_2.text() + '\' '
            else:
                condition += 'dorm_id like \'%\' '
            if len(self.lineEdit.text().split()) != 0:
                condition += 'and floors like \'' + self.lineEdit.text() + '\' '
            if len(self.lineEdit_4.text().split()) != 0:
                condition += 'and rooms like \'' + self.lineEdit_4.text() + '\' '
            if len(self.lineEdit_3.text().split()) != 0:
                condition += 'and has_bath like \'' + self.lineEdit_3.text() + '\' '
            if len(self.lineEdit_5.text().split()) != 0:
                condition += 'and built_year like \'' + self.lineEdit_5.text() + '\''
            sql = 'delete from dorm where ' + condition

        elif button == 'pushButton_6':
            if len(self.lineEdit_9.text().split()) != 0:
                condition += 'dorm_id like \'' + self.lineEdit_9.text() + '\' '
            else:
                condition += 'dorm_id like \'%\' '
            if len(self.lineEdit_7.text().split()) != 0:
                condition += 'and room_id like \'' + self.lineEdit_7.text() + '\' '
            if len(self.lineEdit_6.text().split()) != 0:
                condition += 'and beds like \'' + self.lineEdit_6.text() + '\' '
            if len(self.lineEdit_8.text().split()) != 0:
                condition += 'and has_ac like \'' + self.lineEdit_8.text() + '\' '
            sql = 'delete from room where ' + condition

        elif button == 'pushButton_12':
            if len(self.lineEdit_19.text().split()) != 0:
                condition += 'dorm_id like \'' + self.lineEdit_19.text() + '\' '
            else:
                condition += 'dorm_id like \'%\' '
            if len(self.lineEdit_17.text().split()) != 0:
                condition += 'and room_id like \'' + self.lineEdit_17.text() + '\' '
            if len(self.lineEdit_16.text().split()) != 0:
                condition += 'and bed_id like \'' + self.lineEdit_16.text() + '\' '
            if len(self.lineEdit_18.text().split()) != 0:
                condition += 'and is_long like \'' + self.lineEdit_18.text() + '\' '
            sql = 'delete from bed where ' + condition

        elif button == 'pushButton_15':
            if len(self.lineEdit_24.text().split()) != 0:
                condition += 'Sid like \'' + self.lineEdit_24.text() + '\' '
            else:
                condition += 'Sid like \'%\' '
            if len(self.lineEdit_22.text().split()) != 0:
                condition += 'and Sname like \'' + self.lineEdit_22.text() + '\' '
            if len(self.lineEdit_21.text().split()) != 0:
                condition += 'and Sgender like \'' + self.lineEdit_21.text() + '\' '
            if len(self.lineEdit_23.text().split()) != 0:
                condition += 'and Sage like \'' + self.lineEdit_23.text() + '\' '
            if len(self.lineEdit_25.text().split()) != 0:
                condition += 'and Smajor like \'' + self.lineEdit_25.text() + '\' '
            sql = 'delete from student where ' + condition

        elif button == 'pushButton_18':
            if len(self.lineEdit_29.text().split()) != 0:
                condition += 'semester like \'' + self.lineEdit_29.text() + '\' '
            else:
                condition += 'semester like \'%\' '
            if len(self.lineEdit_27.text().split()) != 0:
                condition += 'and dorm_id like \'' + self.lineEdit_27.text() + '\' '
            if len(self.lineEdit_26.text().split()) != 0:
                condition += 'and room_id like \'' + self.lineEdit_26.text() + '\' '
            if len(self.lineEdit_28.text().split()) != 0:
                condition += 'and bed_id like \'' + self.lineEdit_28.text() + '\' '
            if len(self.lineEdit_30.text().split()) != 0:
                condition += 'and Sid like \'' + self.lineEdit_30.text() + '\' '
            sql = 'delete from student_bed where ' + condition

        elif button == 'pushButton_21':
            if len(self.lineEdit_34.text().split()) != 0:
                condition += 'Eid like \'' + self.lineEdit_34.text() + '\' '
            else:
                condition += 'Eid like \'%\' '
            if len(self.lineEdit_32.text().split()) != 0:
                condition += 'and Ename like \'' + self.lineEdit_32.text() + '\' '
            if len(self.lineEdit_31.text().split()) != 0:
                condition += 'and Egender like \'' + self.lineEdit_31.text() + '\' '
            if len(self.lineEdit_33.text().split()) != 0:
                condition += 'and Eage like \'' + self.lineEdit_33.text() + '\' '
            if len(self.lineEdit_35.text().split()) != 0:
                condition += 'and E_phonenumber like \'' + self.lineEdit_35.text() + '\' '
            sql = 'delete from employee where ' + condition

        elif button == 'pushButton_24':
            if len(self.lineEdit_39.text().split()) != 0:
                condition += 'semester like \'' + self.lineEdit_39.text() + '\' '
            else:
                condition += 'semester like \'%\' '
            if len(self.lineEdit_37.text().split()) != 0:
                condition += 'and Eid like \'' + self.lineEdit_37.text() + '\' '
            if len(self.lineEdit_36.text().split()) != 0:
                condition += 'and dorm_id like \'' + self.lineEdit_36.text() + '\' '
            if len(self.lineEdit_38.text().split()) != 0:
                condition += 'and job like \'' + self.lineEdit_38.text() + '\' '
            sql = 'delete from employee_dorm where ' + condition

        elif button == 'pushButton_27':
            if len(self.lineEdit_44.text().split()) != 0:
                condition += 'dorm_id like \'' + self.lineEdit_44.text() + '\' '
            else:
                condition += 'dorm_id like \'%\' '
            if len(self.lineEdit_42.text().split()) != 0:
                condition += 'and Mname like \'' + self.lineEdit_42.text() + '\' '
            if len(self.lineEdit_41.text().split()) != 0:
                condition += 'and M_phonenumber like \'' + self.lineEdit_41.text() + '\' '
            if len(self.lineEdit_43.text().split()) != 0:
                condition += 'and Mgender like \'' + self.lineEdit_43.text() + '\' '
            sql = 'delete from maintenance_worker where ' + condition

        try:
            cursor.execute(sql)
            db.commit()
            QMessageBox.information(self, '提示', '删除成功')
        except pymysql.Error as err:
            QMessageBox.critical(self, 'Error', str(err))

        db.close()

    def connect_query(self):
        try:
            db = pymysql.connect(host='localhost', user='root', password='1235', database='studentdormitory')
            cursor = db.cursor()
        except pymysql.Error:
            print('连接数据库失败')
        sql = 'select distinct Sname from student, student_bed s1, student_bed s2 \
                where student.Sid=s1.Sid and student.Sid=s2.Sid and\
                s1.dorm_id like \'' + self.lineEdit_10.text() + '\' and s2.dorm_id like \'' + self.lineEdit_11.text() + '\';'
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        self.tableWidget_9.setRowCount(0)
        for row_num, row_data in enumerate(result):
            self.tableWidget_9.insertRow(row_num)
            for column_number, data in enumerate(row_data):
                self.tableWidget_9.setItem(row_num, column_number, QtWidgets.QTableWidgetItem(str(data)))
        db.close()

    def nested_query(self):
        try:
            db = pymysql.connect(host='localhost', user='root', password='1235', database='studentdormitory')
            cursor = db.cursor()
        except pymysql.Error:
            print('连接数据库失败')
        sql = 'select Ename from employee where Eid not in (select Eid from employee_dorm where dorm_id like \'' + \
              self.lineEdit_14.text() + '\');'
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        self.tableWidget_9.setRowCount(0)
        for row_num, row_data in enumerate(result):
            self.tableWidget_9.insertRow(row_num)
            for column_number, data in enumerate(row_data):
                self.tableWidget_9.setItem(row_num, column_number, QtWidgets.QTableWidgetItem(str(data)))
        db.close()

    def group_query(self):
        try:
            db = pymysql.connect(host='localhost', user='root', password='1235', database='studentdormitory')
            cursor = db.cursor()
        except pymysql.Error:
            print('连接数据库失败')
        sql = 'select Ename from employee where Eid in(select Eid from employee_dorm group by Eid having count(distinct job)>=2)'
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        self.tableWidget_9.setRowCount(0)
        for row_num, row_data in enumerate(result):
            self.tableWidget_9.insertRow(row_num)
            for column_number, data in enumerate(row_data):
                self.tableWidget_9.setItem(row_num, column_number, QtWidgets.QTableWidgetItem(str(data)))
        db.close()

    def view_query(self):
        try:
            db = pymysql.connect(host='localhost', user='root', password='1235', database='studentdormitory')
            cursor = db.cursor()
        except pymysql.Error:
            print('连接数据库失败')
        sql = 'select distinct dorm_id from student_bed where Sid in (select Sid from compstud);'
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        self.tableWidget_9.setRowCount(0)
        for row_num, row_data in enumerate(result):
            self.tableWidget_9.insertRow(row_num)
            for column_number, data in enumerate(row_data):
                self.tableWidget_9.setItem(row_num, column_number, QtWidgets.QTableWidgetItem(str(data)))
        db.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.setWindowTitle('学生公寓管理系统')
    ui.show()
    sys.exit(app.exec_())
