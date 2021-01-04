import pandas as pd


class Dataset:
    def __init__(self, last_year, path):
        self._last_year = last_year
        self._path = path
        columns = ["winner_name", "winner_id", "winner_ioc"]
        headers = ["name", "player_id", "nationality"]
        self._players_list = self.create_unique_list_from_all(columns, headers)
        columns = ["loser_name", "loser_id", "loser_ioc"]
        self._players_list = self.create_unique_list_from_all(columns, headers)

    def create_unique_list_from_all(self, columns, headers):
        item_list = []
        last_year = self._last_year
        path = self._path
        for year in range(2000, last_year):
            temp_path = path + str(year) + ".csv"
            item_list = self.create_unique_list(temp_path, item_list, columns, headers)
        return item_list, len(item_list)

    def create_unique_list(self, path, item_list, columns, headers):
        data = pd.read_csv(path, usecols=columns)
        for item in data[columns].values:
            unique_item = {}
            for key_iterator in range(0, len(headers)):
                unique_item[headers[key_iterator]] = item[key_iterator]
            if unique_item not in item_list:
                item_list.append(unique_item)
        return item_list

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
