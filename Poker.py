################################################################################
## Project developed with SBR, MR_Boombastic, Какой-то китаец
##
## Created date: 19.10.23-21.11.23
##
## WARNING! All changes made in this file will be lost your mind!
################################################################################

import socket
import ssl
import string
import pathlib
import hashlib
import os
import json
import base64
import pickle
from pathlib import Path
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtGui import QPixmap, QImage, QMovie
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QGraphicsBlurEffect
from PySide6.QtCore import QRunnable, Slot, Signal, QObject, QThreadPool, Qt, QSize, QEvent, QByteArray
import copy
import imghdr
import webbrowser
import sys
import time
import traceback
from modules.UI.log_in_gui import Ui_MainWindow
from modules.UI.pre_lobby import Ui_pre_lobby
from modules.UI.rules import Ui_rules
from modules.UI.profile import Ui_profile
from modules.UI.lobby import Ui_Lobby
from modules.UI.game import Ui_Game
from modules.UI.admin import Ui_admin
from modules.UI.confirm import Ui_confirm
from modules.UI.statistic import Ui_statistic
from datetime import datetime, timezone

#############################CHANGEABLE VARIABLES###############################
DOMAIN = '127.0.0.1'
PORT = 9091
PEM_Path = 'certs/crt_127.0.0.1/abs.pem'
IMG_Path = 'images/images/loading.gif'
################################################################################

##############################STATICK VARIABLES#################################
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
shadow_data = []
################################################################################


client_soc_ssl = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
client_soc_ssl.load_verify_locations(Path(pathlib.Path.cwd(), PEM_Path))
client_soc = socket.socket()
ssl_client = client_soc_ssl.wrap_socket(client_soc, server_hostname=DOMAIN)
ssl_client.connect((DOMAIN, PORT))

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%


class WorkerSignals(QObject):
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()


def loading_anim(switch, source):
    if switch:
        source.setEnabled(False)
    else:
        source.setEnabled(True)


def check_complexity(password):
    upper_case = any([1 if i in string.ascii_uppercase else 0 for i in password])
    lower_case = any([1 if i in string.ascii_lowercase else 0 for i in password])
    special_s = any([1 if i in string.punctuation else 0 for i in password])
    digits = any([1 if i in string.digits else 0 for i in password])
    return [upper_case, lower_case, special_s, digits]


class Admin(QMainWindow):
    def __init__(self, source, *args, **kwargs):
        super(Admin, self).__init__(*args, **kwargs)
        self.pass_hash = None
        self.shadow_key = None
        self.quantity = None
        self.threadpool = QThreadPool()
        self.rcv_data = []
        self.blur_effect = None
        self.gif = None
        self.chose_user = None
        self.act = None
        self.chose = None
        self.cnt = 10
        self.ui = Ui_admin()
        self.ui.setupUi(self)
        self.source = source
        self.setFixedSize(self.size())
        self.setWindowTitle("Статистика")
        self.widgets = self.ui
        self.gui = [self.widgets.listWidget, self.widgets.frame, self.widgets.label_load, self.widgets.frame_2, self.widgets.label_name, self.widgets.label_login, self.widgets.label_password, self.widgets.label_money, self.widgets.label_2, self.widgets.label_name_2, self.widgets.label_login_2, self.widgets.label_money_2, self.widgets.label_password_2, self.widgets.checkBox, self.widgets.checkBox_2]
        Admin.show(self)
        loading_anim(True, self)
        self.change_data = True
        self.init_connection()
        self.startup(True)
        ssl_client.send('hello_from_admin'.encode('utf-8'))
        ssl_client.send(pickle.dumps([0, self.cnt]))
        self.widgets.listWidget.itemClicked.connect(self.button_handler)
        self.widgets.btn_add.clicked.connect(self.button_handler)
        self.widgets.btn_change.clicked.connect(self.button_handler)
        self.widgets.btn_delete.clicked.connect(self.button_handler)
        self.widgets.btn_block.clicked.connect(self.button_handler)
        self.widgets.btn_save.clicked.connect(self.button_handler)
        self.widgets.btn_exit.clicked.connect(self.button_handler)

    def closeEvent(self, event):
        if self.source == 'pre_lobby':
            loading_anim(True, pre_lobby)
        elif self.source == 'lobby':
            loading_anim(True, open_lobby)
        ssl_client.send(pickle.dumps([1]))

    def init_connection(self):
        receives = Worker(self.receive)

        # Execute
        self.threadpool.start(receives)

    def startup(self, stat):
        if stat:
            self.gui[1].setVisible(False)
            self.gui[2].setVisible(False)
            self.gui[3].setVisible(False)
        else:
            for i in range(len(self.gui[9:13])):
                self.gui[i + 9].setText('')
                self.gui[i + 9].setPlaceholderText('')
            self.gui[13].setChecked(False)
            self.gui[14].setChecked(False)

    def receive(self):
        while True:
            try:
                datad = []
                while True:
                    packet = ssl_client.recv(4096)
                    if packet == b'end': break
                    datad.append(packet)
                msg = pickle.loads(b"".join(datad))
                if msg[0] == 0:
                    self.quantity = msg[1][0]
                    self.rcv_data = msg[2:]
                    if self.change_data:
                        loading_anim(False, self)
                        self.change_data = False
                    self.gui[0].clear()
                    for i in self.rcv_data:
                        self.gui[0].addItem(i[0])
                    if self.quantity > self.cnt:
                        self.gui[0].addItem('загрузить больше')
                elif msg[0] == 1:
                    if self.source == 'pre_lobby':
                        loading_anim(False, pre_lobby)
                        ssl_client.send('hello_from_pre_lobby'.encode('utf-8'))
                        pre_lobby.init_connection()
                        ssl_client.send(pickle.dumps([5]))
                        pre_lobby.setEnabled(True)
                    elif self.source == 'lobby':
                        loading_anim(False, open_lobby)
                        ssl_client.send('hello_from_lobby'.encode('utf-8'))
                        open_lobby.init_connection()
                        ssl_client.send(pickle.dumps([7]))
                        open_lobby.setEnabled(True)
                    return
                elif msg[0] == 2:
                    loading_anim(False, self)
                    self.chose_user = msg[1]
                    self.chose_user.insert(3, '')
                    for i in range(len(msg[1]) - 2):
                        if i == 2:
                            self.gui[i + 5].setText(f'{msg[1][i]} $')
                        elif i == 3:
                            self.gui[i + 3].setText('ENCRYPTED')
                        else:
                            self.gui[i + 4].setText(msg[1][i])
                    self.gui[3].setVisible(True)
            except EOFError:
                pass

    def button_handler(self):
        global confirm
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "btn_exit":
            self.close()
        elif btnName == 'btn_save':
            if self.act:
                not_valid = False
                new_data = []
                pass_req = 0
                anys = False
                if self.gui[13].isChecked():
                    st = 2
                else:
                    st = 0
                if self.gui[14].isChecked():
                    rt = 'False'
                else:
                    rt = 'True'
                for i in range(6):
                    if len(self.gui[i + 9].text()) != 0 and (self.chose_user[4] != st or self.chose_user[5] != rt or (i != 4 and i != 5)):
                        anys = True
                        if i == 3:
                            password = self.gui[i + 9].text()
                            complexity = check_complexity(password)
                            if len(password) > 8 and complexity[0] and complexity[1] and complexity[2] and complexity[3]:
                                pass_req = 2
                                self.pass_hash = hashlib.sha512(password.encode('UTF-8'))
                                self.pass_hash = self.pass_hash.hexdigest()
                                new_data.append(self.pass_hash)
                            else:
                                pass_req = 1
                                self.gui[i + 9].setText('')
                                self.gui[i + 9].setPlaceholderText('пароль не надёжен')
                        elif i == 2:
                            try:
                                if 0 < int(self.gui[i + 9].text()) < 10000000:
                                    new_data.append(int(self.gui[i + 9].text()))
                                else:
                                    raise
                            except:
                                not_valid = True
                                self.gui[i + 9].setText('')
                                self.gui[i + 9].setPlaceholderText('данные не верны')
                        elif i == 4:
                            if self.gui[13].isChecked():
                                new_data.append(2)
                            else:
                                new_data.append(0)
                        elif i == 5:
                            if self.gui[14].isChecked():
                                new_data.append('False')
                            else:
                                new_data.append('True')
                        else:
                            new_data.append(self.gui[i + 9].text())
                    else:
                        new_data.append(self.chose_user[i])
                if anys and (pass_req == 0 or pass_req == 2) and not not_valid:
                    new_data.append(self.chose_user[0])
                    loading_anim(True, self)
                    self.change_data = True
                    self.gui[1].setVisible(False)
                    ssl_client.send(pickle.dumps([3, new_data, self.cnt]))
            else:
                not_valid = False
                self.cnt += 1
                anys = True
                pass_req = 0
                new_data = []
                for i in range(4):
                    if len(self.gui[i + 9].text()) != 0:
                        if i == 3:
                            password = self.gui[i + 9].text()
                            complexity = check_complexity(password)
                            if len(password) > 8 and complexity[0] and complexity[1] and complexity[2] and complexity[3]:
                                pass_req = 2
                                self.pass_hash = hashlib.sha512(password.encode('UTF-8'))
                                self.pass_hash = self.pass_hash.hexdigest()
                                new_data.append(self.pass_hash)
                            else:
                                pass_req = 1
                                self.gui[i + 9].setText('')
                                self.gui[i + 9].setPlaceholderText('пароль не надёжен')
                        elif i == 2:
                            try:
                                if 0 < int(self.gui[i + 9].text()) < 10000000:
                                    new_data.append(int(self.gui[i + 9].text()))
                                else:
                                    raise
                            except:
                                not_valid = True
                                self.gui[i + 9].setText('')
                                self.gui[i + 9].setPlaceholderText('данные не верны')
                        else:
                            new_data.append(self.gui[i + 9].text())
                    else:
                        anys = False
                        self.gui[i + 9].setPlaceholderText('введите значение')
                if self.gui[13].isChecked():
                    new_data.append(2)
                else:
                    new_data.append(0)
                if self.gui[14].isChecked():
                    new_data.append('False')
                else:
                    new_data.append('True')
                if anys and pass_req == 2 and not not_valid:
                    loading_anim(True, self)
                    self.change_data = True
                    self.gui[1].setVisible(False)
                    ssl_client.send(pickle.dumps([4, new_data, self.cnt]))
        elif btnName == 'btn_block':
            loading_anim(True, self)
            self.change_data = True
            self.gui[1].setVisible(False)
            ssl_client.send(pickle.dumps([5, 'False', self.rcv_data[self.chose][0], self.cnt]))
        elif btnName == 'btn_delete':
            confirm = Confirm('admin')
            Admin.setEnabled(self, False)
        elif btnName == 'btn_change':
            self.startup(False)
            self.act = True
            self.gui[8].setText('изменить')
            for i in range(len(self.chose_user)):
                if i == 2:
                    self.gui[i + 9].setPlaceholderText(f'{self.chose_user[i]} $')
                elif i == 3:
                    self.gui[i + 9].setPlaceholderText('ENCRYPTED')
                elif i == 4:
                    if self.chose_user[i] == 2:
                        self.gui[13].setChecked(True)
                    else:
                        self.gui[13].setChecked(False)
                elif i == 5:
                    if self.chose_user[i] == 'False':
                        self.gui[14].setChecked(True)
                    else:
                        self.gui[14].setChecked(False)
                else:
                    self.gui[i + 9].setPlaceholderText(self.chose_user[i])
            self.gui[1].setVisible(True)
        elif btnName == 'btn_add':
            self.startup(False)
            self.act = False
            self.gui[8].setText('добавить')
            self.gui[1].setVisible(True)
        elif btnName == 'listWidget':
            self.chose = self.gui[0].currentRow()
            self.gui[1].setVisible(False)
            if self.chose == len(self.rcv_data) and self.quantity > self.cnt:
                self.cnt += 10
                loading_anim(True, self)
                self.change_data = True
                ssl_client.send(pickle.dumps([0, self.cnt]))
            elif self.shadow_key == self.chose:
                self.shadow_key = -1
                self.gui[1].setVisible(False)
                self.gui[3].setVisible(False)
            else:
                self.shadow_key = self.chose
                loading_anim(True, self)
                ssl_client.send(pickle.dumps([2, self.rcv_data[self.chose][0]]))


