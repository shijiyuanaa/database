import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(919, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(770, 30, 111, 51))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 351, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_5 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_2.addWidget(self.checkBox_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_7 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.horizontalLayout_4.addWidget(self.checkBox_7)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_4.addWidget(self.lineEdit_5)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_3.addWidget(self.checkBox_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(410, 10, 311, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkBox_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_5.addWidget(self.checkBox_4)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_5.addWidget(self.lineEdit_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.checkBox_6 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_6.setObjectName("checkBox_6")
        self.horizontalLayout_7.addWidget(self.checkBox_6)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_7.addWidget(self.lineEdit_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_8.addWidget(self.checkBox_3)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_8.addWidget(self.lineEdit_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 220, 901, 101))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 200, 72, 15))
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 360, 901, 300))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(125)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 340, 72, 15))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(770, 110, 111, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 919, 26))
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
        self.pushButton.setText(_translate("MainWindow", "查询"))
        self.checkBox.setText(_translate("MainWindow", "学号"))
        self.checkBox_5.setText(_translate("MainWindow", "姓名"))
        self.checkBox_7.setText(_translate("MainWindow", "年龄"))
        self.label.setText(_translate("MainWindow", "到"))
        self.checkBox_2.setText(_translate("MainWindow", "性别"))
        self.checkBox_4.setText(_translate("MainWindow", "专业"))
        self.checkBox_6.setText(_translate("MainWindow", "班级"))
        self.checkBox_3.setText(_translate("MainWindow", "生源地"))
        self.label_2.setText(_translate("MainWindow", "SQL语句"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "学号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "年龄"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "性别"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "专业"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "班级"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "生源地"))
        self.label_3.setText(_translate("MainWindow", "查询结果"))
        self.pushButton_2.setText(_translate("MainWindow", "清空"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.query)
        self.pushButton_2.clicked.connect(self.clear)

    def query(self):
        try:
            db = pymysql.connect(host='localhost', user='root', password='1235', database='extra_lab1')
            cursor = db.cursor()
        except pymysql.Error:
            print('Fail to connect to database')
        sql = 'select * from student'
        is_first = True
        if self.checkBox.isChecked() and len(self.lineEdit.text().split()) != 0:
            sql += ' where Sid like \'' + self.lineEdit.text() + '\''
            is_first = False
        if self.checkBox_5.isChecked() and len(self.lineEdit_2.text().split()) != 0:
            if is_first:
                sql += ' where Sname like \'' + self.lineEdit_2.text() + '\''
                is_first = False
            else:
                sql += ' and Sname like \'' + self.lineEdit_2.text() + '\''
        if self.checkBox_7.isChecked():
            if len(self.lineEdit_5.text().split()) != 0:
                if is_first:
                    sql += ' where Sage>=' + self.lineEdit_5.text()
                    is_first = False
                else:
                    sql += ' and Sage>=' + self.lineEdit_5.text()
            if len(self.lineEdit_4.text().split()) != 0:
                if is_first:
                    sql += ' where Sage<=' + self.lineEdit_4.text()
                    is_first =False
                else:
                    sql += ' and Sage<=' + self.lineEdit_4.text()
        if self.checkBox_2.isChecked() and len(self.lineEdit_3.text().split()) != 0:
            if is_first:
                sql += ' where Sgender like \'' + self.lineEdit_3.text() + '\''
                is_first = False
            else:
                sql += ' and Sgender like \'' + self.lineEdit_3.text() + '\''
        if self.checkBox_4.isChecked() and len(self.lineEdit_6.text().split()) != 0:
            if is_first:
                sql += ' where Smajor like \'' + self.lineEdit_6.text() + '\''
                is_first = False
            else:
                sql += ' and Smajor like \'' + self.lineEdit_6.text() + '\''
        if self.checkBox_6.isChecked() and len(self.lineEdit_8.text().split()) != 0:
            if is_first:
                sql += ' where Sclass like \'' + self.lineEdit_8.text() + '\''
                is_first = False
            else:
                sql += ' and Sclass like \'' + self.lineEdit_8.text() + '\''
        if self.checkBox_3.isChecked() and len(self.lineEdit_9.text().split()) != 0:
            if is_first:
                sql += ' where Sorigin like \'' + self.lineEdit_9.text() + '\''
            else:
                sql += ' and Sorigin like \'' + self.lineEdit_9.text() + '\''

        self.textBrowser.setText(sql)
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_num, row_data in enumerate(result):
                self.tableWidget.insertRow(row_num)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_num, column_number, QtWidgets.QTableWidgetItem(str(data)))
        except pymysql.Error as e:
            print('查询失败')

    def clear(self):
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_5.setText('')
        self.lineEdit_6.setText('')
        self.lineEdit_8.setText('')
        self.lineEdit_9.setText('')
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_6.setChecked(False)
        self.checkBox_7.setChecked(False)
        self.textBrowser.setText('')
        self.tableWidget.setRowCount(0)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.setWindowTitle('动态构造SQL')
    ui.show()
    sys.exit(app.exec_())