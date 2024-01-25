# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'statistic.ui'
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
    QHeaderView, QLabel, QListView, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)
import modules.UI.resources

class Ui_statistic(object):
    def setupUi(self, statistic):
        if not statistic.objectName():
            statistic.setObjectName(u"statistic")
        statistic.resize(800, 598)
        statistic.setStyleSheet(u"")
        self.centralwidget = QWidget(statistic)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"font-family: ljk_OCRA;\n"
"         font-weight: bold;\n"
"            color: rgb(255, 255, 255);\n"
"            border-style: solid;")
        self.label_load = QLabel(self.centralwidget)
        self.label_load.setObjectName(u"label_load")
        self.label_load.setGeometry(QRect(240, 140, 301, 304))
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
        self.label_all.setGeometry(QRect(0, 0, 801, 601))
        self.label_all.setStyleSheet(u"background-color: none;")
        self.label_all.setFrameShape(QFrame.StyledPanel)
        self.label_all.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.label_all)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 10, 441, 31))
        self.label_3.setStyleSheet(u"font-size: 17px;\n"
"border-radius: 7px;\n"
"background-color: rgb(149, 149, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.frame = QFrame(self.label_all)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(470, 50, 321, 541))
        self.frame.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.game_result = QLabel(self.frame)
        self.game_result.setObjectName(u"game_result")
        self.game_result.setGeometry(QRect(170, 170, 141, 31))
        self.game_result.setFont(font)
        self.game_result.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.game_result.setAlignment(Qt.AlignCenter)
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 8):
            self.tableWidget.setRowCount(8)
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
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFont(font1);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFont(font1);
        self.tableWidget.setItem(1, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(1, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFont(font1);
        self.tableWidget.setItem(2, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(2, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem12.setFont(font1);
        self.tableWidget.setItem(3, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(3, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem14.setFont(font1);
        self.tableWidget.setItem(4, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(4, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem16.setFont(font1);
        self.tableWidget.setItem(5, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(5, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem18.setFont(font1);
        self.tableWidget.setItem(6, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(6, 1, __qtablewidgetitem19)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 220, 301, 311))
        font2 = QFont()
        font2.setFamilies([u"ljk_OCRA"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.tableWidget.setFont(font2)
        self.tableWidget.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;")
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
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(25)
        self.tableWidget.verticalHeader().setDefaultSectionSize(39)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 50, 131, 31))
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 130, 131, 31))
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 131, 31))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.game_time = QLabel(self.frame)
        self.game_time.setObjectName(u"game_time")
        self.game_time.setGeometry(QRect(170, 10, 141, 31))
        self.game_time.setFont(font)
        self.game_time.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.game_time.setAlignment(Qt.AlignCenter)
        self.game_small = QLabel(self.frame)
        self.game_small.setObjectName(u"game_small")
        self.game_small.setGeometry(QRect(170, 130, 141, 31))
        self.game_small.setFont(font)
        self.game_small.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.game_small.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 90, 131, 31))
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.game_big = QLabel(self.frame)
        self.game_big.setObjectName(u"game_big")
        self.game_big.setGeometry(QRect(170, 90, 141, 31))
        self.game_big.setFont(font)
        self.game_big.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.game_big.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 170, 131, 31))
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.game_pot = QLabel(self.frame)
        self.game_pot.setObjectName(u"game_pot")
        self.game_pot.setGeometry(QRect(170, 50, 141, 31))
        self.game_pot.setFont(font)
        self.game_pot.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.game_pot.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.label_all)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 60, 131, 41))
        self.label.setFont(font2)
        self.label.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.label.setAlignment(Qt.AlignCenter)
        self.all_games_win = QLabel(self.label_all)
        self.all_games_win.setObjectName(u"all_games_win")
        self.all_games_win.setGeometry(QRect(170, 210, 141, 41))
        self.all_games_win.setFont(font)
        self.all_games_win.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.all_games_win.setAlignment(Qt.AlignCenter)
        self.listWidget = QListWidget(self.label_all)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 300, 301, 241))
        font3 = QFont()
        font3.setFamilies([u"ljk_OCRA"])
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        self.listWidget.setFont(font3)
        self.listWidget.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.listWidget.setEditTriggers(QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.listWidget.setMovement(QListView.Static)
        self.listWidget.setResizeMode(QListView.Fixed)
        self.listWidget.setLayoutMode(QListView.SinglePass)
        self.listWidget.setSpacing(7)
        self.listWidget.setViewMode(QListView.ListMode)
        self.listWidget.setModelColumn(0)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setSelectionRectVisible(True)
        self.listWidget.setItemAlignment(Qt.AlignCenter)
        self.listWidget.setSortingEnabled(False)
        self.label_6 = QLabel(self.label_all)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 110, 131, 41))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.label_all)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 160, 131, 41))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.last_date = QLabel(self.label_all)
        self.last_date.setObjectName(u"last_date")
        self.last_date.setGeometry(QRect(170, 60, 141, 41))
        self.last_date.setFont(font)
        self.last_date.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.last_date.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.label_all)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 270, 301, 21))
        font4 = QFont()
        font4.setFamilies([u"ljk_OCRA"])
        font4.setPointSize(13)
        font4.setBold(True)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.all_games = QLabel(self.label_all)
        self.all_games.setObjectName(u"all_games")
        self.all_games.setGeometry(QRect(170, 160, 141, 41))
        self.all_games.setFont(font)
        self.all_games.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.all_games.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.label_all)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 210, 131, 41))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.money_c = QLabel(self.label_all)
        self.money_c.setObjectName(u"money_c")
        self.money_c.setGeometry(QRect(170, 110, 141, 41))
        self.money_c.setFont(font)
        self.money_c.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-style: solid;\n"
