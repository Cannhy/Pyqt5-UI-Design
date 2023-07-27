from PyQt5 import QtGui
from PyQt5.Qt import *
from PyQt5.QtCore import *
import re
from db.user import User
import db.user as u
from ui.Ui_RegisterForm import Ui_RegisterForm

_debug = False


class Register_controller(QMainWindow):
    empty = re.compile(r"^\s*$")
    reworkLoginButtonSignal = pyqtSignal()

    def __init__(self):
        super(Register_controller, self).__init__()
        self.ui = Ui_RegisterForm()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.userPasswordInput.setEchoMode(QLineEdit.Password)
        self.ui.userNameInput.setPlaceholderText('输入长度不得超过6位')
        self.ui.userPasswordInput.setClearButtonEnabled(True)
        self.ui.userNameInput.setClearButtonEnabled(True)
        self.setWindowIcon(QtGui.QIcon("../img/avater.jpg"))
        self.setWindowFlags(Qt.WindowCloseButtonHint)  # 隐藏标题
        self.ui.confirmButton.clicked.connect(self.confirmButtonClicked)

    def _clearLabel(self):
        self.ui.userPasswordTipsLabel.clear()
        self.ui.userNameTipsLabel.clear()

    def _clearInput(self):
        self.ui.userNameInput.clear()
        self.ui.userPasswordInput.clear()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.reworkLoginButtonSignal.emit()
        self._clearInput()
        self._clearLabel()
        a0.accept()

    def confirmButtonClicked(self):
        self._clearLabel()
        flag = True
        userName = str(self.ui.userNameInput.text())
        userPassword = str(self.ui.userPasswordInput.text())
        if _debug:
            print("Register:")
            print("userName: [" + userName + "], userPassword: [" + userPassword + "]")
        if re.match(self.empty, userName):
            self.ui.userNameTipsLabel.setText("用户名不能为空!")
            flag = False
        if flag and len(userName) > 6:
            self.ui.userNameTipsLabel.setText("用户名不能超过6位!")
            flag = False
        if re.match(self.empty, userPassword):
            self.ui.userPasswordTipsLabel.setText("密码不能为空!")
            flag = False
        if flag and len(userPassword) > 12:
            self.ui.userPasswordTipsLabel.setText("密码不能超过12位!")
            flag = False
        if flag and checkUserNameHad(userName):
            self.ui.userNameTipsLabel.setText("用户名已经存在!")
        elif flag:
            signUp(userName, userPassword)
            self.ui.userPasswordTipsLabel.setText("注册成功，请关闭该界面后重新登陆！")
            self._clearInput()
            self.reworkLoginButtonSignal.emit()


def checkUserNameHad(name: str) -> bool:
    return u.check_same('user', 'name', name, 'str')


def signUp(name: str, password: str) -> None:
    user = User()
    user.register(name, password)
