from click.decorators import FC
from matplotlib import pyplot as plt
from pylab import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False

from db.DB import DB
import re
import time
import sys
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QDirModel, QLabel, QVBoxLayout
from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore
from ui.Suggest_window import Suggest_window


class Suggest_controller(QtWidgets.QMainWindow):
    empty = re.compile(r"^\s*$")
    goBackToMainSignal = pyqtSignal(int)

    def __init__(self, userName: str, userPassword: str):
        super(Suggest_controller, self).__init__()
        self.flag = True
        self.ui = Suggest_window()
        self.ui.setupUi(self)
        self.userName = userName
        self.userPassword = userPassword
        self.cnt = 0
        self.res = []
        self.setup_control()

    def setup_control(self):
        self.ui.backButton.clicked.connect(self.backButtonClicked)
        self.ui.reComeButton.clicked.connect(self.reComeButtonClicked)

    def reComeButtonClicked(self):
        self.cnt = (self.cnt + 1) % 3
        pos = self.cnt
        content = self.res[pos][0] + '(' + self.res[pos][1] + '-' + self.res[pos][2] + ')' + '\n' + \
                  self.res[pos + 1][0] + '(' + self.res[pos + 1][1] + '-' + self.res[pos + 1][2] + ')' + '\n' + \
                  self.res[pos + 2][0] + '(' + self.res[pos + 2][1] + '-' + self.res[pos + 2][2] + ')'
        self.ui.suggest_label.setWordWrap(True)
        self.ui.suggest_label.setAlignment(Qt.AlignCenter)
        self.ui.suggest_label.setText(content)

    def backButtonClicked(self):
        self.goBackToMainSignal.emit(6)

    def drawGraph(self):
        self.fig1 = plt.Figure()
        self.canvas1 = FigureCanvas(self.fig1)
        self.ui.verticalLayout.addWidget(self.canvas1)
        self.axes1 = self.fig1.subplots()
        self.axes1.cla()
        self.axes1.set_title('菜品情况', fontsize=12)
        self.axes1.set_xlabel('菜品', fontsize=12)
        self.axes1.set_ylabel('频次', fontsize=12)
        db = DB()
        freq = db.getFreq(self.userName)
        heights = []
        labels = []
        for i in range(len(freq)):
            if i == 5:
                break
            else:
                labels.append(freq[i][2])
                heights.append(freq[i][5])
        self.axes1.bar(labels, heights)
        self.canvas1.draw()
