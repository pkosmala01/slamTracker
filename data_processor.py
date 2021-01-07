import pandas as pd


class Dataset:
    def __init__(self, last_year, path):
        self._last_year = last_year
        self._path = path
        self._players_list = []
        self._tournaments_list = []
        columns = ["winner_name", "winner_id", "winner_ioc"]
        headers = ["name", "player_id", "nationality"]
        self._players_list = self.create_unique_list_from_all(columns, headers, self._players_list)
        columns = ["loser_name", "loser_id", "loser_ioc"]
        self._players_list = self.create_unique_list_from_all(columns, headers, self._players_list)
        columns = ["tourney_name"]
        headers = ["name"]
        self._tournaments_list = self.create_unique_list_from_all(columns, headers, self._tournaments_list)

    def create_unique_list_from_all(self, columns, headers, item_list):
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

    def get_players_with_name(self, name):
        pl_list = []
        for player in self._players_list:
            if name in player["name"]:
                pl_list.append(player["name"])
        return pl_list

    def create_dataframe(self, columns):
        last_year = self._last_year
        path = self._path
        data = pd.read_csv(path + "2000.csv", usecols=columns)
        for year in range(2001, last_year + 1):
            temp_path = path + str(year) + ".csv"
            temp_data = pd.read_csv(temp_path, usecols=columns)
            data = data.append(temp_data, ignore_index=True)
        return data

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
        self._matches_list = self.create_matches_list()

    def __str__(self):
        name = self._name
        player_id = self._player_id
        nationality = self._nationality
        info = f'{name}, id: {player_id}, nationality: {nationality}'
        return info

    def create_matches_list(self):
        player_id = self._player_id
        columns = ["winner_id", "loser_id", "tourney_name", "surface", "tourney_date"]
        temp_list = self._dataset.create_dataframe(columns)
        matches_list = temp_list[temp_list["winner_id"] == player_id]
        self._matches_won = len(matches_list)
        temp_list = temp_list[temp_list["loser_id"] == player_id]
        matches_list = matches_list.append(temp_list)
        self._matches_played = len(matches_list)
        return matches_list

    def get_matches_won(self):
        return self._matches_won

    def get_matches_played(self):
        return self._matches_played


class Tournament:
    def __init__(self, name, dataset):
        self._name = name
        self._dataset = dataset

    def __str__(self):
        name = self._name
        info = f'{name}'
        return info


if __name__ == "__main__":
    my_data = Dataset(2015, "data/atp_matches_")
    while True:
        player_name = input("Enter a player's name: ")
        temp_list = my_data.get_players_with_name(player_name)
        for player in temp_list:
            print(f'{temp_list.index(player)}: {player}')
        if len(temp_list) > 0:
            player_choice = int(input("Choose a player: "))
            my_player = Player(temp_list[player_choice], my_data)
            break
    print(str(my_player))
