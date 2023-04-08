from views.player import PlayerView
from persistance import DatabasesTinydb
from tinydb import where
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
        self.database = DatabasesTinydb()

    def display_menu_players(self):
        """Menu Joueurs"""
        choice = self.view.player_menu()
        if choice == "1":
            # Lister les joueurs
            self.players_list_sorted()
            self.usefull.wait()
            self.display_menu_players()
        elif choice == "2":
            # Ajouter un joueur
            self.create_new_player()
            self.usefull.wait()
            self.display_menu_players()
        elif choice == "3":
            # Supprimer un joueur
            self.delete_player()
            self.usefull.wait()
            self.display_menu_players()
        elif choice == "4":
            # Retour
            return

        else:
            print("Saisie invalide, veuillez réessayer")
            self.display_menu_players()

    def players_list_sorted(self):
        """Liste des joueurs par ordre alphabétique"""

        player_list_alpha = []
        for player in self.database.players:
            ident = player.get("ident")
            surname = player.get("surname")
            firstname = player.get("firstname")
            date_of_birth = player.get("date_of_birth")

            player_list_alpha.append([surname, firstname, ident, date_of_birth])
            # print(f"     {ident} {surname},{firstname}")

        for alpha in sorted(player_list_alpha):
            print(f"{alpha[2]} {alpha[0]} {alpha[1]} {alpha[3]}")

    def create_new_player(self):
        """Ajout d'un joueur dans la table Tinydb.players"""
        index, ident, surname, firstname, date_of_birth = self.view.get_player_data()
        current_player = Player(index, ident, surname, firstname, date_of_birth)
        print(current_player)

        DatabasesTinydb.players.insert(
            {
                "ident": current_player.ident,
                "surname": current_player.surname,
                "firstname": current_player.firstname,
                "date_of_birth": current_player.date_of_birth,
            }
        )
        print("")
        print(f"Le joueur {current_player.firstname} {current_player.surname} ({current_player.ident}) a été créé")
        print("")

    def delete_player(self):
        """Supprime un joueur de la table players"""
        ident = input("Saisir l'identifiant du joueur: ")

        get_info_player = Player(self.database.players.search(where("ident") == ident))
        delete_player_id = self.database.players.remove(where("ident") == ident)
        if not delete_player_id:
            print(f"{ident} n'existe pas !")
            print("")
        else:
            print(f"{get_info_player} {get_info_player} ({ident}) a été supprimé")
            print("")


