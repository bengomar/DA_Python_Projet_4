import time

from termcolor import colored
from tinydb import where

from controllers.tournament import TournamentController
from modeles import Player
from persistance import DatabasesTinydb
from views.common import Usefull
from views.player import PlayerView


class PlayerController:
    def __init__(self):
        self.view = PlayerView()
        self.usefull = Usefull()
        self.player = Player
        self.database = DatabasesTinydb()
        self.form = "{0:9}{1:12}{2:10}{3:10}"

    def display_menu_players(self):
        """Menu Joueurs"""
        choice = self.view.player_menu()

        if choice == "1":
            # Ajouter un joueur
            self.create_new_player()
            self.usefull.wait()
            self.display_menu_players()
        elif choice == "2":
            # Supprimer un joueur
            if not self.database.players:
                print('La table "players" est vide !')
                self.usefull.wait()
            else:
                self.usefull.clear()
                self.view.print_player_list()
                self.players_list_sorted()
                print("")
                self.delete_player()
                self.usefull.wait()
            self.display_menu_players()
        elif choice == "3":
            # Lister les joueurs
            if not self.database.players:
                print('La table "players" est vide !')
                self.usefull.wait()
            else:
                self.view.print_player_list()
                self.players_list_sorted()
                self.usefull.wait()
            self.display_menu_players()
        elif choice == "4":
            # Retour
            return

        else:
            print("Saisie invalide, veuillez réessayer")
            time.sleep(0.4)
            self.display_menu_players()

    def players_list_sorted(self):
        """Liste des joueurs par ordre alphabétique"""
        player_list_alpha = []

        for player in self.database.players:
            ident = player.get("ident")
            surname = player.get("surname")
            firstname = player.get("firstname")
            date_of_birth = player.get("date_of_birth")

            player_list_alpha.append(
                [surname, firstname, ident, date_of_birth]
            )

        for alpha in sorted(player_list_alpha):
            print(self.form.format(alpha[2], alpha[0], alpha[1], alpha[3]))

    def create_new_player(self):
        """Ajout d'un joueur dans la table Tinydb.players"""
        index, ident, surname, firstname, date_of_birth =\
            self.view.get_player_data()
        current_player = Player(index,
                                ident,
                                surname,
                                firstname,
                                date_of_birth)
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
        message = f"Le joueur {current_player.firstname}" \
                  f" {current_player.surname}" \
                  f" {current_player.ident} a été créé."
        print(colored(message, "blue", attrs=["bold"]))
        print("")

    def delete_player(self):
        """Supprime un joueur de la table players"""
        ident = input("Saisir un identifiant: ")

        get_info_player = self.database.players.search(
            where("ident") == ident
            )
        delete_player_id = self.database.players.remove(
            where("ident") == ident
            )
        if not delete_player_id:
            print(colored(f"{ident} n'existe pas !", "red", attrs=["bold"]))
            print("")
        else:
            print(
                colored(
                    f"Le joueur {get_info_player[0]['firstname']}"
                    f" {get_info_player[0]['surname']}"
                    f" ({ident}) a été supprimé",
                    "blue",
                    attrs=["bold"],
                )
            )
            print("")
