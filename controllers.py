from datetime import datetime
from views import MainView, TournamentView, PlayerView
from modeles import Tournament, Player, SearchPlayerIdent
from databases import Tinydb
from samba.common import raw_input
import time
import sys

class Waiting:
    def wait():
        """Permet d'obtenir une pause du programme """
        print("")
        pause = raw_input("Appuyer sur ENTREE pour continuer ...")
        pause
        print("")
class MainControllers:
    def main_menu_choice(self):
        """Menu principal"""
        choice = MainView().main_menu()
        if choice == "1":
            # Lancer un tournoi
            MainControllers().create_tournament_action()
        elif choice == "2":
            # Menu joueurs
            MainControllers().menu_players()
        elif choice == "3":
            # Résultats
            print("-----> 3.Menu Résultats ")
            MainControllers().main_menu_choice()
        elif choice == "4":
            # Rapports
            print("-----> 4.Menu Rapports ")
            MainControllers().main_menu_choice()
        elif choice == "5":
            # Sortir
            sys.exit()
        else:
            print("Invalid option, please try again")
            Waiting.wait()
            MainControllers().main_menu_choice()

    def new_tournament(self):
        """Création d'un tournoi"""
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
        print("")
        print(f'Le tournoi d\'échec "{current_tournament.name}" qui se déroule à {current_tournament.location} comprend {current_tournament.nb_round} rounds')


    def menu_players(self):
        """Menu Joueurs"""
        choice = PlayerView().player_menu()
        if choice == "1":
            # Lister les joueurs
            Tinydb().players_list_ident()
            Waiting.wait()
            MainControllers().menu_players()
        elif choice == "2":
            # Ajouter un joueur
            MainControllers().new_player()
            Waiting.wait()
            MainControllers().menu_players()
        elif choice == "3":
            # Supprimer un joueur
            MainControllers().delete_player()
        elif choice == "4":
            # Retour
            MainControllers().main_menu_choice()
        else:
            print("Invalid option, please try again")
            Waiting.wait()
            MainControllers().menu_players()

    def new_player(self):
        """Ajout d'un joueur dans la table Tinydb.players"""
        ident, surname, firstname, date_of_birth = PlayerView().get_player_data()
        current_player = Player(ident, surname, firstname, date_of_birth)
        Tinydb().add_player(
            current_player.ident,
            current_player.surname,
            current_player.firstname,
            current_player.date_of_birth,
        )
        print("")
        print(f"Le joueur {current_player.firstname} {current_player.surname} ({current_player.ident}) a été créé")
        print("")
        #Tinydb().check_table_players()
        MainControllers().menu_players()

    def delete_player(self):
        """Suppression d'un joueur dans la table Tinydb.players"""
        MainControllers().player_to_delete()
        ident = PlayerView().search_player_id_to_delete()
        current_search_player = SearchPlayerIdent(ident)
        Tinydb().del_player(current_search_player.ident)
        #Waiting.wait()
        MainControllers().menu_players()

    def player_to_delete(self):
        """Affichage personnalisé des joueurs depuis la table Tinydb.players"""
        PlayerView().print_player_list()
        Tinydb().players_list_ident()

    def print_players_by_num(self):

        list_player_tab = Tinydb().players_list()
        npa = 0
        for player in list_player_tab:
            npa += 1
            print(f"  {npa}. {player[0]} {player[1]} {player[2]}")

    def add_players_tournament(self):
        list_player_tab = Tinydb().players_list()
        nb_player = len(list_player_tab)

        list_of_player_of_tournament = []
        while nb_player > 0:
            num_player_list = PlayerView().add_players_to_tournament()
            list_of_player_of_tournament.append(list_player_tab[int(num_player_list) - 1])
            #print(f"{list_player_tab=}")
            #print("")
            del list_player_tab[int(num_player_list) - 1]
            #print(f"{list_of_player_of_tournament=}")
            #print("")
            #print(f"{list_player_tab=}")
            print("")
            npa = 0
            for player_show in list_player_tab:
                npa += 1
                print(f"  {npa}. {player_show[0]} {player_show[1]} {player_show[2]}")
            nb_player -= 1

        print("Liste des joueurs participant au tournoi:")
        for play in list_of_player_of_tournament:
            print(f"  {play[0]} {play[1]} {play[2]}")

    def create_tournament_action(self):

        # créer une instance de tournoi
        MainControllers().new_tournament()

        # Ajouter des joueurs au tournoi
        PlayerView().print_player_list()
        MainControllers().print_players_by_num()
        MainControllers().add_players_tournament()


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




# Lister la table
#Tinydb().check_table_tournaments()
#Tinydb().check_table_players()

# Vider une table
#Tinydb().tournaments.truncate()
#Tinydb().players.truncate()
