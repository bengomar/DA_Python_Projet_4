from datetime import datetime
from modeles import Player, Tournament, Choice, SearchPlayerIdent
from views import PlayerView, TournamentView, MainView
from persistance import Tinydb
import sys
import time

class MainControllers:
    def new_tournament(self):
        name, location, date_start, date_end, nb_round = TournamentView().get_tournament_data()
        current_tournament = Tournament(name, location, date_start, date_end, nb_round)
        Tinydb().add_tournament(current_tournament.name, current_tournament.location,
                                datetime.strptime(current_tournament.date_start, "%d%m%Y").strftime("%d%m%Y"),
                                current_tournament.date_end, current_tournament.nb_round)
        Tinydb.check_table_tournaments()
        MainControllers().menu_tournaments()
    def new_player(self):
        ident, surname, firstname, date_of_birth, score = PlayerView().get_player_data()
        current_player = Player(ident, surname, firstname, date_of_birth, score)
        Tinydb().add_player(current_player.ident, current_player.surname, current_player.firstname,
                            current_player.date_of_birth, current_player.score)
        Tinydb.check_table_players()
        MainControllers().menu_players()

    def delete_player(self):
        ident = PlayerView().menu_delete_player()
        current_search_player = SearchPlayerIdent(ident)
        Tinydb().del_player(current_search_player.ident)
        time.sleep(1)
        MainControllers().menu_players()
    def add_score_player(self):
        print("saisir le score du joueur")
        MainControllers().menu_players()

    def main_menu_choice(self):
        choice = MainView().main_menu()
        current_choice = Choice(choice)
        if choice == '1':
            MainControllers().menu_players()
        elif choice == '2':
            MainControllers().menu_tournaments()
        elif choice == '3':
            print(f"{choice=} --> Menu Resultats")
            MainControllers().main_menu_choice()
        elif choice == '4':
            Tinydb.check_table_players()
            MainControllers().main_menu_choice()

        elif choice == '5':
            sys.exit()
        else:
            print("Invalid option, please try again")
            time.sleep(1)
            MainControllers().choice()

    def menu_players(self):
        choice = PlayerView().player_menu()
        current_choice = Choice(choice)
        if choice == '1':
            MainControllers().new_player()
        elif choice == '2':
            MainControllers().delete_player()
        elif choice == '3':
            MainControllers().add_score_player()
        elif choice == '4':
            MainControllers().main_menu_choice()
        else:
            print("Invalid option, please try again")
            time.sleep(1)
            MainControllers().menu_players()

    def menu_tournaments(self):
        choice = TournamentView().tournament_menu()
        current_choice = Choice(choice)
        if choice == '1':
            Tinydb().get_tournament('')
            MainControllers().menu_tournaments()
        elif choice == '2':
            MainControllers().new_tournament()
        elif choice == '3':
            Tinydb().put_tournament_end_date(TournamentView().get_end_date())
        elif choice == '4':
            MainControllers().main_menu_choice()
        else:
            print("Invalid option, please try again")
            time.sleep(1)
            MainControllers().menu_tournaments()

    def create_tournament_action(self):
        Tinydb().get_tournament('')
        # créer une instance de tournoi

        # Ajouter des joueurs au tournoi
        # créer le 1er tour
        # créer les matchs (paires de joueurs) pour le 1er tour
        # rentrer les résultats du 1er tour
        # créer le 2ème tour
        # créer les matchs en fonction des points des joueurs.
        # 1- Génération des paires --> une liste de listes
        # 2- créer des instances de matchs
        # rentrer les résultats du 2ème tour

MainControllers().main_menu_choice()

#MainControllers().delete_player()

# Ajout de données
# MainControllers().new_tournament()
# MainControllers().new_player()
# Tinydb().put_tournament_end_date(12121985)

# Vider une table
# Tinydb.tournaments.truncate()

# Lister la table
# Tinydb.check_table_tournaments()
#Tinydb.check_table_players()

# Mise à jour
# Tinydb.players.update({'date_of_birth': '25071979'}, Tinydb.query.ident == 'AD12345')
# Tinydb.check_table_players()

# Tinydb.tournaments.update({'date_end': '21012023'}, Tinydb.query.location == 'Bamako')
# Tinydb.check_table_tournaments()

# MainControllers().create_tournament_action()