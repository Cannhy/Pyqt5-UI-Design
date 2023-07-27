from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *

from db.user import User
from ui.Logoff_window import Logoff_window


class LogOff_Controller(QtWidgets.QMainWindow):
    goBackToLoginSignal = pyqtSignal()
    goBackToMainSignal = pyqtSignal(int)

    def __init__(self, userName: str, userPassword: str):
        super(LogOff_Controller, self).__init__()
        self.ui = Logoff_window()
        self.ui.setupUi(self)
        self.userName = userName
        self.userPassword = userPassword
        self.flag = False
        self.setup_control()

    def setup_control(self):
        self.setWindowIcon(QtGui.QIcon("../img/avater.jpg"))
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        # self.ui.writeOfflabel.clear()
        # self.ui.writeOfflabel.setStyleSheet("background-image:url(../img/bye.jpg)")
        self.ui.confirmButton.clicked.connect(self.confirmButtonClicked)

    def confirmButtonClicked(self):
        logOffUser()
        self.goBackToLoginSignal.emit()
        self.flag = True
        self.close()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        if self.flag:
            a0.accept()
        else:
            self.goBackToMainSignal.emit(1)
            a0.ignore()

    def showEvent(self, a0: QtGui.QShowEvent):
        self.flag = False
        a0.accept()


def logOffUser() -> None:
    user = User()
    user.destroy()
