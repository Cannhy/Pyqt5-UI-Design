from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView, QMenu
from PyQt5.QtCore import *

from ui.GetComment import GetComment


class communicate_window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(852, 701)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/avater.jpg"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        #self.name = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 50, 731, 451))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(740, 630, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.backButton.setStyleSheet("font: 13pt")
        self.backButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 570, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setStyleSheet("font: 11pt")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.emitButton = QtWidgets.QPushButton(self.centralwidget)
        self.emitButton.setGeometry(QtCore.QRect(570, 570, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.emitButton.setStyleSheet("font: 13pt")
        self.emitButton.setObjectName("pushButton_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 570, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setStyleSheet("font: 13pt")
        self.label.setObjectName("label")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(680, 570, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cancelButton.setStyleSheet("font: 11pt")
        self.cancelButton.setObjectName("pushButton_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(170, 520, 131, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(320, 520, 231, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(570, 520, 221, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 530, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setStyleSheet("font: 12pt")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tableWidget.verticalHeader().setVisible(False)   # // 隐藏列表头
        self.tableWidget.setShowGrid(False)
        self.tableWidget.horizontalHeader().setVisible(False)   # // 隐藏行表头
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        #self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        #self.tableWidget.customContextMenuRequested.connect(self.generateMenu)

    def generateMenu(self, pos):
        #获得右键所点击的索引值
        for i in self.tableWidget.selectionModel().selection().indexes():
            #获得当前的行数目
            rowIndex = i.row()
            #如果选择的索引小于2, 弹出上下文菜单
            print(self.tableWidget.cellWidget(1, 0))
            if True:
                #构造菜单
                menu = QMenu()
                #添加菜单的选项
                item1 = menu.addAction("删除")
                #获得相对屏幕的位置
                screenPos = self.tableWidget.mapToGlobal(pos)
                #被阻塞, 执行菜单
                action = menu.exec(screenPos)
                if action == item1:
                    print("选择了第一个菜单项", self.tableWidget.item(rowIndex, 0).text())
            else:
                return


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "菜品交流"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "新建列"))
        self.backButton.setText(_translate("MainWindow", "返回"))
        self.emitButton.setText(_translate("MainWindow", "发送"))
        #self.delButton.setText(_translate("MainWindow", "删除"))
        self.label.setText(_translate("MainWindow", "发表评论："))
        self.cancelButton.setText(_translate("MainWindow", "取消回复"))
        self.label_2.setText(_translate("MainWindow", "评价菜品:"))