class Confirm(QMainWindow):
    def __init__(self, source, reason=None, *args, **kwargs):
        super(Confirm, self).__init__(*args, **kwargs)
        self.ui = Ui_confirm()
        self.ui.setupUi(self)
        self.source = source
        self.reason = reason
        self.setFixedSize(self.size())
        self.setWindowTitle("подтвердить")
        self.widgets_confirm = self.ui
        self.yes = False
        self.no = False
        Confirm.show(self)
        self.widgets_confirm.yes.clicked.connect(self.btn_handler)
        self.widgets_confirm.no.clicked.connect(self.btn_handler)

    def closeEvent(self, event):
        if self.source == 'profile':
            if self.yes:
                ssl_client.send(pickle.dumps([5]))
                src = profile.source
                profile.close()
                if src == 'pre_lobby':
                    pre_lobby.close()
                if src == 'lobby':
                    open_lobby.close()
            if self.no:
                profile.setEnabled(True)
        elif self.source == 'game':
            if self.yes:
                if self.reason == 0:
                    loading_anim(True, open_game)
                    open_game.relay = True
                    ssl_client.send(pickle.dumps([4]))
                elif self.reason == 1:
                    open_game.close()
            if self.no:
                open_game.setEnabled(True)
        elif self.source == 'admin':
            if self.yes:
                admin.cnt -= 1
                loading_anim(True, admin)
                admin.change_data = True
                ssl_client.send(pickle.dumps([6, admin.rcv_data[admin.chose][0], admin.cnt]))
            if self.no:
                admin.setEnabled(True)

    def btn_handler(self):
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "yes":
            self.yes = True
            self.close()
        if btnName == "no":
            self.no = True
            self.close()


