from modeles import Tournament, Player
from views import TournamentView, PlayerView


class MainControllers:
    def run(self):
        name, location = TournamentView().get_tournament_data()
        current_tournament = Tournament(name, location)
        print(current_tournament.name, current_tournament.location)

        surname, firstname, date_of_birth = PlayerView().get_player_data()
        current_player = Player(surname, firstname, date_of_birth)
        print(current_player.surname, current_player.firstname, current_player.date_of_birth)

MainControllers().run()
