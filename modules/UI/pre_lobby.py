# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connect_lobby.ui'
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
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import modules.UI.resources

class Ui_pre_lobby(object):
    def setupUi(self, pre_lobby):
        if not pre_lobby.objectName():
            pre_lobby.setObjectName(u"pre_lobby")
        pre_lobby.resize(982, 602)
        pre_lobby.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;")
        self.centralwidget = QWidget(pre_lobby)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_all = QFrame(self.centralwidget)
        self.label_all.setObjectName(u"label_all")
        self.label_all.setGeometry(QRect(10, 10, 991, 611))
        self.label_all.setStyleSheet(u"background-color: None;\n"
"border-style: None;")
        self.label_all.setFrameShape(QFrame.StyledPanel)
        self.label_all.setFrameShadow(QFrame.Raised)
        self.btn_create = QPushButton(self.label_all)
        self.btn_create.setObjectName(u"btn_create")
        self.btn_create.setGeometry(QRect(500, 480, 181, 61))
        font = QFont()
        font.setFamilies([u"ljk_OCRA"])
        font.setPointSize(12)
        font.setBold(True)
        self.btn_create.setFont(font)
        self.btn_create.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_create.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/cil-settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_create.setIcon(icon)
        self.label = QLabel(self.label_all)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 0, 611, 71))
        font1 = QFont()
        font1.setFamilies([u"ljk_OCRA"])
        font1.setPointSize(40)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.label_full = QLabel(self.label_all)
        self.label_full.setObjectName(u"label_full")
        self.label_full.setGeometry(QRect(750, 330, 181, 51))
        font2 = QFont()
        font2.setFamilies([u"ljk_OCRA"])
        font2.setPointSize(17)
        font2.setBold(True)
        self.label_full.setFont(font2)
        self.label_full.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;")
        self.label_exists = QLabel(self.label_all)
        self.label_exists.setObjectName(u"label_exists")
        self.label_exists.setGeometry(QRect(750, 330, 181, 51))
        font3 = QFont()
        font3.setFamilies([u"ljk_OCRA"])
        font3.setPointSize(15)
        font3.setBold(True)
        self.label_exists.setFont(font3)
        self.label_exists.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;")
        self.label_empty = QLabel(self.label_all)
        self.label_empty.setObjectName(u"label_empty")
        self.label_empty.setGeometry(QRect(750, 330, 181, 51))
        self.label_empty.setFont(font2)
        self.label_empty.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;")
        self.btn_join = QPushButton(self.label_all)
        self.btn_join.setObjectName(u"btn_join")
        self.btn_join.setGeometry(QRect(280, 480, 181, 61))
        self.btn_join.setFont(font)
        self.btn_join.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_join.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/cil-user-follow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_join.setIcon(icon1)
        self.btn_exitgame = QPushButton(self.label_all)
        self.btn_exitgame.setObjectName(u"btn_exitgame")
        self.btn_exitgame.setGeometry(QRect(0, 500, 171, 41))
        self.btn_exitgame.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_exitgame.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icons/cil-account-logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exitgame.setIcon(icon2)
        self.btn_logout = QPushButton(self.label_all)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setGeometry(QRect(0, 450, 171, 41))
        self.btn_logout.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_logout.setStyleSheet(u"border-radius: 7px;\n"
"background-color: rgb(149, 149, 255);")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/icons/cil-door.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logout.setIcon(icon3)
        self.label_not_selected = QLabel(self.label_all)
        self.label_not_selected.setObjectName(u"label_not_selected")
        self.label_not_selected.setGeometry(QRect(720, 260, 231, 31))
        font4 = QFont()
        font4.setFamilies([u"ljk_OCRA"])
        font4.setBold(True)
        self.label_not_selected.setFont(font4)
        self.label_not_selected.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 17px;")
        self.frame_add = QFrame(self.label_all)
        self.frame_add.setObjectName(u"frame_add")
        self.frame_add.setGeometry(QRect(710, 90, 251, 381))
        font5 = QFont()
        font5.setFamilies([u"ljk_OCRA"])
        font5.setPointSize(18)
        font5.setBold(True)
        self.frame_add.setFont(font5)
        self.frame_add.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.lineEdit_lobby_name = QLineEdit(self.frame_add)
        self.lineEdit_lobby_name.setObjectName(u"lineEdit_lobby_name")
        self.lineEdit_lobby_name.setGeometry(QRect(10, 20, 231, 31))
        font6 = QFont()
        font6.setFamilies([u"ljk_OCRA"])
        font6.setPointSize(13)
        font6.setBold(True)
        self.lineEdit_lobby_name.setFont(font6)
        self.lineEdit_lobby_name.setStyleSheet(u"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;\n"
"            border-radius:21px;\n"
"border-radius: 7px;")
        self.btn_confirm = QPushButton(self.frame_add)
        self.btn_confirm.setObjectName(u"btn_confirm")
        self.btn_confirm.setGeometry(QRect(10, 140, 121, 31))
        font7 = QFont()
        font7.setFamilies([u"ljk_OCRA"])
        font7.setPointSize(10)
        font7.setBold(True)
        self.btn_confirm.setFont(font7)
        self.btn_confirm.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_confirm.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/icons/cil-check-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_confirm.setIcon(icon4)
        self.lineEdit_small_blind = QLineEdit(self.frame_add)
        self.lineEdit_small_blind.setObjectName(u"lineEdit_small_blind")
        self.lineEdit_small_blind.setGeometry(QRect(10, 100, 231, 31))
        self.lineEdit_small_blind.setFont(font6)
        self.lineEdit_small_blind.setStyleSheet(u"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;\n"
"            border-radius:21px;\n"
"border-radius: 7px;")
        self.lineEdit_big_blind = QLineEdit(self.frame_add)
        self.lineEdit_big_blind.setObjectName(u"lineEdit_big_blind")
        self.lineEdit_big_blind.setGeometry(QRect(10, 60, 231, 31))
        self.lineEdit_big_blind.setFont(font6)
        self.lineEdit_big_blind.setStyleSheet(u"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;\n"
"            border-radius:21px;\n"
"border-radius: 7px;")
        self.frame_2 = QFrame(self.label_all)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 220, 181, 221))
        self.frame_2.setStyleSheet(u"image: url(:/photos/icons/25451e51f89d681ca1d40d9c703e9578.jpg);\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.btn_profile = QPushButton(self.label_all)
        self.btn_profile.setObjectName(u"btn_profile")
        self.btn_profile.setGeometry(QRect(0, 70, 171, 41))
        self.btn_profile.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_profile.setStyleSheet(u"\n"
"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/icons/cil-home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_profile.setIcon(icon5)
        self.btn_rules = QPushButton(self.label_all)
        self.btn_rules.setObjectName(u"btn_rules")
        self.btn_rules.setGeometry(QRect(0, 120, 171, 41))
        self.btn_rules.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_rules.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/icons/cil-notes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_rules.setIcon(icon6)
        self.btn_admin = QPushButton(self.label_all)
        self.btn_admin.setObjectName(u"btn_admin")
        self.btn_admin.setEnabled(False)
        self.btn_admin.setGeometry(QRect(0, 550, 171, 41))
        self.btn_admin.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_admin.setStyleSheet(u"border-radius: 7px;\n"
"image: url(:/newPrefix/icons/cil-briefcase.png);\n"
"background-color: rgb(149, 149, 255);")
        self.listWidget = QListWidget(self.label_all)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(280, 90, 401, 381))
        font8 = QFont()
        font8.setFamilies([u"ljk_OCRA"])
        font8.setPointSize(17)
        font8.setBold(True)
        font8.setKerning(True)
        self.listWidget.setFont(font8)
        self.listWidget.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.listWidget.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;")
        self.btn_statistic = QPushButton(self.label_all)
        self.btn_statistic.setObjectName(u"btn_statistic")
        self.btn_statistic.setGeometry(QRect(0, 170, 171, 41))
        self.btn_statistic.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_statistic.setStyleSheet(u"\n"
"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/icons/cil-chart-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_statistic.setIcon(icon7)
        self.label_load = QLabel(self.label_all)
        self.label_load.setObjectName(u"label_load")
        self.label_load.setGeometry(QRect(330, 120, 301, 304))
        font9 = QFont()
        font9.setFamilies([u"ljk_OCRA"])
        font9.setPointSize(9)
        font9.setBold(True)
        self.label_load.setFont(font9)
        self.label_load.setStyleSheet(u"background-color: none;\n"
"\n"
"\n"
"")
        self.label_not_valid = QLabel(self.label_all)
        self.label_not_valid.setObjectName(u"label_not_valid")
        self.label_not_valid.setGeometry(QRect(750, 330, 181, 51))
        font10 = QFont()
        font10.setFamilies([u"ljk_OCRA"])
        font10.setPointSize(14)
        font10.setBold(True)
        self.label_not_valid.setFont(font10)
        self.label_not_valid.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;")
        self.label_not_valid.setAlignment(Qt.AlignCenter)
        self.label_not_valid.setWordWrap(False)
        self.label_size_error = QLabel(self.label_all)
        self.label_size_error.setObjectName(u"label_size_error")
        self.label_size_error.setGeometry(QRect(750, 330, 181, 51))
        self.label_size_error.setFont(font7)
        self.label_size_error.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;")
        self.label_size_error.setAlignment(Qt.AlignCenter)
        self.label_size_error.setWordWrap(False)
        self.label_not_enough = QLabel(self.label_all)
        self.label_not_enough.setObjectName(u"label_not_enough")
        self.label_not_enough.setGeometry(QRect(750, 330, 181, 51))
        self.label_not_enough.setFont(font7)
        self.label_not_enough.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;")
        self.label_not_enough.setAlignment(Qt.AlignCenter)
        self.label_not_enough.setWordWrap(False)
        self.frame_add.raise_()
        self.btn_create.raise_()
        self.label.raise_()
        self.label_full.raise_()
        self.label_exists.raise_()
        self.label_empty.raise_()
        self.btn_join.raise_()
        self.btn_exitgame.raise_()
        self.btn_logout.raise_()
        self.label_not_selected.raise_()
        self.frame_2.raise_()
        self.btn_profile.raise_()
        self.btn_rules.raise_()
        self.btn_admin.raise_()
        self.listWidget.raise_()
        self.btn_statistic.raise_()
        self.label_load.raise_()
        self.label_not_valid.raise_()
        self.label_size_error.raise_()
        self.label_not_enough.raise_()
        pre_lobby.setCentralWidget(self.centralwidget)

        self.retranslateUi(pre_lobby)

        QMetaObject.connectSlotsByName(pre_lobby)
    # setupUi

    def retranslateUi(self, pre_lobby):
        pre_lobby.setWindowTitle(QCoreApplication.translate("pre_lobby", u"MainWindow", None))
        self.btn_create.setText(QCoreApplication.translate("pre_lobby", u"\u0441\u043e\u0437\u0434\u0430\u0442\u044c \u043b\u043e\u0431\u0431\u0438", None))
        self.label.setText(QCoreApplication.translate("pre_lobby", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u043a \u0438\u0433\u0440\u0435", None))
        self.label_full.setText(QCoreApplication.translate("pre_lobby", u"\u043b\u043e\u0431\u0431\u0438 \u043f\u043e\u043b\u043d\u043e\u0435", None))
        self.label_exists.setText(QCoreApplication.translate("pre_lobby", u"\u0442\u0430\u043a\u043e\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435\n"
"\u0443\u0436\u0435 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442", None))
        self.label_empty.setText(QCoreApplication.translate("pre_lobby", u"\u043f\u043e\u043b\u044f \u043d\u0435 \u043c\u043e\u0433\u0443\u0442\n"
"\u0431\u044b\u0442\u044c \u043f\u0443\u0441\u0442\u044b\u043c\u0438", None))
        self.btn_join.setText(QCoreApplication.translate("pre_lobby", u"\u043f\u0440\u0438\u0441\u043e\u0435\u0434\u0438\u043d\u0438\u0442\u044c\u0441\u044f", None))
        self.btn_exitgame.setText(QCoreApplication.translate("pre_lobby", u"\u0432\u044b\u0439\u0442\u0438 \u0438\u0437 \u0438\u0433\u0440\u044b", None))
        self.btn_logout.setText(QCoreApplication.translate("pre_lobby", u"\u0432\u044b\u0439\u0442\u0438 \u0438\u0437 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None))
        self.label_not_selected.setText(QCoreApplication.translate("pre_lobby", u"\u0432\u044b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043b\u0438 \u043b\u043e\u0431\u0431\u0438", None))
        self.lineEdit_lobby_name.setInputMask("")
        self.lineEdit_lobby_name.setPlaceholderText(QCoreApplication.translate("pre_lobby", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043b\u043e\u0431\u0431\u0438", None))
        self.btn_confirm.setText(QCoreApplication.translate("pre_lobby", u"\u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.lineEdit_small_blind.setInputMask("")
        self.lineEdit_small_blind.setPlaceholderText(QCoreApplication.translate("pre_lobby", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043c\u043b\u0430\u0434\u0448\u0443\u044e \u0440\u0443\u043a\u0443", None))
        self.lineEdit_big_blind.setInputMask("")
        self.lineEdit_big_blind.setPlaceholderText(QCoreApplication.translate("pre_lobby", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0442\u0430\u0440\u0448\u0443\u044e \u0440\u0443\u043a\u0443", None))
        self.btn_profile.setText(QCoreApplication.translate("pre_lobby", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.btn_rules.setText(QCoreApplication.translate("pre_lobby", u"\u043f\u0440\u0430\u0432\u0438\u043b\u0430 \u0438\u0433\u0440\u044b", None))
        self.btn_admin.setText("")
        self.btn_statistic.setText(QCoreApplication.translate("pre_lobby", u"\u043f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0443", None))
        self.label_load.setText("")
        self.label_not_valid.setText(QCoreApplication.translate("pre_lobby", u"\u0432\u0432\u0435\u0434\u0435\u043d\u044b \u043d\u0435\u0432\u0435\n"
"\u0440\u043d\u044b\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
        self.label_size_error.setText(QCoreApplication.translate("pre_lobby", u"\u0441\u0442\u0430\u0440\u0448\u0430\u044f \u0440\u0443\u043a\u0430 \u043d\u0435 \u043c\u043e\u0436\u0435\u0442\n"
"\u0431\u044b\u0442\u044c \u043c\u0435\u043d\u044c\u0448\u0435 \u043c\u043b\u0430\u0434\u0448\u0435\u0439", None))
        self.label_not_enough.setText(QCoreApplication.translate("pre_lobby", u"\u043d\u0435\u0434\u043e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u043e \u0441\u0440\u0435\u0434\u0441\u0442\u0432\n"
"\u0434\u043b\u044f \u0441\u0442\u0430\u0440\u0448\u0435\u0439 \u0440\u0443\u043a\u0438", None))
    # retranslateUi

