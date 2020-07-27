import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QMessageBox, QPushButton, QCheckBox, QLineEdit, QTextEdit, QGridLayout, QApplication, QMessageBox, QListWidget, \
    QHBoxLayout, QVBoxLayout


class Example(QWidget):

    def __init__(self):
        super().__init__()
        # 工号 姓名 性别 年龄 职位 住址 工资
        id = QCheckBox('工号', self)
        name = QCheckBox('姓名', self)
        gender = QCheckBox('性别', self)
        age = QCheckBox('年龄', self)
        position = QCheckBox('职位', self)
        address = QCheckBox('住址', self)
        salary = QCheckBox('工资', self)

        id_edit = QLineEdit()
        id_edit.resize(5, 6)
        self.name_edit = QLineEdit()
        gender_edit = QLineEdit()
        age_edit = QLineEdit()
        position_edit = QLineEdit()
        address_edit = QLineEdit()
        salary_edit = QLineEdit()

        btn = QPushButton('查询')
        btn.clicked.connect(self.query)

        grid = QGridLayout()
        grid.setVerticalSpacing(1)
        grid.setHorizontalSpacing(10)

        grid.addWidget(id, 1, 0)
        grid.addWidget(id_edit, 1, 1)

        grid.addWidget(name, 1, 2)
        grid.addWidget(self.name_edit, 1, 3)

        grid.addWidget(gender, 2, 0)
        grid.addWidget(gender_edit, 2, 1)

        grid.addWidget(age, 2, 2)
        grid.addWidget(age_edit, 2, 3)

        grid.addWidget(position, 3, 0)
        grid.addWidget(position_edit, 3, 1)

        grid.addWidget(address, 3, 2)
        grid.addWidget(address_edit, 3, 3)

        grid.addWidget(salary, 4, 0)
        grid.addWidget(salary_edit, 4, 1)

        grid.addWidget(btn, 4, 2)

        self.setLayout(grid)
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Review')
        self.show()

    # TODO 获得所有复选框、输入，构建查询语句
    # TODO 构建数据库

    def query(self):
        text = self.name_edit.text()
        inf = QMessageBox.information(self, 'inf', text)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


