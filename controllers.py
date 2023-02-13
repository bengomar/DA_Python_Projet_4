from datetime import datetime
from views import MainView, TournamentView, PlayerView, ReportsView
from modeles import Tournament, Player, SearchPlayerIdent
from databases import Tinydb
from samba.common import raw_input
import time
import sys
import random

class Waiting:
    def wait():
        """Permet d'obtenir une pause du programme """
        print("")
        pause = raw_input("Appuyer sur ENTREE pour continuer ...")
        pause
        print("")
class MainControllers:
    list_of_player_of_tournament = []
    current_tournament = []
    matchs_list = []
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
            print("-----> 4.Menu Résultats ")
            MainControllers().main_menu_choice()
        elif choice == "4":
            # Rapports
            MainControllers().menu_reports()
            '''
            print("Liste des tournois (tournaments)")
            
            print("")
            print("Liste des joueurs participant au tournoi en cours (competitor)")
            
            print("")
            '''
            #MainControllers().main_menu_choice()
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
        self.current_tournament = Tournament(name, location, date_start, date_end, nb_round)
        Tinydb().add_tournament(
            self.current_tournament.name,
            self.current_tournament.location,
            datetime.strptime(self.current_tournament.date_start, "%d%m%Y").strftime(
                "%d%m%Y"
            ),
            self.current_tournament.date_end,
            self.current_tournament.nb_round,
        )

        print("")
        print(f'Le tournoi d\'échec "{self.current_tournament.name}" qui se déroule à {self.current_tournament.location} comprend {self.current_tournament.nb_round} rounds')

    def menu_players(self):
        """Menu Joueurs"""
        choice = PlayerView().player_menu()
        if choice == "1":
            # Lister les joueurs
            PlayerView().print_player_list()
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
        """ Affichage des joueurs disponibles avec numérotation en préfixe"""
        list_player_tab = Tinydb().players_list()
        npa = 0
        for player in list_player_tab:
            npa += 1
            print(f"  {npa}. {player[0]} {player[1]} {player[2]}")

    def add_players_tournament(self):
        """ Ajout de joueurs disponibles dans le tournoi en cours"""
        list_player_tab = Tinydb().players_list()
        nb_player = len(list_player_tab)
        Tinydb().competitor.truncate()
        #print(list_player_tab)
        while nb_player > 0:
            num_player_list = PlayerView().add_players_to_tournament()
            self.list_of_player_of_tournament.append(list_player_tab[int(num_player_list) - 1])
            #print(f"{self.list_of_player_of_tournament=}")
            del list_player_tab[int(num_player_list) - 1]
            print("")
            print(f"Liste des joueurs participants au tournoi (récupérer nom tournoi en cours):")
            for play in self.list_of_player_of_tournament:
                print(f"  {play[0]} {play[1]} {play[2]}")
            print("")
            Tinydb().add_player_tournament(
                play[0],
                play[1],
                play[2],
            )
            if len(list_player_tab) == 0:
                pass
            else:
                print("Joueurs disponibles:")
            npa = 0
            for player_show in list_player_tab:
                npa += 1

                print(f"  {npa}. {player_show[0]} {player_show[1]} {player_show[2]}")
            nb_player -= 1

    def generate_players_pairs(self):
        """ Génération de pairs de joueurs (match) depuis la liste des joueurs selectionnés pour le tournoi """
        list_p_o = []
        for player in Tinydb.competitor:
            print(player.get('ident'), player.get('surname'), player.get('firstname'))
            list_p_o.append((player.get('ident'), player.get('surname'), player.get('firstname')))
        print("")
        print("                **********************")
        print("                * Match du 1er tour: *")
        print("                **********************")
        nb_match = len(list_p_o)//2
        while nb_match > 0:
            #player = random.choice(list_p_o)
            #opponent = random.choice(list_p_o)

            player = list_p_o[0]
            opponent = list_p_o[1]
            match = [[player, 0], [opponent, 0]]
            player = match[0][0]
            opponent = match[1][0]
            print(f"  {player[0]} {player[1]} {player[2]} --vs-- {opponent[0]} {opponent[1]} {opponent[2]}")
            list_p_o.remove(player)
            list_p_o.remove(opponent)

            '''
            while player == opponent:
                player = random.choice(list_p_o)
                opponent = random.choice(list_p_o)
            else:
                match = [[player, 0], [opponent, 0]]
                list_p_o.remove(player)
                list_p_o.remove(opponent)
                player = match[0][0]
                opponent = match[1][0]
                print(f"    {player[0]} {player[1]} {player[2]} --vs-- {opponent[0]} {opponent[1]} {opponent[2]}")
                self.matchs_list.append([[player, 0], [opponent, 0]])
            '''
            nb_match -= 1
    def match_score_player(self):
        dico_score_ident = {}
        list_player_tab = self.list_of_player_of_tournament
        nb_player = len(list_player_tab)
        while nb_player > 0:
            print("")
            print("Saisir les scores des matchs aux joueurs (Gagné = 1, Perdu = 0, Nul = 0.5)")
            npa = 0
            for play in self.list_of_player_of_tournament:
                npa += 1
                player = f"  {npa}. {play[0]} {play[1]} {play[2]}"
                print(player)
                #self.list_of_player_of_tournament.remove()

                #print(f"  {npa}.   {play[0]} {play[1]} {play[2]}")

            choice = TournamentView().get_score_match()
            player_scored = self.list_of_player_of_tournament[int(choice)-1]

            #print(f"{choice=}")
            '''
            for play in self.matchs_list:
                print(play[0][1])
                print(play[1][1])
            '''

            #print(f"{nb_player=}")



            if choice:
                ident = list_player_tab[int(choice) - 1][0]
                print(list_player_tab[int(choice) - 1])
            score_in = PlayerView().get_score_player()
            print(score_in)
            dico_score_ident[ident] = score_in

            print(dico_score_ident)
            self.list_of_player_of_tournament.remove(player_scored)
        nb_player -= 1

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
        MainControllers().generate_players_pairs()

        # rentrer les résultats du 1er tour
            #les scores seront enregistés dans l'instances de tournoi dans un dico {ident:score}
        MainControllers().match_score_player()

        # créer le 2ème tour
        # créer les matchs en fonction des points des joueurs.
        # 1- Génération des paires --> une liste de listes
        # 2- créer des instances de matchs
        # rentrer les résultats du 2ème tour

    def testing(self):
        pass

    def menu_reports(self):
        """Menu Rapports"""
        choice = ReportsView().reports_infos_menu()

        if choice == "1":
            # Liste des joueurs par ordre alphabétique
            Tinydb().players_list_ident()
            Waiting.wait()
            MainControllers().menu_reports()
        elif choice == "2":
            # Liste des tournois
            Tinydb().tournaments_list_formated()
            Waiting.wait()
            MainControllers().menu_reports()
        elif choice == "3":
            # Données d'un tournoi
            print("nom et dates d’un tournoi donné")
            Waiting.wait()
            MainControllers().menu_reports()
        elif choice == "4":
            # Liste des joueurs du dernier tournoi par ordre alphabétique
            Tinydb().check_table_competitor()
            Waiting.wait()
            MainControllers().menu_reports()
        elif choice == "5":
            # Liste des tours et matchs du dernier tournoi
            print("Liste des tours et matchs des tours du dernier tournoi")
            Waiting.wait()
            MainControllers().menu_reports()
        elif choice == "6":
            # Retour
            MainControllers().main_menu_choice()
        else:
            print("Invalid option, please try again")
            Waiting.wait()
            MainControllers().menu_reports()

#start programme
MainControllers().main_menu_choice()

#MainControllers().match_score_player()
# Lister la table
#Tinydb().check_table_tournaments()
#print("")
#Tinydb().check_table_players()
#print("")
#Tinydb().check_table_competitor()

# Vider une table
#Tinydb().tournaments.truncate()
#Tinydb().players.truncate()
#Tinydb().competitor.truncate()

