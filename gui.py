import sys
from PySide2.QtWidgets import QApplication, QMainWindow
import ui_search_window
import ui_stats_window
from data_processor import Dataset, Player, Tournament


class SearchWindow(QMainWindow):
    def __init__(self, dataset):
        super().__init__()
        self._dataset = dataset
        self._player_1_name = None
        self._player_2_name = None
        self._tourney_name = None
        self._stats_window = None
        self.ui = ui_search_window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.view_widgets_setup()
        self.next_button_control()

    def set_stats_window(self, stats_window):
        self._stats_window = stats_window

    def view_widgets_setup(self):
        self.ui.lineEdit.textChanged.connect(lambda: self.populate_player_list(
            self.ui.lineEdit, self.ui.listWidget))
        self.ui.lineEdit_2.textChanged.connect(
            lambda: self.populate_player_list(
                self.ui.lineEdit_2, self.ui.listWidget_2))
        self.ui.lineEdit_3.textChanged.connect(
            lambda: self.populate_tournament_list(
                self.ui.lineEdit_3, self.ui.listWidget_3))
        self.ui.listWidget.itemClicked.connect(self.set_player_1_parameters)
        self.ui.listWidget_2.itemClicked.connect(self.set_player_2_parameters)
        self.ui.listWidget_3.itemClicked.connect(self.set_tourney_parameters)
        self.ui.NextButton.clicked.connect(
            lambda: self.change_window(
                self._player_1_name, self._player_2_name, self._tourney_name))

    def next_button_control(self):
        if self._player_1_name and self._player_2_name and self._tourney_name:
            self.ui.NextButton.setEnabled(True)

    def populate_player_list(self, l_edit, l_widget):
        player_name = l_edit.text()
        player_list = self._dataset.get_players_with_name(player_name)
        l_widget.clear()
        for player in player_list:
            l_widget.addItem(player)

    def populate_tournament_list(self, l_edit, l_widget):
        dataset = self._dataset
        tournament_name = l_edit.text()
        tournament_list = dataset.get_tournaments_with_name(tournament_name)
        l_widget.clear()
        for tournament in tournament_list:
            l_widget.addItem(tournament)

    def set_player_1_parameters(self, item):
        self._player_1_name = item.text()
        self.next_button_control()

    def set_player_2_parameters(self, item):
        self._player_2_name = item.text()
        self.next_button_control()

    def set_tourney_parameters(self, item):
        self._tourney_name = item.text()
        self.next_button_control()

    def change_window(self, player_1, player_2, tourney):
        self._stats_window.create_players(player_1, player_2)
        self._stats_window.create_tournament(tourney)
        self.close()
        self._stats_window.set_search_window(self)
        self._stats_window.show()


class StatsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui_stats_window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionOd_poczatku.triggered.connect(self.restart_app)

    def create_players(self, name_1, name_2):
        self._player_1 = Player(name_1, my_data)
        self._player_2 = Player(name_2, my_data)
        self._player_1.set_other_player(self._player_2)
        self._player_2.set_other_player(self._player_1)

    def create_tournament(self, name):
        self._tournament = Tournament(name, my_data)
        self._player_1.set_tournament(self._tournament)
        self._player_2.set_tournament(self._tournament)
        self.show_data()

    def show_data(self):
        player_1 = self._player_1
        player_2 = self._player_2
        self.ui.player_1_name.setText(player_1.name())
        self.ui.player_1_nationality.setText(player_1.nationality())
        self.ui.player_1_best_finish.setText(player_1.best_finish())
        self.ui.player_1_best_finish_grand_slam.setText(
            player_1.best_finish_grand_slam())
        self.ui.player_1_first_match.setText(str(player_1.first_match()))
        self.ui.player_1_matches_played.setText(str(player_1.matches_played()))
        self.ui.player_1_matches_won.setText(str(player_1.matches_won()))
        self.ui.player_1_same_surface_played.setText(
            str(player_1.same_surface_played()))
        self.ui.player_1_same_surface_won.setText(
            str(player_1.same_surface_won()))
        self.ui.player_1_titles.setText(str(player_1.titles()))
        self.ui.player_1_best_finish_tournament.setText(
            player_1.best_finish_tournament())
        self.ui.player_2_name.setText(player_2.name())
        self.ui.player_2_nationality.setText(player_2.nationality())
        self.ui.player_2_best_finish.setText(player_2.best_finish())
        self.ui.player_2_best_finish_grand_slam.setText(
            player_2.best_finish_grand_slam())
        self.ui.player_2_first_match.setText(str(player_2.first_match()))
        self.ui.player_2_matches_played.setText(str(player_2.matches_played()))
        self.ui.player_2_matches_won.setText(str(player_2.matches_won()))
        self.ui.player_2_same_surface_played.setText(
            str(player_2.same_surface_played()))
        self.ui.player_2_same_surface_won.setText(
            str(player_2.same_surface_won()))
        self.ui.player_2_titles.setText(str(player_2.titles()))
        self.ui.player_2_best_finish_tournament.setText(
            player_2.best_finish_tournament())

    def set_search_window(self, search_window):
        self._search_window = search_window

    def restart_app(self):
        self.close()
        self._search_window.show()


if __name__ == '__main__':
    my_data = Dataset(2015, "data/atp_matches_")
    app = QApplication(sys.argv)
    search_window = SearchWindow(my_data)
    stats_window = StatsWindow()
    search_window.set_stats_window(stats_window)
    search_window.show()
    sys.exit(app.exec_())
