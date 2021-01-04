from data_processor import Dataset, Player


def test_dataset_typical():
    my_data = Dataset(2001, "test_data/players")
    info = my_data.get_players_list()
    assert len(info) == 16


def test_new_player_typical_loser():
    my_data = Dataset(2001, "test_data/players")
    my_player = Player("Alex Lopez Moron", my_data)
    info = str(my_player)
    assert info == "Alex Lopez Moron, id: 101826, nationality: ESP"


def test_new_player_typical_winner():
    my_data = Dataset(2001, "test_data/players")
    my_player = Player("Jan Siemerink", my_data)
    info = str(my_player)
    assert info == "Jan Siemerink, id: 101733, nationality: NED"
