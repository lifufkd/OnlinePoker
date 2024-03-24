# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirm.ui'
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
    QSizePolicy, QStatusBar, QWidget)
import modules.UI.resources

class Ui_confirm(object):
    def setupUi(self, confirm):
        if not confirm.objectName():
            confirm.setObjectName(u"confirm")
        confirm.resize(439, 238)
        confirm.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;")
        self.centralwidget = QWidget(confirm)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 50, 301, 71))
        font = QFont()
        font.setFamilies([u"ljk_OCRA"])
        font.setPointSize(23)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;\n"
"            border-radius:21px;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.no = QPushButton(self.centralwidget)
        self.no.setObjectName(u"no")
        self.no.setGeometry(QRect(70, 140, 131, 41))
        self.no.setStyleSheet(u"\n"
"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.no.setIcon(icon)
        self.yes = QPushButton(self.centralwidget)
        self.yes.setObjectName(u"yes")
        self.yes.setGeometry(QRect(240, 140, 131, 41))
        font1 = QFont()
        font1.setFamilies([u"ljk_OCRA"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.yes.setFont(font1)
        self.yes.setStyleSheet(u"\n"
"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/cil-check-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.yes.setIcon(icon1)
        confirm.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(confirm)
        self.statusbar.setObjectName(u"statusbar")
        confirm.setStatusBar(self.statusbar)

        self.retranslateUi(confirm)

        QMetaObject.connectSlotsByName(confirm)
    # setupUi

    def retranslateUi(self, confirm):
        confirm.setWindowTitle(QCoreApplication.translate("confirm", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("confirm", u"\u0412\u044b \u0443\u0432\u0435\u0440\u0435\u043d\u044b?", None))
        self.no.setText("")
        self.yes.setText("")
    # retranslateUi

