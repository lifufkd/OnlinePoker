# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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

class Ui_profile(object):
    def setupUi(self, profile):
        if not profile.objectName():
            profile.setObjectName(u"profile")
        profile.resize(779, 600)
        profile.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;")
        self.centralwidget = QWidget(profile)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_all = QFrame(self.centralwidget)
        self.label_all.setObjectName(u"label_all")
        self.label_all.setGeometry(QRect(0, 0, 781, 601))
        self.label_all.setStyleSheet(u"background-color: none")
        self.label_all.setFrameShape(QFrame.StyledPanel)
        self.label_all.setFrameShadow(QFrame.Raised)
        self.transaction_frame = QFrame(self.label_all)
        self.transaction_frame.setObjectName(u"transaction_frame")
        self.transaction_frame.setGeometry(QRect(410, 330, 351, 201))
        self.transaction_frame.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"border-radius: 7px;")
        self.transaction_frame.setFrameShape(QFrame.StyledPanel)
        self.transaction_frame.setFrameShadow(QFrame.Raised)
        self.lineEdit_money = QLineEdit(self.transaction_frame)
        self.lineEdit_money.setObjectName(u"lineEdit_money")
        self.lineEdit_money.setGeometry(QRect(10, 150, 291, 31))
        self.btn_money = QPushButton(self.transaction_frame)
        self.btn_money.setObjectName(u"btn_money")
        self.btn_money.setGeometry(QRect(300, 150, 41, 31))
        self.btn_money.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/cil-cursor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_money.setIcon(icon)
        self.label_2 = QLabel(self.transaction_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 331, 41))
        font = QFont()
        font.setFamilies([u"ljk_OCRA"])
        font.setPointSize(16)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: None;\n"
