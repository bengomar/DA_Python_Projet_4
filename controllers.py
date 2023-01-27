from modeles import Tournament
from views import TournamentView


class MainControllers:
    def run(self):
        name, location = TournamentView().get_tournament_data()
        current_tournament = Tournament(name, location)
        print(current_tournament.name, current_tournament.location)


MainControllers().run()
