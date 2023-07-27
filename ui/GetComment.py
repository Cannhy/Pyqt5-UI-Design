import qtawesome
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QFontMetrics
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSpacerItem, QToolButton, QSizePolicy, QLabel
from PyQt5.Qt import *

from db.DB import DB


class GetComment(QWidget):
    def __init__(self, item, user, parent=None):
        super(GetComment, self).__init__(parent)
        self.flag = False
        self.send = item['uname']
        self.revc = item['receiver']
        self.layout_main = QHBoxLayout()  # 点体横向布局
        self.layout_right = QVBoxLayout()  # 右边的纵向布局
        self.layout_right_up = QHBoxLayout()  # 右边的上面横向布局
        self.layout_right_up_inner = QHBoxLayout()  # 右边上面里边的横向布局
        self.spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.userHeadBtn = QToolButton()
        self.userHeadBtn.setIconSize(QSize(40, 40))
        '''
        pix = QPixmap()
        pic_url = ''
        img_bytes = self.spider.get_pic_bytes(pic_url)
        if img_bytes:
            pix.loadFromData(img_bytes)
            pixMap = self.PixmapToRound(pix, 50)
            userHeadBtn.setIcon(QIcon(pixMap))
        else:
        '''
        self.userHeadBtn.setText("未知头像")
        self.userHeadBtn.setStyleSheet("font: 12pt")
        self.layout_main.addWidget(self.userHeadBtn)
        self.userNameLabel = QLabel()
        self.userNmae = item['uname']
        self.userNameLabel.setStyleSheet("font: 12pt")
        self.userNameLabel.setText(self.userNmae)
        self.dishLabel = QLabel()
        self.dishLabel.setStyleSheet("font: 11pt; font: Consolas")
        if item['type'] == 0:
            self.dishLabel.setText('评价 ' + self.revc)
        else:
            self.dishLabel.setText('回复 ' + self.revc)
        self.userCommentDateLabel = QLabel()
        self.userCommentDateLabel.setStyleSheet("font: 11pt")
        self.userCommentDateLabel.setText(item['create_time'])
        self.likeNum = item['like_count']
        self.likeNumToolBtn = QToolButton()
        self.likeNumToolBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        if item['is_uped'] == 0:
            self.likeNumToolBtn.setIcon(QIcon(qtawesome.icon('fa.thumbs-o-up', color='gray')))
        else:
            self.likeNumToolBtn.setIcon(QIcon(qtawesome.icon('fa.thumbs-up', color="red")))
            self.likeNumToolBtn.setToolTip("取消点赞")
            self.flag = True
        self.likeNumToolBtn.setText(str(self.likeNum))
        self.likeNumToolBtn.setStyleSheet("font: 14pt")
        self.likeNumToolBtn.setToolTip("点赞")
        self.likeNumToolBtn.clicked.connect(lambda: self.do_thumbs_comment(user.userName, item['id']))
        self.userCommentLabel = QLabel()
        self.commentContent = item['content']
        self.userCommentLabel.setText(self.commentContent)
        self.userCommentLabel.setStyleSheet("font: 14pt")
        self.userCommentLabel.setToolTip(self.commentContent)
        self.userCommentLabel.setWordWrap(True)  # 换行
        text_width = QFontMetrics(self.userCommentLabel.font()).width(self.commentContent)
        isWordWarp = True
        self.userCommentLabel.setWordWrap(True)
        self.layout_right_up_inner.addWidget(self.userNameLabel)
        self.layout_right_up_inner.addItem(self.spacer)
        self.layout_right_up_inner.addWidget(self.userCommentDateLabel)
        self.layout_right_up_inner.addItem(self.spacer)
        self.layout_right_up.addLayout(self.layout_right_up_inner)
        self.layout_right_up.addWidget(self.likeNumToolBtn)
        self.layout_right.addLayout(self.layout_right_up)
        self.layout_right.addWidget(self.dishLabel)
        self.spacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.layout_right.addItem(self.spacer2)
        self.layout_right.addWidget(self.userCommentLabel)
        self.layout_main.addLayout(self.layout_right)
        self.setLayout(self.layout_main)
        self.userHeadBtn.clicked.connect(lambda: self.do_show_reply_user_comment(self.userNmae, user))

    def do_show_reply_user_comment(self, userNmae, user):
        if user.userName != userNmae:
            user.ui.cancelButton.setText('取消回复')
            user.ui.lineEdit.setPlaceholderText('回复@' + self.send)
            user.replyName = userNmae
            user.ui.cancelButton.setHidden(False)
            user.ReplyFlag = True

    def do_thumbs_comment(self, username, id):
        db = DB()
        if self.flag:
            self.likeNumToolBtn.setIcon(QIcon(qtawesome.icon('fa.thumbs-o-up', color='gray')))
            self.flag = False
            self.likeNum -= 1
            db.update_comment(username, 0, self.likeNum, id)
        else:
            self.likeNumToolBtn.setIcon(QIcon(qtawesome.icon('fa.thumbs-up', color="red")))
            self.likeNumToolBtn.setToolTip("取消点赞")
            self.flag = True
            self.likeNum += 1
            db.update_comment(username, 1, self.likeNum, id)
        self.likeNumToolBtn.setText(str(self.likeNum))

