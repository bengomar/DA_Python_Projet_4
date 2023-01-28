class TournamentView:
    def get_tournament_data(self):
        name = input("Nom du tournoi: ")
        location = input("Lieu du tournoi: ")
        return [name, location]

class PlayerView:
    def get_player_data(self):
        surname = input("Nom du joueur: ")
        firstname = input("Prénom du joueur: ")
        date_of_birth = input("Date de naissance du joueur: ")
        return [surname, firstname, date_of_birth]