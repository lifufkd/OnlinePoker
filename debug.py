import math
import sys
from datetime import datetime
import time


class Debug:
    def __init__(self, clients, lobby, clients_pre_lobby, name_deck_players, photo_deck_players, shadow_data, active_games, active_games_events, exited_active_game):
        super(Debug, self).__init__()
        self.game_data = [clients, lobby, clients_pre_lobby, name_deck_players, photo_deck_players, shadow_data, active_games, active_games_events, exited_active_game]
        self.memory_log = ''
        self.Memory_analyzer()

    def convert_size(self, size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])

    def Memory_analyzer(self):
        while True:
            self.memory_log += f'Runtime debug {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n {"-"*50}\n size of clients {self.convert_size(sys.getsizeof(self.game_data[0]))}\n size of lobby {self.convert_size(sys.getsizeof(self.game_data[1]))}\n size of clients_pre_lobby {self.convert_size(sys.getsizeof(self.game_data[2]))}\n size of name_deck_players {self.convert_size(sys.getsizeof(self.game_data[3]))}\n size of photo_deck_players {self.convert_size(sys.getsizeof(self.game_data[4]))}\n size of shadow_data {self.convert_size(sys.getsizeof(self.game_data[5]))}\n size of active_games {self.convert_size(sys.getsizeof(self.game_data[6]))}\n size of active_games_events {self.convert_size(sys.getsizeof(self.game_data[7]))}\n size of exited_active_players {self.convert_size(sys.getsizeof(self.game_data[8]))}\n {"-" * 50}\n'
            self.Write_in_file(self.memory_log)
            self.memory_log = ''
            time.sleep(5)

    def Write_in_file(self, data):
        with open("debug_log.txt", "a") as file:
            file.write(f'\n{data}')