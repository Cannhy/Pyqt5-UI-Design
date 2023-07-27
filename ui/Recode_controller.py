import re
import time
import sys
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QDirModel, QLabel, QVBoxLayout
from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore
from ui.addRecord import Ui_Dialog
from db.DB import DB

from ui.Record_window import Record_window

'''
def deleteButtonClicked():
    dialog = QDialog()
    dialog.resize(400, 300)
    dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)
    label = QtWidgets.QLabel(dialog)
    label.setGeometry(QtCore.QRect(50, 70, 72, 31))
    font = QtGui.QFont()
    font.setPointSize(14)
    label.setStyleSheet("font: 14pt")
    label.setObjectName("label")
    lineEdit = QtWidgets.QLineEdit(dialog)
    lineEdit.setGeometry(QtCore.QRect(120, 70, 211, 31))
    lineEdit.setObjectName("lineEdit")
    label_2 = QtWidgets.QLabel(dialog)
    label_2.setGeometry(QtCore.QRect(50, 140, 72, 31))
    font = QtGui.QFont()
    font.setPointSize(14)
    label_2.setStyleSheet("font: 14pt")
    label_2.setObjectName("label_2")
    lineEdit_2 = QtWidgets.QLineEdit(dialog)
    lineEdit_2.setGeometry(QtCore.QRect(120, 140, 211, 31))
    lineEdit_2.setObjectName("lineEdit_2")
    pushButton = QtWidgets.QPushButton(dialog)
    pushButton.setGeometry(QtCore.QRect(180, 240, 101, 41))
    font = QtGui.QFont()
    font.setPointSize(14)
    pushButton.setStyleSheet("font: 14pt")
    pushButton.setObjectName("pushButton")
    pushButton_2 = QtWidgets.QPushButton(dialog)
    pushButton_2.setGeometry(QtCore.QRect(290, 240, 101, 41))
    font = QtGui.QFont()
    font.setPointSize(14)
    pushButton_2.setStyleSheet("font: 14pt")
    pushButton_2.setObjectName("pushButton_2")
    pushButton_2.clicked.connect(dialog.close)

    _translate = QtCore.QCoreApplication.translate
    dialog.setWindowTitle(_translate("Dialog", "删除记录"))
    label.setText(_translate("Dialog", "菜名:"))
    label_2.setText(_translate("Dialog", "书签:"))
    pushButton.setText(_translate("Dialog", "确定"))
    pushButton_2.setText(_translate("Dialog", "取消"))
    QtCore.QMetaObject.connectSlotsByName(dialog)
    dialog.setWindowModality(Qt.ApplicationModal)
    dialog.exec()  # t弹出对话框
'''


