# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import modules.UI.resources

class Ui_admin(object):
    def setupUi(self, admin):
        if not admin.objectName():
            admin.setObjectName(u"admin")
        admin.resize(800, 606)
        admin.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;")
        self.centralwidget = QWidget(admin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_load = QLabel(self.centralwidget)
        self.label_load.setObjectName(u"label_load")
        self.label_load.setGeometry(QRect(270, 140, 301, 304))
        font = QFont()
        font.setFamilies([u"ljk_OCRA"])
        font.setPointSize(9)
        font.setBold(True)
        self.label_load.setFont(font)
        self.label_load.setStyleSheet(u"background-color: none;\n"
"\n"
"\n"
"")
        self.label_all = QFrame(self.centralwidget)
        self.label_all.setObjectName(u"label_all")
        self.label_all.setGeometry(QRect(0, 0, 801, 611))
        self.label_all.setStyleSheet(u"background-color: none;\n"
"")
        self.label_all.setFrameShape(QFrame.StyledPanel)
        self.label_all.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.label_all)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 10, 221, 31))
        self.label.setStyleSheet(u"font-size: 24px;\n"
"border-radius: 7px;\n"
"background-color: rgb(149, 149, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.btn_exit = QPushButton(self.label_all)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(600, 550, 181, 41))
        self.btn_exit.setStyleSheet(u"border-radius: 7px;\n"
"background-color: rgb(149, 149, 255);")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/cil-account-logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exit.setIcon(icon)
        self.listWidget = QListWidget(self.label_all)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 50, 401, 241))
        self.listWidget.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.frame_2 = QFrame(self.label_all)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 300, 401, 291))
        self.frame_2.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 60, 181, 31))
        self.label_10.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 20, 181, 31))
        self.label_14.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 140, 181, 31))
        self.label_15.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 100, 181, 31))
        self.label_17.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.btn_add = QPushButton(self.frame_2)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setGeometry(QRect(10, 180, 181, 41))
        self.btn_add.setStyleSheet(u"border-radius: 7px;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/cil-settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add.setIcon(icon1)
        self.btn_change = QPushButton(self.frame_2)
        self.btn_change.setObjectName(u"btn_change")
        self.btn_change.setGeometry(QRect(200, 180, 181, 41))
        self.btn_change.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;\n"
"border-radius: 7px;")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icons/cil-credit-card.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_change.setIcon(icon2)
        self.btn_delete = QPushButton(self.frame_2)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setGeometry(QRect(10, 230, 181, 41))
        self.btn_delete.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;\n"
"border-radius: 7px;")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/icons/cil-check-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete.setIcon(icon3)
        self.btn_block = QPushButton(self.frame_2)
        self.btn_block.setObjectName(u"btn_block")
        self.btn_block.setGeometry(QRect(200, 230, 181, 41))
        self.btn_block.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;\n"
"border-radius: 7px;")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/icons/cil-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_block.setIcon(icon4)
        self.label_name = QLabel(self.frame_2)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(200, 20, 181, 31))
        self.label_name.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_login = QLabel(self.frame_2)
        self.label_login.setObjectName(u"label_login")
        self.label_login.setGeometry(QRect(200, 60, 181, 31))
        self.label_login.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_money = QLabel(self.frame_2)
        self.label_money.setObjectName(u"label_money")
        self.label_money.setGeometry(QRect(200, 140, 181, 31))
        self.label_money.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_password = QLabel(self.frame_2)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setGeometry(QRect(200, 100, 181, 31))
        self.label_password.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.frame = QFrame(self.label_all)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(460, 50, 321, 491))
        self.frame.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 250, 301, 31))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 271, 31))
        font1 = QFont()
        font1.setFamilies([u"ljk_OCRA"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 140, 151, 31))
        self.label_18.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 100, 151, 31))
        self.label_11.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(0, 180, 151, 31))
        self.label_16.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(0, 60, 151, 31))
        self.label_19.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.btn_save = QPushButton(self.frame)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(70, 320, 181, 41))
        self.btn_save.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;\n"
"border-radius: 7px;")
        self.btn_save.setIcon(icon2)
        self.label_name_2 = QLineEdit(self.frame)
        self.label_name_2.setObjectName(u"label_name_2")
        self.label_name_2.setGeometry(QRect(160, 60, 151, 31))
        self.label_name_2.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_login_2 = QLineEdit(self.frame)
        self.label_login_2.setObjectName(u"label_login_2")
        self.label_login_2.setGeometry(QRect(160, 100, 151, 31))
        self.label_login_2.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_password_2 = QLineEdit(self.frame)
        self.label_password_2.setObjectName(u"label_password_2")
        self.label_password_2.setGeometry(QRect(160, 140, 151, 31))
        self.label_password_2.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.label_money_2 = QLineEdit(self.frame)
        self.label_money_2.setObjectName(u"label_money_2")
        self.label_money_2.setGeometry(QRect(160, 180, 151, 31))
        self.label_money_2.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.checkBox_2 = QCheckBox(self.frame)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(10, 220, 301, 31))
        admin.setCentralWidget(self.centralwidget)
        self.label_all.raise_()
        self.label_load.raise_()

        self.retranslateUi(admin)

        QMetaObject.connectSlotsByName(admin)
    # setupUi

    def retranslateUi(self, admin):
        admin.setWindowTitle(QCoreApplication.translate("admin", u"MainWindow", None))
        self.label_load.setText("")
        self.label.setText(QCoreApplication.translate("admin", u"\u041f\u0430\u043d\u0435\u043b\u044c \u043e\u0442\u043b\u0430\u0434\u043a\u0438", None))
        self.btn_exit.setText(QCoreApplication.translate("admin", u"\u0432\u044b\u0439\u0442\u0438 \u0438\u0437 \u043f\u0430\u043d\u0435\u043b\u0438", None))
        self.label_10.setText(QCoreApplication.translate("admin", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_14.setText(QCoreApplication.translate("admin", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label_15.setText(QCoreApplication.translate("admin", u"\u0414\u0435\u043d\u044c\u0433\u0438", None))
        self.label_17.setText(QCoreApplication.translate("admin", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.btn_add.setText(QCoreApplication.translate("admin", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btn_change.setText(QCoreApplication.translate("admin", u"\u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.btn_delete.setText(QCoreApplication.translate("admin", u"\u0443\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btn_block.setText(QCoreApplication.translate("admin", u"\u0437\u0430\u0431\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_name.setText("")
        self.label_login.setText("")
        self.label_money.setText("")
        self.label_password.setText("")
        self.checkBox.setText(QCoreApplication.translate("admin", u"\u043d\u0430\u0437\u043d\u0430\u0447\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u043e\u043c", None))
        self.label_2.setText(QCoreApplication.translate("admin", u"TextLabel", None))
        self.label_18.setText(QCoreApplication.translate("admin", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_11.setText(QCoreApplication.translate("admin", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_16.setText(QCoreApplication.translate("admin", u"\u0414\u0435\u043d\u044c\u0433\u0438", None))
        self.label_19.setText(QCoreApplication.translate("admin", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.btn_save.setText(QCoreApplication.translate("admin", u"\u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.checkBox_2.setText(QCoreApplication.translate("admin", u"\u0437\u0430\u0431\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
    # retranslateUi

