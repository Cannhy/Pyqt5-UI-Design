from db.DB import DB
from ui.BookMark_window import BookMark_window
import re
import time
import sys
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QDirModel, QLabel, QVBoxLayout
from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore
from ui.add_mark_new import AddMark_Dialog


class BookMark_controller(QtWidgets.QMainWindow):
    empty = re.compile(r"^\s*$")
    goBackToMainSignal = pyqtSignal(int)

    def __init__(self, userName: str, userPassword: str):
        super(BookMark_controller, self).__init__()
        self.flag = True
        self.ui = BookMark_window()
        self.ui.setupUi(self)
        self.dic = {'ID': 'ID', '名称': 'name', '书签': 'mark'}
        self.Addui = AddMark_Dialog()
        self.userName = userName
        self.userPassword = userPassword
        self.setup_control()

    def setup_control(self):
        self.importMarks()
        self.ui.tableWidget.itemChanged.connect(self.changeClicked)
        self.ui.fixButton.clicked.connect(self.fixButtonToggled)
        self.Addui.radioButton.clicked.connect(self.canteen_selected)
        self.Addui.radioButton_2.clicked.connect(self.counter_selected)
        self.Addui.radioButton_3.clicked.connect(self.dish_selected)
        self.Addui.canteen_lineedit2.currentTextChanged.connect(self.canteen2Changed)
        self.Addui.canteen_lineedit3.currentTextChanged.connect(self.canteen3Changed)
        self.Addui.counter_lineedit3.currentTextChanged.connect(self.counter3Changed)
        self.Addui.pushButton.clicked.connect(self.addOkClicked)
        self.ui.addButton.clicked.connect(self.addButtonClicked)
        self.ui.backButton.clicked.connect(self.backButtonClicked)
        self.ui.deleteButton.clicked.connect(self.deleteButtonClicked)

    def addButtonClicked(self):
        self.Addui.exec_()

    def canteen_selected(self):
        self.Addui.stackedWidget.setCurrentIndex(0)
        db = DB()
        self.Addui.canteen_lineedit1.clear()
        self.Addui.canteen_lineedit1.addItems(db.get_canteens())
        self.Addui.canteen_lineedit1.setStyleSheet("font:13pt")

    def counter_selected(self):
        self.Addui.stackedWidget.setCurrentIndex(1)
        db = DB()
        self.Addui.canteen_lineedit2.currentTextChanged.disconnect()
        self.Addui.canteen_lineedit2.clear()
        self.Addui.canteen_lineedit2.currentTextChanged.connect(self.canteen2Changed)
        self.Addui.canteen_lineedit2.addItems(db.get_canteens())
        self.Addui.canteen_lineedit2.setStyleSheet("font:13pt")

    def canteen2Changed(self):
        db = DB()
        self.Addui.counter_lineedit2.clear()
        self.Addui.counter_lineedit2.addItems(db.get_counters(self.Addui.canteen_lineedit2.currentText()))

    def dish_selected(self):
        self.Addui.stackedWidget.setCurrentIndex(2)
        db = DB()
        self.Addui.canteen_lineedit3.currentTextChanged.disconnect()
        self.Addui.canteen_lineedit3.clear()
        self.Addui.canteen_lineedit3.currentTextChanged.connect(self.canteen3Changed)
        self.Addui.canteen_lineedit3.addItems(db.get_canteens())
        self.Addui.canteen_lineedit3.setStyleSheet("font:13pt")

    def canteen3Changed(self):
        db = DB()
        self.Addui.counter_lineedit3.clear()
        self.Addui.counter_lineedit3.addItems(db.get_counters(self.Addui.canteen_lineedit3.currentText()))
        self.Addui.counter_lineedit3.setStyleSheet("font:13pt")

    def counter3Changed(self):
        db = DB()
        self.Addui.counter_lineedit3.currentTextChanged.disconnect()
        self.Addui.dish_lineedit3.clear()
        self.Addui.counter_lineedit3.currentTextChanged.connect(self.counter3Changed)
        self.Addui.dish_lineedit3.addItems(db.get_dishes(self.Addui.canteen_lineedit3.currentText(), self.Addui.counter_lineedit3.currentText()))
        self.Addui.dish_lineedit3.setStyleSheet("font:13pt")

    def addOkClicked(self):
        if not (self.Addui.radioButton.isChecked() or self.Addui.radioButton_2.isChecked() or self.Addui.radioButton_3.isChecked()):
            QMessageBox.information(self, 'Error', '请选择添加类型', QMessageBox.Ok)
            return
        db = DB()
        key_list = []
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)
        item = QTableWidgetItem(str(row + 1))
        key_list.append(row + 1)
        item.setFont(QFont('Consolas', 15))
        self.ui.tableWidget.setItem(row, 0, item)
        if self.Addui.radioButton.isChecked():
            item = QTableWidgetItem(self.Addui.canteen_lineedit1.currentText())
            key_list.append(self.Addui.canteen_lineedit1.currentText())
            item.setFont(QFont('Consolas', 15))
            self.ui.tableWidget.setItem(row, 1, item)
            item = QTableWidgetItem(self.Addui.mark_lineedit1.text())
            key_list.append(self.Addui.mark_lineedit1.text())
            item.setFont(QFont('Consolas', 15))
            self.ui.tableWidget.setItem(row, 2, item)
        elif self.Addui.radioButton_2.isChecked():
            item = QTableWidgetItem(self.Addui.canteen_lineedit2.currentText() + ' -> ' + self.Addui.counter_lineedit2.currentText())
            key_list.append(self.Addui.canteen_lineedit2.currentText() + ' -> ' + self.Addui.counter_lineedit2.currentText())
            item.setFont(QFont('Consolas', 15))
            self.ui.tableWidget.setItem(row, 1, item)
            item = QTableWidgetItem(self.Addui.mark_lineedit2.text())
            key_list.append(self.Addui.mark_lineedit2.text())
            item.setFont(QFont('Consolas', 15))
            self.ui.tableWidget.setItem(row, 2, item)
        elif self.Addui.radioButton_3.isChecked():
            item = QTableWidgetItem(
                self.Addui.canteen_lineedit3.currentText() + ' -> ' + self.Addui.counter_lineedit3.currentText() + ' -> ' + self.Addui.dish_lineedit3.currentText())
            key_list.append(self.Addui.canteen_lineedit3.currentText() + ' -> ' + self.Addui.counter_lineedit3.currentText() + ' -> ' + self.Addui.dish_lineedit3.currentText())
            item.setFont(QFont('Consolas', 15))
            self.ui.tableWidget.setItem(row, 1, item)
            item = QTableWidgetItem(self.Addui.mark_lineedit3.text())
            key_list.append(self.Addui.mark_lineedit3.text())
            item.setFont(QFont('Consolas', 15))
            self.ui.tableWidget.setItem(row, 2, item)
        db.insert_mark(self.userName, key_list)
        self.Addui.close()

    def fixButtonToggled(self):
        if self.flag:
            QMessageBox.information(self, "hint", "双击单元格即可修改 书签ID无法修改", QMessageBox.Ok)
            self.ui.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
            for row in range(self.ui.tableWidget.rowCount()):
                item = self.ui.tableWidget.item(row, 0)
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            # self.ui.treeWidget.setFlags(self.ui.treeWidget.flags() | QtCore.Qt.ItemIsEditable)
            #self.ui.treeWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        else:
            self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
            # self.ui.treeWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.flag = not self.flag

    def backButtonClicked(self):
        self.goBackToMainSignal.emit(3)
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.flag = True

    def deleteButtonClicked(self):
        if len(self.ui.tableWidget.selectedItems()) == 0:
            QMessageBox.information(self, '提示', '请选择要删除的书签(可多选)', QMessageBox.Ok)
            return
        if QMessageBox.question(self, '确认', '您确定要删除选中的所有书签吗?') == QMessageBox.Yes:
            sets = set([])
            for item in self.ui.tableWidget.selectedItems():
                sets.add(item.row())
            des = list(sets)
            des.reverse()
            delDes = []
            toDel = []
            for row in des:
                delDes.append(int(self.ui.tableWidget.item(row, 0).text()))
                temp = [self.ui.tableWidget.item(row, 0).text(), self.ui.tableWidget.item(row, 1).text(), self.ui.tableWidget.item(row, 2).text()]
                toDel.append(temp)
                self.ui.tableWidget.removeRow(row)
            db = DB()
            db.delete_mark(delDes, self.userName)

    def changeClicked(self):
        if not self.flag:
            row = self.ui.tableWidget.currentRow()
            col = self.ui.tableWidget.currentColumn()
            iD = int(self.ui.tableWidget.item(row, 0).text())
            db = DB()
            db.fix_mark(self.userName, self.dic[self.ui.tableWidget.horizontalHeaderItem(col).text()], self.ui.tableWidget.currentItem().text(), iD)

    def importMarks(self):
        db = DB()
        res = db.get_marks(self.userName)
        for row in range(len(res)):
            rownum = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rownum)
            for col in range(len(res[row])):
                item = QTableWidgetItem(str(res[row][col]))
                item.setFont(QFont('Consolas', 15))
                self.ui.tableWidget.setItem(rownum, col, item)