"font-family: ljk_OCRA;\n"
"border-radius: 7px;\n"
"")
        self.money_c.setAlignment(Qt.AlignCenter)
        self.btn_exit_stat = QPushButton(self.label_all)
        self.btn_exit_stat.setObjectName(u"btn_exit_stat")
        self.btn_exit_stat.setGeometry(QRect(10, 550, 181, 41))
        self.btn_exit_stat.setStyleSheet(u"background-color: rgb(149, 149, 255);\n"
"border-radius: 7px;")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/cil-power-standby.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exit_stat.setIcon(icon)
        statistic.setCentralWidget(self.centralwidget)
        self.label_all.raise_()
        self.label_load.raise_()

        self.retranslateUi(statistic)

        QMetaObject.connectSlotsByName(statistic)
    # setupUi

    def retranslateUi(self, statistic):
        statistic.setWindowTitle(QCoreApplication.translate("statistic", u"MainWindow", None))
        self.label_load.setText("")
        self.label_3.setText(QCoreApplication.translate("statistic", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u0432\u0430\u0448\u0435\u0433\u043e \u043f\u0440\u043e\u0444\u0438\u043b\u044f", None))
        self.game_result.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("statistic", u"wefwf", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem1 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("statistic", u"4t43t4", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_8.setText(QCoreApplication.translate("statistic", u"\u0411\u0430\u043d\u043a", None))
        self.label_10.setText(QCoreApplication.translate("statistic", u"\u041c\u043b\u0430\u0434\u0448\u0430\u044f \u0440\u0443\u043a\u0430", None))
        self.label_7.setText(QCoreApplication.translate("statistic", u"\u0412\u0440\u0435\u043c\u044f \u0438\u0433\u0440\u044b", None))
        self.game_time.setText("")
        self.game_small.setText("")
        self.label_9.setText(QCoreApplication.translate("statistic", u"\u0421\u0442\u0430\u0440\u0448\u0430\u044f \u0440\u0443\u043a\u0430", None))
        self.game_big.setText("")
        self.label_11.setText(QCoreApplication.translate("statistic", u"\u0418\u0442\u043e\u0433", None))
        self.game_pot.setText("")
        self.label.setText(QCoreApplication.translate("statistic", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u044f\u044f \u0438\u0433\u0440\u0430", None))
        self.all_games_win.setText("")
        self.label_6.setText(QCoreApplication.translate("statistic", u"\u0411\u0430\u043b\u0430\u043d\u0441", None))
        self.label_4.setText(QCoreApplication.translate("statistic", u"\u0412\u0441\u0435\u0433\u043e \u0438\u0433\u0440", None))
        self.last_date.setText("")
        self.label_2.setText(QCoreApplication.translate("statistic", u"\u0432\u044b\u0431\u043e\u0440 \u0438\u0433\u0440\u044b", None))
        self.all_games.setText("")
        self.label_5.setText(QCoreApplication.translate("statistic", u"\u041f\u043e\u0431\u0435\u0434", None))
        self.money_c.setText("")
        self.btn_exit_stat.setText(QCoreApplication.translate("statistic", u"\u0437\u0430\u043a\u0440\u044b\u0442\u044c \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0443", None))
    # retranslateUi

