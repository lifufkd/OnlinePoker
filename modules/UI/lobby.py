# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lobby.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget)
import modules.UI.resources

class Ui_Lobby(object):
    def setupUi(self, Lobby):
        if not Lobby.objectName():
            Lobby.setObjectName(u"Lobby")
        Lobby.resize(1006, 603)
        Lobby.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;")
        self.centralwidget = QWidget(Lobby)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_all = QFrame(self.centralwidget)
        self.label_all.setObjectName(u"label_all")
        self.label_all.setGeometry(QRect(0, 0, 1011, 601))
        self.label_all.setStyleSheet(u"background-color: none")
        self.label_all.setFrameShape(QFrame.StyledPanel)
        self.label_all.setFrameShadow(QFrame.Raised)
        self.label_exists = QLabel(self.label_all)
        self.label_exists.setObjectName(u"label_exists")
        self.label_exists.setGeometry(QRect(440, 250, 231, 51))
        font = QFont()
        font.setFamilies([u"ljk_OCRA"])
        font.setPointSize(15)
        font.setBold(True)
        self.label_exists.setFont(font)
        self.label_exists.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;")
        self.label_exists.setAlignment(Qt.AlignCenter)
        self.btn_logout = QPushButton(self.label_all)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setGeometry(QRect(10, 400, 211, 41))
        self.btn_logout.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_logout.setStyleSheet(u"border-radius: 7px;\n"
"background-color: rgb(149, 149, 255);")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/cil-account-logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logout.setIcon(icon)
        self.btn_rules = QPushButton(self.label_all)
        self.btn_rules.setObjectName(u"btn_rules")
        self.btn_rules.setGeometry(QRect(10, 140, 211, 41))
        self.btn_rules.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_rules.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/cil-notes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_rules.setIcon(icon1)
        self.label_2 = QLabel(self.label_all)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 211, 31))
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"font-size: 17px;\n"
"border-radius: 7px;\n"
"background-color: rgb(149, 149, 255);")
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.frame_add = QFrame(self.label_all)
        self.frame_add.setObjectName(u"frame_add")
        self.frame_add.setGeometry(QRect(430, 80, 251, 221))
        font1 = QFont()
        font1.setFamilies([u"ljk_OCRA"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.frame_add.setFont(font1)
        self.frame_add.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"\n"
"")
        self.btn_confirm = QPushButton(self.frame_add)
        self.btn_confirm.setObjectName(u"btn_confirm")
        self.btn_confirm.setGeometry(QRect(10, 130, 231, 31))
        font2 = QFont()
        font2.setFamilies([u"ljk_OCRA"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.btn_confirm.setFont(font2)
        self.btn_confirm.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_confirm.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icons/cil-chevron-bottom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_confirm.setIcon(icon2)
        self.lineEdit_small_blind = QLineEdit(self.frame_add)
        self.lineEdit_small_blind.setObjectName(u"lineEdit_small_blind")
        self.lineEdit_small_blind.setGeometry(QRect(10, 80, 231, 31))
        font3 = QFont()
        font3.setFamilies([u"ljk_OCRA"])
        font3.setPointSize(13)
        font3.setBold(True)
        self.lineEdit_small_blind.setFont(font3)
        self.lineEdit_small_blind.setStyleSheet(u"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;\n"
"            border-radius:21px;\n"
"border-radius: 7px;")
        self.lineEdit_small_blind.setAlignment(Qt.AlignCenter)
        self.lineEdit_big_blind = QLineEdit(self.frame_add)
        self.lineEdit_big_blind.setObjectName(u"lineEdit_big_blind")
        self.lineEdit_big_blind.setGeometry(QRect(10, 30, 231, 31))
        self.lineEdit_big_blind.setFont(font3)
        self.lineEdit_big_blind.setStyleSheet(u"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;\n"
"            border-radius:21px;\n"
"border-radius: 7px;")
        self.lineEdit_big_blind.setAlignment(Qt.AlignCenter)
        self.textEdit = QTextEdit(self.label_all)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(240, 350, 441, 191))
        self.textEdit.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.btn_profile = QPushButton(self.label_all)
        self.btn_profile.setObjectName(u"btn_profile")
        self.btn_profile.setGeometry(QRect(10, 350, 211, 41))
        self.btn_profile.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_profile.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/icons/cil-home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_profile.setIcon(icon3)
        self.label_3 = QLabel(self.label_all)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 10, 441, 31))
        self.label_3.setStyleSheet(u"font-size: 17px;\n"
"border-radius: 7px;\n"
"background-color: rgb(149, 149, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_empty = QLabel(self.label_all)
        self.label_empty.setObjectName(u"label_empty")
        self.label_empty.setGeometry(QRect(440, 250, 231, 51))
        font4 = QFont()
        font4.setFamilies([u"ljk_OCRA"])
        font4.setPointSize(17)
        font4.setBold(True)
        self.label_empty.setFont(font4)
        self.label_empty.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;")
        self.label_empty.setAlignment(Qt.AlignCenter)
        self.label_small_blind = QLabel(self.label_all)
        self.label_small_blind.setObjectName(u"label_small_blind")
        self.label_small_blind.setGeometry(QRect(240, 200, 181, 101))
        font5 = QFont()
        font5.setFamilies([u"ljk_OCRA"])
        font5.setPointSize(12)
        font5.setBold(True)
        self.label_small_blind.setFont(font5)
        self.label_small_blind.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.label_small_blind.setAlignment(Qt.AlignCenter)
        self.label_big_blind = QLabel(self.label_all)
        self.label_big_blind.setObjectName(u"label_big_blind")
        self.label_big_blind.setGeometry(QRect(240, 80, 181, 101))
        self.label_big_blind.setFont(font5)
        self.label_big_blind.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.label_big_blind.setAlignment(Qt.AlignCenter)
        self.btn_exitgame = QPushButton(self.label_all)
        self.btn_exitgame.setObjectName(u"btn_exitgame")
        self.btn_exitgame.setGeometry(QRect(10, 500, 211, 41))
        self.btn_exitgame.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_exitgame.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/icons/cil-door.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exitgame.setIcon(icon4)
        self.btn_admin = QPushButton(self.label_all)
        self.btn_admin.setObjectName(u"btn_admin")
        self.btn_admin.setEnabled(False)
        self.btn_admin.setGeometry(QRect(10, 550, 211, 41))
        self.btn_admin.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_admin.setStyleSheet(u"border-radius: 7px;\n"
"image: url(:/newPrefix/icons/cil-briefcase.png);\n"
"background-color: rgb(149, 149, 255);")
        self.tableWidget = QTableWidget(self.label_all)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 7):
            self.tableWidget.setRowCount(7)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem5)
        font6 = QFont()
        font6.setPointSize(13)
        font6.setBold(True)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFont(font6);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem6)
        font7 = QFont()
        font7.setPointSize(13)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFont(font7);
        self.tableWidget.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFont(font6);
        self.tableWidget.setItem(1, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFont(font7);
        self.tableWidget.setItem(1, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFont(font6);
        self.tableWidget.setItem(2, 0, __qtablewidgetitem10)
        font8 = QFont()
        font8.setPointSize(13)
        font8.setBold(False)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem11.setFont(font8);
        self.tableWidget.setItem(2, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem12.setFont(font6);
        self.tableWidget.setItem(3, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setFont(font7);
        self.tableWidget.setItem(3, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem14.setFont(font6);
        self.tableWidget.setItem(4, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem15.setFont(font7);
        self.tableWidget.setItem(4, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem16.setFont(font6);
        self.tableWidget.setItem(5, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem17.setFont(font7);
        self.tableWidget.setItem(5, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem18.setFont(font6);
        self.tableWidget.setItem(6, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem19.setFont(font7);
        self.tableWidget.setItem(6, 1, __qtablewidgetitem19)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(700, 80, 291, 511))
        self.tableWidget.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 14px")
        self.tableWidget.setFrameShadow(QFrame.Raised)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setAutoScrollMargin(22)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setRowCount(7)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(97)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(145)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(73)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.label = QLabel(self.label_all)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(700, 10, 291, 31))
        self.label.setStyleSheet(u"font-size: 17px;\n"
"border-radius: 7px;\n"
"background-color: rgb(149, 149, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.btn_chat_send = QPushButton(self.label_all)
        self.btn_chat_send.setObjectName(u"btn_chat_send")
        self.btn_chat_send.setGeometry(QRect(580, 550, 101, 41))
        self.btn_chat_send.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_chat_send.setStyleSheet(u"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"background-color: rgb(149, 149, 255);")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/icons/cil-cursor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_chat_send.setIcon(icon5)
        self.lineEdit_chat_input = QLineEdit(self.label_all)
        self.lineEdit_chat_input.setObjectName(u"lineEdit_chat_input")
        self.lineEdit_chat_input.setGeometry(QRect(240, 550, 341, 41))
        self.lineEdit_chat_input.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"font-size: 15px;")
        self.btn_configure = QPushButton(self.label_all)
        self.btn_configure.setObjectName(u"btn_configure")
        self.btn_configure.setGeometry(QRect(10, 200, 211, 41))
        self.btn_configure.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_configure.setStyleSheet(u"\n"
"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/icons/cil-settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_configure.setIcon(icon6)
        self.btn_statistic = QPushButton(self.label_all)
        self.btn_statistic.setObjectName(u"btn_statistic")
        self.btn_statistic.setGeometry(QRect(10, 260, 211, 41))
        self.btn_statistic.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_statistic.setStyleSheet(u"\n"
"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/icons/cil-chart-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_statistic.setIcon(icon7)
        self.btn_exit_lobby = QPushButton(self.label_all)
        self.btn_exit_lobby.setObjectName(u"btn_exit_lobby")
        self.btn_exit_lobby.setGeometry(QRect(10, 450, 211, 41))
        self.btn_exit_lobby.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_exit_lobby.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/icons/cil-power-standby.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exit_lobby.setIcon(icon8)
        self.btn_gostart = QPushButton(self.label_all)
        self.btn_gostart.setObjectName(u"btn_gostart")
        self.btn_gostart.setGeometry(QRect(10, 80, 211, 41))
        self.btn_gostart.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_gostart.setStyleSheet(u"border-radius: 7px;\n"
"background-color: rgb(149, 149, 255);")
        icon9 = QIcon()
        icon9.addFile(u":/newPrefix/icons/cil-check-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_gostart.setIcon(icon9)
        self.label_not_valid = QLabel(self.label_all)
        self.label_not_valid.setObjectName(u"label_not_valid")
        self.label_not_valid.setGeometry(QRect(440, 250, 231, 51))
        self.label_not_valid.setFont(font4)
        self.label_not_valid.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;")
        self.label_not_valid.setAlignment(Qt.AlignCenter)
        self.label_load = QLabel(self.centralwidget)
        self.label_load.setObjectName(u"label_load")
        self.label_load.setGeometry(QRect(320, 150, 301, 304))
        font9 = QFont()
        font9.setFamilies([u"ljk_OCRA"])
        font9.setPointSize(9)
        font9.setBold(True)
        self.label_load.setFont(font9)
        self.label_load.setStyleSheet(u"background-color: none;\n"
"\n"
"\n"
"")
        self.label_size_error = QLabel(self.centralwidget)
        self.label_size_error.setObjectName(u"label_size_error")
        self.label_size_error.setGeometry(QRect(440, 250, 231, 51))
        self.label_size_error.setFont(font3)
        self.label_size_error.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;")
        self.label_size_error.setAlignment(Qt.AlignCenter)
        self.label_not_enough = QLabel(self.centralwidget)
        self.label_not_enough.setObjectName(u"label_not_enough")
        self.label_not_enough.setGeometry(QRect(440, 250, 231, 51))
        self.label_not_enough.setFont(font5)
        self.label_not_enough.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;")
        self.label_not_enough.setAlignment(Qt.AlignCenter)
        self.label_not_enough.setWordWrap(False)
        self.label_not_enough_2 = QLabel(self.centralwidget)
        self.label_not_enough_2.setObjectName(u"label_not_enough_2")
        self.label_not_enough_2.setGeometry(QRect(440, 250, 231, 51))
        self.label_not_enough_2.setFont(font5)
        self.label_not_enough_2.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;")
        self.label_not_enough_2.setAlignment(Qt.AlignCenter)
        self.label_not_enough_2.setWordWrap(False)
        Lobby.setCentralWidget(self.centralwidget)

        self.retranslateUi(Lobby)

        QMetaObject.connectSlotsByName(Lobby)
    # setupUi

    def retranslateUi(self, Lobby):
        Lobby.setWindowTitle(QCoreApplication.translate("Lobby", u"MainWindow", None))
        self.label_exists.setText(QCoreApplication.translate("Lobby", u"\u0442\u0430\u043a\u043e\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435\n"
"\u0443\u0436\u0435 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442", None))
        self.btn_logout.setText(QCoreApplication.translate("Lobby", u"\u0432\u044b\u0439\u0442\u0438 \u0438\u0437 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None))
        self.btn_rules.setText(QCoreApplication.translate("Lobby", u"\u043f\u0440\u0430\u0432\u0438\u043b\u0430 \u0438\u0433\u0440\u044b", None))
        self.label_2.setText(QCoreApplication.translate("Lobby", u"\u041f\u043e\u0438\u0441\u043a \u0438\u0433\u0440\u043e\u043a\u043e\u0432...", None))
        self.btn_confirm.setText(QCoreApplication.translate("Lobby", u"\u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.lineEdit_small_blind.setInputMask("")
        self.lineEdit_small_blind.setPlaceholderText(QCoreApplication.translate("Lobby", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043c\u043b\u0430\u0434\u0448\u0443\u044e \u0440\u0443\u043a\u0443", None))
        self.lineEdit_big_blind.setInputMask("")
        self.lineEdit_big_blind.setPlaceholderText(QCoreApplication.translate("Lobby", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0442\u0430\u0440\u0448\u0443\u044e \u0440\u0443\u043a\u0443", None))
        self.btn_profile.setText(QCoreApplication.translate("Lobby", u"\u043f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.label_3.setText(QCoreApplication.translate("Lobby", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0438\u0433\u0440\u043e\u043a\u043e\u0432... \u043f\u0440\u043e\u0433\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u043b\u043e \u0437\u0430 \"\u0441\u0442\u0430\u0440\u0442\"", None))
        self.label_empty.setText(QCoreApplication.translate("Lobby", u"\u043f\u043e\u043b\u044f \u043d\u0435 \u043c\u043e\u0433\u0443\u0442\n"
"\u0431\u044b\u0442\u044c \u043f\u0443\u0441\u0442\u044b\u043c\u0438", None))
        self.label_small_blind.setText(QCoreApplication.translate("Lobby", u"\u043c\u043b\u0430\u0434\u0448\u0430\u044f \u0440\u0443\u043a\u0430: ...", None))
        self.label_big_blind.setText(QCoreApplication.translate("Lobby", u"\u0441\u0442\u0430\u0440\u0448\u0430\u044f \u0440\u0443\u043a\u0430: ...", None))
        self.btn_exitgame.setText(QCoreApplication.translate("Lobby", u"\u0432\u044b\u0439\u0442\u0438 \u0438\u0437 \u0438\u0433\u0440\u044b", None))
        self.btn_admin.setText("")

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("Lobby", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0438\u0433\u0440\u043e\u043a\u043e\u0432 \u0432 \u043b\u043e\u0431\u0431\u0438...", None))
        self.btn_chat_send.setText(QCoreApplication.translate("Lobby", u"\u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.lineEdit_chat_input.setPlaceholderText(QCoreApplication.translate("Lobby", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
        self.btn_configure.setText(QCoreApplication.translate("Lobby", u"\u043d\u0430\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u043b\u043e\u0431\u0431\u0438", None))
        self.btn_statistic.setText(QCoreApplication.translate("Lobby", u"\u043f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0443", None))
        self.btn_exit_lobby.setText(QCoreApplication.translate("Lobby", u"\u0432\u044b\u0439\u0442\u0438 \u0438\u0437 \u043b\u043e\u0431\u0431\u0438", None))
        self.btn_gostart.setText(QCoreApplication.translate("Lobby", u"\u043f\u0440\u043e\u0433\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u0442\u044c \u0437\u0430 \u0441\u0442\u0430\u0440\u0442", None))
        self.label_not_valid.setText(QCoreApplication.translate("Lobby", u"\u0434\u0430\u043d\u043d\u044b\u0435 \u043d\u0435\u0432\u0435\u0440\u043d\u044b", None))
        self.label_load.setText("")
        self.label_size_error.setText(QCoreApplication.translate("Lobby", u"\u0441\u0442\u0430\u0440\u0448\u0430\u044f \u0440\u0443\u043a\u0430 \u043d\u0435 \u043c\u043e\u0436\u0435\u0442\n"
"\u0431\u044b\u0442\u044c \u043c\u0435\u043d\u044c\u0448\u0435 \u043c\u043b\u0430\u0434\u0448\u0435\u0439", None))
        self.label_not_enough.setText(QCoreApplication.translate("Lobby", u"\u043d\u0435\u0434\u043e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u043e \u0441\u0440\u0435\u0434\u0441\u0442\u0432\n"
"\u0434\u043b\u044f \u0441\u0442\u0430\u0440\u0448\u0435\u0439 \u0440\u0443\u043a\u0438", None))
        self.label_not_enough_2.setText(QCoreApplication.translate("Lobby", u"\u0443 \u0438\u0433\u0440\u043e\u043a\u0430(\u043e\u0432)\n"
"\u043d\u0435\u0434\u043e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u043e \u0441\u0440\u0435\u0434\u0441\u0442\u0432", None))
    # retranslateUi

