from datetime import datetime
from views import MainView, TournamentView, PlayerView
from modeles import Tournament, Player, SearchPlayerIdent
from databases import Tinydb
import time
import sys

class MainControllers:
    def main_menu_choice(self):
        choice = MainView().main_menu()
        if choice == "1":
            MainControllers().create_tournament_action()
        elif choice == "2":
            MainControllers().menu_players()
        elif choice == "3":
            print("-----> 3.Menu Joueurs ")
            MainControllers().main_menu_choice()
        elif choice == "4":
            print("-----> 4.Menu Joueurs ")
            MainControllers().main_menu_choice()

        elif choice == "5":
            sys.exit()
        else:
            print("Invalid option, please try again")
            time.sleep(1)
            MainControllers().main_menu_choice()

    def new_tournament(self):
        (
            name,
            location,
            date_start,
            date_end,
            nb_round,
        ) = TournamentView().get_tournament_data()
        current_tournament = Tournament(name, location, date_start, date_end, nb_round)
        Tinydb().add_tournament(
            current_tournament.name,
            current_tournament.location,
            datetime.strptime(current_tournament.date_start, "%d%m%Y").strftime(
                "%d%m%Y"
            ),
            current_tournament.date_end,
            current_tournament.nb_round,
        )
        print(f'Le tournoi "{current_tournament.name}" de {current_tournament.location} comprend {current_tournament.nb_round} rounds')


    def menu_players(self):
        choice = PlayerView().player_menu()
        if choice == "1":
            Tinydb().players_list()
            MainControllers().menu_players()
        elif choice == "2":
            MainControllers().new_player()
        elif choice == "3":
            MainControllers().delete_player()
        elif choice == "4":
            MainControllers().main_menu_choice()
        else:
            print("Invalid option, please try again")
            time.sleep(1)
            MainControllers().menu_players()

    def new_player(self):
        ident, surname, firstname, date_of_birth = PlayerView().get_player_data()
        current_player = Player(ident, surname, firstname, date_of_birth)
        Tinydb().add_player(
            current_player.ident,
            current_player.surname,
            current_player.firstname,
            current_player.date_of_birth,
        )
        Tinydb().check_table_players()
        MainControllers().menu_players()

    def delete_player(self):
        MainControllers().player_to_delete()
        ident = PlayerView().search_player_id_to_delete()
        current_search_player = SearchPlayerIdent(ident)
        Tinydb().del_player(current_search_player.ident)
        time.sleep(1)
        MainControllers().menu_players()

    def player_to_delete(self):
        Tinydb().players_list()


    def create_tournament_action(self):

        # créer une instance de tournoi
        MainControllers().new_tournament()

        # Ajouter des joueurs au tournoi
        Tinydb().players_list()

        # Génération des paires de joueurs
            #Liste de paires de joueurs (aléatoire)
        # créer le 1er tour
        # créer les matchs avec les paires de joueurs générés pour le 1er tour
        # rentrer les résultats du 1er tour
            #les scores seront enregistés dans l'instances de tournoi dans un dico {ident:score}


        # créer le 2ème tour
        # créer les matchs en fonction des points des joueurs.
        # 1- Génération des paires --> une liste de listes
        # 2- créer des instances de matchs
        # rentrer les résultats du 2ème tour

#start programme
MainControllers().main_menu_choice()