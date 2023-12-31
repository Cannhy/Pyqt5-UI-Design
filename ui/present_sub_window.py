
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'present_add_new.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *


class present_sub(QDialog):
    def __init__(self, parent=None):
        super(present_sub, self).__init__(parent)
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle("删除")
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setupUi()

    def setupUi(self):
        self.resize(410, 302)
        self.radioCanteen = QtWidgets.QRadioButton(self)
        self.radioCanteen.setGeometry(QtCore.QRect(40, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.radioCanteen.setStyleSheet("font: 13pt")
        self.radioCanteen.setObjectName("radioCanteen")
        self.radioCounter = QtWidgets.QRadioButton(self)
        self.radioCounter.setGeometry(QtCore.QRect(170, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.radioCounter.setStyleSheet("font: 13pt")
        self.radioCounter.setObjectName("radioCounter")
        self.radioDish = QtWidgets.QRadioButton(self)
        self.radioDish.setGeometry(QtCore.QRect(290, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.radioDish.setStyleSheet("font: 13pt")
        self.radioDish.setObjectName("radioDish")
        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 70, 371, 161))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.canteen_label1 = QtWidgets.QLabel(self.page)
        self.canteen_label1.setGeometry(QtCore.QRect(10, 50, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.canteen_label1.setStyleSheet("font: 15pt")
        self.canteen_label1.setObjectName("canteen_label1")
        self.canteen_lineedit1 = QtWidgets.QComboBox(self.page)
        self.canteen_lineedit1.setGeometry(QtCore.QRect(130, 60, 201, 41))
        self.canteen_lineedit1.setObjectName("canteen_lineedit1")
        self.canteen_lineedit1.setStyleSheet("font:13pt")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.canteen_label2 = QtWidgets.QLabel(self.page_2)
        self.canteen_label2.setGeometry(QtCore.QRect(10, 20, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.canteen_label2.setStyleSheet("font: 15pt")
        self.canteen_label2.setObjectName("canteen_label2")
        self.counter_label2 = QtWidgets.QLabel(self.page_2)
        self.counter_label2.setGeometry(QtCore.QRect(10, 100, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.counter_label2.setStyleSheet("font: 15pt")
        self.counter_label2.setObjectName("counter_label2")
        self.canteen_lineedit2 = QtWidgets.QComboBox(self.page_2)
        self.canteen_lineedit2.setGeometry(QtCore.QRect(130, 30, 201, 41))
        self.canteen_lineedit2.setObjectName("canteen_lineedit2")
        self.canteen_lineedit2.setStyleSheet("font:13pt")
        self.counter_lineedit2 = QtWidgets.QComboBox(self.page_2)
        self.counter_lineedit2.setGeometry(QtCore.QRect(130, 110, 201, 41))
        self.counter_lineedit2.setObjectName("counter_lineedit2")
        self.counter_lineedit2.setStyleSheet("font:13pt")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.dish_label3 = QtWidgets.QLabel(self.page_3)
        self.dish_label3.setGeometry(QtCore.QRect(20, 50, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.dish_label3.setStyleSheet("font: 15pt")
        self.dish_label3.setObjectName("dish_label3")
        self.dish_lineedit3 = QtWidgets.QLineEdit(self.page_3)
        self.dish_lineedit3.setGeometry(QtCore.QRect(120, 60, 201, 41))
        self.dish_lineedit3.setObjectName("dish_lineedit3")
        self.dish_lineedit3.setStyleSheet("font:13pt")
        self.stackedWidget.addWidget(self.page_3)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(312, 250, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setStyleSheet("font: 11pt")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(self)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        # Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.radioCanteen.setText(_translate("Dialog", "餐厅"))
        self.radioCounter.setText(_translate("Dialog", "档口"))
        self.radioDish.setText(_translate("Dialog", "菜品"))
        self.canteen_label1.setText(_translate("Dialog", "餐厅名称:"))
        self.canteen_label2.setText(_translate("Dialog", "所属餐厅:"))
        self.counter_label2.setText(_translate("Dialog", "档口名称:"))
        self.dish_label3.setText(_translate("Dialog", "菜品ID:"))
        self.pushButton.setText(_translate("Dialog", "确定"))
