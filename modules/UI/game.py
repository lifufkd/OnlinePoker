# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import modules.UI.resources

class Ui_Game(object):
    def setupUi(self, Game):
        if not Game.objectName():
            Game.setObjectName(u"Game")
        Game.resize(1280, 733)
        Game.setStyleSheet(u"\n"
"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;")
        self.centralwidget = QWidget(Game)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_exitgame = QPushButton(self.centralwidget)
        self.btn_exitgame.setObjectName(u"btn_exitgame")
        self.btn_exitgame.setGeometry(QRect(10, 670, 121, 41))
        self.btn_exitgame.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/cil-door.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exitgame.setIcon(icon)
        self.game_frame = QFrame(self.centralwidget)
        self.game_frame.setObjectName(u"game_frame")
        self.game_frame.setGeometry(QRect(190, 20, 1071, 651))
        self.game_frame.setStyleSheet(u"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;")
        self.game_frame.setFrameShape(QFrame.StyledPanel)
        self.game_frame.setFrameShadow(QFrame.Raised)
        self.label_card2_1 = QLabel(self.game_frame)
        self.label_card2_1.setObjectName(u"label_card2_1")
        self.label_card2_1.setGeometry(QRect(180, 340, 51, 91))
        self.label_card2_1.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_card2_1.setFrameShape(QFrame.NoFrame)
        self.label_card2_2 = QLabel(self.game_frame)
        self.label_card2_2.setObjectName(u"label_card2_2")
        self.label_card2_2.setGeometry(QRect(180, 160, 51, 91))
        self.label_card2_2.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_card2_2.setFrameShape(QFrame.NoFrame)
        self.frame = QFrame(self.game_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, -30, 1061, 850))
        font = QFont()
        font.setFamilies([u"ljk_OCRA"])
        font.setPointSize(18)
        font.setBold(True)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"border-image: url(:/photos/images/\u0411\u0435\u0437 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f.png);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_info_4 = QLabel(self.frame)
        self.label_info_4.setObjectName(u"label_info_4")
        self.label_info_4.setGeometry(QRect(870, 60, 151, 61))
        self.label_info_4.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.label_info_4.setAlignment(Qt.AlignCenter)
        self.label_card1_3 = QLabel(self.frame)
        self.label_card1_3.setObjectName(u"label_card1_3")
        self.label_card1_3.setGeometry(QRect(480, 140, 51, 91))
        self.label_card1_3.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_card1_3.setFrameShape(QFrame.NoFrame)
        self.label_card2_3 = QLabel(self.frame)
        self.label_card2_3.setObjectName(u"label_card2_3")
        self.label_card2_3.setGeometry(QRect(540, 140, 51, 91))
        self.label_card2_3.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_card2_3.setFrameShape(QFrame.NoFrame)
        self.label_card1_4 = QLabel(self.frame)
        self.label_card1_4.setObjectName(u"label_card1_4")
        self.label_card1_4.setGeometry(QRect(830, 190, 51, 91))
        self.label_card1_4.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_card1_4.setFrameShape(QFrame.NoFrame)
        self.label_card2_4 = QLabel(self.frame)
        self.label_card2_4.setObjectName(u"label_card2_4")
        self.label_card2_4.setGeometry(QRect(770, 190, 51, 91))
        self.label_card2_4.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_card2_4.setFrameShape(QFrame.NoFrame)
        self.label_info_5 = QLabel(self.frame)
        self.label_info_5.setObjectName(u"label_info_5")
        self.label_info_5.setGeometry(QRect(870, 500, 151, 61))
        self.label_info_5.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.label_info_5.setAlignment(Qt.AlignCenter)
        self.label_card2_0 = QLabel(self.frame)
        self.label_card2_0.setObjectName(u"label_card2_0")
        self.label_card2_0.setGeometry(QRect(540, 420, 51, 91))
        self.label_card2_0.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_card2_0.setFrameShape(QFrame.NoFrame)
        self.label_card1_0 = QLabel(self.frame)
        self.label_card1_0.setObjectName(u"label_card1_0")
        self.label_card1_0.setGeometry(QRect(480, 420, 51, 91))
        self.label_card1_0.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_card1_0.setFrameShape(QFrame.NoFrame)
        self.label_card1_5 = QLabel(self.frame)
        self.label_card1_5.setObjectName(u"label_card1_5")
        self.label_card1_5.setGeometry(QRect(830, 370, 51, 91))
        self.label_card1_5.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_card1_5.setFrameShape(QFrame.NoFrame)
        self.label_card2_5 = QLabel(self.frame)
        self.label_card2_5.setObjectName(u"label_card2_5")
        self.label_card2_5.setGeometry(QRect(770, 370, 51, 91))
        self.label_card2_5.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_card2_5.setFrameShape(QFrame.NoFrame)
        self.label_info_1 = QLabel(self.frame)
        self.label_info_1.setObjectName(u"label_info_1")
        self.label_info_1.setGeometry(QRect(70, 510, 151, 61))
        self.label_info_1.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.label_info_1.setAlignment(Qt.AlignCenter)
        self.label_info_0 = QLabel(self.frame)
        self.label_info_0.setObjectName(u"label_info_0")
        self.label_info_0.setGeometry(QRect(460, 540, 151, 61))
        self.label_info_0.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.label_info_0.setAlignment(Qt.AlignCenter)
        self.frame_input = QFrame(self.frame)
        self.frame_input.setObjectName(u"frame_input")
        self.frame_input.setGeometry(QRect(300, 640, 461, 41))
        self.frame_input.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;")
        self.frame_input.setFrameShape(QFrame.StyledPanel)
        self.frame_input.setFrameShadow(QFrame.Raised)
        self.entry_raise = QLineEdit(self.frame_input)
        self.entry_raise.setObjectName(u"entry_raise")
        self.entry_raise.setGeometry(QRect(20, 10, 371, 31))
        font1 = QFont()
        font1.setFamilies([u"ljk_OCRA"])
        font1.setBold(True)
        self.entry_raise.setFont(font1)
        self.entry_raise.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.btn_accept = QPushButton(self.frame_input)
        self.btn_accept.setObjectName(u"btn_accept")
        self.btn_accept.setGeometry(QRect(390, 10, 61, 31))
        self.btn_accept.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/cil-check-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_accept.setIcon(icon1)
        self.game_card_5 = QLabel(self.frame)
        self.game_card_5.setObjectName(u"game_card_5")
        self.game_card_5.setGeometry(QRect(660, 280, 61, 91))
        self.game_card_5.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.game_card_4 = QLabel(self.frame)
        self.game_card_4.setObjectName(u"game_card_4")
        self.game_card_4.setGeometry(QRect(580, 280, 61, 91))
        self.game_card_4.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.game_card_1 = QLabel(self.frame)
        self.game_card_1.setObjectName(u"game_card_1")
        self.game_card_1.setGeometry(QRect(340, 280, 61, 91))
        self.game_card_1.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.game_card_3 = QLabel(self.frame)
        self.game_card_3.setObjectName(u"game_card_3")
        self.game_card_3.setGeometry(QRect(500, 280, 61, 91))
        self.game_card_3.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.game_card_2 = QLabel(self.frame)
        self.game_card_2.setObjectName(u"game_card_2")
        self.game_card_2.setGeometry(QRect(420, 280, 61, 91))
        self.game_card_2.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_card1_1 = QLabel(self.frame)
        self.label_card1_1.setObjectName(u"label_card1_1")
        self.label_card1_1.setGeometry(QRect(250, 370, 51, 91))
        self.label_card1_1.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_card1_1.setFrameShape(QFrame.NoFrame)
        self.label_card1_2 = QLabel(self.frame)
        self.label_card1_2.setObjectName(u"label_card1_2")
        self.label_card1_2.setGeometry(QRect(250, 190, 51, 91))
        self.label_card1_2.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_card1_2.setFrameShape(QFrame.NoFrame)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-150, 110, 1371, 431))
        self.frame_2.setStyleSheet(u"image: url(:/newPrefix/images/\u0431\u0435\u0437 \u0442\u0435\u043d\u0435\u04391.png);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_dealer_5 = QLabel(self.frame)
        self.label_dealer_5.setObjectName(u"label_dealer_5")
        self.label_dealer_5.setGeometry(QRect(870, 560, 151, 31))
        self.label_dealer_5.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.label_info_2 = QLabel(self.frame)
        self.label_info_2.setObjectName(u"label_info_2")
        self.label_info_2.setGeometry(QRect(70, 50, 151, 61))
        self.label_info_2.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.label_info_2.setAlignment(Qt.AlignCenter)
        self.label_dealer_2 = QLabel(self.frame)
        self.label_dealer_2.setObjectName(u"label_dealer_2")
        self.label_dealer_2.setGeometry(QRect(70, 110, 151, 31))
        self.label_dealer_2.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.label_dealer_1 = QLabel(self.frame)
        self.label_dealer_1.setObjectName(u"label_dealer_1")
        self.label_dealer_1.setGeometry(QRect(70, 570, 151, 31))
        self.label_dealer_1.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.label_dealer_0 = QLabel(self.frame)
        self.label_dealer_0.setObjectName(u"label_dealer_0")
        self.label_dealer_0.setGeometry(QRect(460, 600, 151, 31))
        self.label_dealer_0.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.label_dealer_4 = QLabel(self.frame)
        self.label_dealer_4.setObjectName(u"label_dealer_4")
        self.label_dealer_4.setGeometry(QRect(870, 120, 151, 31))
        self.label_dealer_4.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.label_info_3 = QLabel(self.frame)
        self.label_info_3.setObjectName(u"label_info_3")
        self.label_info_3.setGeometry(QRect(460, 20, 151, 61))
        self.label_info_3.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.label_info_3.setAlignment(Qt.AlignCenter)
        self.label_dealer_3 = QLabel(self.frame)
        self.label_dealer_3.setObjectName(u"label_dealer_3")
        self.label_dealer_3.setGeometry(QRect(460, 80, 151, 31))
        self.label_dealer_3.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.label_lose = QLabel(self.frame)
        self.label_lose.setObjectName(u"label_lose")
        self.label_lose.setGeometry(QRect(120, -30, 781, 181))
        font2 = QFont()
        font2.setFamilies([u"ljk_OCRA"])
        font2.setPointSize(63)
        font2.setBold(True)
        self.label_lose.setFont(font2)
        self.label_lose.setStyleSheet(u"font-color: black")
        self.label_lose.setAlignment(Qt.AlignCenter)
        self.timer_2 = QLabel(self.frame)
        self.timer_2.setObjectName(u"timer_2")
        self.timer_2.setGeometry(QRect(20, 50, 49, 41))
        font3 = QFont()
        font3.setFamilies([u"ljk_OCRA"])
        font3.setPointSize(19)
        font3.setBold(True)
        self.timer_2.setFont(font3)
        self.timer_2.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.timer_2.setAlignment(Qt.AlignCenter)
        self.timer_3 = QLabel(self.frame)
        self.timer_3.setObjectName(u"timer_3")
        self.timer_3.setGeometry(QRect(410, 30, 49, 41))
        self.timer_3.setFont(font3)
        self.timer_3.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.timer_3.setAlignment(Qt.AlignCenter)
        self.timer_4 = QLabel(self.frame)
        self.timer_4.setObjectName(u"timer_4")
        self.timer_4.setGeometry(QRect(820, 60, 49, 41))
        self.timer_4.setFont(font3)
        self.timer_4.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.timer_4.setAlignment(Qt.AlignCenter)
        self.timer_1 = QLabel(self.frame)
        self.timer_1.setObjectName(u"timer_1")
        self.timer_1.setGeometry(QRect(20, 510, 49, 41))
        self.timer_1.setFont(font3)
        self.timer_1.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.timer_1.setAlignment(Qt.AlignCenter)
        self.timer_0 = QLabel(self.frame)
        self.timer_0.setObjectName(u"timer_0")
        self.timer_0.setGeometry(QRect(410, 540, 49, 41))
        self.timer_0.setFont(font3)
        self.timer_0.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.timer_0.setAlignment(Qt.AlignCenter)
        self.timer_5 = QLabel(self.frame)
        self.timer_5.setObjectName(u"timer_5")
        self.timer_5.setGeometry(QRect(820, 500, 49, 41))
        self.timer_5.setFont(font3)
        self.timer_5.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.timer_5.setAlignment(Qt.AlignCenter)
        self.photo_1 = QLabel(self.frame)
        self.photo_1.setObjectName(u"photo_1")
        self.photo_1.setGeometry(QRect(210, 470, 91, 81))
        self.photo_1.setFont(font3)
        self.photo_1.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.photo_1.setAlignment(Qt.AlignCenter)
        self.photo_0 = QLabel(self.frame)
        self.photo_0.setObjectName(u"photo_0")
        self.photo_0.setGeometry(QRect(600, 490, 91, 81))
        self.photo_0.setFont(font3)
        self.photo_0.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.photo_0.setAlignment(Qt.AlignCenter)
        self.photo_5 = QLabel(self.frame)
        self.photo_5.setObjectName(u"photo_5")
        self.photo_5.setGeometry(QRect(1000, 460, 91, 81))
        self.photo_5.setFont(font3)
        self.photo_5.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.photo_5.setAlignment(Qt.AlignCenter)
        self.photo_4 = QLabel(self.frame)
        self.photo_4.setObjectName(u"photo_4")
        self.photo_4.setGeometry(QRect(1000, 10, 91, 81))
        self.photo_4.setFont(font3)
        self.photo_4.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.photo_4.setAlignment(Qt.AlignCenter)
        self.photo_3 = QLabel(self.frame)
        self.photo_3.setObjectName(u"photo_3")
        self.photo_3.setGeometry(QRect(600, -20, 91, 81))
        self.photo_3.setFont(font3)
        self.photo_3.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.photo_3.setAlignment(Qt.AlignCenter)
        self.photo_2 = QLabel(self.frame)
        self.photo_2.setObjectName(u"photo_2")
        self.photo_2.setGeometry(QRect(210, 0, 91, 81))
        self.photo_2.setFont(font3)
        self.photo_2.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.photo_2.setAlignment(Qt.AlignCenter)
        self.frame_2.raise_()
        self.label_info_4.raise_()
        self.label_card1_3.raise_()
        self.label_card2_3.raise_()
        self.label_card1_4.raise_()
        self.label_card2_4.raise_()
        self.label_info_5.raise_()
        self.label_card2_0.raise_()
        self.label_card1_0.raise_()
        self.label_card1_5.raise_()
        self.label_card2_5.raise_()
        self.label_info_1.raise_()
        self.label_info_0.raise_()
        self.frame_input.raise_()
        self.game_card_5.raise_()
        self.game_card_4.raise_()
        self.game_card_1.raise_()
        self.game_card_3.raise_()
        self.game_card_2.raise_()
        self.label_card1_1.raise_()
        self.label_card1_2.raise_()
        self.label_dealer_5.raise_()
        self.label_info_2.raise_()
        self.label_dealer_2.raise_()
        self.label_dealer_1.raise_()
        self.label_dealer_0.raise_()
        self.label_dealer_4.raise_()
        self.label_info_3.raise_()
        self.label_dealer_3.raise_()
        self.label_lose.raise_()
        self.timer_2.raise_()
        self.timer_3.raise_()
        self.timer_4.raise_()
        self.timer_1.raise_()
        self.timer_0.raise_()
        self.timer_5.raise_()
        self.photo_1.raise_()
        self.photo_0.raise_()
        self.photo_5.raise_()
        self.photo_4.raise_()
        self.photo_3.raise_()
        self.photo_2.raise_()
        self.frame.raise_()
        self.label_card2_1.raise_()
        self.label_card2_2.raise_()
        self.btn_exit_game = QPushButton(self.centralwidget)
        self.btn_exit_game.setObjectName(u"btn_exit_game")
        self.btn_exit_game.setGeometry(QRect(10, 620, 121, 41))
        self.btn_exit_game.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icons/cil-power-standby.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exit_game.setIcon(icon2)
        self.frame_game_btns = QFrame(self.centralwidget)
        self.frame_game_btns.setObjectName(u"frame_game_btns")
        self.frame_game_btns.setGeometry(QRect(470, 670, 481, 71))
        self.frame_game_btns.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;")
        self.frame_game_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_game_btns.setFrameShadow(QFrame.Raised)
        self.btn_call = QPushButton(self.frame_game_btns)
        self.btn_call.setObjectName(u"btn_call")
        self.btn_call.setGeometry(QRect(10, 10, 141, 51))
        self.btn_call.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/icons/cil-arrow-top.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_call.setIcon(icon3)
        self.btn_fold = QPushButton(self.frame_game_btns)
        self.btn_fold.setObjectName(u"btn_fold")
        self.btn_fold.setGeometry(QRect(330, 10, 141, 51))
        self.btn_fold.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fold.setIcon(icon4)
        self.btn_raise = QPushButton(self.frame_game_btns)
        self.btn_raise.setObjectName(u"btn_raise")
        self.btn_raise.setGeometry(QRect(170, 10, 141, 51))
        self.btn_raise.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/icons/cil-chevron-double-up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_raise.setIcon(icon5)
        self.btn_fold.raise_()
        self.btn_call.raise_()
        self.btn_raise.raise_()
        self.label_all = QFrame(self.centralwidget)
        self.label_all.setObjectName(u"label_all")
        self.label_all.setGeometry(QRect(0, -10, 1291, 761))
        self.label_all.setStyleSheet(u"background-image: url(:/newPrefix/images/faux-silk-150236.jpg);")
        self.label_all.setFrameShape(QFrame.StyledPanel)
        self.label_all.setFrameShadow(QFrame.Raised)
        self.label_win = QLabel(self.label_all)
        self.label_win.setObjectName(u"label_win")
        self.label_win.setGeometry(QRect(280, -30, 781, 181))
        self.label_win.setFont(font2)
        self.label_win.setStyleSheet(u"font-color: black")
        self.label_win.setAlignment(Qt.AlignCenter)
        self.label_pot = QLabel(self.centralwidget)
        self.label_pot.setObjectName(u"label_pot")
        self.label_pot.setGeometry(QRect(0, 0, 161, 51))
        self.label_pot.setFont(font1)
        self.label_pot.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_load = QLabel(self.centralwidget)
        self.label_load.setObjectName(u"label_load")
        self.label_load.setGeometry(QRect(560, 170, 301, 304))
        font4 = QFont()
        font4.setFamilies([u"ljk_OCRA"])
        font4.setPointSize(9)
        font4.setBold(True)
        self.label_load.setFont(font4)
        self.label_load.setStyleSheet(u"background-color: none;\n"
"\n"
"\n"
"")
        Game.setCentralWidget(self.centralwidget)
        self.label_all.raise_()
        self.btn_exitgame.raise_()
        self.game_frame.raise_()
        self.btn_exit_game.raise_()
        self.frame_game_btns.raise_()
        self.label_pot.raise_()
        self.label_load.raise_()

        self.retranslateUi(Game)

        QMetaObject.connectSlotsByName(Game)
    # setupUi

    def retranslateUi(self, Game):
        Game.setWindowTitle(QCoreApplication.translate("Game", u"MainWindow", None))
        self.btn_exitgame.setText(QCoreApplication.translate("Game", u"\u0432\u044b\u0439\u0442\u0438 \u0438\u0437 \u0438\u0433\u0440\u044b", None))
        self.label_card2_1.setText("")
        self.label_card2_2.setText("")
        self.label_info_4.setText("")
        self.label_card1_3.setText("")
        self.label_card2_3.setText("")
        self.label_card1_4.setText("")
        self.label_card2_4.setText("")
        self.label_info_5.setText("")
        self.label_card2_0.setText("")
        self.label_card1_0.setText("")
        self.label_card1_5.setText("")
        self.label_card2_5.setText("")
        self.label_info_1.setText("")
        self.label_info_0.setText("")
        self.entry_raise.setPlaceholderText(QCoreApplication.translate("Game", u"\u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0443\u043c\u043c\u0443", None))
        self.btn_accept.setText("")
        self.game_card_5.setText("")
        self.game_card_4.setText("")
        self.game_card_1.setText("")
        self.game_card_3.setText("")
        self.game_card_2.setText("")
        self.label_card1_1.setText("")
        self.label_card1_2.setText("")
        self.label_dealer_5.setText("")
        self.label_info_2.setText("")
        self.label_dealer_2.setText("")
        self.label_dealer_1.setText("")
        self.label_dealer_0.setText("")
        self.label_dealer_4.setText("")
        self.label_info_3.setText("")
        self.label_dealer_3.setText("")
        self.label_lose.setText(QCoreApplication.translate("Game", u"\u0412\u044b \u043f\u0440\u043e\u0438\u0433\u0440\u0430\u043b\u0438", None))
        self.timer_2.setText(QCoreApplication.translate("Game", u"30", None))
        self.timer_3.setText(QCoreApplication.translate("Game", u"TextLabel", None))
        self.timer_4.setText(QCoreApplication.translate("Game", u"TextLabel", None))
        self.timer_1.setText(QCoreApplication.translate("Game", u"TextLabel", None))
        self.timer_0.setText(QCoreApplication.translate("Game", u"TextLabel", None))
        self.timer_5.setText(QCoreApplication.translate("Game", u"TextLabel", None))
        self.photo_1.setText(QCoreApplication.translate("Game", u"TextLabel", None))
        self.photo_0.setText(QCoreApplication.translate("Game", u"TextLabel", None))
        self.photo_5.setText(QCoreApplication.translate("Game", u"TextLabel", None))
        self.photo_4.setText(QCoreApplication.translate("Game", u"TextLabel", None))
        self.photo_3.setText(QCoreApplication.translate("Game", u"TextLabel", None))
        self.photo_2.setText(QCoreApplication.translate("Game", u"TextLabel", None))
        self.btn_exit_game.setText(QCoreApplication.translate("Game", u"\u0437\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u0438\u0433\u0440\u0443", None))
        self.btn_call.setText(QCoreApplication.translate("Game", u"CALL", None))
        self.btn_fold.setText(QCoreApplication.translate("Game", u"FOLD", None))
        self.btn_raise.setText(QCoreApplication.translate("Game", u"RAISE", None))
        self.label_win.setText(QCoreApplication.translate("Game", u"\u0412\u044b \u043f\u043e\u0431\u0435\u0434\u0438\u043b\u0438", None))
        self.label_pot.setText(QCoreApplication.translate("Game", u"\u0411\u0430\u043d\u043a:", None))
        self.label_load.setText("")
    # retranslateUi

