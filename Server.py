################################################################################
## Project developed with SBR, MR_Boombastic, Какой-то китаец
##
## Created date: 19.10.23-21.11.23
##
## WARNING! All changes made in this file will be lost your mind!
################################################################################

import copy
import socket
import ssl
import threading
import pathlib
import hashlib
import os
import base64
import json
import random
import time
import pickle
import sqlite3
from pathlib import Path
from treys import Card, Evaluator
from debug import Debug

#############################CHANGEABLE VARIABLES###############################
DOMAIN = '127.0.0.1'
PORT = 9091
PEM_Path = 'certs/crt_127.0.0.1/abs.pem'
KEY_Path = 'certs/crt_127.0.0.1/private.key'
NO_PHOTO_Path = 'images/images/no_photo.png'
DB_name = 'poker.db'
################################################################################

##############################STATICK VARIABLES#################################
clients = {}
lobby = {}
clients_pre_lobby = []
name_deck_players = {}
photo_deck_players = {}
shadow_data = {}
active_games = {}
active_games_events = {}
exited_active_game = {}
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
################################################################################


def get_rtc():
    return str(int(round(time.time() * 1000)))


def convert_to_binary_data(filename):
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


db_path = Path(pathlib.Path.cwd(), DB_name)
if not os.path.exists(db_path):
    db = sqlite3.connect(DB_name, check_same_thread=False)
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE users (
        name text,
        login text,
        password text,
        active text,
        date_created integer,
        date_deleted integer,
        money integer,
        all_games integer,
        win_games integer,
        permissions integer,
        level integer,
        photo BLOB
    )
    ''')
    cursor.execute('''CREATE TABLE messages (
        ID_users integer,
        message text,
        send_time text,
        deleted text
    )
    ''')
    cursor.execute('''CREATE TABLE statistics (
        ID_users integer,
        game_time integer,
        win text,
        players_with_cards text,
        pot integer,
        small_blind integer, 
        big_blind integer,
        full_bet integer
        )
        ''')
    db.commit()
    pass_hash = hashlib.sha512('toor'.encode('UTF-8'))
    pass_hash = pass_hash.hexdigest()
    cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", ('super_admin', 'root', f'{pass_hash}', 'True', f'{get_rtc()}', '0', '999999999', '0', '0', '2', '0', convert_to_binary_data(Path(pathlib.Path.cwd(), NO_PHOTO_Path))))
    db.commit()
else:
    db = sqlite3.connect(DB_name, check_same_thread=False)
    cursor = db.cursor()

server_soc_ssl = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
server_soc_ssl.load_cert_chain(Path(pathlib.Path.cwd(), PEM_Path), Path(pathlib.Path.cwd(), KEY_Path))
server_soc = socket.socket()
server_soc.bind((DOMAIN, PORT))
server_soc.listen()
ssl_server = server_soc_ssl.wrap_socket(server_soc, server_side=True)


def broadcast_lobby_inform(lobby_name):
    while True:
        if len(lobby[lobby_name]) == 7:
            del lobby[lobby_name]
            return
        clients_money = []
        d = {}
        game_players = []
        current_clients = []
        another_window = False
        for i in lobby[lobby_name][7:]:
            clients_money.append(clients[i][6])
            if clients[i][16]:
                another_window = True
            current_clients.extend([clients[i][0], clients[i][10]])
        lobby[lobby_name][6] = min(clients_money)
        for i in lobby[lobby_name][7:]:
            if not (clients[i][13] or clients[i][16]):
                i.send(pickle.dumps([0, lobby[lobby_name][0], lobby[lobby_name][1], lobby[lobby_name][2], lobby[lobby_name][3], lobby[lobby_name][4], '', current_clients]))
        if (len(lobby[lobby_name]) - 7 == lobby[lobby_name][1]) and (len(lobby[lobby_name]) - 7 > 1) and not another_window:
            if not lobby[lobby_name][0]:
                lobby[lobby_name][0] = True
                lobby[lobby_name][1] = 0
                for i in lobby[lobby_name][7:]:
                    game_players.append(clients[i][0])
                random.shuffle(game_players)
                name_deck_players.update({lobby_name: game_players})
                for i in game_players:
                    for g in clients.values():
                        if g[0] == i:
                            d.update({i: g[11]})
                            break
                photo_deck_players.update({lobby_name: d})
                for i in lobby[lobby_name][7:]:
                    clients[i][13] = True
                    i.send(pickle.dumps([2]))
                threading.Thread(target=game_c, args=(lobby_name, )).start()
        time.sleep(1)


def game_c(lobby_name):
    global shadow_data
    z = -1
    small_flag = False
    big_flag = False
    startup = True
    timer = True
    index = 0
    confirmed = 0
    out = [1]
    gen_pull = []
    deck = []
    suits = ["d", "c", "h", "s"]
    numeros = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    for suit in suits:
        for value in numeros:
            gen_pull.append(f'{value}{suit}')
    for i in range(5):
        z += 1
        deck.append(gen_pull.pop(random.randrange(0, 51 - z, 1)))
    deck.extend([lobby[lobby_name][2] + lobby[lobby_name][3], lobby[lobby_name][2], 1, 2, False, False, 0])

    for i in range(len(name_deck_players[lobby_name])):
        out.append([name_deck_players[lobby_name][i]])
        for g in range(2):
            out[i + 1].append(gen_pull.pop(random.randrange(0, 51 - z, 1)))
            z += 1
        for k in clients.values():
            if name_deck_players[lobby_name][i] in k:
                out[i + 1].append(k[6])
                break
        if i == 0:
            out[i + 1].append(True)
        else:
            out[i + 1].append(False)
        if name_deck_players[lobby_name][i] == name_deck_players[lobby_name][-1]:
            small_flag = True
            out[i + 1].append(True)
        else:
            out[i + 1].append(False)
        if name_deck_players[lobby_name][i] == name_deck_players[lobby_name][-2]:
            big_flag = True
            out[i + 1].append(True)
        else:
            out[i + 1].append(False)
        out[i + 1].extend(['', 0])
        if small_flag:
            out[i + 1][8] = lobby[lobby_name][3]
            out[i + 1][3] -= lobby[lobby_name][3]
            small_flag = False
        if big_flag:
            out[i + 1][8] = lobby[lobby_name][2]
            out[i + 1][3] -= lobby[lobby_name][2]
            big_flag = False
    for i in range(len(out[1:])):
        if len(name_deck_players[lobby_name]) == 2:
            if i == 1:
                out[i + 1].append(True)
                index = i + 1
            else:
                out[i + 1].append(False)
            out[i + 1].append(0)
        if len(name_deck_players[lobby_name]) > 2:
            if i == len(out[1:]) - 3:
                out[i + 1].append(True)
                index = i + 1
            else:
                out[i + 1].append(False)
            out[i + 1].append(0)
    out.append(deck)
    active_games.update({lobby_name: out})
    active_games_events.update({lobby_name: [threading.Event(), False]})
    shadow_data.update({lobby_name: []})
    while True:
        if startup:
            for i in lobby[lobby_name][7:]:
                if clients[i][13] and clients[i][15]:
                    if confirmed >= len(name_deck_players[lobby_name]):
                        startup = False
                        break
                    else:
                        confirmed += 1
        if active_games[lobby_name][-1][7] < 5 and ((len(active_games[lobby_name][1:-1]) > 1 and not active_games[lobby_name][-1][10]) or (len(active_games[lobby_name][1:-1]) > 0 and active_games[lobby_name][-1][10])):
            if not startup and shadow_data[lobby_name] != active_games[lobby_name]:
                for i in lobby[lobby_name][7:]:
                    if clients[i][13]:
                        for g in range(3):
                            i.send(pickle.dumps(active_games[lobby_name])) # name, card1, card2, money, dealer, small_bl, big_bl, text_bet, step, summ_rnd_bet
                            time.sleep(0.01)
                if timer:
                    threading.Thread(target=game_timer, args=(lobby_name, active_games[lobby_name][index][0])).start()
                    timer = False
                shadow_data = copy.deepcopy(active_games)
        else:
            active_games_events[lobby_name][0].set()
            threading.Thread(target=requiem, args=(lobby_name, )).start()
            break
        time.sleep(1)


def db_wr(name, money, state, pot, small, big, full_bet, report, current_cli, leave=None):
    level = 0
    cursor.execute(f"SELECT all_games, win_games, rowid FROM users WHERE name = '{name}'")
    pre_wr = list(cursor.fetchone())
    if state:
        pre_wr[1] += 1
        cursor.execute("UPDATE users SET win_games = ? WHERE name = ?", (pre_wr[1], name))
    pre_wr[0] += 1
    percent = (pre_wr[1] / pre_wr[0]) * 100
    if percent < 20:
        level = 1
    elif 20 <= percent < 40:
        level = 2
    elif 40 <= percent < 60:
        level = 3
    elif 60 <= percent < 80:
        level = 4
    elif 80 <= percent <= 100:
        level = 5
    clients[current_cli][10] = level
    if leave == 2:
        del clients[current_cli]
    cursor.execute("UPDATE users SET money = ?, all_games = ?, level = ? WHERE name = ?", (money, pre_wr[0], level, name))
    cursor.execute(
        f"INSERT INTO statistics VALUES ('{pre_wr[2]}', '{get_rtc()}', '{state}', '{json.dumps(report, sort_keys=True, indent=4)}', '{pot}', '{small}', '{big}', '{full_bet}')")
    db.commit()
    pre_wr.clear()


def requiem(lobby_name):
    results = [6]
    table = []
    first_start = True
    scores = []
    winner = []
    report = {}
    temp = []
    if lobby_name in exited_active_game.keys():
        temp.extend(exited_active_game[lobby_name])
    temp.extend(active_games[lobby_name][1:-1])
    for i in temp:
        report.update({i[0]: [i[1], i[2]]})
    report.update({'deck': [active_games[lobby_name][-1][0], active_games[lobby_name][-1][1], active_games[lobby_name][-1][2], active_games[lobby_name][-1][3], active_games[lobby_name][-1][4]]})
    if lobby_name in exited_active_game.keys():
        for data in range(len(exited_active_game[lobby_name])):
            if exited_active_game[lobby_name][data][-1] == 1:
                exited_active_game[lobby_name][data].pop(-1)
                active_games[lobby_name].insert(1, exited_active_game[lobby_name][data])
            else:
                leave = exited_active_game[lobby_name][data].pop(-1)
                current_cli = None
                for cli, g in clients.items():
                    if g[0] == exited_active_game[lobby_name][data][0]:
                        current_cli = cli
                        break
                clients[current_cli][6] = exited_active_game[lobby_name][data][3]
                db_wr(exited_active_game[lobby_name][data][0], exited_active_game[lobby_name][data][3], False,
                      active_games[lobby_name][-1][5], lobby[lobby_name][3], lobby[lobby_name][2],
                      clients[current_cli][6] - exited_active_game[lobby_name][data][3], report, current_cli, leave)
    evaluator = Evaluator()
    for i in range(len(active_games[lobby_name][1:-1])):
        hand = []
        current_cli = None
        if first_start:
            for g in active_games[lobby_name][-1][0:5]:
                table.append(Card.new(g))
            first_start = False
        for g in active_games[lobby_name][i + 1][1:3]:
            hand.append(Card.new(g))
        for cli, g in clients.items():
            if g[0] == active_games[lobby_name][i + 1][0]:
                current_cli = cli
                break
        score = evaluator.evaluate(table, hand)
        combination = evaluator.class_to_string(evaluator.get_rank_class(score))
        results.append([active_games[lobby_name][i + 1][0], combination, score, active_games[lobby_name][i + 1][3], clients[current_cli][6] - active_games[lobby_name][i + 1][3], current_cli])
        scores.append(score)
    min_score = min(scores)
    if len(scores) == len(set(scores)):
        for i in range(len(results[1:])):
            if results[i + 1][2] == min_score:
                db_wr(results[i + 1][0], results[i + 1][3] + active_games[lobby_name][-1][5], True, active_games[lobby_name][-1][5], lobby[lobby_name][3], lobby[lobby_name][2], results[i + 1][4], report, results[i + 1][5])
                clients[results[i + 1][5]][6] = results[i + 1][3] + active_games[lobby_name][-1][5]
                active_games[lobby_name][i + 1][3] = results[i + 1][3] + active_games[lobby_name][-1][5]
                results[i + 1] = results[i + 1][:2]
                winner.append(results[i + 1][0])
            else:
                db_wr(results[i + 1][0], results[i + 1][3], False, active_games[lobby_name][-1][5], lobby[lobby_name][3], lobby[lobby_name][2], results[i + 1][4], report, results[i + 1][5])
                clients[results[i + 1][5]][6] = results[i + 1][3]
                active_games[lobby_name][i + 1][3] = results[i + 1][3]
                results[i + 1] = results[i + 1][:2]
        results.append(winner)
    else:
        for i in range(len(results[1:])):
            if results[i + 1][2] == min_score:
                db_wr(results[i + 1][0], results[i + 1][3] + int(active_games[lobby_name][-1][5] / scores.count(min_score)), True, active_games[lobby_name][-1][5], lobby[lobby_name][3], lobby[lobby_name][2], results[i + 1][4], report, results[i + 1][5])
                clients[results[i + 1][5]][6] = results[i + 1][3] + int(active_games[lobby_name][-1][5] / scores.count(min_score))
                active_games[lobby_name][i + 1][3] = results[i + 1][3] + int(active_games[lobby_name][-1][5] / scores.count(min_score))
                results[i + 1] = results[i + 1][:2]
                winner.append(results[i + 1][0])
            else:
                db_wr(results[i + 1][0], results[i + 1][3], False, active_games[lobby_name][-1][5], lobby[lobby_name][3], lobby[lobby_name][2], results[i + 1][4], report, results[i + 1][5])
                clients[results[i + 1][5]][6] = results[i + 1][3]
                active_games[lobby_name][i + 1][3] = results[i + 1][3]
                results[i + 1] = results[i + 1][:2]
        results.append(winner)
    results.append(None)
    for i in lobby[lobby_name][7:]:
        if clients[i][13]:
            clients[i][13] = False
            clients[i][14] = False
            clients[i][15] = False
            if clients[i][6] < lobby[lobby_name][2]:
                lobby[lobby_name].remove(i)
                clients[i] = clients[i][:12]
                results[-1] = True
            else:
                results[-1] = False
            i.send(pickle.dumps(active_games[lobby_name]))
            i.send(pickle.dumps(results))
    lobby[lobby_name][0] = False
    del active_games_events[lobby_name]
    del name_deck_players[lobby_name]
    del active_games[lobby_name]
    del shadow_data[lobby_name]
    del photo_deck_players[lobby_name]
    if lobby_name in exited_active_game.keys():
        del exited_active_game[lobby_name]


def send_game_exit_broad(lobby_name, name, full, all_in, msges):
    for i in lobby[lobby_name][7:]:
        if clients[i][13]:
            i.send(pickle.dumps([4, name, full, all_in, msges]))


def round_control(lobby_name, raise_a, steps):
    digits = [2.0, 3.0, 4.0, 5.0]
    if len(name_deck_players[lobby_name]) != 0:
        counter = steps / len(name_deck_players[lobby_name])
        if counter in digits:
            if raise_a:
                steps -= len(name_deck_players[lobby_name])
                raise_a = False
            else:
                active_games[lobby_name][-1][6] = 0
                for i in active_games[lobby_name][1:-1]:
                    i[8] = 0
                    i[7] = ''
        counter = steps / len(name_deck_players[lobby_name])
        if counter == 2:
            active_games[lobby_name][-1][7] = 2
        elif counter == 3:
            active_games[lobby_name][-1][7] = 3
        elif counter == 4:
            active_games[lobby_name][-1][7] = 4
        elif counter == 5:
            active_games[lobby_name][-1][7] = 5
        return raise_a, steps
    else:
        active_games[lobby_name][-1][7] = 6
        return False, 0


def wr_msg(message, name, lobby_name, cl_obj, start):
    if not start:
        c_text = f'{name} > {message}'
        for i in lobby[lobby_name][7:]:
            if not clients[i][13]:
                i.send(pickle.dumps([5, c_text]))
        cursor.execute(f"SELECT rowid FROM users WHERE name = '{name}'")
        cursor.execute(f"INSERT INTO messages VALUES ('{cursor.fetchone()[0]}', '{message}', '{get_rtc()}', '0')")
        db.commit()
    else:
        cl_obj.send(pickle.dumps([5, 'Можете оставлять свои сообщения']))


def del_from_pre_lobby(client):
    if client in clients_pre_lobby:
        clients_pre_lobby.remove(client)


def send_active_lobby():
    x = []
    while True:
        if len(clients_pre_lobby) != 0:
            for i in lobby.keys():
                x.append(i)
            for i in clients_pre_lobby:
                i.send(pickle.dumps([3, x]))
            x.clear()
        time.sleep(1)


def update_player(name):
    for i, g in clients.items():
        if g[0] == name:
            del clients[i]
            cursor.execute("SELECT * FROM users WHERE name = ?", (name, ))
            clients.update({i: list(cursor.fetchone())})
            if len(g) > 12:
                clients[i].extend(g[12:])
            break


def admin_list(client, cnt):
    send_c = [0]
    cursor.execute("SELECT COUNT(*) FROM users")
    send_c.append(list(cursor.fetchone()))
    cursor.execute("SELECT name FROM users ORDER BY name ASC LIMIT ?", (cnt, ))
    send_c.extend(list(cursor.fetchall()))
    client.send(pickle.dumps(send_c))
    client.send(b'end')


def log_in_calc(data, client):
    authorization = 0
    reg = True
    if data[0]:
        cursor.execute('SELECT login, password, active FROM users')
        for creds in cursor.fetchall():
            if data[1] == creds[0] and data[2] == creds[1] and creds[2] == 'True':
                authorization = 2
                cursor.execute(f"SELECT * FROM users WHERE login = '{data[1]}' AND password = '{data[2]}'")
                user_data = cursor.fetchone()
                for i in clients.values():
                    if i[0] == user_data[0]:
                        authorization = 3
                        break
                if authorization != 3:
                    datab = list(user_data)
                    datab[11] = base64.b64encode(datab[11])
                    clients.update({client: datab})
                authorization = f'{authorization}{user_data[0]}'
                break
            elif data[1] == creds[0] and data[2] == creds[1] and creds[2] == 'False':
                authorization = 1
                break
        return [1, authorization]
    else:
        cursor.execute('SELECT name, login, password FROM users')
        for creds in cursor.fetchall():
            if (data[2] == creds[1] and data[3] == creds[2]) or data[1] == creds[0]:
                reg = False
                break
        if reg:
            cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (f'{data[1]}', f'{data[2]}', f'{data[3]}', 'True', f'{get_rtc()}', '0', '1000', '0', '0', '0', '0', convert_to_binary_data(Path(pathlib.Path.cwd(), NO_PHOTO_Path))))
            db.commit()
            cursor.execute(f"SELECT * FROM users WHERE login = '{data[2]}' AND password = '{data[3]}'")
            user_data = cursor.fetchone()
            datab = list(user_data)
            datab[11] = base64.b64encode(datab[11])
            clients.update({client: datab})
            return [2, 0]
        return [2, 1]


def visual_timer(lobby_name, player_name):
    print(f'visual open')
    index = -1
    for i in range(len(active_games[lobby_name][1:-1])):
        if active_games[lobby_name][i + 1][0] == player_name:
            index = i + 1
        else:
            active_games[lobby_name][i + 1][10] = 0
    for i in reversed(range(0, 3100)):
        if active_games_events[lobby_name][1]: break
        if (i / 100).is_integer():
            active_games[lobby_name][index][10] = int(i / 100)
        time.sleep(0.01)
    print(f'visual close')


def game_timer(lobby_name, player_name):
    print(f'timer {active_games_events[lobby_name][0].is_set()}, {lobby_name}, {player_name}')
    threading.Thread(target=visual_timer, args=(lobby_name, player_name)).start()
    active_games_events[lobby_name][0].wait(timeout=30)
    active_games_events[lobby_name][1] = True
    if not active_games_events[lobby_name][0].is_set():
        fold(lobby_name, player_name)
    active_games_events[lobby_name][0].clear()
    active_games_events[lobby_name][1] = False
    print('TIMER_close')



def client_handler(client):
    rnd = ''
    answer = ''
    while True:
        try:
            message = client.recv(4096)
            if message[:5] == b'hello':
                answer = message.decode('utf-8')
            else:
                if answer == 'hello_from_log_in_form':
                    log_in_form = pickle.loads(message)
                    if log_in_form[0] == 0:
                        client.send(b'connection')
                    elif log_in_form[0] == 1:
                        x = log_in_calc(log_in_form[1:], client)
                        if x[0] == 1:
                            client.send(bytes(f'{x[1]}log_in_stat', 'utf-8'))
                        elif x[0] == 2:
                            client.send(bytes(f'{x[1]}reg_in_stat', 'utf-8'))
                    elif log_in_form[0] == 2:
                        client.send(b'exit')
                elif answer == 'hello_from_pre_lobby':
                    data = pickle.loads(message)
                    if data[0] == 0:
                        clients_pre_lobby.append(client)
                        client.send(pickle.dumps([8, clients[client][9]]))
                    elif data[0] == 1:
                        if len(lobby[data[1]]) < 12:
                            if clients[client][6] > lobby[data[1]][2]:
                                clients[client].extend([data[1], False, False, False, False])
                                lobby[data[1]].append(client)
                                del_from_pre_lobby(client)
                                client.send(pickle.dumps([0, True]))
                            else:
                                client.send(pickle.dumps([0, False]))
                        else:
                            client.send(pickle.dumps([4]))
                    elif data[0] == 2:
                        if data[1] in lobby.keys():
                            client.send(pickle.dumps([1]))
                        elif clients[client][6] > data[2]:
                            clients[client].extend([data[1], False, False, False, False])
                            lobby.update({data[1]: [False, 0, data[2], data[3], clients[client][0], False, clients[client][6],
                                                    client]})  # записываем состояния лобби
                            del_from_pre_lobby(client)
                            client.send(pickle.dumps([2, True]))
                            threading.Thread(target=broadcast_lobby_inform, args=(data[1],)).start()
                        else:
                            client.send(pickle.dumps([2, False]))
                    elif data[0] == 3:
                        for i in range(32):
                            rnd += random.choice(chars)
                        clients[client][0] = rnd
                        del_from_pre_lobby(client)
                        client.send(pickle.dumps([5]))
                    elif data[0] == 4:
                        del_from_pre_lobby(client)
                        client.send(pickle.dumps([6, data[1]]))
                    elif data[0] == 5:
                        clients_pre_lobby.append(client)
                    elif data[0] == 6:
                        client.send(pickle.dumps([7]))
                elif answer == 'hello_from_lobby':
                    data = pickle.loads(message)
                    name = clients[client][12]
                    if data[0] == 0:
                        if data[1] in lobby.keys():
                            client.send(pickle.dumps([1]))
                        elif data[1] > lobby[name][6]:
                            client.send(pickle.dumps([9, True]))
                        elif clients[client][6] > data[1]:
                            lobby[name][2] = data[1]
                            lobby[name][3] = data[2]
                        else:
                            client.send(pickle.dumps([9, False]))
                    elif data[0] == 1:
                        lobby[name][1] += 1
                        clients[client][14] = True
                    elif data[0] == 2:
                        if client in clients_pre_lobby:
                            clients_pre_lobby.remove(client)
                        wr_msg('', clients[client][0], name, client, True)
                        client.send(pickle.dumps([8, clients[client][9]]))
                    elif data[0] == 3:
                        if clients[client][14]:
                            lobby[name][1] -= 1
                            clients[client][14] = False
                        lobby[name].remove(client)
                        clients[client] = clients[client][:12]
                        client.send(pickle.dumps([3]))
                    elif data[0] == 4:
                        if clients[client][14]:
                            lobby[name][1] -= 1
                            clients[client][14] = False
                        lobby[name].remove(client)
                        current_client = clients[client][:12]
                        clients.update({client: current_client})
                        for i in range(32):
                            rnd += random.choice(chars)
                        clients[client][0] = rnd
                        client.send(pickle.dumps([4]))
                    elif data[0] == 5:
                        wr_msg(data[1], clients[client][0], name, client, False)
                    elif data[0] == 6:
                        clients[client][16] = True
                        client.send(pickle.dumps([6, data[1]]))
                    elif data[0] == 7:
                        clients[client][16] = False
                    elif data[0] == 8:
                        client.send(pickle.dumps([7]))
                elif answer == 'hello_from_profile':
                    data = pickle.loads(message)
                    name = clients[client][0]
                    if data[0] == 0:
                        user = [0]
                        user.extend(clients[client])
                        client.send(pickle.dumps(user))
                        client.send(b'end')
                    elif data[0] == 1:
                        client.send(pickle.dumps([1]))
                        client.send(b'end')
                    elif data[0] == 2:
                        datab = []
                        while True:
                            packet = client.recv(4096)
                            if packet == b'end': break
                            datab.append(packet)
                        clients[client][11] = b"".join(datab)
                        cursor.execute("UPDATE users SET photo = ? WHERE name = ?", (base64.b64decode(b"".join(datab)), name))
                        db.commit()
                        user = [0]
                        user.extend(clients[client])
                        client.send(pickle.dumps(user))
                        client.send(b'end')
                    elif data[0] == 3:
                        cursor.execute("UPDATE users SET password = ? WHERE name = ?",
                                       (data[1], name))
                        db.commit()
                        client.send(pickle.dumps([2]))
                        client.send(b'end')
                    elif data[0] == 4:
                        clients[client][6] += data[1]
                        cursor.execute("UPDATE users SET money = ? WHERE name = ?",
                                       (clients[client][6], name))
                        db.commit()
                        client.send(pickle.dumps([3]))
                        client.send(b'end')
                        user = [0]
                        user.extend(clients[client])
                        client.send(pickle.dumps(user))
                        client.send(b'end')
                    elif data[0] == 5:
                        cursor.execute(f"DELETE FROM users WHERE name = '{name}'")
                        db.commit()
                    elif data[0] == 6:
                        client.send(pickle.dumps([4]))
                        client.send(b'end')
                elif answer == 'hello_from_statistic':
                    data = pickle.loads(message)
                    name = clients[client][0]
                    if data[0] == 0:
                        send_d = [0]
                        cursor.execute("SELECT money, all_games, win_games FROM users WHERE name = ?", (name,))
                        idu = list(cursor.fetchone())
                        send_d.append(idu)
                        if data[1] == 0:
                            cursor.execute(
                                f"SELECT game_time, players_with_cards FROM statistics WHERE ID_users = (SELECT rowid "
                                f"FROM users WHERE name = ?) ORDER BY game_time DESC LIMIT 5",
                                (name, ))
                        else:
                            cursor.execute(
                                f"SELECT game_time, players_with_cards FROM statistics WHERE ID_users = (SELECT rowid "
                                f"FROM users WHERE name = ?) AND game_time < ? ORDER BY game_time DESC LIMIT 5",
                                (name, data[1]))
                        for i in list(cursor.fetchall())[::-1]:
                            pls = ''
                            users = json.loads(i[1])
                            for g in users.keys():
                                if g != 'deck':
                                    pls += f'{g} '
                            send_d.append([i[0], pls])
                        cursor.execute(
                            f"SELECT COUNT(*) FROM statistics WHERE ID_users = (SELECT rowid FROM users WHERE name = ?)",
                            (name,))
                        send_d[1].append(cursor.fetchone()[0])
                        client.send(pickle.dumps(send_d))
                        client.send(b'end')
                    elif data[0] == 1:
                        client.send(pickle.dumps([1]))
                        client.send(b'end')
                    elif data[0] == 2:
                        cursor.execute(
                            f"SELECT game_time, win, players_with_cards, pot, small_blind, big_blind FROM statistics "
                            f"WHERE ID_users = (SELECT rowid FROM users WHERE name = ?) AND game_time = ?",
                            (name, data[1]))
                        client.send(pickle.dumps([2, list(cursor.fetchone())]))
                        client.send(b'end')
                elif answer == 'hello_from_admin':
                    data = pickle.loads(message)
                    if data[0] == 0:
                        admin_list(client, data[1])
                    elif data[0] == 1:
                        client.send(pickle.dumps([1]))
                        client.send(b'end')
                    elif data[0] == 2:
                        cursor.execute(
                            f"SELECT name, login, money, permissions, active FROM users "
                            f"WHERE name = ?",
                            (data[1],))
                        client.send(pickle.dumps([2, list(cursor.fetchone())]))
                        client.send(b'end')
                    elif data[0] == 3:
                        if len(data[1][3]) == 0:
                            cursor.execute("UPDATE users SET name = ?, login = ?, money = ?, permissions = ?, active = ? WHERE "
                                           "name = ?",
                                           (data[1][0], data[1][1], data[1][2], data[1][4], data[1][5], data[1][6]))
                            db.commit()
                        else:
                            cursor.execute(
                                "UPDATE users SET name = ?, login = ?, money = ?, password = ?, permissions = ?, active = ? WHERE name = ?",
                                (data[1][0], data[1][1], data[1][2], data[1][3], data[1][4], data[1][5], data[1][6]))
                            db.commit()
                        update_player(data[1][6])
                        admin_list(client, data[2])
                    elif data[0] == 4:
                        cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                            data[1][0], data[1][1], data[1][3], data[1][5], f'{get_rtc()}', '0', data[1][2], '0', '0',
                            data[1][4],
                            '0', convert_to_binary_data(Path(pathlib.Path.cwd(), NO_PHOTO_Path))))
                        db.commit()
                        admin_list(client, data[2])
                    elif data[0] == 5:
                        cursor.execute("UPDATE users SET active = ?, date_deleted = ? WHERE "
                                       "name = ?",
                                       (data[1], get_rtc(), data[2]))
                        db.commit()
                        update_player(data[2])
                        admin_list(client, data[3])
                    elif data[0] == 6:
                        cursor.execute(f"DELETE FROM users WHERE name = '{data[1]}'")
                        db.commit()
                        admin_list(client, data[2])
                elif answer == 'hello_from_game':
                    data = pickle.loads(message)
                    name = clients[client][0]
                    lobby_name = clients[client][12]
                    if data[0] == 0:
                        client.send(pickle.dumps([0]))
                        client.send(pickle.dumps(photo_deck_players[lobby_name]))
                        client.send(b'end')
                        clients[client][15] = True
                    if data[0] == 1:
                        active_games_events[lobby_name][0].set()
                        for i in range(len(active_games[lobby_name][1:])):
                            if active_games[lobby_name][i + 1][0] == name:
                                if not active_games[lobby_name][i + 1][8] == active_games[lobby_name][-1][6]:
                                    if not (active_games[lobby_name][i + 1][3] - (
                                            active_games[lobby_name][-1][6] - active_games[lobby_name][i + 1][8]) <= 0):
                                        active_games[lobby_name][-1][8] += 1
                                        active_games[lobby_name][-1][9], active_games[lobby_name][-1][
                                            8] = round_control(lobby_name, active_games[lobby_name][-1][9],
                                                               active_games[lobby_name][-1][8])
                                        active_games[lobby_name][-1][5] += active_games[lobby_name][-1][6] - \
                                                                           active_games[lobby_name][i + 1][8]
                                        active_games[lobby_name][i + 1][3] -= active_games[lobby_name][-1][6] - \
                                                                              active_games[lobby_name][i + 1][8]
                                        active_games[lobby_name][i + 1][
                                            7] = f'CALL {active_games[lobby_name][-1][6] - active_games[lobby_name][i + 1][8]}$'
                                        active_games[lobby_name][i + 1][8] += active_games[lobby_name][-1][6] - \
                                                                              active_games[lobby_name][i + 1][8]
                                        if not (active_games[lobby_name][-1][10] and len(
                                                active_games[lobby_name][1:-1]) == 1):
                                            active_games[lobby_name][i + 1][9] = False
                                            if i > 0:
                                                active_games[lobby_name][i][9] = True
                                                threading.Thread(target=game_timer, args=(lobby_name, active_games[lobby_name][i][0])).start()
                                            else:
                                                active_games[lobby_name][-2][9] = True
                                                threading.Thread(target=game_timer, args=(lobby_name, active_games[lobby_name][-2][0])).start()
                                    else:
                                        active_games[lobby_name][-1][10] = True
                                        active_games[lobby_name][-1][11] += 1
                                        active_games[lobby_name][-1][5] += active_games[lobby_name][i + 1][3]
                                        active_games[lobby_name][i + 1][8] += active_games[lobby_name][i + 1][3]
                                        send_game_exit_broad(lobby_name, name, False, True, 'ALL IN')
                                        active_games[lobby_name][i + 1][3] = 0
                                        name_deck_players[lobby_name].remove(name)
                                        active_games[lobby_name][i + 1].append(1)
                                        active_games[lobby_name][-1][8] -= len(name_deck_players[lobby_name])
                                        active_games[lobby_name][-1][9] = True
                                        active_games[lobby_name][-1][9], active_games[lobby_name][-1][
                                            8] = round_control(lobby_name, active_games[lobby_name][-1][9],
                                                               active_games[lobby_name][-1][8])
                                        if not (active_games[lobby_name][-1][10] and len(
                                                active_games[lobby_name][1:-1]) == 1):
                                            active_games[lobby_name][i + 1][9] = False
                                            if i > 0:
                                                active_games[lobby_name][i][9] = True
                                                threading.Thread(target=game_timer, args=(lobby_name, active_games[lobby_name][i][0])).start()
                                            else:
                                                active_games[lobby_name][-2][9] = True
                                                threading.Thread(target=game_timer, args=(lobby_name, active_games[lobby_name][-2][0])).start()
                                        if lobby_name in exited_active_game.keys():
                                            exited_active_game[lobby_name].append(active_games[lobby_name].pop(i + 1))
                                        else:
                                            exited_active_game.update(
                                                {lobby_name: [active_games[lobby_name].pop(i + 1)]})
                                else:
                                    active_games[lobby_name][-1][8] += 1
                                    active_games[lobby_name][-1][9], active_games[lobby_name][-1][
                                        8] = round_control(lobby_name, active_games[lobby_name][-1][9],
                                                           active_games[lobby_name][-1][8])
                                    active_games[lobby_name][i + 1][7] = 'CHECK'
                                    if not (active_games[lobby_name][-1][10] and len(
                                            active_games[lobby_name][1:-1]) == 1):
                                        active_games[lobby_name][i + 1][9] = False
                                        if i > 0:
                                            active_games[lobby_name][i][9] = True
                                            threading.Thread(target=game_timer, args=(lobby_name, active_games[lobby_name][i][0])).start()
                                        else:
                                            active_games[lobby_name][-2][9] = True
                                            threading.Thread(target=game_timer, args=(lobby_name, active_games[lobby_name][-2][0])).start()
                                break
                    elif data[0] == 2:
                        for i in range(len(active_games[lobby_name][1:])):
                            if active_games[lobby_name][i + 1][0] == name:
                                if data[1] == active_games[lobby_name][i + 1][3]:
                                    active_games_events[lobby_name][0].set()
                                    active_games[lobby_name][-1][10] = True
                                    active_games[lobby_name][-1][11] += 1
                                    active_games[lobby_name][-1][5] += active_games[lobby_name][i + 1][3]
                                    active_games[lobby_name][i + 1][8] += active_games[lobby_name][i + 1][3]
                                    active_games[lobby_name][-1][6] += active_games[lobby_name][i + 1][3]
                                    send_game_exit_broad(lobby_name, name, False, True, 'ALL IN')
                                    active_games[lobby_name][i + 1][3] = 0
                                    name_deck_players[lobby_name].remove(name)
                                    active_games[lobby_name][i + 1].append(1)
                                    active_games[lobby_name][-1][8] -= len(name_deck_players[lobby_name])
                                    active_games[lobby_name][-1][9] = True
                                    active_games[lobby_name][-1][9], active_games[lobby_name][-1][8] = round_control(
                                        lobby_name, active_games[lobby_name][-1][9], active_games[lobby_name][-1][8])
                                    active_games[lobby_name][i + 1][9] = False
                                    if i > 0:
                                        active_games[lobby_name][i][9] = True
                                        threading.Thread(target=game_timer, args=(lobby_name, active_games[lobby_name][i][0])).start()
                                    else:
                                        active_games[lobby_name][-2][9] = True
                                        threading.Thread(target=game_timer, args=(lobby_name, active_games[lobby_name][-2][0])).start()
                                    if lobby_name in exited_active_game.keys():
                                        exited_active_game[lobby_name].append(active_games[lobby_name].pop(i + 1))
                                    else:
                                        exited_active_game.update({lobby_name: [active_games[lobby_name].pop(i + 1)]})
                                elif active_games[lobby_name][i + 1][3] - data[1] + (
                                        active_games[lobby_name][-1][6] - active_games[lobby_name][i + 1][8]) <= 0:
                                    client.send(pickle.dumps([7]))
                                elif data[1] < active_games[lobby_name][-1][6] + 1:
                                    client.send(pickle.dumps([3]))
                                else:
                                    active_games_events[lobby_name][0].set()
                                    active_games[lobby_name][i + 1][7] = f'RAISE {data[1]}$'
                                    active_games[lobby_name][-1][8] += 1
                                    active_games[lobby_name][-1][9] = True
                                    active_games[lobby_name][-1][9], active_games[lobby_name][-1][8] = round_control(
                                        lobby_name, active_games[lobby_name][-1][9], active_games[lobby_name][-1][8])
                                    active_games[lobby_name][-1][5] += data[1] + (
                                            active_games[lobby_name][-1][6] - active_games[lobby_name][i + 1][8])
                                    active_games[lobby_name][i + 1][3] -= data[1] + (
                                            active_games[lobby_name][-1][6] - active_games[lobby_name][i + 1][8])
                                    active_games[lobby_name][i + 1][8] += data[1] + (
                                            active_games[lobby_name][-1][6] - active_games[lobby_name][i + 1][8])
                                    active_games[lobby_name][-1][6] += data[1]
                                    active_games[lobby_name][i + 1][9] = False
                                    if i > 0:
                                        active_games[lobby_name][i][9] = True
                                        threading.Thread(target=game_timer, args=(lobby_name, active_games[lobby_name][i][0])).start()
                                    else:
                                        active_games[lobby_name][-2][9] = True
                                        threading.Thread(target=game_timer, args=(lobby_name, active_games[lobby_name][-2][0])).start()
                                break

                    elif data[0] == 3:
                        active_games_events[lobby_name][0].set()
                        fold(lobby_name, name)
                    elif data[0] == 4:
                        active_games_events[lobby_name][0].set()
                        if lobby_name in exited_active_game.keys():
                            for i in range(len(exited_active_game[lobby_name])):
                                if exited_active_game[lobby_name][i][0] == name:
                                    if exited_active_game[lobby_name][i][-1] == 1 and active_games[lobby_name][-1][11] == 1:
                                        active_games[lobby_name][-1][10] = False
                                    exited_active_game[lobby_name][i][-1] = 3
                                    clients[client][13] = False
                                    clients[client][14] = False
                                    clients[client][15] = False
                                    client.send(pickle.dumps([5]))
                                    send_game_exit_broad(lobby_name, name, True, False, None)
                                    break
                        for i in range(len(active_games[lobby_name][1:])):
                            if active_games[lobby_name][i + 1][0] == name:
                                name_deck_players[lobby_name].remove(name)
                                active_games[lobby_name][i + 1].append(3)
                                active_games[lobby_name][-1][8] -= len(name_deck_players[lobby_name]) + 1
                                active_games[lobby_name][-1][9], active_games[lobby_name][-1][8] = round_control(
                                    lobby_name, active_games[lobby_name][-1][9], active_games[lobby_name][-1][8])
                                clients[client][13] = False
                                clients[client][14] = False
                                clients[client][15] = False
                                client.send(pickle.dumps([5]))
                                send_game_exit_broad(lobby_name, name, True, False, None)
                                if not (active_games[lobby_name][-1][10] and len(active_games[lobby_name][1:-1]) == 1):
                                    if i > 0:
                                        active_games[lobby_name][i][9] = True
                                        threading.Thread(target=game_timer, args=(lobby_name, active_games[lobby_name][i][0])).start()
                                    else:
                                        active_games[lobby_name][-2][9] = True
                                        threading.Thread(target=game_timer, args=(lobby_name, active_games[lobby_name][-2][0])).start()
                                if lobby_name in exited_active_game.keys():
                                    exited_active_game[lobby_name].append(active_games[lobby_name].pop(i + 1))
                                else:
                                    exited_active_game.update({lobby_name: [active_games[lobby_name].pop(i + 1)]})
                                break
                    elif data[0] == 5:
                        client.send(pickle.dumps([2]))
        except:
            print('client disconnected')
            if client in clients.keys():
                name = clients[client][0]
                if len(clients[client]) > 12:
                    lobby_name = clients[client][12]
                    if clients[client][14]:
                        active_games_events[lobby_name][0].set()
                        if clients[client][12] in exited_active_game.keys():
                            for i in range(len(exited_active_game[lobby_name])):
                                if exited_active_game[lobby_name][i][0] == name:
                                    if exited_active_game[lobby_name][i][-1] == 1 and active_games[lobby_name][-1][11] == 1:
                                        active_games[lobby_name][-1][10] = False
                                    exited_active_game[lobby_name][i][-1] = 2
                                    clients[client][13] = False
                                    clients[client][14] = False
                                    clients[client][15] = False
                                    send_game_exit_broad(lobby_name, name, True, False, None)
                                    lobby[lobby_name].remove(client)
                                    break
                        if clients[client][12] in active_games.keys():
                            for i in range(len(active_games[lobby_name][1:])):
                                if active_games[lobby_name][i + 1][0] == name:
                                    name_deck_players[lobby_name].remove(name)
                                    active_games[lobby_name][i + 1].append(2)
                                    active_games[lobby_name][-1][8] -= len(name_deck_players[lobby_name]) + 1
                                    active_games[lobby_name][-1][9], active_games[lobby_name][-1][8] = round_control(
                                        lobby_name, active_games[lobby_name][-1][9], active_games[lobby_name][-1][8])
                                    lobby[lobby_name].remove(client)
                                    send_game_exit_broad(lobby_name, name, True, False, None)
                                    if not (active_games[lobby_name][-1][10] and active_games[lobby_name][1:-1] == 1):
                                        if i > 0:
                                            active_games[lobby_name][i][9] = True
                                            threading.Thread(target=game_timer, args=(lobby_name, active_games[lobby_name][i][0])).start()
                                        else:
                                            active_games[lobby_name][-2][9] = True
                                            threading.Thread(target=game_timer, args=(lobby_name, active_games[lobby_name][-2][0])).start()
                                    if lobby_name in exited_active_game.keys():
                                        exited_active_game[lobby_name].append(active_games[lobby_name].pop(i + 1))
                                    else:
                                        exited_active_game.update({lobby_name: [active_games[lobby_name].pop(i + 1)]})
                                    break
                    else:
                        lobby[lobby_name].remove(client)
                        if clients[client][14]:
                            lobby[lobby_name][1] -= 1
                        del clients[client]
                        client.close()

                else:
                    if client in clients_pre_lobby:
                        clients_pre_lobby.remove(client)
                    del clients[client]
                    client.close()
            else:
                client.close()
            break


def fold(lobby_name, name):
    for i in range(len(active_games[lobby_name][1:])):
        if active_games[lobby_name][i + 1][0] == name:
            name_deck_players[lobby_name].remove(name)
            active_games[lobby_name][i + 1].append(0)
            active_games[lobby_name][-1][8] -= len(name_deck_players[lobby_name])
            active_games[lobby_name][-1][9], active_games[lobby_name][-1][8] = round_control(
                lobby_name, active_games[lobby_name][-1][9], active_games[lobby_name][-1][8])
            send_game_exit_broad(lobby_name, name, False, False, None)
            if not (active_games[lobby_name][-1][10] and len(active_games[lobby_name][1:-1]) == 1):
                if i > 0:
                    active_games[lobby_name][i][9] = True
                    threading.Thread(target=game_timer, args=(lobby_name, active_games[lobby_name][i][0])).start()
                else:
                    active_games[lobby_name][-2][9] = True
                    threading.Thread(target=game_timer, args=(lobby_name, active_games[lobby_name][-2][0])).start()
            if lobby_name in exited_active_game.keys():
                exited_active_game[lobby_name].append(active_games[lobby_name].pop(i + 1))
            else:
                exited_active_game.update({lobby_name: [active_games[lobby_name].pop(i + 1)]})
            break


def init():
    while True:
        try:
            client, addr = ssl_server.accept()
            print(f'New connection with client ({addr})')
            stream = threading.Thread(target=client_handler, args=(client,))
            stream.start()
        except:
            break


if '__main__' == __name__:
    threading.Thread(target=send_active_lobby, args=()).start()
    ## threading.Thread(target=Debug, args=(clients, lobby, clients_pre_lobby, name_deck_players, photo_deck_players, shadow_data, active_games, active_games_events, exited_active_game)).start() ## Enable debugger
    init()
