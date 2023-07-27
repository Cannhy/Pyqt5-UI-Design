import re
import time
import sys

import qtawesome as qtawesome
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QDirModel, QLabel, QVBoxLayout
from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore

from db.DB import DB
from ui.Communicate_window import communicate_window
from ui.GetComment import GetComment


class Communicate_controller(QtWidgets.QMainWindow):
    empty = re.compile(r"^\s*$")
    goBackToMainSignal = pyqtSignal(int)

    def __init__(self, userName: str, userPassword: str):
        super(Communicate_controller, self).__init__()
        self.ui = communicate_window()
        self.ui.setupUi(self)
        self.ReplyFlag = False
        self.userName = userName
        self.replyName = ''
        self.userPassword = userPassword
        self.setup_control()

    def setup_control(self):
        self.ui.backButton.clicked.connect(self.backButtonClicked)
        self.importComment()
        # self.ui.delButton.clicked.connect(self.delButtonClicked)
        self.ui.cancelButton.setHidden(True)
        self.ui.cancelButton.clicked.connect(self.cancelButtonClicked)
        self.ui.emitButton.clicked.connect(lambda: self.emitButtonClicked(self.ui.lineEdit.text()))

    def delButtonClicked(self):
        self.ui.tableWidget.removeRow(0)

    def backButtonClicked(self):
        self.goBackToMainSignal.emit(5)

    def cancelButtonClicked(self):
        self.ReplyFlag = False
        self.ui.lineEdit.clear()
        self.ui.lineEdit.setPlaceholderText('选择菜品评论或者点击头像回复~')
        self.ui.cancelButton.setHidden(True)

    def emitButtonClicked(self, text):
        if not text == '':
            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
            current_time = time.strftime(" %Y年%m月%d日  %H:%M:%S ", time.localtime(time.time()))
            item = {'uname': self.userName, 'create_time': current_time, 'like_count': 0, 'is_uped': 0, 'id': '123',
                    'content': text, 'type': 0, 'receiver': ''}
            if self.ReplyFlag:
                item['type'] = 1
                item['receiver'] = self.replyName
            else:
                item['receiver'] = self.ui.comboBox.currentText() + '-' + self.ui.comboBox_2.currentText() + '-' + self.ui.comboBox_3.currentText()
            db = DB()
            item['id'] = db.insert_comment(item)
            if self.ReplyFlag:
                self.ReplyFlag = False
            self.ui.cancelButton.setHidden(True)
            self.ui.lineEdit.clear()
            self.ui.lineEdit.setPlaceholderText('留下你的精彩评论吧~（点击头像回复')
            self.ui.tableWidget.setCellWidget(self.ui.tableWidget.rowCount() - 1, 0, GetComment(item, self))

    def importComment(self):
        db = DB()
        res = db.get_content()
        for row in res:
            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
            item = {'create_time': "  " + row[4], 'like_count': row[7], 'is_uped': 0,
                    'id': row[0], 'content': row[5], 'receiver': row[3]}
            if self.userName in str(row[6]).split():
                item['is_uped'] = 1
            if row[2] == 1:
                item['uname'] = row[1]
                item['type'] = 1
            else:
                item['uname'] = row[1]
                item['type'] = 0
            self.ui.tableWidget.setCellWidget(self.ui.tableWidget.rowCount() - 1, 0, GetComment(item, self))
            # self.ui.tableWidget.setItemDelegateForColumn(0, GetComment(item, self))
