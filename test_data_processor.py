from data_processor import Dataset, Player, Tournament


def test_dataset_typical_players():
    my_data = Dataset(2001, "test_data/players")
    info = my_data.get_players_list()
    assert len(info) == 16


def test_dataset_typical_tournaments():
    my_data = Dataset(2001, "test_data/tournaments")
    info = my_data.get_tournaments_list()
    assert len(info) == 5


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


def test_new_tournament_typical():
    my_data = Dataset(2001, "test_data/tournaments")
    my_tournament = Tournament("Australian Open", my_data)
    info = str(my_tournament)
    assert info == "Australian Open"


def test_listing_players():
    my_data = Dataset(2001, "test_data/players")
    info = my_data.get_players_with_name("Ja")
    assert len(info) == 2


def test_matches_won():
    my_data = Dataset(2001, "test_data/players")
    my_player = Player("Alex Lopez Moron", my_data)
    info = my_player.get_matches_won()
    assert info == 0


def test_matches_played():
    my_data = Dataset(2001, "test_data/players")
    my_player = Player("Alex Lopez Moron", my_data)
    info = my_player.get_matches_played()
    assert info == 1
