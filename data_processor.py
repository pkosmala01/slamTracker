from datetime import datetime
import pandas as pd
from exceptions import NoPlayerError


class Dataset:
    def __init__(self, last_year, path):
        self._last_year = last_year
        self._path = path
        self._players_list = []
        self._tournaments_list = []
        columns = ["winner_name", "winner_id", "winner_ioc"]
        headers = ["name", "player_id", "nationality"]
        self._players_list = self.create_unique_list_from_all(
                columns, headers, self._players_list)
        columns = ["loser_name", "loser_id", "loser_ioc"]
        self._players_list = self.create_unique_list_from_all(
                columns, headers, self._players_list)
        columns = ["tourney_name", "surface"]
        headers = ["name", "surface"]
        self._tournaments_list = self.create_unique_list_from_all(
            columns, headers, self._tournaments_list)

    def create_unique_list_from_all(self, columns, headers, item_list):
        last_year = self._last_year
        path = self._path
        for year in range(2000, last_year + 1):
            temp_path = path + str(year) + ".csv"
            item_list = self.create_unique_list(
                    temp_path, item_list, columns, headers)
        return item_list

    def create_unique_list(self, path, item_list, columns, headers):
        try:
            data = pd.read_csv(path, usecols=columns)
        except(FileNotFoundError):
            print('Wrong path, may be caused by a wrong value of last_year')
        data = pd.read_csv(path, usecols=columns)
        for item in data[columns].values:
            unique_item = {}
            for key_iterator in range(0, len(headers)):
                unique_item[headers[key_iterator]] = item[key_iterator]
            if unique_item not in item_list:
                item_list.append(unique_item)
        return item_list

    def get_player_data_from_name(self, name):
        player_data = None
        for player in self._players_list:
            if player["name"] == name:
                player_data = player
                return player_data
        if player_data is None:
            raise(NoPlayerError)

    def get_players_with_name(self, name):
        pl_list = []
        for player in self._players_list:
            if name in player["name"]:
                pl_list.append(player["name"])
        return pl_list

    def get_tournament_surface(self, name):
        for tournament in self._tournaments_list:
            if tournament["name"] == name:
                return tournament["surface"]

    def create_dataframe(self, columns):
        last_year = self._last_year
        path = self._path
        try:
            data = pd.read_csv(path + "2000.csv", usecols=columns)
        except(FileNotFoundError):
            print('Wrong path, may be caused by a wrong value of last_year')
        for year in range(2001, last_year + 1):
            temp_path = path + str(year) + ".csv"
            try:
                temp_data = pd.read_csv(temp_path, usecols=columns)
            except(FileNotFoundError):
                print(
                    'Wrong path, may be caused by a wrong value of last_year')
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
        player_id = self.player_id()
        nationality = self._nationality
        info = f'{name}, id: {player_id}, nationality: {nationality}'
        return info

    def create_matches_list(self):
        player_id = self.player_id()
        columns = [
            "winner_id", "loser_id", "tourney_name", "surface",
            "tourney_date", "draw_size", "match_num", "tourney_level"]
        temp_list = self._dataset.create_dataframe(columns)
        matches_list = temp_list[temp_list["winner_id"] == player_id]
        self._matches_won = len(matches_list)
        if not matches_list.empty:
            first_match_winner = matches_list["tourney_date"].iloc[0]
        else:
            first_match_winner = 99999999
        temp_list = temp_list[temp_list["loser_id"] == player_id]
        matches_list = matches_list.append(temp_list)
        if not temp_list.empty:
            first_match_loser = temp_list["tourney_date"].iloc[0]
        else:
            first_match_loser = 99999999
        first_match = str(min(first_match_loser, first_match_winner))
        self._first_match = datetime.strptime(first_match, '%Y%m%d')
        self._matches_played = len(matches_list)
        return matches_list

    def list_of_matches_against(self):
        other_id = self._other_player.player_id()
        temp_list = self._matches_list
        matches_against = temp_list[temp_list["loser_id"] == other_id]
        if not matches_against.empty:
            self._vs_matches_won = len(matches_against)
        else:
            self._vs_matches_won = 0
        temp_list = temp_list[temp_list["winner_id"] == other_id]
        matches_against = matches_against.append(temp_list)
        if not matches_against.empty:
            self._vs_matches_played = len(matches_against)
        else:
            self._vs_matches_played = 0
        self._matches_against = matches_against

    def same_surface_stats(self):
        surface = self._tournament.surface()
        player_id = self.player_id()
        same_surface_won = 0
        same_surface_played = 0
        for match in self._matches_list.values:
            if match[1] == surface:
                same_surface_played += 1
                if match[6] == player_id:
                    same_surface_won += 1
        self._same_surface_won = same_surface_won
        self._same_surface_played = same_surface_played
        same_surface_vs_won = 0
        same_surface_vs_played = 0
        if not self._matches_against.empty:
            for match in self._matches_against.values:
                if match[1] == surface:
                    same_surface_vs_played += 1
                    if match[6] == player_id:
                        same_surface_vs_won += 1
            self._same_surface_vs_won = same_surface_vs_won
            self._same_surface_vs_played = same_surface_vs_played
        else:
            self._same_surface_vs_won = 0
            self._same_surface_vs_played = 0

    def tournament_stats(self):
        tournament_name = self._tournament.name()
        player_id = self.player_id()
        round_names = [
            "zwycięstwo", "finał", "1/2", "1/4",
            "1/8", "1/16", "1/32", "1/64", "1/128", "b/d"
        ]
        best_finish = 9
        best_finish_tournament = 9
        best_finish_grand_slam = 9
        titles = 0
        for match in self._matches_list.values:
            print(match)
            draw_size = match[2]
            match_num = match[5]
            finish = 9
            if match_num == draw_size - 1:
                if player_id == match[6]:
                    finish = 0
                    titles += 1
                else:
                    finish = 1
            else:
                temp_num = draw_size
                round_num = 0
                while temp_num > 0:
                    if temp_num < match_num:
                        finish = round_num
                        break
                    else:
                        temp_num -= 2**round_num
                        round_num += 1
            best_finish = min(finish, best_finish)
            if tournament_name == match[0]:
                best_finish_tournament = min(finish, best_finish_tournament)
            if match[3] == "G":
                best_finish_grand_slam = min(finish, best_finish_grand_slam)
        self._best_finish = round_names[best_finish]
        self._best_finish_tournament = round_names[best_finish_tournament]
        self._best_finish_grand_slam = round_names[best_finish_grand_slam]
        self._titles = titles

    def set_other_player(self, player):
        self._other_player = player
        self.list_of_matches_against()

    def set_tournament(self, tournament):
        self._tournament = tournament
        self.same_surface_stats()
        self.tournament_stats()

    def matches_won(self):
        return self._matches_won

    def matches_played(self):
        return self._matches_played

    def player_id(self):
        return self._player_id

    def vs_matches_played(self):
        return self._vs_matches_played

    def vs_matches_won(self):
        return self._vs_matches_won

    def same_surface_played(self):
        return self._same_surface_played

    def same_surface_won(self):
        return self._same_surface_won

    def same_surface_vs_played(self):
        return self._same_surface_vs_played

    def same_surface_vs_won(self):
        return self._same_surface_vs_won

    def first_match(self):
        return self._first_match.date()

    def best_finish(self):
        return self._best_finish

    def best_finish_tournament(self):
        return self._best_finish_tournament

    def best_finish_grand_slam(self):
        return self._best_finish_grand_slam

    def titles(self):
        return self._titles


class Tournament:
    def __init__(self, name, dataset):
        self._name = name
        self._dataset = dataset
        self._surface = dataset.get_tournament_surface(name)

    def __str__(self):
        name = self._name
        surface = self._surface
        info = f'{name}, surface: {surface}'
        return info

    def name(self):
        return self._name

    def surface(self):
        return self._surface


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
    while True:
        player_name = input("Enter a player's name: ")
        temp_list = my_data.get_players_with_name(player_name)
        for player in temp_list:
            print(f'{temp_list.index(player)}: {player}')
        if len(temp_list) > 0:
            player_choice = int(input("Choose a player: "))
            my_player_2 = Player(temp_list[player_choice], my_data)
            my_player_2.set_other_player(my_player)
            break
    print(my_player_2._matches_against)
    print(my_player.first_match())
    print(my_player_2.first_match())
    my_tournament = Tournament("Australian Open", my_data)
    my_player_2.set_tournament(my_tournament)
    print(my_player_2._best_finish)
    print(my_player_2._best_finish_tournament)
    print(my_player_2._best_finish_grand_slam)
    print(my_player_2._titles)
