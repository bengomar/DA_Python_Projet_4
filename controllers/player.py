from views.player import PlayerView
from persistance import DatabasesTinydb
from modeles import Player
from controllers.tournament import TournamentController
from views.common import Usefull
import controllers.main

class PlayerController:

    def __init__(self):
        self.view = PlayerView()
        self.usefull = Usefull()
        self.player = Player
        self.tournament_controller = TournamentController()

    def display_menu_players(self):
        """Menu Joueurs"""
        choice = self.view.player_menu()
        if choice == "1":
            # Lister les joueurs
            self.print_all_players_sorted_by_alphabet()
            self.usefull.wait()
            self.display_menu_players()
        elif choice == "2":
            # Ajouter un joueur
            self.create_new_player()
            self.display_menu_players()
        elif choice == "3":
            # Supprimer un joueur
            self.display_menu_players()
        elif choice == "4":
            # Retour
            return

        else:
            print("Saisie invalide, veuillez réessayer")
            self.display_menu_players()

    def create_new_player(self):
        """Ajout d'un joueur dans la table Tinydb.players"""
        index, ident, surname, firstname, date_of_birth = PlayerView().get_player_data()
        current_player = Player(index, ident, surname, firstname, date_of_birth)
        print(current_player)
        '''
        DatabasesTinydb.players.insert(
            {
                "ident": current_player.ident,
                "surname": current_player.surname,
                "firstname": current_player.firstname,
                "date_of_birth": current_player.date_of_birth,
            }
        )
        print("")
        print(
            f"Le joueur {current_player.firstname} {current_player.surname} ({current_player.ident}) a été créé"
        )
        print("")
        '''

    def print_all_players_sorted_by_alphabet(self):
        """ Liste de tous les joueurs du club """

        print("Liste des joueurs du Club:")
        print("Id      Nom, Prénom")
        for player in self.tournament_controller.players:
            print(player)