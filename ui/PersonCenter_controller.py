import re
import time
import sys
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QDirModel, QLabel, QVBoxLayout
from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore

from ui.PersonCenter_window import PersonCenter_window
from ui.changePassword import changePasswordDialog


class PersonCenter_controller(QtWidgets.QMainWindow):
    empty = re.compile(r"^\s*$")
    goBackToMainSignal = pyqtSignal(int)

    def __init__(self, userName: str, userPassword: str):
        super(PersonCenter_controller, self).__init__()
        self.flag = True
        self.ui = PersonCenter_window()
        self.secui = changePasswordDialog()
        self.ui.setupUi(self)
        self.userName = userName
        self.userPassword = userPassword
        self.setup_control()

    def setup_control(self):
        self.ui.secret.clicked.connect(self.secretButtonClicked)
        self.ui.back.clicked.connect(self.backButtonClicked)
        self.ui.setphoto.clicked.connect(self.setphotoButtonClicked)
        _translate = QtCore.QCoreApplication.translate
        self.ui.name.setText(_translate("MainWindow", self.userName))

    def backButtonClicked(self):
        self.goBackToMainSignal.emit(4)

    def setphotoButtonClicked(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = filenames[0]
            suffix = f.split('.')[-1]
            if suffix == 'jpg' or suffix == 'jpeg' or suffix == 'png':
                self.ui.photo.setPixmap(QtGui.QPixmap(f))
            else:
                QMessageBox.critical(self, "错误", "错误的图片类型", QMessageBox.Ok)

    def secretButtonClicked(self):
        self.secui.exec_()
