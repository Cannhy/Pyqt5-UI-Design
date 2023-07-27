from PyQt5 import QtCore, QtGui, QtWidgets


class Main_window(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(1200, 755)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/avater.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainForm.setWindowIcon(icon)
        self.horizontalLayoutWidget = QtWidgets.QWidget(MainForm)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 520, 1091, 171))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutForButtons = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayoutForButtons.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutForButtons.setObjectName("horizontalLayoutForButtons")
        self.mustEat = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.mustEat.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.mustEat.setObjectName("mustEat")
        self.horizontalLayoutForButtons.addWidget(self.mustEat)
        self.commentButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.commentButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.commentButton.setObjectName("commentButton")
        self.horizontalLayoutForButtons.addWidget(self.commentButton)
        self.PresentButton = QtWidgets.QPushButton(MainForm)
        self.PresentButton.setGeometry(QtCore.QRect(50, 70, 151, 51))
        self.PresentButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.PresentButton.setObjectName("PresentButton")
        self.questionTextEdit = QtWidgets.QTextBrowser(MainForm)
        self.questionTextEdit.setGeometry(QtCore.QRect(240, 60, 821, 431))
        self.questionTextEdit.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.questionTextEdit.setObjectName("questionTextEdit")
        self.bookMarkButton = QtWidgets.QPushButton(MainForm)
        self.bookMarkButton.setGeometry(QtCore.QRect(50, 310, 151, 51))
        self.bookMarkButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.bookMarkButton.setObjectName("searchButton")
        self.recordButton = QtWidgets.QPushButton(MainForm)
        self.recordButton.setGeometry(QtCore.QRect(50, 190, 151, 51))
        self.recordButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.recordButton.setObjectName("recordButton")
        self.suggestButton = QtWidgets.QPushButton(MainForm)
        self.suggestButton.setGeometry(QtCore.QRect(50, 430, 151, 51))
        self.suggestButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.suggestButton.setObjectName("quizButton")
        self.logoutButton = QtWidgets.QPushButton(MainForm)
        self.logoutButton.setGeometry(QtCore.QRect(950, 700, 91, 41))
        self.logoutButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.logoutButton.setObjectName("logoutButton")
        self.userNamelabel = QtWidgets.QLabel(MainForm)
        self.userNamelabel.setGeometry(QtCore.QRect(1000, 10, 191, 41))
        self.userNamelabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.userNamelabel.setObjectName("userNamelabel")
        self.label = QtWidgets.QLabel(MainForm)
        self.label.setGeometry(QtCore.QRect(580, 10, 161, 41))
        self.label.setText("")
        self.label.setObjectName("label")
        self.scheduleLabel = QtWidgets.QLabel(MainForm)
        self.scheduleLabel.setGeometry(QtCore.QRect(510, 30, 301, 31))
        self.scheduleLabel.setStyleSheet("font: 9pt \"Consolas\" rgb(255, 14, 30);")
        self.scheduleLabel.setObjectName("scheduleLabel")
        self.centerButton = QtWidgets.QPushButton(MainForm)
        self.centerButton.setGeometry(QtCore.QRect(40, 700, 131, 41))
        self.centerButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.centerButton.setObjectName("contributeButton")
        self.writeOffButton = QtWidgets.QPushButton(MainForm)
        self.writeOffButton.setGeometry(QtCore.QRect(1050, 700, 91, 41))
        self.writeOffButton.setStyleSheet("font: 75 10pt \"Consolas\" rgb(241, 255, 235);")
        self.writeOffButton.setObjectName("writeOffButton")

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "航味食堂"))
        self.mustEat.setText(_translate("MainForm", "必吃榜"))
        self.mustEat.setStyleSheet("font: 12pt")
        self.commentButton.setText(_translate("MainForm", "菜品交流"))
        self.commentButton.setStyleSheet("font: 12pt")
        self.PresentButton.setText(_translate("MainForm", "菜品展示"))
        self.PresentButton.setStyleSheet("font: 12pt")
        self.bookMarkButton.setText(_translate("MainForm", "添加书签"))
        self.bookMarkButton.setStyleSheet("font: 12pt")
        self.recordButton.setText(_translate("MainForm", "菜品记录"))
        self.recordButton.setStyleSheet("font: 12pt")
        self.suggestButton.setText(_translate("MainForm", "膳食建议"))
        self.suggestButton.setStyleSheet("font: 12pt")
        self.logoutButton.setText(_translate("MainForm", "登出"))
        self.logoutButton.setStyleSheet("font: 12pt")
        self.userNamelabel.setText(_translate("MainForm", "用户名：Buaaer"))
        self.scheduleLabel.setText(_translate("MainForm", "想吃点什么捏。。。"))
        self.centerButton.setText(_translate("MainForm", "个人信息"))
        self.centerButton.setStyleSheet("font: 12pt")
        self.writeOffButton.setText(_translate("MainForm", "注销"))
        self.writeOffButton.setStyleSheet("font: 12pt")
        self.questionTextEdit.setStyleSheet(
            "background-color: white")
        self.questionTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:600; color:#ff0c2c;\">欢迎来到航味食堂~</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\',\'微软雅黑\',\'黑体\',\'_sans\'; font-size:16pt; font-weight:600; color:#5555ff; background-color:#ffffff;\">北区食堂</span><span style=\" font-family:\'Arial\',\'微软雅黑\',\'黑体\',\'_sans\'; font-size:16pt; color:#000000; background-color:#ffffff;\">：集品牌化餐饮、联营风味、基本伙保障于一体的风味型餐饮楼，共4个食堂（B1层学三食堂、一层学五食堂、二层学六食堂、三层京鲁菜-火锅-南时羽港式餐厅）</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\',\'微软雅黑\',\'黑体\',\'_sans\'; font-size:16pt; font-weight:600; color:#5555ff; background-color:#ffffff;\">西区食堂（合一楼）</span><span style=\" font-family:\'Arial\',\'微软雅黑\',\'黑体\',\'_sans\'; font-size:16pt; font-weight:600; color:#000000; background-color:#ffffff;\">：</span><span style=\" font-family:\'Arial\',\'微软雅黑\',\'黑体\',\'_sans\'; font-size:16pt; color:#000000; background-color:#ffffff;\">基本伙保障兼顾联营风味、民族餐的综合型餐饮楼，共4个食堂（一层二层学一食堂、三层学四食堂、四层南侧清真食堂、四层北侧合一厅）</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\',\'微软雅黑\',\'黑体\',\'_sans\'; font-size:16pt; font-weight:600; color:#5555ff; background-color:#ffffff;\">东区食堂（学二食堂楼）</span><span style=\" font-family:\'Arial\',\'微软雅黑\',\'黑体\',\'_sans\'; font-size:16pt; color:#000000; background-color:#ffffff;\">：基本保障型餐饮楼，共2个食堂（一层学二食堂、二层教工食堂）</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\',\'微软雅黑\',\'黑体\',\'_sans\'; font-size:16pt; font-weight:600; color:#5555ff; background-color:#ffffff;\">美食苑</span><span style=\" font-family:\'Arial\',\'微软雅黑\',\'黑体\',\'_sans\'; font-size:16pt; color:#000000; background-color:#ffffff;\">：位于大运村附近，包含各种小吃</span></p></body></html>"))

    def setBrowser(self):
        _translate = QtCore.QCoreApplication.translate
        self.questionTextEdit.setStyleSheet(
            "background-color: white")
        self.questionTextEdit.setHtml(_translate("MainWindow",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'Consolas\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:600; color:#ff0c2c;\">欢迎来到航味食堂~</span></p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\',\'微软雅黑\',\'黑体\',\'_sans\'; font-size:16pt; font-weight:600; color:#5555ff; background-color:#ffffff;\">北区食堂</span><span style=\" font-family:\'Arial\',\'微软雅黑\',\'黑体\',\'_sans\'; font-size:16pt; color:#000000; background-color:#ffffff;\">：集品牌化餐饮、联营风味、基本伙保障于一体的风味型餐饮楼，共4个食堂（B1层学三食堂、一层学五食堂、二层学六食堂、三层京鲁菜-火锅-南时羽港式餐厅）</span></p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\',\'微软雅黑\',\'黑体\',\'_sans\'; font-size:16pt; font-weight:600; color:#5555ff; background-color:#ffffff;\">西区食堂（合一楼）</span><span style=\" font-family:\'Arial\',\'微软雅黑\',\'黑体\',\'_sans\'; font-size:16pt; font-weight:600; color:#000000; background-color:#ffffff;\">：</span><span style=\" font-family:\'Arial\',\'微软雅黑\',\'黑体\',\'_sans\'; font-size:16pt; color:#000000; background-color:#ffffff;\">基本伙保障兼顾联营风味、民族餐的综合型餐饮楼，共4个食堂（一层二层学一食堂、三层学四食堂、四层南侧清真食堂、四层北侧合一厅）</span></p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\',\'微软雅黑\',\'黑体\',\'_sans\'; font-size:16pt; font-weight:600; color:#5555ff; background-color:#ffffff;\">东区食堂（学二食堂楼）</span><span style=\" font-family:\'Arial\',\'微软雅黑\',\'黑体\',\'_sans\'; font-size:16pt; color:#000000; background-color:#ffffff;\">：基本保障型餐饮楼，共2个食堂（一层学二食堂、二层教工食堂）</span></p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\',\'微软雅黑\',\'黑体\',\'_sans\'; font-size:16pt; font-weight:600; color:#5555ff; background-color:#ffffff;\">美食苑</span><span style=\" font-family:\'Arial\',\'微软雅黑\',\'黑体\',\'_sans\'; font-size:16pt; color:#000000; background-color:#ffffff;\">：位于大运村附近，包含各种小吃</span></p></body></html>"))

    def setTitle(self):
        _translate = QtCore.QCoreApplication.translate
        self.questionTextEdit.setHtml(_translate("MainWindow",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'Consolas\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:800; color:#ffd700;\">必吃榜</span></p>\n"))