"border-style: None;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_5 = QLabel(self.transaction_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 50, 331, 61))
        font1 = QFont()
        font1.setFamilies([u"ljk_OCRA"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color: None;\n"
"border-style: None;")
        self.label_5.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_5.setWordWrap(True)
        self.lineEdit_2 = QLineEdit(self.transaction_frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 120, 331, 22))
        self.lineEdit_2.setStyleSheet(u"")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.label_all)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 10, 221, 31))
        self.label.setStyleSheet(u"font-size: 24px;\n"
"border-radius: 7px;\n"
"background-color: rgb(149, 149, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.btn_balance = QPushButton(self.label_all)
        self.btn_balance.setObjectName(u"btn_balance")
        self.btn_balance.setGeometry(QRect(20, 290, 181, 41))
        self.btn_balance.setStyleSheet(u"\n"
"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/cil-credit-card.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_balance.setIcon(icon1)
        self.login = QLabel(self.label_all)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(580, 110, 181, 41))
        self.login.setStyleSheet(u"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;\n"
"            border-radius:21px;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.login.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.label_all)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(410, 260, 151, 41))
        self.label_9.setStyleSheet(u"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;\n"
"            border-radius:21px;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.balance = QLabel(self.label_all)
        self.balance.setObjectName(u"balance")
        self.balance.setGeometry(QRect(580, 160, 181, 41))
        self.balance.setStyleSheet(u"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;\n"
"            border-radius:21px;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.balance.setAlignment(Qt.AlignCenter)
        self.btn_statistic = QPushButton(self.label_all)
        self.btn_statistic.setObjectName(u"btn_statistic")
        self.btn_statistic.setGeometry(QRect(20, 390, 181, 41))
        self.btn_statistic.setStyleSheet(u"\n"
"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icons/cil-chart-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_statistic.setIcon(icon2)
        self.label_4 = QLabel(self.label_all)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(410, 160, 151, 41))
        self.label_4.setStyleSheet(u"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;\n"
"            border-radius:21px;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.level = QLabel(self.label_all)
        self.level.setObjectName(u"level")
        self.level.setGeometry(QRect(580, 260, 181, 41))
        self.level.setStyleSheet(u"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;\n"
"            border-radius:21px;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.level.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.label_all)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(410, 110, 151, 41))
        self.label_7.setStyleSheet(u"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;\n"
"            border-radius:21px;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.photo = QLabel(self.label_all)
        self.photo.setObjectName(u"photo")
        self.photo.setGeometry(QRect(20, 60, 211, 201))
        self.photo.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.btn_exitgame = QPushButton(self.label_all)
        self.btn_exitgame.setObjectName(u"btn_exitgame")
        self.btn_exitgame.setGeometry(QRect(10, 550, 181, 41))
        self.btn_exitgame.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/icons/cil-door.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exitgame.setIcon(icon3)
        self.name = QLabel(self.label_all)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(580, 60, 181, 41))
        self.name.setStyleSheet(u"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;\n"
"            border-radius:21px;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.name.setAlignment(Qt.AlignCenter)
        self.btn_delete = QPushButton(self.label_all)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setGeometry(QRect(580, 550, 181, 41))
        self.btn_delete.setStyleSheet(u"\n"
"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete.setIcon(icon4)
        self.btn_change_pass = QPushButton(self.label_all)
        self.btn_change_pass.setObjectName(u"btn_change_pass")
        self.btn_change_pass.setGeometry(QRect(20, 340, 181, 41))
        self.btn_change_pass.setStyleSheet(u"\n"
"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/icons/cil-settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_change_pass.setIcon(icon5)
        self.frame_pass = QFrame(self.label_all)
        self.frame_pass.setObjectName(u"frame_pass")
        self.frame_pass.setGeometry(QRect(410, 330, 351, 201))
        self.frame_pass.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"border-radius: 7px;")
        self.frame_pass.setFrameShape(QFrame.StyledPanel)
        self.frame_pass.setFrameShadow(QFrame.Raised)
        self.lineEdit_old = QLineEdit(self.frame_pass)
        self.lineEdit_old.setObjectName(u"lineEdit_old")
        self.lineEdit_old.setGeometry(QRect(30, 21, 291, 41))
        font2 = QFont()
        font2.setFamilies([u"ljk_OCRA"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.lineEdit_old.setFont(font2)
        self.lineEdit_new = QLineEdit(self.frame_pass)
        self.lineEdit_new.setObjectName(u"lineEdit_new")
        self.lineEdit_new.setGeometry(QRect(30, 80, 291, 41))
        self.lineEdit_new.setFont(font2)
        self.btn_pass_conf = QPushButton(self.frame_pass)
        self.btn_pass_conf.setObjectName(u"btn_pass_conf")
        self.btn_pass_conf.setGeometry(QRect(30, 140, 291, 41))
        self.btn_pass_conf.setFont(font2)
        self.btn_pass_conf.setStyleSheet(u"\n"
"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/icons/cil-check-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pass_conf.setIcon(icon6)
        self.label_3 = QLabel(self.label_all)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(410, 60, 151, 41))
        self.label_3.setStyleSheet(u"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;\n"
"            border-radius:21px;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.label_all)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(410, 210, 151, 41))
        self.label_10.setStyleSheet(u"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;\n"
"            border-radius:21px;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.date_created = QLabel(self.label_all)
        self.date_created.setObjectName(u"date_created")
        self.date_created.setGeometry(QRect(580, 210, 181, 41))
        self.date_created.setStyleSheet(u"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;\n"
"            border-radius:21px;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.date_created.setAlignment(Qt.AlignCenter)
        self.label_to_big = QLabel(self.label_all)
        self.label_to_big.setObjectName(u"label_to_big")
        self.label_to_big.setGeometry(QRect(30, 10, 181, 51))
        font3 = QFont()
        font3.setFamilies([u"ljk_OCRA"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.label_to_big.setFont(font3)
        self.label_to_big.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;")
        self.label_to_big.setAlignment(Qt.AlignCenter)
        self.label_to_big.setWordWrap(False)
        self.label_corrupted = QLabel(self.label_all)
        self.label_corrupted.setObjectName(u"label_corrupted")
        self.label_corrupted.setGeometry(QRect(30, 10, 181, 51))
        self.label_corrupted.setFont(font3)
        self.label_corrupted.setStyleSheet(u"\n"
"font-color: black")
        self.label_corrupted.setAlignment(Qt.AlignCenter)
        self.label_corrupted.setWordWrap(False)
        self.label_load = QLabel(self.centralwidget)
        self.label_load.setObjectName(u"label_load")
        self.label_load.setGeometry(QRect(250, 140, 301, 304))
        font4 = QFont()
        font4.setFamilies([u"ljk_OCRA"])
        font4.setPointSize(9)
        font4.setBold(True)
        self.label_load.setFont(font4)
        self.label_load.setStyleSheet(u"background-color: none;\n"
"\n"
"\n"
"")
        profile.setCentralWidget(self.centralwidget)

        self.retranslateUi(profile)

        QMetaObject.connectSlotsByName(profile)
    # setupUi

    def retranslateUi(self, profile):
        profile.setWindowTitle(QCoreApplication.translate("profile", u"MainWindow", None))
        self.lineEdit_money.setPlaceholderText(QCoreApplication.translate("profile", u"\u0441\u0443\u043c\u043c\u0430 \u0434\u043b\u044f \u043f\u043e\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None))
        self.btn_money.setText("")
        self.label_2.setText(QCoreApplication.translate("profile", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f \u0434\u043b\u044f \u043f\u043e\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None))
        self.label_5.setText(QCoreApplication.translate("profile", u"1.\u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0443\u043c\u043c\u0443 \u0434\u043b\u044f \u043f\u043e\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u0432 \u043f\u043e\u043b\u0435 \u043d\u0438\u0436\u0435\n"
"2.\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0430\u0434\u0440\u0435\u0441 \u0434\u043b\u044f \u043f\u0435\u0440\u0435\u0432\u043e\u0434\u0430", None))
        self.lineEdit_2.setText(QCoreApplication.translate("profile", u"1N4Qbzg6LSXUXyXu2MDuGfzxwMA7do8AyL", None))
        self.label.setText(QCoreApplication.translate("profile", u"\u0412\u0430\u0448 \u043f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.btn_balance.setText(QCoreApplication.translate("profile", u"\u043f\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0431\u0430\u043b\u0430\u043d\u0441", None))
        self.login.setText("")
        self.label_9.setText(QCoreApplication.translate("profile", u"\u0412\u0430\u0448 \u0442\u0435\u043a\u0443\u0449\u0438\u0439 \u0443\u0440\u043e\u0432\u0435\u043d\u044c", None))
        self.balance.setText("")
        self.btn_statistic.setText(QCoreApplication.translate("profile", u"\u043f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0443", None))
        self.label_4.setText(QCoreApplication.translate("profile", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u0431\u0430\u043b\u0430\u043d\u0441", None))
        self.level.setText("")
        self.label_7.setText(QCoreApplication.translate("profile", u"\u0412\u0430\u0448 \u043b\u043e\u0433\u0438\u043d", None))
        self.photo.setText("")
        self.btn_exitgame.setText(QCoreApplication.translate("profile", u"\u0437\u0430\u043a\u0440\u044b\u0442\u044c \u043f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.name.setText("")
        self.btn_delete.setText(QCoreApplication.translate("profile", u"\u0443\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.btn_change_pass.setText(QCoreApplication.translate("profile", u"\u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.lineEdit_old.setPlaceholderText(QCoreApplication.translate("profile", u"\u0442\u0435\u043a\u0443\u0449\u0438\u0439 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.lineEdit_new.setPlaceholderText(QCoreApplication.translate("profile", u"\u043d\u043e\u0432\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.btn_pass_conf.setText(QCoreApplication.translate("profile", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("profile", u"\u0412\u0430\u0448 \u043d\u0438\u043a\u043d\u0435\u0439\u043c", None))
        self.label_10.setText(QCoreApplication.translate("profile", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None))
        self.date_created.setText("")
        self.label_to_big.setText(QCoreApplication.translate("profile", u"\u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f\n"
"\u0441\u043b\u0438\u0448\u043a\u043e\u043c \u0431\u043e\u043b\u044c\u0448\u0430\u044f", None))
        self.label_corrupted.setText(QCoreApplication.translate("profile", u"\u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f\n"
"\u043f\u043e\u0432\u0440\u0435\u0436\u0434\u0435\u043d\u0430", None))
        self.label_load.setText("")
    # retranslateUi

