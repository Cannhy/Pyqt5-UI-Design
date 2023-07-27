from PyQt5 import QtCore, QtGui, QtWidgets

from ui.changePassword import changePasswordDialog


class PersonCenter_window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 411)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(120, 40, 151, 141))
        self.photo.setAutoFillBackground(False)
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("../img/xg.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.username = QtWidgets.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(70, 220, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.username.setStyleSheet("font: 16pt; font: bold")
        self.username.setObjectName("username")
        self.secret = QtWidgets.QPushButton(self.centralwidget)
        self.secret.setGeometry(QtCore.QRect(150, 310, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.secret.setStyleSheet("font: 13pt")
        self.secret.setObjectName("pushButton")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(290, 310, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.back.setStyleSheet("font: 13pt")
        self.back.setObjectName("pushButton_2")
        self.setphoto = QtWidgets.QPushButton(self.centralwidget)
        self.setphoto.setGeometry(QtCore.QRect(10, 310, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.setphoto.setStyleSheet("font: 13pt")
        self.setphoto.setObjectName("pushButton_3")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(180, 220, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.name.setStyleSheet("font: 16pt; font: bold")
        self.name.setObjectName("name")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # self.secret.clicked.connect(secretButtonClicked)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "个人中心"))
        self.username.setText(_translate("MainWindow", "用户名:"))
        self.secret.setText(_translate("MainWindow", "修改密码"))
        self.back.setText(_translate("MainWindow", "返回"))
        self.setphoto.setText(_translate("MainWindow", "更换头像"))

