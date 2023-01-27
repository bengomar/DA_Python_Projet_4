class TournamentView:
    def get_tournament_data(self):
        name = input("Nom du tournoi: ")
        location = input("Lieu du tournoi: ")
        return [name, location]
