# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log_in_forn.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(546, 589)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;\n"
"            \n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_load = QLabel(self.centralwidget)
        self.label_load.setObjectName(u"label_load")
        self.label_load.setGeometry(QRect(130, 170, 301, 304))
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
        self.label_all.setGeometry(QRect(-10, 10, 561, 581))
        self.label_all.setStyleSheet(u"background-color: none")
        self.label_all.setFrameShape(QFrame.StyledPanel)
        self.label_all.setFrameShadow(QFrame.Raised)
        self.login_frame = QFrame(self.label_all)
        self.login_frame.setObjectName(u"login_frame")
        self.login_frame.setGeometry(QRect(70, 140, 441, 401))
        font1 = QFont()
        font1.setFamilies([u"ljk_OCRA"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.login_frame.setFont(font1)
        self.login_frame.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"\n"
"")
        self.lineEdit_login = QLineEdit(self.login_frame)
        self.lineEdit_login.setObjectName(u"lineEdit_login")
        self.lineEdit_login.setGeometry(QRect(150, 50, 281, 31))
        font2 = QFont()
        font2.setFamilies([u"ljk_OCRA"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.lineEdit_login.setFont(font2)
        self.lineEdit_login.setStyleSheet(u"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;\n"
"            border-radius:21px;")
        self.lineEdit_password = QLineEdit(self.login_frame)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setGeometry(QRect(150, 90, 281, 31))
        self.lineEdit_password.setFont(font2)
        self.lineEdit_password.setStyleSheet(u"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;\n"
"            border-radius:21px;")
        self.label_login = QLabel(self.login_frame)
        self.label_login.setObjectName(u"label_login")
        self.label_login.setGeometry(QRect(10, 50, 121, 31))
        font3 = QFont()
        font3.setFamilies([u"ljk_OCRA"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.label_login.setFont(font3)
        self.label_login.setStyleSheet(u"background-color:: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));")
        self.label_login.setAlignment(Qt.AlignCenter)
        self.label_password = QLabel(self.login_frame)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setGeometry(QRect(10, 90, 121, 31))
        font4 = QFont()
        font4.setFamilies([u"ljk_OCRA"])
        font4.setPointSize(10)
        font4.setBold(True)
        self.label_password.setFont(font4)
        self.label_password.setStyleSheet(u"background-color:: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));")
        self.label_password.setAlignment(Qt.AlignCenter)
        self.label_name = QLabel(self.login_frame)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(10, 10, 121, 31))
        self.label_name.setFont(font3)
        self.label_name.setStyleSheet(u"background-color:: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));")
        self.label_name.setAlignment(Qt.AlignCenter)
        self.lineEdit_name = QLineEdit(self.login_frame)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setGeometry(QRect(150, 10, 281, 31))
        self.lineEdit_name.setFont(font2)
        self.lineEdit_name.setStyleSheet(u"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;\n"
"            border-radius:21px;")
        self.pushButton_enterens = QPushButton(self.login_frame)
        self.pushButton_enterens.setObjectName(u"pushButton_enterens")
        self.pushButton_enterens.setGeometry(QRect(10, 300, 181, 81))
        font5 = QFont()
        font5.setFamilies([u"ljk_OCRA"])
        font5.setPointSize(20)
        font5.setBold(True)
        self.pushButton_enterens.setFont(font5)
        self.pushButton_enterens.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_registration = QPushButton(self.login_frame)
        self.pushButton_registration.setObjectName(u"pushButton_registration")
        self.pushButton_registration.setGeometry(QRect(250, 300, 181, 81))
        font6 = QFont()
        font6.setFamilies([u"ljk_OCRA"])
        font6.setPointSize(19)
        font6.setBold(True)
        self.pushButton_registration.setFont(font6)
        self.pushButton_registration.setCursor(QCursor(Qt.PointingHandCursor))
        self.line = QFrame(self.login_frame)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 150, 441, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_reg_complexity = QLabel(self.login_frame)
        self.label_reg_complexity.setObjectName(u"label_reg_complexity")
        self.label_reg_complexity.setGeometry(QRect(10, 190, 421, 81))
        font7 = QFont()
        font7.setFamilies([u"ljk_OCRA"])
        font7.setPointSize(15)
        font7.setBold(True)
        self.label_reg_complexity.setFont(font7)
        self.label_reg_complexity.setStyleSheet(u"background-color:: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));")
        self.label_reg_complexity.setAlignment(Qt.AlignCenter)
        self.label_reg_8characters = QLabel(self.login_frame)
        self.label_reg_8characters.setObjectName(u"label_reg_8characters")
        self.label_reg_8characters.setGeometry(QRect(10, 190, 421, 81))
        self.label_reg_8characters.setFont(font6)
        self.label_reg_8characters.setStyleSheet(u"background-color:: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));")
        self.label_reg_8characters.setAlignment(Qt.AlignCenter)
        self.label_reg_notvalid = QLabel(self.login_frame)
        self.label_reg_notvalid.setObjectName(u"label_reg_notvalid")
        self.label_reg_notvalid.setGeometry(QRect(10, 190, 421, 81))
        font8 = QFont()
        font8.setFamilies([u"ljk_OCRA"])
        font8.setPointSize(28)
        font8.setBold(True)
        self.label_reg_notvalid.setFont(font8)
        self.label_reg_notvalid.setStyleSheet(u"background-color:: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));")
        self.label_reg_notvalid.setAlignment(Qt.AlignCenter)
        self.label_reg_block = QLabel(self.login_frame)
        self.label_reg_block.setObjectName(u"label_reg_block")
        self.label_reg_block.setGeometry(QRect(10, 190, 421, 81))
        self.label_reg_block.setFont(font6)
        self.label_reg_block.setStyleSheet(u"background-color:: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));")
        self.label_reg_block.setAlignment(Qt.AlignCenter)
        self.label_reg_empty = QLabel(self.login_frame)
        self.label_reg_empty.setObjectName(u"label_reg_empty")
        self.label_reg_empty.setGeometry(QRect(10, 190, 421, 81))
        self.label_reg_empty.setFont(font5)
        self.label_reg_empty.setStyleSheet(u"background-color:: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));")
        self.label_reg_empty.setAlignment(Qt.AlignCenter)
        self.label_reg_success = QLabel(self.login_frame)
        self.label_reg_success.setObjectName(u"label_reg_success")
        self.label_reg_success.setGeometry(QRect(10, 190, 421, 81))
        font9 = QFont()
        font9.setFamilies([u"ljk_OCRA"])
        font9.setPointSize(16)
        font9.setBold(True)
        self.label_reg_success.setFont(font9)
        self.label_reg_success.setStyleSheet(u"background-color:: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));")
        self.label_reg_success.setAlignment(Qt.AlignCenter)
        self.label_reg_already = QLabel(self.login_frame)
        self.label_reg_already.setObjectName(u"label_reg_already")
        self.label_reg_already.setGeometry(QRect(10, 190, 421, 81))
        font10 = QFont()
        font10.setFamilies([u"ljk_OCRA"])
        font10.setPointSize(22)
        font10.setBold(True)
        self.label_reg_already.setFont(font10)
        self.label_reg_already.setStyleSheet(u"background-color:: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));")
        self.label_reg_already.setAlignment(Qt.AlignCenter)
        self.label_reg_already_used = QLabel(self.login_frame)
        self.label_reg_already_used.setObjectName(u"label_reg_already_used")
        self.label_reg_already_used.setGeometry(QRect(10, 190, 421, 81))
        self.label_reg_already_used.setFont(font10)
        self.label_reg_already_used.setStyleSheet(u"background-color:: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));")
        self.label_reg_already_used.setAlignment(Qt.AlignCenter)
        self.label_log_in = QLabel(self.label_all)
        self.label_log_in.setObjectName(u"label_log_in")
        self.label_log_in.setGeometry(QRect(70, 40, 441, 91))
        self.label_log_in.setFont(font10)
        self.label_log_in.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"\n"
"")
        self.label_log_in.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_all.raise_()
        self.label_load.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label_load.setText("")
        self.label_login.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f", None))
        self.pushButton_enterens.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
        self.pushButton_registration.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.label_reg_complexity.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c \u0434\u043e\u043b\u0436\u0435\u043d \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0442\u044c \n"
"\u0431\u0443\u043a\u0432\u044b \u0432\u0435\u0440\u0445\u043d\u0435\u0433\u043e \u0438 \u043d\u0438\u0436\u043d\u0435\u0433\u043e \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430, \n"
"\u0446\u0438\u0444\u0440\u044b, \u0441\u043f\u0435\u0446\u0441\u0438\u043c\u0432\u043e\u043b\u044b", None))
        self.label_reg_8characters.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430 \u043f\u0430\u0440\u043e\u043b\u044f \u0434\u043e\u043b\u0436\u043d\u0430 \n"
"\u0431\u044b\u0442\u044c \u0431\u043e\u043b\u044c\u0448\u0435 8 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432", None))
        self.label_reg_notvalid.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043d\u0435 \u0432\u0435\u0440\u043d\u044b", None))
        self.label_reg_block.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0451\u0442\u043d\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c \u0437\u0430\u0431\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u0430\u043d\u0430", None))
        self.label_reg_empty.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044f \u043d\u0435 \u043c\u043e\u0433\u0443\u0442 \u0431\u044b\u0442\u044c \u043f\u0443\u0441\u0442\u044b\u043c\u0438", None))
        self.label_reg_success.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b \u0443\u0441\u043f\u0435\u0448\u043d\u043e \u0437\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u044b!\n"
" \u0432 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0435 \u0431\u043e\u043d\u0443\u0441\u0430 \u043d\u0430 \u0412\u0430\u0448 \u0441\u0447\u0451\u0442\n"
"\u0437\u0430\u0447\u0438\u0441\u043b\u0435\u043d\u0430 1000$", None))
        self.label_reg_already.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u043a\u0430\u0443\u043d\u0442 \u0443\u0436\u0435 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442", None))
        self.label_reg_already_used.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u0430\u043a\u043a\u0430\u0443\u043d\u0442 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d \u0432\u0445\u043e\u0434\n"
"\u0441 \u0434\u0440\u0443\u0433\u043e\u0433\u043e \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430", None))
        self.label_log_in.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
    # retranslateUi

