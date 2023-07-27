import re
import time
import numpy as np
import random

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import *
from PyQt5.QtWidgets import QFileDialog

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
from ui.BookMark_controller import BookMark_controller
from ui.Logoff_controller import LogOff_Controller
from ui.Main_window import Main_window
from ui.Present_controller import Present_controller
from ui.Recode_controller import Record_controller
from ui.PersonCenter_controller import PersonCenter_controller
from ui.Communicate_controller import Communicate_controller
from ui.Suggest_controller import Suggest_controller


nutritionDic = {0: '碳水', 1: '肉类', 2: '蔬菜'}
tasteDic = {0: '麻辣', 1: '清淡', 2: '酸辣', 3: '香辣', 4: '酱香', 5: '甜味', 6: '酸甜', 7: '酸咸', 8: '甜咸', 9: '咸香'}


class Main_controller(QtWidgets.QMainWindow):
    empty = re.compile(r"^\s*$")
    flag = True
    logOutSignal = pyqtSignal()  # 回到登陆界面

    def __init__(self, userName: str, userPassword: str):
        super(Main_controller, self).__init__()
        self.ui = Main_window()
        self.ui.setupUi(self)
        self.userName = userName
        self.userPassword = userPassword
        self.present_ui = Present_controller(userName, userPassword)
        self.logOff_ui = LogOff_Controller(userName, userPassword)
        self.record_ui = Record_controller(userName, userPassword)
        self.book_ui = BookMark_controller(userName, userPassword)
        self.person_ui = PersonCenter_controller(userName, userPassword)
        self.comment_ui = Communicate_controller(userName, userPassword)
        self.suggest_ui = Suggest_controller(userName, userPassword)
        self.setup_control()

    def _show(self, tyPe: int):
        self.hide()
        if tyPe == 0:
            self.present_ui.show()
        if tyPe == 1:
            self.logOff_ui.show()
        if tyPe == 2:
            self.record_ui.show()
        if tyPe == 3:
            self.book_ui.show()
        if tyPe == 4:
            self.person_ui.show()
        if tyPe == 5:
            self.comment_ui.show()
        if tyPe == 6:
            self.suggest_ui.show()

    def _reshow(self, tyPe: int):
        if tyPe == 0:
            self.present_ui.hide()
        elif tyPe == 1:
            self.logOff_ui.hide()
        elif tyPe == 2:
            self.record_ui.hide()
        elif tyPe == 3:
            self.book_ui.hide()
        elif tyPe == 4:
            self.person_ui.hide()
        elif tyPe == 5:
            self.comment_ui.hide()
        elif tyPe == 6:
            self.suggest_ui.hide()
        self.show()

    def logoutButtonClicked(self):
        self.ui.scheduleLabel.clear()
        #userExit()
        self.logOutSignal.emit()

    def setup_control(self):
        self.ui.userNamelabel.setText("用户：" + self.userName)
        self.present_ui.goBackToMainSignal.connect(self._reshow)
        self.record_ui.goBackToMainSignal.connect(self._reshow)
        self.ui.PresentButton.clicked.connect(self.PresentButtonClicked)
        self.ui.mustEat.clicked.connect(self.mustEatClicked)
        self.ui.logoutButton.clicked.connect(self.logoutButtonClicked)
        self.ui.writeOffButton.clicked.connect(self.logOffButtonClicked)
        self.ui.recordButton.clicked.connect(self.recordButtonClicked)
        self.ui.suggestButton.clicked.connect(self.suggestButtonClicked)
        self.suggest_ui.goBackToMainSignal.connect(self._reshow)
        self.ui.suggestButton.clicked.connect(self.drawPic)
        self.logOff_ui.goBackToMainSignal.connect(self._reshow)
        self.logOff_ui.goBackToLoginSignal.connect(self.logOffBackButtonClicked)
        self.ui.bookMarkButton.clicked.connect(self.bookMarkButtonClicked)
        self.book_ui.goBackToMainSignal.connect(self._reshow)
        self.ui.centerButton.clicked.connect(self.centerButtonClicked)
        self.person_ui.goBackToMainSignal.connect(self._reshow)
        self.ui.commentButton.clicked.connect(self.commentButtonClicked)
        self.comment_ui.goBackToMainSignal.connect(self._reshow)
        self.comment_ui.ui.comboBox.currentTextChanged.connect(self.commentCanteenChanged)
        self.comment_ui.ui.comboBox_2.currentTextChanged.connect(self.commentCounterChanged)

    def drawPic(self):
        self.fig1 = plt.Figure()
        self.canvas1 = FigureCanvas(self.fig1)
        for i in range(self.suggest_ui.ui.verticalLayout.count()):
            self.suggest_ui.ui.verticalLayout.removeItem(self.suggest_ui.ui.verticalLayout.itemAt(i))
        self.suggest_ui.ui.verticalLayout.addWidget(self.canvas1)
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
        color_backup = ['lightgreen', 'skyblue', 'plum', 'c', 'tan']
        self.axes1.bar(labels, heights, color=color_backup)
        self.canvas1.draw()

        nutri = db.getNutri(self.userName)
        if len(nutri) != 0:
            if not (nutri[0][0] == 0 and nutri[0][1] == 0 and nutri[0][2] == 0):
                self.fig2 = plt.Figure()
                self.canvas2 = FigureCanvas(self.fig2)
                for i in range(self.suggest_ui.ui.verticalLayout_2.count()):
                    self.suggest_ui.ui.verticalLayout_2.removeItem(self.suggest_ui.ui.verticalLayout_2.itemAt(i))
                self.suggest_ui.ui.verticalLayout_2.addWidget(self.canvas2)
                ax = self.fig2.add_axes([0, 0, 1, 1])
                ax.axis('equal')
                langs = ['碳水', '肉类', '蔬菜']
                students = [nutri[0][0], nutri[0][1], nutri[0][2]]
                ax.pie(students, labels=langs, autopct='%1.2f%%')
        
        taste = db.getTaste(self.userName)
        if len(taste) != 0:
            self.fig3 = plt.Figure()
            self.canvas3 = FigureCanvas(self.fig3)
            for i in range(self.suggest_ui.ui.verticalLayout_3.count()):
                self.suggest_ui.ui.verticalLayout_3.removeItem(self.suggest_ui.ui.verticalLayout_3.itemAt(i))
            self.suggest_ui.ui.verticalLayout_3.addWidget(self.canvas3)
            self.axes3 = self.fig3.subplots()
            self.axes3.cla()
            self.axes3.set_xlabel('口味', fontsize=12)
            self.axes3.set_ylabel('频次', fontsize=12)
            heights = []
            labels = ['麻辣', '清淡', '酸辣', '香辣', '酱香', '甜味', '酸甜', '酸咸', '甜咸', '咸香']
            for i in range(len(taste[0])):
                heights.append(taste[0][i])
            color_backup = ['grey', 'gold', 'darkviolet', 'turquoise', 'r', 'g', 'b', 'c', 'm', 'y',
                            'k', 'darkorange', 'lightgreen', 'plum', 'tan',
                            'khaki', 'pink', 'skyblue', 'lawngreen', 'salmon']
            self.axes3.bar(labels, heights, color=color_backup)

        self.randomDish()

    def randomDish(self):
        db = DB()
        if len(db.getNutri(self.userName)) == 0:
            return
        nutri = list(db.getNutri(self.userName)[0])
        taste = list(db.getTaste(self.userName)[0])
        nutri_ans, taste_ans = [], []
        nutri_np = np.array(nutri)
        for i in range(len(nutri)):
            pos = int(np.argmax(nutri_np))
            nutri_ans.append(nutritionDic[pos])
            nutri[pos] = -1
            nutri_np = np.array(nutri)
        nutri_ans[0], nutri_ans[2] = nutri_ans[2], nutri_ans[0]
        for j in range(len(taste)):
            pos = taste.index(max(taste))
            taste_ans.append(tasteDic[pos])
            taste[pos] = -1
        res = db.generateDish(nutri_ans, taste_ans)
        self.suggest_ui.res = res
        pos = self.suggest_ui.cnt
        content = res[pos][0] + '(' + res[pos][1] + '-' + res[pos][2] + ')' + '\n' + \
                  res[pos + 1][0] + '(' + res[pos + 1][1] + '-' + res[pos + 1][2] + ')' + '\n' + \
                  res[pos + 2][0] + '(' + res[pos + 2][1] + '-' + res[pos + 2][2] + ')'
        self.suggest_ui.ui.suggest_label.setWordWrap(True)
        self.suggest_ui.ui.suggest_label.setAlignment(Qt.AlignCenter)
        self.suggest_ui.ui.suggest_label.setText(content)

    def PresentButtonClicked(self):
        self._show(0)

    def logOffButtonClicked(self):
        self._show(1)

    def logOffBackButtonClicked(self):
        self.ui.scheduleLabel.clear()
        # userExit()
        self.logOutSignal.emit()

    def mustEatClicked(self):
        if self.flag:
            value, ok = QInputDialog.getInt(self, "输入数量", "请输入要展示的菜品数量:", 10, 1, 50, 2)
            if ok:
                db = DB()
                res = db.get_des_eat(int(value))
                self.ui.questionTextEdit.clear()
                # self.ui.setTitle()
                self.ui.questionTextEdit.setAlignment(QtCore.Qt.AlignCenter)
                self.ui.questionTextEdit.setStyleSheet(
                    "font: 17pt; font: bold; color: rgb(225,22,173,255); background-color: #B0E0E6")
                self.ui.questionTextEdit.insertHtml(
                    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:800; color:#ff9912;\">必吃榜</span></p>\n")
                for row in range(len(res)):
                    dish = str(row + 1) + ' ' + res[row][0] + ' (' + res[row][1] + '-' + res[row][2] + ') ' + str(
                        res[row][5]) + '次'
                    self.ui.questionTextEdit.append(dish)
                    if row != len(res) - 1:
                        self.ui.questionTextEdit.append('\n')
                self.ui.questionTextEdit.moveCursor(QTextCursor.Start)  # 将光标移动到行首
            else:
                self.flag = not self.flag
        else:
            self.ui.setBrowser()
        self.flag = not self.flag

    def recordButtonClicked(self):
        self._show(2)

    def bookMarkButtonClicked(self):
        self._show(3)

    def centerButtonClicked(self):
        self._show(4)

    def commentButtonClicked(self):
        self._show(5)
        db = DB()
        self.comment_ui.ui.comboBox.disconnect()
        self.comment_ui.ui.comboBox.clear()
        self.comment_ui.ui.comboBox.addItems(db.get_canteens())
        self.comment_ui.ui.comboBox.setStyleSheet("font: 13pt")
        self.comment_ui.ui.comboBox.currentTextChanged.connect(self.commentCanteenChanged)

    def suggestButtonClicked(self):
        self._show(6)

    def commentCanteenChanged(self):
        db = DB()
        self.comment_ui.ui.comboBox_2.disconnect()
        self.comment_ui.ui.comboBox_2.clear()
        self.comment_ui.ui.comboBox_2.addItems(db.get_counters(self.comment_ui.ui.comboBox.currentText()))
        self.comment_ui.ui.comboBox_2.setStyleSheet("font: 13pt")
        self.comment_ui.ui.comboBox_2.currentTextChanged.connect(self.commentCounterChanged)

    def commentCounterChanged(self):
        db = DB()
        self.comment_ui.ui.comboBox_3.clear()
        self.comment_ui.ui.comboBox_3.addItems(db.get_dishes(self.comment_ui.ui.comboBox.currentText(), self.comment_ui.ui.comboBox_2.currentText()))
        self.comment_ui.ui.comboBox_3.setStyleSheet("font: 13pt")

def randomDish(self):
    db = DB()
    if len(db.getNutri(self.userName)) == 0:
        return
    nutri = list(db.getNutri(self.userName)[0])
    taste = list(db.getTaste(self.userName)[0])
    nutri_ans, taste_ans = [], []
    nutri_np = np.array(nutri)
    for i in range(len(nutri)):
        pos = int(np.argmax(nutri_np))
        nutri_ans.append(nutritionDic[pos])
        nutri[pos] = -1
        nutri_np = np.array(nutri)
    nutri_ans[0], nutri_ans[2] = nutri_ans[2], nutri_ans[0]
    for j in range(len(taste)):
        pos = taste.index(max(taste))
        taste_ans.append(tasteDic[pos])
        taste[pos] = -1
    res = db.generateDish(nutri_ans, taste_ans)
    self.suggest_ui.res = res
    pos = self.suggest_ui.cnt
    content = res[pos][0] + '(' + res[pos][1] + '-' + res[pos][2] + ')' + '\n' + \
              res[pos + 1][0] + '(' + res[pos + 1][1] + '-' + res[pos + 1][2] + ')' + '\n' + \
              res[pos + 2][0] + '(' + res[pos + 2][1] + '-' + res[pos + 2][2] + ')'
    self.suggest_ui.ui.suggest_label.setWordWrap(True)
    self.suggest_ui.ui.suggest_label.setAlignment(Qt.AlignCenter)
    self.suggest_ui.ui.suggest_label.setText(content)

def mustEatClicked(self):
    if self.flag:
        value, ok = QInputDialog.getInt(self, "输入数量", "请输入要展示的菜品数量:", 10, 1, 50, 2)
        if ok:
            db = DB()
            res = db.get_des_eat(int(value))
            self.ui.questionTextEdit.clear()
            # self.ui.setTitle()
            self.ui.questionTextEdit.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.questionTextEdit.setStyleSheet(
                "font: 17pt; font: bold; color: rgb(225,22,173,255); background-color: #B0E0E6")
            self.ui.questionTextEdit.insertHtml(
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:800; color:#ff9912;\">必吃榜</span></p>\n")
            for row in range(len(res)):
                dish = str(row + 1) + ' ' + res[row][0] + ' (' + res[row][1] + '-' + res[row][2] + ') ' + str(
                    res[row][5]) + '次'
                self.ui.questionTextEdit.append(dish)
                if row != len(res) - 1:
                    self.ui.questionTextEdit.append('\n')
            self.ui.questionTextEdit.moveCursor(QTextCursor.Start)  # 将光标移动到行首
        else:
            self.flag = not self.flag
    else:
        self.ui.setBrowser()
    self.flag = not self.flag