class Record_controller(QtWidgets.QMainWindow):
    empty = re.compile(r"^\s*$")
    goBackToMainSignal = pyqtSignal(int)

    def __init__(self, userName: str, userPassword: str):
        super(Record_controller, self).__init__()
        self.flag = True
        self.ui = Record_window()
        self.ui.setupUi(self)
        self.dic = {'餐厅': 'canteen', '档口': 'counter', '菜品': 'dish', '日期': 'date', '时间': 'times', 'ID': 'ID'}
        self.userName = userName
        self.userPassword = userPassword
        self.setup_control()

    def setup_control(self):
        self.importRecord()
        self.ui.fixButton.clicked.connect(self.fixButtonToggled)
        self.ui.tableWidget.itemChanged.connect(self.changeClicked)
        self.ui.addButton.clicked.connect(self.addButtonClicked)
        self.ui.backButton.clicked.connect(self.backButtonClicked)
        self.ui.deleteButton.clicked.connect(self.deleteButtonClicked)

    def fixButtonToggled(self):
        if self.flag:
            QMessageBox.information(self, "hint", "双击单元格即可修改 记录ID无法修改", QMessageBox.Ok)
            self.ui.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
            for row in range(self.ui.tableWidget.rowCount()):
                item = self.ui.tableWidget.item(row, 5)
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        else:
            self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.flag = not self.flag

    def changeClicked(self):
        if not self.flag:
            row = self.ui.tableWidget.currentRow()
            col = self.ui.tableWidget.currentColumn()
            iD = int(self.ui.tableWidget.item(row, 5).text())
            db = DB()
            db.fix_record(self.userName, self.dic[self.ui.tableWidget.horizontalHeaderItem(col).text()], self.ui.tableWidget.currentItem().text(), iD)

    def backButtonClicked(self):
        self.goBackToMainSignal.emit(2)
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.flag = True

    def addButtonClicked(self):
        dialog = QDialog()
        dialog.resize(400, 366)
        dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        label = QtWidgets.QLabel(dialog)
        label.setGeometry(QtCore.QRect(60, 30, 72, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        label.setStyleSheet("font: 14pt")
        label.setObjectName("label")
        label_2 = QtWidgets.QLabel(dialog)
        label_2.setGeometry(QtCore.QRect(60, 90, 72, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        label_2.setStyleSheet("font: 14pt")
        label_2.setObjectName("label_2")
        pushButton = QtWidgets.QPushButton(dialog)
        pushButton.setGeometry(QtCore.QRect(210, 320, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        pushButton.setStyleSheet("font: 14pt")
        pushButton.setObjectName("pushButton")
        pushButton_2 = QtWidgets.QPushButton(dialog)
        pushButton_2.setGeometry(QtCore.QRect(310, 320, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        pushButton_2.setStyleSheet("font: 14pt")
        pushButton_2.setObjectName("pushButton_2")
        label_3 = QtWidgets.QLabel(dialog)
        label_3.setGeometry(QtCore.QRect(60, 150, 72, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        label_3.setStyleSheet("font: 14pt")
        label_3.setObjectName("label_3")
        label_4 = QtWidgets.QLabel(dialog)
        label_4.setGeometry(QtCore.QRect(60, 270, 72, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        label_4.setStyleSheet("font: 14pt")
        label_4.setObjectName("label_4")
        comboBox = QtWidgets.QComboBox(dialog)
        comboBox.setGeometry(QtCore.QRect(130, 30, 191, 31))
        comboBox.setObjectName("comboBox")
        comboBox_2 = QtWidgets.QComboBox(dialog)
        comboBox_2.setGeometry(QtCore.QRect(130, 90, 191, 31))
        comboBox_2.setObjectName("comboBox_2")
        comboBox_3 = QtWidgets.QComboBox(dialog)
        comboBox_3.setGeometry(QtCore.QRect(130, 150, 191, 31))
        comboBox_3.setObjectName("comboBox_3")
        comboBox_4 = QtWidgets.QComboBox(dialog)
        comboBox_4.setGeometry(QtCore.QRect(130, 270, 191, 31))
        comboBox_4.setObjectName("comboBox_4")
        comboBox_4.addItem("")
        comboBox_4.addItem("")
        comboBox_4.addItem("")
        comboBox_4.setStyleSheet("font: 14pt")
        comboBox.setStyleSheet("font: 14pt")
        label_5 = QtWidgets.QLabel(dialog)
        label_5.setGeometry(QtCore.QRect(60, 210, 72, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        label_5.setStyleSheet("font: 14pt")
        label_5.setObjectName("label_5")
        dateEdit = QtWidgets.QDateEdit(dialog)
        dateEdit.setGeometry(QtCore.QRect(130, 210, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        dateEdit.setStyleSheet("font: 13pt")
        dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 7, 31), QtCore.QTime(0, 0, 0)))
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("Dialog", "添加记录"))
        label.setText(_translate("Dialog", "餐厅:"))
        label_2.setText(_translate("Dialog", "档口:"))
        pushButton.setText(_translate("Dialog", "确定"))
        pushButton_2.setText(_translate("Dialog", "取消"))
        pushButton_2.clicked.connect(dialog.close)
        label_3.setText(_translate("Dialog", "菜品:"))
        label_4.setText(_translate("Dialog", "时间:"))
        comboBox_4.setItemText(0, _translate("Dialog", "早餐"))
        comboBox_4.setItemText(1, _translate("Dialog", "午餐"))
        comboBox_4.setItemText(2, _translate("Dialog", "晚餐"))
        label_5.setText(_translate("Dialog", "日期:"))

        QtCore.QMetaObject.connectSlotsByName(dialog)
        db = DB()
        comboBox.addItem('请选择餐厅')
        comboBox.insertSeparator(1)
        comboBox.addItems(db.get_canteens())
        comboBox.currentTextChanged.connect(lambda: self.canteen_changed(comboBox.currentText(), comboBox_2))
        comboBox_2.currentTextChanged.connect(lambda: self.counter_changed(comboBox.currentText(), comboBox_2.currentText(), comboBox_3))
        pushButton.clicked.connect(lambda: self.addClicked(comboBox.currentText(), comboBox_2.currentText(), comboBox_3.currentText(), dateEdit.text(), comboBox_4.currentText(), dialog))
        dialog.exec_()

    def deleteButtonClicked(self):
        if len(self.ui.tableWidget.selectedItems()) == 0:
            QMessageBox.information(self, '提示', '请选择要删除的记录(可多选)', QMessageBox.Ok)
            return
        if QMessageBox.question(self, '确认', '您确定要删除选中的所有记录吗?') == QMessageBox.Yes:
            sets = set([])
            for item in self.ui.tableWidget.selectedItems():
                sets.add(item.row())
            des = list(sets)
            des.reverse()
            delDes = []
            toDel = []
            for row in des:
                delDes.append(int(self.ui.tableWidget.item(row, 5).text()))
                temp = [self.ui.tableWidget.item(row, 0).text(), self.ui.tableWidget.item(row, 1).text(), self.ui.tableWidget.item(row, 2).text()]
                toDel.append(temp)
                self.ui.tableWidget.removeRow(row)
            db = DB()
            db.delete_record(delDes, self.userName)
            db.sub_eaten_time(toDel, self.userName)

    def canteen_changed(self, canteen, combox):
        if canteen != '请选择餐厅':
            db = DB()
            combox.clear()
            combox.addItems(db.get_counters(canteen))
            combox.setStyleSheet("font: 13pt")

    def counter_changed(self, canteen, counter, combox):
        db = DB()
        combox.clear()
        combox.addItems(db.get_dishes(canteen, counter))
        combox.setStyleSheet("font: 13pt")

    def addClicked(self, can, cou, dis, dat, tim, dialog):
        row = self.ui.tableWidget.rowCount()
        list2 = [can, cou, dis, dat, tim, row + 1]
        if list2[0] == '请选择餐厅':
            QMessageBox.critical(self, 'Error', '请选择正确的餐厅名字!', QMessageBox.Ok)
            return
        self.ui.tableWidget.insertRow(row)
        for i in range(self.ui.tableWidget.columnCount()):
            item = QTableWidgetItem(str(list2[i]))
            item.setFont(QFont('Consolas', 15))
            self.ui.tableWidget.setItem(row, i, item)
        db = DB()
        db.insert_record(list2, self.userName)
        db.add_eaten_time(list2, self.userName)
        dialog.close()

    def importRecord(self):
        db = DB()
        res = db.get_record(self.userName)
        for row in range(len(res)):
            rownum = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rownum)
            for col in range(len(res[row])):
                item = QTableWidgetItem(str(res[row][col]))
                item.setFont(QFont('Consolas', 15))
                self.ui.tableWidget.setItem(rownum, col, item)
