import pandas as pd


class Dataset:
    def __init__(self, last_year, path):
        self._last_year = last_year
        self._path = path
        self._players_list = self.create_list_from_all()

    def create_list_from_all(self):
        players_list = []
        last_year = self._last_year
        path = self._path
        for year in range(2000, last_year):
            temp_path = path + str(year) + ".csv"
            players_list = self.create_players_list(temp_path, players_list)
        return players_list

    def create_players_list(self, path, players_list):
        columns = ["winner_name", "loser_name"]
        data = pd.read_csv(path, usecols=columns)
        for player in data["winner_name"]:
            if player not in players_list:
                players_list.append(player)
        for player in data["loser_name"]:
            if player not in players_list:
                players_list.append(player)
        return players_list

    def get_players_list(self):
        return self._players_list


class Player:
    def __init__(self, name, hand, nationality, record, best_finish, best_finish_g, titles):
        pass


class Tournament:
    def __init__(self, name, surface, level, draw_size):
        pass


my_data = Dataset(2016, "data/atp_matches_")
print(my_data.get_players_list())
