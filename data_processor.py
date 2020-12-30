import pandas as pd


def create_list_from_all(path):
    players_list = []
    for year in range(2000, 2016):
        temp_path = path + str(year) + ".csv"
        players_list = create_players_list(temp_path, players_list)
    return players_list


def create_players_list(path, players_list):
    col_list = ["winner_name", "loser_name"]
    data = pd.read_csv(path, usecols=col_list)
    for player in data["winner_name"]:
        if player not in players_list:
            players_list.append(player)
    for player in data["loser_name"]:
        if player not in players_list:
            players_list.append(player)
    return players_list


pl_list = create_list_from_all("data/atp_matches_")
print(pl_list)
print(len(pl_list))
