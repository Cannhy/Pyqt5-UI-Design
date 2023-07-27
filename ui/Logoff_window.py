from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont


class Logoff_window(object):
    def setupUi(self, Logoff):
        Logoff.setObjectName("WriteOffForm")
        Logoff.resize(400, 180)
        self.writeOfflabel = QtWidgets.QLabel(Logoff)
        self.writeOfflabel.setGeometry(QtCore.QRect(130, 10, 121, 101))
        self.writeOfflabel.setObjectName("writeOfflabel")
        self.writeOfflabel.setStyleSheet("QLabel{color:rgb(225,22,173,255);font-size:16px;font-weight:normal;font-family:Arial;}")
        self.confirmButton = QtWidgets.QPushButton(Logoff)
        self.confirmButton.setGeometry(QtCore.QRect(140, 120, 112, 41))
        self.confirmButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.confirmButton.setObjectName("confirmButton")
        self.retranslateUi(Logoff)
        QtCore.QMetaObject.connectSlotsByName(Logoff)

    def retranslateUi(self, WriteOffForm):
        _translate = QtCore.QCoreApplication.translate
        WriteOffForm.setWindowTitle(_translate("WriteOffForm", "用户注销"))
        self.writeOfflabel.setText("您真的要注销吗？")
        self.confirmButton.setText(_translate("WriteOffForm", "确认"))