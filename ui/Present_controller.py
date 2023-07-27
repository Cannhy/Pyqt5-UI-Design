import re
import time
import sys
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QDirModel, QLabel, QVBoxLayout
from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore

from db.DB import DB
from db.user import User
from ui.Main_window import Main_window
from ui.Present_window import Present_window
from ui.present_add_window import present_add
from ui.present_sub_window import present_sub


class Present_controller(QtWidgets.QMainWindow):
    empty = re.compile(r"^\s*$")
    goBackToMainSignal = pyqtSignal(int)

    def __init__(self, userName: str, userPassword: str):
        super(Present_controller, self).__init__()
        self.flag = True
        self.ui = Present_window()
        self.dic = {'餐品': 'name', '食堂': 'canteen', '档口': 'counter', '价格': 'price', '时间': 'times', 'ID': 'dish_id'}
        db = DB()
        self.canteen_counter = db.canteen_counter_search()
        self.addUi = present_add()
        self.subUI = present_sub()
        self.ui.setupUi(self, self.canteen_counter)
        self.userName = userName
        self.canteen = [i[0] for i in self.canteen_counter]
        self.counter = []
        self.userPassword = userPassword
        self.setup_control()

    def setup_control(self):
        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.ui.fixButton.clicked.connect(self.fixButtonToggled)
        self.ui.tableWidget.itemChanged.connect(self.changeClicked)
        self.ui.addButton.clicked.connect(self.addButtonClicked)
        self.addUi.radioCanteen.clicked.connect(self.canteen_add_selected)
        self.addUi.radioCounter.clicked.connect(self.counter_add_selected)
        self.addUi.radiodish.clicked.connect(self.dish_add_selected)
        self.addUi.canteen_lineedit3.currentTextChanged.connect(self.canteen3Changed)
        self.addUi.pushButton.clicked.connect(self.add_ok)
        self.subUI.radioCanteen.clicked.connect(self.canteen_sub_selected)
        self.subUI.radioCounter.clicked.connect(self.counter_sub_selected)
        self.subUI.radioDish.clicked.connect(self.dish_sub_selected)
        self.subUI.canteen_lineedit2.currentTextChanged.connect(self.canteen2Changed)
        self.subUI.pushButton.clicked.connect(self.del_ok)
        self.ui.backButton.clicked.connect(self.goBackToMainSignal.emit)
        self.ui.deleteButton.clicked.connect(self.deleteButtonClicked)
        self.ui.treeWidget.clicked.connect(self.treeClicked)

    def changeClicked(self):
        if not self.flag:
            if self.ui.tableWidget.currentRow() > 0:
                row = self.ui.tableWidget.currentRow()
                col = self.ui.tableWidget.currentColumn()
                iD = int(self.ui.tableWidget.item(row, 5).text())
                db = DB()
                db.present_fix(self.dic[self.ui.tableWidget.horizontalHeaderItem(col).text()],
                               self.ui.tableWidget.currentItem().text(), iD)

    def fixButtonToggled(self):
        if self.flag:
            QMessageBox.information(self, "hint", "双击单元格即可修改 菜品ID无法修改", QMessageBox.Ok)
            self.ui.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
            # self.ui.treeWidget.setFlags(self.ui.treeWidget.flags() | QtCore.Qt.ItemIsEditable)
            # self.ui.treeWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
            if self.ui.tableWidget.rowCount() > 0:
                for row in range(self.ui.tableWidget.rowCount()):
                    item = self.ui.tableWidget.item(row, 5)
                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        else:
            self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
            # self.ui.treeWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.flag = not self.flag

    def treeClicked(self):
        item = self.ui.treeWidget.currentItem()
        if item.text(0) not in self.canteen:
            db = DB()
            result = db.present_search(item.parent().text(0), item.text(0))
            self.ui.tableWidget.setRowCount(len(result))
            self.ui.tableWidget.setColumnCount(6)
            self.ui.tableWidget.setHorizontalHeaderLabels(['餐品', '档口', '价格', '口味', '时间', 'ID'])
            for i in range(len(result)):
                for j in range(6):
                    if j == 5:
                        data = QTableWidgetItem(str(result[i][8]))
                    elif j == 1:
                        data = QTableWidgetItem(str(result[i][2]))
                    elif j == 2:
                        data = QTableWidgetItem(str(result[i][3]))
                    elif j == 3:
                        data = QTableWidgetItem(str(result[i][6]))
                    else:
                        data = QTableWidgetItem(str(result[i][j]))
                    self.ui.tableWidget.setItem(i, j, data)
                    self.ui.tableWidget.item(i, j).setFont(QFont('Consolas', 15))
                    self.ui.tableWidget.setWordWrap(True)

    def addButtonClicked(self):
        self.addUi.exec_()

    def canteen_add_selected(self):
        self.addUi.stackedWidget.setCurrentIndex(0)

    def counter_add_selected(self):
        self.addUi.stackedWidget.setCurrentIndex(1)
        db = DB()
        self.addUi.canteen_lineedit2.clear()
        self.addUi.canteen_lineedit2.addItems(db.get_canteens())

    def dish_add_selected(self):
        self.addUi.stackedWidget.setCurrentIndex(2)
        db = DB()
        self.addUi.canteen_lineedit3.currentTextChanged.disconnect()
        self.addUi.canteen_lineedit3.clear()
        self.addUi.canteen_lineedit3.currentTextChanged.connect(self.canteen3Changed)
        self.addUi.canteen_lineedit3.addItems(db.get_canteens())

    def canteen3Changed(self):
        db = DB()
        self.addUi.counter_lineedit3.clear()
        self.addUi.counter_lineedit3.addItems(db.get_counters(self.addUi.canteen_lineedit3.currentText()))

    def add_ok(self):
        _translate = QtCore.QCoreApplication.translate
        if self.addUi.radioCanteen.isChecked():
            text = self.addUi.canteen_lineedit1.text()
            if text not in self.canteen:
                self.canteen.append(text)
                db = DB()
                db.present_add(text, 1)
                item = QTreeWidgetItem()
                self.ui.treeWidget.addTopLevelItem(item)
                self.ui.treeWidget.topLevelItem(self.ui.treeWidget.topLevelItemCount() - 1).setText(0, _translate(
                    "MainWindow", text))
                self.ui.treeWidget.topLevelItem(self.ui.treeWidget.topLevelItemCount() - 1).setFont(0, QFont('Consolas',
                                                                                                             13))
            else:
                QMessageBox.critical(self, "错误", "该食堂已存在！", QMessageBox.Ok)
                return
        if self.addUi.radioCounter.isChecked():
            db = DB()
            text = self.addUi.canteen_lineedit2.currentText() + ' ' + self.addUi.counter_lineedit2.text()
            if db.present_add(text, 2):
                QMessageBox.critical(self, "错误", "该档口已存在！", QMessageBox.Ok)
                return
            else:
                self.updateCounter(text)
        if self.addUi.radiodish.isChecked():
            text = self.addUi.dish_lineedit3.text() + ' ' + self.addUi.canteen_lineedit3.currentText() + ' ' + self.addUi.counter_lineedit3.currentText() \
                   + ' ' + self.addUi.price_lineedit3.text() + ' ' + self.addUi.time_lineedit3.currentText() + ' ' + self.addUi.taste_edit3.currentText() + ' ' + self.addUi.nutri_edit3.currentText()
            db = DB()
            db.present_add(text, 3)
            QMessageBox.information(self, "Okk", "添加成功", QMessageBox.Ok)
        self.addUi.close()

    def deleteButtonClicked(self):
        self.subUI.exec_()

    def canteen_sub_selected(self):
        self.subUI.stackedWidget.setCurrentIndex(0)
        db = DB()
        self.subUI.canteen_lineedit1.clear()
        self.subUI.canteen_lineedit1.addItems(db.get_canteens())

    def counter_sub_selected(self):
        self.subUI.stackedWidget.setCurrentIndex(1)
        db = DB()
        self.subUI.canteen_lineedit2.currentTextChanged.disconnect()
        self.subUI.canteen_lineedit2.clear()
        self.subUI.canteen_lineedit2.currentTextChanged.connect(self.canteen2Changed)
        self.subUI.canteen_lineedit2.addItems(db.get_canteens())

    def dish_sub_selected(self):
        self.subUI.stackedWidget.setCurrentIndex(2)

    def canteen2Changed(self):
        db = DB()
        self.subUI.counter_lineedit2.clear()
        self.subUI.counter_lineedit2.addItems(db.get_counters(self.subUI.canteen_lineedit2.currentText()))

    def del_ok(self):
        _translate = QtCore.QCoreApplication.translate
        if self.subUI.radioCanteen.isChecked():
            text = self.subUI.canteen_lineedit1.currentText()
            self.canteen.remove(text)
            db = DB()
            db.present_del(text, 1)
            self.deleteRoot(text)
        if self.subUI.radioCounter.isChecked():
            db = DB()
            text = self.subUI.canteen_lineedit2.currentText() + ' ' + self.subUI.counter_lineedit2.currentText()
            db.present_del(text, 2)
            self.deleteCounter(text)
        if self.subUI.radioDish.isChecked():
            text = self.subUI.dish_lineedit3.text()
            db = DB()
            if not text.isdigit():
                QMessageBox.critical(self, "错误", "请输入要删除的餐品ID", QMessageBox.Ok)
                return
            if not db.present_del(text, 3):
                QMessageBox.critical(self, "错误", "要删除的菜品不存在", QMessageBox.Ok)
                return
            else:
                QMessageBox.information(self, "Okk", "删除成功", QMessageBox.Ok)
        self.subUI.close()

    def updateCounter(self, des):
        n = self.ui.treeWidget.topLevelItemCount()
        for i in range(n):
            item = self.ui.treeWidget.topLevelItem(i)
            text = item.text(0)
            if text == des.split()[0]:
                item = QTreeWidgetItem()
                self.ui.treeWidget.topLevelItem(i).addChild(item)
                item.setText(0, des.split()[1])
                return

    def deleteRoot(self, des):
        n = self.ui.treeWidget.topLevelItemCount()
        for i in range(n):
            item = self.ui.treeWidget.topLevelItem(i)
            text = item.text(0)
            if text == des:
                self.ui.treeWidget.takeTopLevelItem(i)
                return

    def deleteCounter(self, des):
        n = self.ui.treeWidget.topLevelItemCount()
        for i in range(n):
            item = self.ui.treeWidget.topLevelItem(i)
            text = item.text(0)
            if text == des.split()[0]:
                childcount = item.childCount()
                for j in range(childcount):
                    if des.split()[1] == item.child(j).text(0):
                        self.ui.treeWidget.topLevelItem(i).takeChild(j)
                        return