class Statistic(QMainWindow):
    def __init__(self, source, *args, **kwargs):
        super(Statistic, self).__init__(*args, **kwargs)
        self.quantity = None
        self.threadpool = QThreadPool()
        self.name = None
        self.row = None
        self.rcv_data = []
        self.blur_effect = None
        self.gif = None
        self.chose = None
        self.cnt = 5
        self.ui = Ui_statistic()
        self.ui.setupUi(self)
        self.source = source
        self.shadow_key = -1
        self.end = None
        self.out_suit = None
        self.pretty_suits = {'s': chr(9824), 'h': chr(9829), 'd': chr(9830), 'c': chr(9827)}
        self.setFixedSize(self.size())
        self.setWindowTitle("Статистика")
        self.widgets = self.ui
        self.gui = [self.widgets.last_date, self.widgets.money_c, self.widgets.all_games, self.widgets.all_games_win, self.widgets.listWidget, self.widgets.game_time, self.widgets.game_pot, self.widgets.game_big, self.widgets.game_small, self.widgets.game_result, self.widgets.tableWidget]
        Statistic.show(self)
        loading_anim(True, self)
        self.change_data = True
        self.init_connection()
        self.startup()
        ssl_client.send('hello_from_statistic'.encode('utf-8'))
        ssl_client.send(pickle.dumps([0, 0]))
        self.widgets.listWidget.itemClicked.connect(self.button_handler)
        self.widgets.btn_exit_stat.clicked.connect(self.button_handler)

    def closeEvent(self, event):
        if self.source == 'pre_lobby':
            loading_anim(True, pre_lobby)
        elif self.source == 'lobby':
            loading_anim(True, open_lobby)
        elif self.source == 'profile':
            loading_anim(True, profile)
        ssl_client.send(pickle.dumps([1]))

    def init_connection(self):
        receives = Worker(self.receive)

        # Execute
        self.threadpool.start(receives)

    def startup(self):
        self.widgets.label_load.setVisible(False)
        self.widgets.frame.setVisible(False)
        self.widgets.tableWidget.setEnabled(False)

    def receive(self):
        while True:
            try:
                datad = []
                while True:
                    packet = ssl_client.recv(4096)
                    if packet == b'end': break
                    datad.append(packet)
                msg = pickle.loads(b"".join(datad))
                if msg[0] == 0:
                    if self.change_data:
                        loading_anim(False, self)
                        self.change_data = False
                    for i in range(len(self.gui[1:4])):
                        if i == 0:
                            pts = f'{msg[1][i]} $'
                        else:
                            pts = str(msg[1][i])
                        self.gui[i + 1].setText(pts)
                    if len(msg) > 2:
                        self.quantity = msg[1][-1]
                        self.gui[0].setText(datetime.fromtimestamp(msg[-1][0]/1000, timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M"))
                        self.gui[4].clear()
                        self.rcv_data = msg[2:] + self.rcv_data
                        for i in range(len(self.rcv_data)):
                            utc_time = datetime.fromtimestamp(self.rcv_data[i][0]/1000, timezone.utc).astimezone()
                            date = utc_time.strftime("%Y-%m-%d %H:%M")
                            output_str = f'{date}({self.rcv_data[i][1]})'
                            self.gui[4].addItem(output_str)
                        if self.quantity > self.cnt:
                            self.gui[4].addItem('загрузить больше')
                elif msg[0] == 1:
                    if self.source == 'pre_lobby':
                        loading_anim(False, pre_lobby)
                        ssl_client.send('hello_from_pre_lobby'.encode('utf-8'))
                        pre_lobby.init_connection()
                        ssl_client.send(pickle.dumps([5]))
                        pre_lobby.setEnabled(True)
                    elif self.source == 'lobby':
                        loading_anim(False, open_lobby)
                        ssl_client.send('hello_from_lobby'.encode('utf-8'))
                        open_lobby.init_connection()
                        ssl_client.send(pickle.dumps([7]))
                        open_lobby.setEnabled(True)
                    elif self.source == 'profile':
                        loading_anim(False, profile)
                        ssl_client.send('hello_from_profile'.encode('utf-8'))
                        profile.init_connection()
                        profile.stat_open = False
                        profile.setEnabled(True)
                    return False
                elif msg[0] == 2:
                    loading_anim(False, self)
                    self.row = 0
                    users = json.loads(msg[1][2])
                    if msg[1][1] == 'True':
                        self.end = 'Победа'
                    elif msg[1][1] == 'False':
                        self.end = 'Поражение'
                    utc_time = datetime.fromtimestamp(msg[1][0] / 1000,
                                                      timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M")
                    self.gui[5].setText(utc_time)
                    self.gui[9].setText(self.end)
                    for i in range(len(msg[1][3:6])):
                        pts = f'{msg[1][i + 3]} $'
                        self.gui[i + 6].setText(pts)
                    self.player_l = QTableWidgetItem('рука')
                    self.level_l = QTableWidgetItem('карты')
                    self.player_l.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                    self.level_l.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                    self.widgets.tableWidget.setItem(self.row, 0, self.player_l)
                    self.widgets.tableWidget.setItem(self.row, 1, self.level_l)
                    for i in range(6):
                        for j in range(2):
                            self.widgets.tableWidget.setItem(i + 1, j, QTableWidgetItem(''))
                    for key, values in users.items():
                        if key == 'deck':
                            self.name = 'крупье'
                        else:
                            self.name = key
                        self.out_suit = ''
                        self.row += 1
                        for i in values:
                            if i[0] == 'T':
                                left = '10'
                            else:
                                left = i[0]
                            s = f'{left}{self.pretty_suits[i[1].lower()]}'
                            self.out_suit += f'{s} '
                        self.player = QTableWidgetItem(self.name)
                        self.level = QTableWidgetItem(self.out_suit)
                        self.player.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                        self.level.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                        self.widgets.tableWidget.setItem(self.row, 0, self.player)
                        self.widgets.tableWidget.setItem(self.row, 1, self.level)
                    self.widgets.frame.setVisible(True)
            except EOFError:
                pass

    def button_handler(self):
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "btn_exit_stat":
            self.close()
        elif btnName == 'listWidget':
            self.chose = self.gui[4].currentRow()
            if self.chose == len(self.rcv_data) and self.quantity > self.cnt:
                self.cnt += 5
                loading_anim(True, self)
                self.change_data = True
                ssl_client.send(pickle.dumps([0, self.rcv_data[0][0]]))
            elif self.shadow_key == self.chose:
                self.shadow_key = -1
                self.widgets.frame.setVisible(False)
            else:
                self.shadow_key = self.chose
                loading_anim(True, self)
                ssl_client.send(pickle.dumps([2, self.rcv_data[self.chose][0]]))


class Profile(QMainWindow):
    def __init__(self, source, clear_pass, *args, **kwargs):
        super(Profile, self).__init__(*args, **kwargs)
        self.threadpool = QThreadPool()
        self.pass_hash = None
        self.stat_open = False
        self.blur_effect = None
        self.gif = None
        self.ui = Ui_profile()
        self.ui.setupUi(self)
        self.source = source
        self.change_pass = False
        self.get_money = False
        self.clear_pass = clear_pass
        self.user_photo = None
        self.setFixedSize(self.size())
        self.setWindowTitle("Профиль")
        self.widgets = self.ui
        self.info = [self.widgets.name, self.widgets.login, self.widgets.balance,
                     self.widgets.date_created, self.widgets.level, self.widgets.photo]
        Profile.show(self)
        loading_anim(True, self)
        self.change_data = True
        self.startup(True)
        self.init_connection()
        ssl_client.send('hello_from_profile'.encode('utf-8'))
        ssl_client.send(pickle.dumps([0]))
        self.widgets.btn_exitgame.clicked.connect(self.button_handler)
        self.widgets.btn_statistic.clicked.connect(self.button_handler)
        self.widgets.btn_money.clicked.connect(self.button_handler)
        self.widgets.btn_delete.clicked.connect(self.button_handler)
        self.widgets.btn_balance.clicked.connect(self.button_handler)
        self.widgets.btn_change_pass.clicked.connect(self.button_handler)
        self.widgets.btn_pass_conf.clicked.connect(self.button_handler)
        self.widgets.photo.installEventFilter(self)

    def exit_loop(self, stat):
        global statistic
        if stat:
            loading_anim(False, self)
            statistic = Statistic('profile')
            self.stat_open = True
            Profile.setEnabled(self, False)

    def img_native_resize(self, photo):
        scale = QSize(211, 201)
        img = QPixmap(f'images/images/{photo}.png')
        img = img.scaled(scale)
        return img

    def eventFilter(self, object, event):
        if not self.stat_open:
            if event.type() == QEvent.Enter:
                self.info[5].setPixmap(self.img_native_resize('add-user'))
            elif event.type() == QEvent.Leave:
                self.info[5].setPixmap(self.img_byte_resize(self.user_photo))
            elif event.type() == QEvent.MouseButtonPress:
                self.startup(False)
                data = QFileDialog.getOpenFileName(self, 'Open File', f'{pathlib.Path.cwd()}',
                                                       'JPG Images (*.jpg);;PNG Images (*.png)')
                if len(data[0]) != 0:
                    if os.path.getsize(data[0]) < 31457280:
                        img = self.convert_to_binary_data(data[0])
                        if img[0]:
                            loading_anim(True, self)
                            self.change_data = True
                            ssl_client.send(pickle.dumps([2]))
                            ssl_client.send(base64.b64encode(img[1]))
                            ssl_client.send(b'end')
                        else:
                            self.widgets.label_corrupted.setVisible(True)
                    else:
                        self.widgets.label_to_big.setVisible(True)
            return False
        else:
            return False

    def closeEvent(self, event):
        if self.source == 'pre_lobby':
            loading_anim(True, pre_lobby)
        elif self.source == 'lobby':
            loading_anim(True, open_lobby)
        ssl_client.send(pickle.dumps([1]))

    def convert_to_binary_data(self, filename):
        with open(filename, 'rb') as file:
            blob_data = file.read()
            if imghdr.what(None, blob_data) not in ['png', 'jpeg']:
                print(imghdr.what(None, blob_data))
                return [False]
        return [True, blob_data]

    def img_byte_resize(self, data):
        scale = QSize(211, 201)
        mass = QByteArray(data)
        qp = QImage()
        img = qp.fromData(mass, format=None)
        img = img.scaled(scale)
        img = QPixmap.fromImage(img)
        return img

    def init_connection(self):
        receives = Worker(self.receive)
        receives.signals.result.connect(self.exit_loop)

        # Execute
        self.threadpool.start(receives)

    def startup(self, stat):
        wdg = [self.widgets.label_load, self.widgets.frame_pass, self.widgets.transaction_frame,  self.widgets.label_corrupted, self.widgets.label_to_big]
        if stat:
            for i in wdg:
                i.setVisible(False)
        else:
            for i in range(2):
                wdg[i + 3].setVisible(False)

    def receive(self):
        while True:
            try:
                datad = []
                while True:
                    packet = ssl_client.recv(4096)
                    if packet == b'end': break
                    datad.append(packet)
                msg = pickle.loads(b"".join(datad))
                if msg[0] == 0:
                    if self.change_data:
                        loading_anim(False, self)
                        self.change_data = False
                    self.user_photo = base64.b64decode(msg[12])
                    self.info[0].setText(msg[1])
                    self.info[1].setText(msg[2])
                    self.info[2].setText(f'{msg[7]} $')
                    self.info[3].setText(datetime.utcfromtimestamp(msg[5]/1000).strftime('%Y-%m-%d'))
                    self.info[4].setText(str(msg[11]))
                    self.info[5].setPixmap(self.img_byte_resize(self.user_photo))
                elif msg[0] == 1:
                    if self.source == 'pre_lobby':
                        loading_anim(False, pre_lobby)
                        ssl_client.send('hello_from_pre_lobby'.encode('utf-8'))
                        pre_lobby.init_connection()
                        ssl_client.send(pickle.dumps([5]))
                        pre_lobby.setEnabled(True)
                    elif self.source == 'lobby':
                        loading_anim(False, open_lobby)
                        ssl_client.send('hello_from_lobby'.encode('utf-8'))
                        open_lobby.init_connection()
                        ssl_client.send(pickle.dumps([7]))
                        open_lobby.setEnabled(True)
                    return False
                elif msg[0] == 2:
                    loading_anim(False, self)
                    self.widgets.lineEdit_old.setText('')
                    self.widgets.lineEdit_new.setText('')
                    self.widgets.lineEdit_new.setPlaceholderText('пароль обновлён')
                elif msg[0] == 3:
                    self.widgets.lineEdit_money.setText('')
                    self.widgets.lineEdit_money.setPlaceholderText('баланс пополнен')
                elif msg[0] == 4:
                    return True
            except EOFError:
                pass

    def button_handler(self):
        global confirm
        self.startup(False)
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "btn_exitgame":
            self.close()
        if btnName == "btn_statistic":
            loading_anim(True, self)
            ssl_client.send(pickle.dumps([6]))
        if btnName == "btn_money":
            text = self.widgets.lineEdit_money.text()
            try:
                if 9 < int(text) < 10000000:
                    loading_anim(True, self)
                    webbrowser.open('https://uniochange.com/ru/exchange-advcusd-to-etc/', new=2)
                    self.change_data = True
                    ssl_client.send(pickle.dumps([4, int(text)]))
                else:
                    raise
            except:
                self.widgets.lineEdit_money.setText('')
                self.widgets.lineEdit_money.setPlaceholderText('Неверная сумма')
        if btnName == "btn_delete":
            confirm = Confirm('profile')
            Profile.setEnabled(self, False)
        if btnName == "btn_balance":
            if self.get_money:
                self.widgets.transaction_frame.setVisible(False)
                self.get_money = False
            else:
                self.widgets.transaction_frame.setVisible(True)
                self.widgets.frame_pass.setVisible(False)
                self.change_pass = False
                self.get_money = True
        if btnName == "btn_change_pass":
            if self.change_pass:
                self.widgets.frame_pass.setVisible(False)
                self.change_pass = False
            else:
                self.widgets.frame_pass.setVisible(True)
                self.widgets.transaction_frame.setVisible(False)
                self.get_money = False
                self.change_pass = True
        if btnName == "btn_pass_conf":
            old = self.widgets.lineEdit_old.text()
            new = self.widgets.lineEdit_new.text()
            if old == self.clear_pass:
                self.pass_hash = hashlib.sha512(new.encode('UTF-8'))
                self.pass_hash = self.pass_hash.hexdigest()
                loading_anim(True, self)
                ssl_client.send(pickle.dumps([3, self.pass_hash]))
            else:
                self.widgets.lineEdit_old.setText('')
                self.widgets.lineEdit_old.setPlaceholderText('пароль неверен')


class Rules(QMainWindow):
    def __init__(self, source, *args, **kwargs):
        super(Rules, self).__init__(*args, **kwargs)
        self.ui = Ui_rules()
        self.source = source
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowTitle("Правила игры")
        self.widgets_rules = self.ui
        Rules.show(self)
        self.widgets_rules.btn_exitgame.clicked.connect(self.button_handler)

    def closeEvent(self, event):
        if self.source == 'pre_lobby':
            pre_lobby.setEnabled(True)
        if self.source == 'lobby':
            open_lobby.setEnabled(True)

    def button_handler(self):
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "btn_exitgame":
            self.close()


class Game(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Game, self).__init__(*args, **kwargs)
        self.user_photo = None
        self.relay = False
        self.threadpool = QThreadPool()
        self.on = False
        self.first_lap = True
        self.river = True
        self.closed = False
        self.four = True
        self.blur_effect = None
        self.gif = None
        self.five = True
        self.requiem = True
        self.ui = Ui_Game()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowTitle("Покер")
        self.widgets = self.ui
        self.graphics = [[self.widgets.label_info_0, self.widgets.label_dealer_0, self.widgets.timer_0, self.widgets.photo_0],
                         [self.widgets.label_info_1, self.widgets.label_dealer_1, self.widgets.timer_1, self.widgets.photo_1],
                         [self.widgets.label_info_2, self.widgets.label_dealer_2, self.widgets.timer_2, self.widgets.photo_2],
                         [self.widgets.label_info_3, self.widgets.label_dealer_3, self.widgets.timer_3, self.widgets.photo_3],
                         [self.widgets.label_info_4, self.widgets.label_dealer_4, self.widgets.timer_4, self.widgets.photo_4],
                         [self.widgets.label_info_5, self.widgets.label_dealer_5, self.widgets.timer_5, self.widgets.photo_5]]
        self.cards = [[self.widgets.label_card1_0, self.widgets.label_card2_0], [self.widgets.label_card1_1, self.widgets.label_card2_1], [self.widgets.label_card1_2, self.widgets.label_card2_2], [self.widgets.label_card1_3, self.widgets.label_card2_3], [self.widgets.label_card1_4, self.widgets.label_card2_4], [self.widgets.label_card1_5, self.widgets.label_card2_5], [self.widgets.game_card_1, self.widgets.game_card_2, self.widgets.game_card_3, self.widgets.game_card_4, self.widgets.game_card_5]]
        self.labels = [self.widgets.frame_game_btns, self.widgets.frame_input, self.widgets.label_win, self.widgets.label_lose]
        Game.show(self)
        loading_anim(True, self)
        self.startup(True)
        self.init_connection()
        ssl_client.send('hello_from_game'.encode('utf-8'))
        ssl_client.send(pickle.dumps([0]))
        self.widgets.btn_exitgame.clicked.connect(self.button_handler)
        self.widgets.btn_exit_game.clicked.connect(self.button_handler)
        self.widgets.btn_call.clicked.connect(self.button_handler)
        self.widgets.btn_raise.clicked.connect(self.button_handler)
        self.widgets.btn_fold.clicked.connect(self.button_handler)
        self.widgets.btn_accept.clicked.connect(self.button_handler)

    def closeEvent(self, event):
        if not self.closed:
            ssl_client.send(pickle.dumps([5]))

    def init_connection(self):
        receives = Worker(self.receive)
        receives.signals.result.connect(self.exit_loop)

        # Execute
        self.threadpool.start(receives)

    def exit_loop(self, stat):
        global open_lobby, pre_lobby
        if stat != 0:
            loading_anim(False, self)
            self.closed = True
            self.close()
        if stat == 1:
            open_lobby = lobby()
        elif stat == 2:
            pre_lobby = connect_to_lobby()

    def receive(self):
        global shadow_data
        game_players = {}
        while True:
            try:
                msg = pickle.loads(ssl_client.recv(4096))
                if msg[0] == 0:
                    datad = []
                    while True:
                        packet = ssl_client.recv(4096)
                        if packet == b'end': break
                        datad.append(packet)
                    pkg = pickle.loads(b"".join(datad))
                    loading_anim(False, self)
                    players = list(pkg.keys())
                    print(players)
                    c = 0
                    index = players.index(user_data[1])
                    game_players.update({user_data[1]: 0})
                    for i in players[:index][::-1]:
                        c += 1
                        game_players.update({i: c})
                    c = 6
                    for i in players[index + 1:]:
                        c -= 1
                        game_players.update({i: c})
                    print(game_players)
                    for i, g in game_players.items():
                        self.user_photo = base64.b64decode(pkg[i])
                        self.graphics[g][3].setPixmap(self.img_byte_resize(self.user_photo))
                elif msg[0] == 1:
                    if shadow_data != msg:
                        print(msg)
                        for i in msg[1:]:
                            if not i == msg[-1]:
                                strs = f'{i[0]}\n \n{i[3]}$'
                                self.graphics[game_players[i[0]]][0].setText(strs)
                                if self.first_lap:
                                    if i[0] == user_data[1]:
                                        self.cards[game_players[i[0]]][0].setPixmap(self.img_players_resize(i[1]))
                                        self.cards[game_players[i[0]]][1].setPixmap(self.img_players_resize(i[2]))
                                    else:
                                        self.cards[game_players[i[0]]][0].setPixmap(self.img_players_resize('back2x'))
                                        self.cards[game_players[i[0]]][1].setPixmap(self.img_players_resize('back2x'))
                                    for g in range(4):
                                        if g != 2:
                                            self.graphics[game_players[i[0]]][g].setVisible(True)
                                    self.cards[game_players[i[0]]][0].setVisible(True)
                                    self.cards[game_players[i[0]]][1].setVisible(True)
                                    if i[5]:
                                        self.graphics[game_players[i[0]]][1].setText(f'small blind {small}$')
                                    if i[6]:
                                        self.graphics[game_players[i[0]]][1].setText(f'big blind {big}$')
                                if i[10] != 0:
                                    self.graphics[game_players[i[0]]][2].setVisible(True)
                                    self.graphics[game_players[i[0]]][2].setText(str(i[10]))
                                elif i[10] == 0 and self.graphics[game_players[i[0]]][2].isVisible():
                                    self.graphics[game_players[i[0]]][2].setVisible(False)
                                if len(i[7]) > 0:
                                    self.graphics[game_players[i[0]]][1].setText(i[7])
                                if user_data[1] == i[0] and len(msg[1:-1]) == 1:
                                    self.widgets.btn_raise.setDisabled(True)
                                if user_data[1] == i[0] and i[8] == msg[-1][6]:
                                    self.widgets.btn_call.setText('CHECK')
                                elif user_data[1] == i[0] and i[3] <= (msg[-1][6] - i[8]):
                                    self.widgets.btn_call.setText('ALL IN')
                                    self.widgets.btn_raise.setDisabled(True)
                                elif user_data[1] == i[0] and i[8] != msg[-1][6]:
                                    self.widgets.btn_call.setText(f'CALL ({msg[-1][6] - i[8]}$)')
                                if user_data[1] == i[0] and i[9] and msg[-1][7] < 5:
                                    self.widgets.frame_game_btns.setVisible(True)
                            else:
                                if self.river:
                                    if i[7] == 2:
                                        self.cards[6][0].setPixmap(self.img_table_resize(i[0]))
                                        self.cards[6][1].setPixmap(self.img_table_resize(i[1]))
                                        self.cards[6][2].setPixmap(self.img_table_resize(i[2]))
                                        self.river = False
                                if self.four:
                                    if i[7] == 3:
                                        self.cards[6][3].setPixmap(self.img_table_resize(i[3]))
                                        self.four = False
                                if self.five:
                                    if i[7] == 4:
                                        self.cards[6][4].setPixmap(self.img_table_resize(i[4]))
                                        self.five = False
                                if self.requiem:
                                    if i[7] >= 5:
                                        for g in msg[1:-1]:
                                            self.cards[game_players[g[0]]][0].setPixmap(self.img_players_resize(g[1]))
                                            self.cards[game_players[g[0]]][1].setPixmap(self.img_players_resize(g[2]))
                                        self.requiem = False
                                self.widgets.label_pot.setText(f'pot: {i[5]}$')
                        self.first_lap = False
                        shadow_data = copy.deepcopy(msg)
                elif msg[0] == 2:
                    return 0
                elif msg[0] == 3:
                    self.widgets.entry_raise.setText('')
                    self.widgets.entry_raise.setPlaceholderText('Ставка меньше старшей руки')
                    self.widgets.frame_input.setVisible(True)
                elif msg[0] == 4:
                    if not msg[2]:
                        if not msg[3]:
                            self.graphics[game_players[msg[1]]][1].setText('FOLDED')
                            if msg[1] == user_data[1]:
                                self.startup(False)
                        else:
                            strs = f'{msg[1]}\n \n0$'
                            self.graphics[game_players[msg[1]]][0].setText(strs)
                            self.graphics[game_players[msg[1]]][1].setText(msg[4])
                    else:
                        self.cards[game_players[msg[1]]][0].setVisible(False)
                        self.cards[game_players[msg[1]]][1].setVisible(False)
                        for g in range(4):
                            self.graphics[game_players[msg[1]]][g].setVisible(False)
                elif msg[0] == 5:
                    return 1
                elif msg[0] == 6:
                    self.startup(False)
                    self.widgets.btn_exit_game.setEnabled(False)
                    self.widgets.btn_exitgame.setEnabled(False)
                    for i in self.graphics:
                        i[2].setVisible(False)
                    if (shadow_data[-1][10] and len(shadow_data[1:-1]) == 1) or len(shadow_data[1:-1]) > 1:
                        for i in msg[1:-2]:
                            self.graphics[game_players[i[0]]][1].setText(f'{i[1]}')
                        time.sleep(5)
                    for i in msg[-2]:
                        if user_data[1] in msg[-2]:
                            self.widgets.label_win.setVisible(True)
                        else:
                            self.widgets.label_lose.setVisible(True)
                        self.graphics[game_players[i]][1].setText('WINNER')
                    time.sleep(3)
                    if msg[-1]:
                        return 2
                    else:
                        return 1
                elif msg[0] == 7:
                    self.widgets.entry_raise.setText('')
                    self.widgets.entry_raise.setPlaceholderText('Недостаточно средств')
                    self.widgets.frame_input.setVisible(True)
            except EOFError:
                pass

    def img_table_resize(self, card):
        scale = QSize(61, 91)
        img = QPixmap(f'images/cards/{card}.png')
        img = img.scaled(scale)
        return img

    def img_players_resize(self, card):
        scale = QSize(51, 91)
        img = QPixmap(f'images/cards/{card}.png')
        img = img.scaled(scale)
        return img

    def img_byte_resize(self, data):
        scale = QSize(91, 81)
        mass = QByteArray(data)
        qp = QImage()
        img = qp.fromData(mass, format=None)
        img = img.scaled(scale)
        img = QPixmap.fromImage(img)
        return img

    def startup(self, state):
        if state:
            for i in self.labels:
                i.setVisible(False)
            for i in self.graphics:
                for g in i:
                    g.setVisible(False)
            for i in self.cards[:-1]:
                for g in i:
                    g.setVisible(False)
            self.widgets.label_load.setVisible(False)
        else:
            self.widgets.frame_game_btns.setVisible(False)
            self.widgets.frame_input.setVisible(False)

    def button_handler(self):
        global confirm
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "btn_call":
            self.startup(False)
            ssl_client.send(pickle.dumps([1]))
        if btnName == "btn_raise":
            if self.on:
                self.widgets.frame_input.setVisible(False)
                self.on = False
            else:
                self.widgets.frame_input.setVisible(True)
                self.on = True
        if btnName == "btn_fold":
            self.startup(False)
            ssl_client.send(pickle.dumps([3]))
        if btnName == "btn_accept":
            self.widgets.entry_raise.setPlaceholderText('Введите ставку')
            text = self.widgets.entry_raise.text()
            try:
                if 0 < int(text) < 10000000:
                    self.startup(False)
                    ssl_client.send(pickle.dumps([2, int(text)]))
                else:
                    raise
            except:
                self.widgets.entry_raise.setText('')
                self.widgets.entry_raise.setPlaceholderText('Неверная ставка')
        if btnName == "btn_exitgame":
            confirm = Confirm('game', 1)
            Profile.setEnabled(self, False)
        if btnName == "btn_exit_game":
            confirm = Confirm('game', 0)
            Profile.setEnabled(self, False)


class lobby(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(lobby, self).__init__(*args, **kwargs)
        self.relay = False
        self.level = None
        self.player = None
        self.player_l = None
        self.to_pre_lobby = False
        self.level_l = None
        self.blur_effect = None
        self.gif = None
        self.group_admin = True
        self.on = False
        self.row = -1
        self.threadpool = QThreadPool()
        self.ui = Ui_Lobby()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowTitle("Лобби")
        self.widgets = self.ui
        lobby.show(self)
        loading_anim(True, self)
        self.widgets.tableWidget.setEnabled(False)
        self.startup(0)
        self.init_connection()
        ssl_client.send('hello_from_lobby'.encode('utf-8'))
        ssl_client.send(pickle.dumps([2]))
        self.widgets.btn_gostart.clicked.connect(self.button_handler)
        self.widgets.btn_confirm.clicked.connect(self.button_handler)
        self.widgets.btn_statistic.clicked.connect(self.button_handler)
        self.widgets.btn_rules.clicked.connect(self.button_handler)
        self.widgets.btn_profile.clicked.connect(self.button_handler)
        self.widgets.btn_logout.clicked.connect(self.button_handler)
        self.widgets.btn_exitgame.clicked.connect(self.button_handler)
        self.widgets.btn_admin.clicked.connect(self.button_handler)
        self.widgets.btn_exit_lobby.clicked.connect(self.button_handler)
        self.widgets.btn_configure.clicked.connect(self.button_handler)
        self.widgets.btn_chat_send.clicked.connect(self.button_handler)

    def closeEvent(self, event):
        if not self.to_pre_lobby:
            ssl_client.send(pickle.dumps([8]))

    def init_connection(self):
        receives = Worker(self.receive)
        receives.signals.result.connect(self.exit_loop)

        # Execute
        self.threadpool.start(receives)

    def exit_loop(self, stat):
        global open_game, statistic, profile, window_log_in, pre_lobby, admin
        if stat[0] == 1:
            loading_anim(False, self)
            self.close()
            open_game = Game()
        elif stat[0] == 2:
            loading_anim(False, self)
            if stat[1] == 0:
                statistic = Statistic('lobby')
                lobby.setEnabled(self, False)
            elif stat[1] == 1:
                profile = Profile('lobby', user_data[4])
                lobby.setEnabled(self, False)
            elif stat[1] == 2:
                admin = Admin('lobby')
                connect_to_lobby.setEnabled(self, False)
        elif stat[0] == 3:
            loading_anim(False, self)
            self.to_pre_lobby = True
            self.close()
            pre_lobby = connect_to_lobby()
        elif stat[0] == 4:
            loading_anim(False, self)
            self.to_pre_lobby = True
            self.close()
            window_log_in = log_in()

    def receive(self):
        global small, big
        while True:
            try:
                msg = pickle.loads(ssl_client.recv(4096))
                if msg[0] == 0:
                    if self.relay:
                        loading_anim(False, self)
                        self.relay = False
                    first_start = True
                    for i in range(7):
                        for j in range(2):
                            self.widgets.tableWidget.setItem(i, j, QTableWidgetItem(''))
                    for items in range(0, len(msg[7]), 2):
                        if first_start:
                            self.row += 1
                            self.player_l = QTableWidgetItem('игрок')
                            self.level_l = QTableWidgetItem('уровень')
                            self.player_l.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                            self.level_l.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                            self.widgets.tableWidget.setItem(self.row, 0, self.player_l)
                            self.widgets.tableWidget.setItem(self.row, 1, self.level_l)
                            first_start = False
                        self.row += 1
                        self.player = QTableWidgetItem(str(msg[7][items]))
                        self.level = QTableWidgetItem(str(msg[7][items + 1]))
                        self.player.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                        self.level.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                        self.widgets.tableWidget.setItem(self.row, 0, self.player)
                        self.widgets.tableWidget.setItem(self.row, 1, self.level)
                    if msg[1]:
                        self.widgets.label_2.setText('Игра идёт')
                    else:
                        if (len(msg[7]) / 2) < 2:
                            self.widgets.label_2.setText('Поиск игроков (1)')
                        else:
                            self.widgets.label_2.setText('ожидание начала игры')
                    if msg[5] != user_data[1]:
                        self.group_admin = False
                        self.startup(2)
                    self.widgets.label_3.setText(f'{msg[2]} игроков проголосовало за "старт"')
                    self.widgets.label.setText(f'Количество игроков в лобби: {int(len(msg[7]) / 2)}')
                    self.widgets.label_big_blind.setText(f'старшая рука: {msg[3]}$')
                    self.widgets.label_small_blind.setText(f'младшая рука: {msg[4]}$')
                    small = msg[4]
                    big = msg[3]
                    self.row = -1
                elif msg[0] == 1:
                    self.widgets.label_exists.setVisible(True)
                elif msg[0] == 2:
                    self.to_pre_lobby = True
                    return [1]
                elif msg[0] == 3:
                    return [3]
                elif msg[0] == 4:
                    return [4]
                elif msg[0] == 5:
                    loading_anim(False, self)
                    self.widgets.textEdit.append(msg[1])
                elif msg[0] == 6:
                    return [2, msg[1]]
                elif msg[0] == 7:
                    return [0]
                elif msg[0] == 8:
                    if msg[1] == 2:
                        self.widgets.btn_admin.setEnabled(True)
                elif msg[0] == 9:
                    if msg[1]:
                        self.widgets.label_not_enough_2.setVisible(True)
                    else:
                        self.widgets.label_not_enough.setVisible(True)
            except EOFError:
                pass

    def confirm(self, big, small):
        try:
            if (len(big) and len(small)) != 0:
                if 0 < int(big) < 10000000 and int(small) > 0:
                    if int(big) > int(small):
                        loading_anim(True, self)
                        self.relay = True
                        ssl_client.send(pickle.dumps([0, int(big), int(small)]))
                    else:
                        self.widgets.label_size_error.setVisible(True)
                else:
                    raise
            else:
                self.widgets.label_empty.setVisible(True)
        except:
            self.widgets.label_not_valid.setVisible(True)
        self.startup(3)

    def startup(self, flag):
        hide = [self.widgets.frame_add, self.widgets.label_load, self.widgets.lineEdit_big_blind,
                self.widgets.lineEdit_small_blind,
                self.widgets.btn_confirm, self.widgets.label_empty,
                self.widgets.label_exists, self.widgets.label_not_valid, self.widgets.label_size_error, self.widgets.label_not_enough, self.widgets.label_not_enough_2]
        if flag == 0:
            for i in hide:
                i.setVisible(False)
            self.widgets.textEdit.setEnabled(False)
        elif flag == 1:
            for i in range(5, len(hide)):
                hide[i].setVisible(False)
        elif flag == 2:
            if not self.group_admin:
                self.widgets.btn_configure.setEnabled(False)
        elif flag == 3:
            for i in range(2):
                hide[i + 2].setText('')

    def button_handler(self):
        global rules
        self.startup(1)
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "btn_admin":
            loading_anim(True, self)
            ssl_client.send(pickle.dumps([6, 2]))
        if btnName == "btn_confirm":
            big_blind = self.widgets.lineEdit_big_blind.text()
            small_blind = self.widgets.lineEdit_small_blind.text()
            self.confirm(big_blind, small_blind)
        if btnName == "btn_configure":
            add = [self.widgets.frame_add, self.widgets.lineEdit_big_blind, self.widgets.lineEdit_small_blind,
                   self.widgets.btn_confirm]
            if self.on:
                for i in add:
                    i.setVisible(False)
                    self.on = False
            else:
                for i in add:
                    i.setVisible(True)
                    self.on = True
        if btnName == "btn_exitgame":
            self.close()
        if btnName == "btn_logout":
            loading_anim(True, self)
            self.to_pre_lobby = True
            ssl_client.send(pickle.dumps([4]))
        if btnName == "btn_profile":
            loading_anim(True, self)
            ssl_client.send(pickle.dumps([6, 1]))
        if btnName == "btn_rules":
            rules = Rules('lobby')
            lobby.setEnabled(self, False)
        if btnName == "btn_statistic":
            loading_anim(True, self)
            ssl_client.send(pickle.dumps([6, 0]))
        if btnName == "btn_gostart":
            loading_anim(True, self)
            self.relay = True
            self.widgets.btn_gostart.setDisabled(True)
            ssl_client.send(pickle.dumps([1]))
        if btnName == "btn_exit_lobby":
            loading_anim(True, self)
            self.to_pre_lobby = True
            ssl_client.send(pickle.dumps([3]))
        if btnName == 'btn_chat_send':
            self.widgets.lineEdit_chat_input.setPlaceholderText('Введите сообщение')
            text = self.widgets.lineEdit_chat_input.text()
            if (len(text) and len(text.split())) > 0:
                if len(text) < 128:
                    loading_anim(True, self)
                    self.widgets.lineEdit_chat_input.setText('')
                    ssl_client.send(pickle.dumps([5, text]))
                else:
                    self.widgets.lineEdit_chat_input.setText('')
                    self.widgets.lineEdit_chat_input.setPlaceholderText('Сообщение слишком длинное')
            else:
                self.widgets.lineEdit_chat_input.setText('')
                self.widgets.lineEdit_chat_input.setPlaceholderText('Сообщение не может быть пустым')


class connect_to_lobby(QMainWindow):
    def __init__(self, *args, **kwargs):
        self.on = False
        self.chose = ''
        super(connect_to_lobby, self).__init__(*args, **kwargs)
        self.threadpool = QThreadPool()
        self.ui = Ui_pre_lobby()
        self.to_lobby = False
        self.blur_effect = None
        self.gif = None
        self.blur_effect = None
        self.gif = None
        self.startups = True
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowTitle("Подключение к игре")
        self.widgets = self.ui
        connect_to_lobby.show(self)
        loading_anim(True, self)
        self.startup(0)
        self.init_connection()
        ssl_client.send('hello_from_pre_lobby'.encode('utf-8'))
        ssl_client.send(pickle.dumps([0]))
        self.widgets.btn_statistic.clicked.connect(self.buttonClick)
        self.widgets.listWidget.itemClicked.connect(self.buttonClick)
        self.widgets.btn_admin.clicked.connect(self.buttonClick)
        self.widgets.btn_confirm.clicked.connect(self.buttonClick)
        self.widgets.btn_create.clicked.connect(self.buttonClick)
        self.widgets.btn_exitgame.clicked.connect(self.buttonClick)
        self.widgets.btn_join.clicked.connect(self.buttonClick)
        self.widgets.btn_logout.clicked.connect(self.buttonClick)
        self.widgets.btn_profile.clicked.connect(self.buttonClick)
        self.widgets.btn_rules.clicked.connect(self.buttonClick)

    def closeEvent(self, event):
        if not self.to_lobby:
            ssl_client.send(pickle.dumps([6]))

    def init_connection(self):
        receives = Worker(self.receive)
        receives.signals.result.connect(self.exit_loop)

        # Execute
        self.threadpool.start(receives)

    def exit_loop(self, stat):
        global open_lobby, profile, statistic, window_log_in, admin
        if stat[0] == 1:
            self.to_lobby = True
            self.close()
            open_lobby = lobby()
        elif stat[0] == 2:
            loading_anim(False, self)
            if stat[1] == 0:
                statistic = Statistic('pre_lobby')
                connect_to_lobby.setEnabled(self, False)
            elif stat[1] == 1:
                profile = Profile('pre_lobby', user_data[4])
                connect_to_lobby.setEnabled(self, False)
            elif stat[1] == 2:
                admin = Admin('pre_lobby')
                connect_to_lobby.setEnabled(self, False)
        elif stat[0] == 3:
            loading_anim(False, self)
            self.close()
            window_log_in = log_in()

    def receive(self):
        while True:
            try:
                msg = pickle.loads(ssl_client.recv(4096))
                if msg[0] == 0:
                    loading_anim(False, self)
                    if msg[1]:
                        return [1]
                    else:
                        self.widgets.label_not_enough.setVisible(True)
                elif msg[0] == 1:
                    self.widgets.label_exists.setVisible(True)
                elif msg[0] == 2:
                    loading_anim(False, self)
                    if msg[1]:
                        return [1]
                    else:
                        self.widgets.label_not_enough.setVisible(True)
                elif msg[0] == 3:
                    if self.startups:
                        loading_anim(False, self)
                        self.startups = False
                    self.widgets.listWidget.clear()
                    for i in msg[1]:
                        self.widgets.listWidget.addItem(str(i))
                elif msg[0] == 4:
                    self.widgets.label_full.setVisible(True)
                elif msg[0] == 5:
                    return [3]
                elif msg[0] == 6:
                    return [2, msg[1]]
                elif msg[0] == 7:
                    return [0]
                elif msg[0] == 8:
                    if msg[1] == 2:
                        self.widgets.btn_admin.setEnabled(True)
            except EOFError:
                pass

    def startup(self, flag):
        hide = [self.widgets.frame_add, self.widgets.lineEdit_lobby_name,
                self.widgets.lineEdit_big_blind, self.widgets.lineEdit_small_blind,
                self.widgets.btn_confirm, self.widgets.label_load, self.widgets.label_not_selected, self.widgets.label_empty,
                self.widgets.label_exists, self.widgets.label_full, self.widgets.label_not_valid, self.widgets.label_not_enough, self.widgets.label_size_error]
        if flag == 0:
            for i in hide:
                i.setVisible(False)
        elif flag == 1:
            for i in range(6, len(hide)):
                hide[i].setVisible(False)
        elif flag == 2:
            for i in range(2):
                hide[i + 2].setText('')

    def confirm(self, name, big, small):
        try:
            if (len(name) and len(big) and len(small)) != 0:
                if 0 < int(big) < 10000000 and int(small) > 0:
                    if int(big) > int(small):
                        loading_anim(True, self)
                        ssl_client.send(pickle.dumps([2, name, int(big), int(small)]))
                    else:
                        self.widgets.label_size_error.setVisible(True)
                else:
                    raise
            else:
                self.startup(2)
                self.widgets.label_empty.setVisible(True)
        except:
            self.startup(2)
            self.widgets.label_not_valid.setVisible(True)

    def buttonClick(self):
        global rules
        self.startup(1)
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "btn_admin":
            loading_anim(True, self)
            ssl_client.send(pickle.dumps([4, 2]))
        if btnName == "btn_confirm":
            name_group = self.widgets.lineEdit_lobby_name.text()
            big_blind = self.widgets.lineEdit_big_blind.text()
            small_blind = self.widgets.lineEdit_small_blind.text()
            self.confirm(name_group, big_blind, small_blind)
        if btnName == "btn_create":
            add = [self.widgets.frame_add, self.widgets.lineEdit_lobby_name,
                   self.widgets.lineEdit_big_blind, self.widgets.lineEdit_small_blind,
                   self.widgets.btn_confirm]
            if self.on:
                for i in add:
                    i.setVisible(False)
                    self.on = False
            else:
                for i in add:
                    i.setVisible(True)
                    self.on = True
        if btnName == "btn_exitgame":
            self.close()
        if btnName == "btn_logout":
            loading_anim(True, self)
            ssl_client.send(pickle.dumps([3]))
            self.to_lobby = True
        if btnName == "btn_profile":
            loading_anim(True, self)
            ssl_client.send(pickle.dumps([4, 1]))
        if btnName == "btn_rules":
            rules = Rules('pre_lobby')
            connect_to_lobby.setEnabled(self, False)
        if btnName == "btn_statistic":
            loading_anim(True, self)
            ssl_client.send(pickle.dumps([4, 0]))
        if btnName == "listWidget":
            self.chose = self.widgets.listWidget.currentItem().text()
        if btnName == "btn_join":
            if len(self.chose) != 0:
                loading_anim(True, self)
                ssl_client.send(pickle.dumps([1, self.chose]))
            else:
                self.widgets.label_not_selected.setVisible(True)


class log_in(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(log_in, self).__init__(*args, **kwargs)
        self.threadpool = QThreadPool()
        self.first_time_reg = True
        self.per_close = True
        self.blur_effect = None
        self.gif = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowTitle("Авторизация")
        self.widgets = self.ui
        log_in.show(self)
        self.startup(True)
        self.init_connection()
        ssl_client.send('hello_from_log_in_form'.encode('utf-8'))
        ssl_client.send(pickle.dumps([0]))
        self.widgets.pushButton_enterens.clicked.connect(self.buttonClick)
        self.widgets.pushButton_registration.clicked.connect(self.buttonClick)

    def closeEvent(self, event):
        if self.per_close:
            ssl_client.send(pickle.dumps([2]))

    def init_connection(self):
        receives = Worker(self.receive)
        receives.signals.result.connect(self.exit_loop)

        # Execute
        self.threadpool.start(receives)

    def startup(self, start):
        hide_all = [self.widgets.label_name, self.widgets.lineEdit_name, self.widgets.label_load, self.widgets.label_reg_block, self.widgets.label_reg_empty,
                    self.widgets.label_reg_complexity, self.widgets.label_reg_notvalid, self.widgets.label_reg_8characters,
                    self.widgets.label_reg_success, self.widgets.label_reg_already, self.widgets.label_reg_already_used]
        if start:
            for i in hide_all:
                i.setVisible(False)
        else:
            for i in range(3, len(hide_all)):
                hide_all[i].setVisible(False)

    def receive(self):
        while True:
            try:
                msg = ssl_client.recv(1024).decode('utf-8')
                if msg[-11:] == 'log_in_stat':
                    loading_anim(False, self)
                    code = int(msg[:-11][0])
                    if code == 0:
                        self.widgets.label_reg_notvalid.setVisible(True)
                    elif code == 1:
                        self.widgets.label_reg_block.setVisible(True)
                    elif code == 2:
                        user_datas = [True, msg[:-11][1:], self.log, self.pass_hash, self.passw]
                        self.per_close = False
                        return [True, user_datas]
                    elif code == 3:
                        self.widgets.label_reg_already_used.setVisible(True)
                elif msg[-11:] == 'reg_in_stat':
                    if int(msg[:-11]) == 0:
                        self.widgets.label_reg_success.setVisible(True)
                        time.sleep(5)
                        user_datas = [True, self.namee, self.log, self.pass_hash, self.passw]
                        self.per_close = False
                        loading_anim(False, self)
                        return [True, user_datas]
                    else:
                        self.widgets.label_reg_already.setVisible(True)
                elif msg == 'exit':
                    return [False]
            except EOFError:
                pass

    def exit_loop(self, data):
        global user_data, pre_lobby
        if data[0]:
            user_data = data[1]
            self.close()
            pre_lobby = connect_to_lobby()

    def log_in_handler(self, login, password):
        self.log = login
        self.passw = password
        if (len(password) and len(login)) != 0:
            self.pass_hash = hashlib.sha512(password.encode('UTF-8'))
            self.pass_hash = self.pass_hash.hexdigest()
            loading_anim(True, self)
            ssl_client.send(pickle.dumps([1, True, login, self.pass_hash]))
        else:
            self.widgets.label_reg_empty.setVisible(True)

    def reg_handler(self, name, login, password):
        self.namee = name
        self.log = login
        self.passw = password
        complexity = check_complexity(password)
        if (len(password) and len(login) and len(name)) != 0:
            if len(password) > 8:
                if complexity[0] and complexity[1] and complexity[2] and complexity[3]:
                    self.pass_hash = hashlib.sha512(password.encode('UTF-8'))
                    self.pass_hash = self.pass_hash.hexdigest()
                    loading_anim(True, self)
                    ssl_client.send(pickle.dumps([1, False, name, login, self.pass_hash]))
                else:
                    self.widgets.label_reg_complexity.setVisible(True)
            else:
                self.widgets.label_reg_8characters.setVisible(True)
        else:
            self.widgets.label_reg_empty.setVisible(True)

    def buttonClick(self):
        self.startup(False)
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "pushButton_enterens":
            login = self.widgets.lineEdit_login.text()
            password = self.widgets.lineEdit_password.text()
            self.log_in_handler(login, password)
        if btnName == "pushButton_registration":
            if self.first_time_reg:
                self.widgets.label_name.setVisible(True)
                self.widgets.lineEdit_name.setVisible(True)
                self.widgets.label_log_in.setText('Регистрация')
                self.first_time_reg = False
            else:
                name = self.widgets.lineEdit_name.text()
                login = self.widgets.lineEdit_login.text()
                password = self.widgets.lineEdit_password.text()
                self.reg_handler(name, login, password)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window_log_in = log_in()
    sys.exit(app.exec())
