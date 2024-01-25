# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rules.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import modules.UI.resources

class Ui_rules(object):
    def setupUi(self, rules):
        if not rules.objectName():
            rules.setObjectName(u"rules")
        rules.resize(800, 585)
        rules.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;")
        self.centralwidget = QWidget(rules)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_exitgame = QPushButton(self.centralwidget)
        self.btn_exitgame.setObjectName(u"btn_exitgame")
        self.btn_exitgame.setGeometry(QRect(10, 540, 211, 41))
        self.btn_exitgame.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/cil-door.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exitgame.setIcon(icon)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 20, 441, 31))
        self.label_3.setStyleSheet(u"font-size: 24px;\n"
"border-radius: 7px;\n"
"background-color: rgb(149, 149, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 70, 751, 61))
        self.label_4.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 17px;\n"
"")
        self.label_4.setWordWrap(True)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 140, 751, 71))
        self.label_5.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 17px;\n"
"")
        self.label_5.setWordWrap(True)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 220, 751, 211))
        self.label_6.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 17px;\n"
"")
        self.label_6.setWordWrap(True)
        rules.setCentralWidget(self.centralwidget)

        self.retranslateUi(rules)

        QMetaObject.connectSlotsByName(rules)
    # setupUi

    def retranslateUi(self, rules):
        rules.setWindowTitle(QCoreApplication.translate("rules", u"MainWindow", None))
        self.btn_exitgame.setText(QCoreApplication.translate("rules", u"\u0437\u0430\u043a\u0440\u044b\u0442\u044c \u043f\u0440\u0430\u0432\u0438\u043b\u0430", None))
        self.label_3.setText(QCoreApplication.translate("rules", u"\u041f\u0440\u0430\u0432\u0438\u043b\u0430 \u0438\u0433\u0440\u044b", None))
        self.label_4.setText(QCoreApplication.translate("rules", u"\u0411\u043e\u043b\u044c\u0448\u043e\u0439 \u0431\u043b\u0430\u0439\u043d\u0434. \u0418\u0433\u0440\u043e\u043a, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0441\u0438\u0434\u0438\u0442 \u0441\u043b\u0435\u0432\u0430 \u043e\u0442 \u043c\u0430\u043b\u043e\u0433\u043e \u0431\u043b\u0430\u0439\u043d\u0434\u0430. \u041e\u043d \u0441\u0442\u0430\u0432\u0438\u0442 \u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0443\u044e \u0441\u0442\u0430\u0432\u043a\u0443 \u0432 \u0438\u0433\u0440\u0435, \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u0432 \u0434\u0432\u0430 \u0440\u0430\u0437\u0430 \u0431\u043e\u043b\u044c\u0448\u0435 \u0441\u0442\u0430\u0432\u043a\u0438 \u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0435\u0433\u043e \u0438\u0433\u0440\u043e\u043a\u0430.", None))
        self.label_5.setText(QCoreApplication.translate("rules", u"\u041c\u0430\u043b\u044b\u0439 \u0431\u043b\u0430\u0439\u043d\u0434 \u0432 \u043f\u043e\u043a\u0435\u0440\u0435 \u0432\u044b\u043f\u043e\u043b\u043d\u044f\u0435\u0442 \u0443\u0447\u0430\u0441\u0442\u043d\u0438\u043a, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0438\u043b\u0441\u044f \u043f\u0435\u0440\u0432\u044b\u043c \u043f\u043e \u043b\u0435\u0432\u0443\u044e \u0441\u0442\u043e\u0440\u043e\u043d\u0443 \u043e\u0442 \u0431\u0430\u0442\u0442\u043e\u043d\u0430. \u0421\u0443\u043c\u043c\u0430 \u0440\u0430\u0432\u043d\u044f\u0435\u0442\u0441\u044f 1/2 \u0441\u0442\u0430\u0432\u043a\u0438, \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u0431\u044b\u043b\u0430 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u0430 \u0432 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u043e\u0439 \u0440\u0430\u0437\u0434\u0430\u0447\u0435.", None))
        self.label_6.setText(QCoreApplication.translate("rules", u"\u0415\u0441\u043b\u0438 \u0438\u0433\u0440\u043e\u043a \u0434\u0435\u043b\u0430\u0435\u0442 \u0441\u0442\u0430\u0432\u043a\u0443 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u043c, \u0442\u043e \u0435\u0441\u0442\u044c \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u0442 \u043a\u0430\u043a\u0443\u044e-\u043b\u0438\u0431\u043e \u0441\u0442\u0430\u0432\u043a\u0443, \u0442\u043e \u043e\u043d \u0432\u044b\u0431\u0438\u0440\u0430\u0435\u0442, \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u043a\u0430\u0440\u0442\u044b \u0432 \u043a\u043e\u043d\u0446\u0435 \u0438\u043b\u0438 \u043d\u0435\u0442.\n"
"\n"
"\u0415\u0441\u043b\u0438 \u0438\u0433\u0440\u043e\u043a \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u0430\u043b \u0441\u0442\u0430\u0432\u043a\u0443 \u0438 \u043f\u0440\u043e\u0438\u0433\u0440\u0430\u043b, \u0442\u043e \u043e\u043d \u043c\u043e\u0436\u0435\u0442 \u0441\u043a\u0438\u043d\u0443\u0442\u044c \u043a\u0430\u0440\u0442\u044b, \u043d\u0435 \u043e\u0442\u043a\u0440\u044b"
                        "\u0432\u0430\u044f \u0438\u0445.\n"
"\n"
"\u041e\u0447\u0435\u0440\u0435\u0434\u043d\u043e\u0441\u0442\u044c \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u043a\u0430\u0440\u0442 \u043f\u0440\u0438 \u0432\u0441\u043a\u0440\u044b\u0442\u0438\u0438 \u043d\u0430\u0447\u0438\u043d\u0430\u0435\u0442\u0441\u044f \u0441 \u0442\u043e\u0433\u043e, \u043a\u0442\u043e \u043f\u043e\u0441\u0442\u0430\u0432\u0438\u043b \u043d\u0430\u0438\u0431\u043e\u043b\u044c\u0448\u0443\u044e \u0441\u0442\u0430\u0432\u043a\u0443 \u0432 \u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0435\u043c \u043a\u043e\u043d\u0443, \u0432 \u0441\u043b\u0443\u0447\u0430\u0435, \u0435\u0441\u043b\u0438 \u0438\u0433\u0440\u043e\u043a \u0438\u0434\u0435\u0442 \u00ab\u043e\u043b\u043b \u0438\u043d\u00bb, \u0442\u043e \u043a\u0430\u0440\u0442\u044b \u0432\u0441\u043a\u0440\u044b\u0432\u0430\u044e\u0442\u0441\u044f \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e.", None))
    # retranslateUi

