import os

from PyQt5.QtWidgets import QApplication, QMainWindow
from qt_material import apply_stylesheet
import sys

from ui.Login_controller import Login_controller
import db.initial
import db.DB


def runGui():
    os.chdir('./ui')
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='light_blue.xml')
    window = Login_controller()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    db.DB.data_path = db.initial.initial()
    runGui()
