import pandas as pd


class Dataset:
    def __init__(self, last_year, path):
        self._last_year = last_year
        self._path = path
        columns = ["winner_name", "winner_id", "winner_ioc"]
        headers = ["name", "player_id", "nationality"]
        self._players_list = self.create_unique_list_from_all(columns, headers)
        columns = ["loser_name", "loser_id", "loser_ioc"]
        self._players_list += self.create_unique_list_from_all(columns, headers)
        columns = ["tourney_name", "surface", "draw_size", "tourney_level"]
        headers = ["name", "surface", "draw_size", "level"]
        self._tournaments_list = self.create_unique_list_from_all(columns, headers)

    def create_unique_list_from_all(self, columns, headers):
        item_list = []
        last_year = self._last_year
        path = self._path
        for year in range(2000, last_year + 1):
            temp_path = path + str(year) + ".csv"
            item_list = self.create_unique_list(temp_path, item_list, columns, headers)
        return item_list

    def create_unique_list(self, path, item_list, columns, headers):
        data = pd.read_csv(path, usecols=columns)
        for item in data[columns].values:
            unique_item = {}
            for key_iterator in range(0, len(headers)):
                unique_item[headers[key_iterator]] = item[key_iterator]
            if unique_item not in item_list:
                item_list.append(unique_item)
        return item_list

    def get_player_data_from_name(self, name):
        for player in self._players_list:
            if player["name"] == name:
                return player

    def get_tournament_data_from_name(self, name):
        for tournament in self._tournaments_list:
            if tournament["name"] == name:
                return tournament

    def get_players_list(self):
        return self._players_list

    def get_tournaments_list(self):
        return self._tournaments_list


class Player:
    def __init__(self, name, dataset):
        self._name = name
        self._dataset = dataset
        player_data = dataset.get_player_data_from_name(name)
        self._player_id = player_data["player_id"]
        self._nationality = player_data["nationality"]

    def __str__(self):
        name = self._name
        player_id = self._player_id
        nationality = self._nationality
        info = f'{name}, id: {player_id}, nationality: {nationality}'
        return info


class Tournament:
    def __init__(self, name, dataset):
        self._name = name
        self._dataset = dataset
        tournament_data = dataset.get_tournament_data_from_name(name)
        self._surface = tournament_data["surface"]
        self._draw_size = tournament_data["draw_size"]
        self._level = tournament_data["level"]

    def __str__(self):
        name = self._name
        surface = self._surface
        draw_size = self._draw_size
        level = self._level
        info = f'{name}, surface: {surface}, {draw_size} players, level: {level}'
        return info


my_data = Dataset(2015, "data/atp_matches_")
print(my_data.get_players_list())
player1 = Player("Rodrigo Arus", my_data)
print(str(player1))
