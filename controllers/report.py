from pprint import pprint
from tinydb import where

from controllers.player import PlayerController
from views.common import Usefull
from views.player import PlayerView
from views.report import ReportsView
from persistance import DatabasesTinydb
from termcolor import colored


class ReportController:
    def __init__(self):
        self.player_controller = PlayerController()
        self.database = DatabasesTinydb()
        self.usefull = Usefull()
        self.form = "{0:9}{1:12}{2:10}{3:10}"
        self.tournament_name = ""

    def menu_reports(self):
        """Menu Rapports"""
        choice = ReportsView().reports_infos_menu()

        if choice == "1":
            # Liste des joueurs par ordre alphabétique
            PlayerView().print_player_list()
            self.player_controller.players_list_sorted()
            self.usefull.wait()
            self.menu_reports()
        elif choice == "2":
            # Liste des tournois
            self.database.tournaments_list_formated()
            self.usefull.wait()
            self.menu_reports()
        elif choice == "3":
            #  Classement des joueurs d'un tournoi par score
            self.get_tournament_players()
            self.usefull.wait()
            self.menu_reports()
        elif choice == "4":
            # Résultat des matchs de chaque tour d'un tournoi
            print("Résultat des matchs de chaque tour d'un tournoi")
            self.get_tournament_matches_by_round()
            self.usefull.wait()
            self.menu_reports()
        elif choice == "5":
            # Retour
            return
        else:
            print("Saisie invalide, veuillez réessayer")
            Usefull.wait()
            self.menu_reports()

    def get_tournaments_tournament(self):
        """Récupère les données d'un tournoi en utilisant le nom de tournoi"""
        indice = 1
        tournaments_list = []

        if not self.database.tournaments:
            print("Il n'y a actuellement aucun tournoi d'enregistré !!!")
            Usefull.wait()
            self.menu_reports()
        else:
            print(colored("Tournois existants", "blue", attrs=["bold"]))
            for tournament in self.database.tournaments:
                tournament_name = tournament.get('name')
                print(f"{indice}. {tournament_name}")
                tournaments_list.append(tournament_name)
                # for key in tournament:
                #     print(f"{indice}. {key}")
                #     tournaments_list.append(key)
                indice += 1
            print("")
            choice = input("Sélectionnez un tournoi ---> ")
            self.tournament_name = tournaments_list[int(choice) - 1]
            print("")

            return self.tournament_name

    def get_tournament_players(self):
        """Liste des joueurs d'un tournoi donné"""

        players_list = []
        self.get_tournaments_tournament()
        ask_tournament = self.database.tournaments.search(where('name') == self.tournament_name)
        players = ask_tournament[0]['players']

        for player in players:
            players_list.append([player['ident'], player['surname'], player['firstname'], player['score']])
        score_sorted_players = sorted(players_list, key=lambda x: x[3], reverse=True)
        print(colored(f"Classement des joueurs du tournoi \"{self.tournament_name}\" par score:", 'blue', attrs=['bold']))
        print("")
        for gamer in score_sorted_players:
            print(self.form.format(gamer[0], gamer[1], gamer[2], gamer[3]))

    def get_tournament_matches_by_round(self):
        """Liste des matchs de chaque tour d'un tournoi donné"""
        form = "{0:10}{1:10}{2:6}{3:8}{4:10}{5:10}{6:0}"
        self.get_tournaments_tournament()
        print(colored(f"Tournoi \"{self.tournament_name}\"", 'blue', attrs=['bold']))

        ask_tournament = self.database.tournaments.search(where('name') == self.tournament_name)

        matches_data = ask_tournament[0]['round_list']

        for matches in matches_data:
            print(colored(f"{matches['name']}", 'blue', attrs=['bold']))
            match_players = matches['matches']
            for match in match_players:
                #print(match['players'])
                player_1 = match['players'][0][0]
                player_2 = match['players'][1][0]
                score_p1 = match['players'][0][1]
                score_p2 = match['players'][1][1]
                print(
                    form.format
                    (
                        player_1['surname'], player_1['firstname'], f"({score_p1})",
                        " -vs- ",
                        player_2['surname'], player_2['firstname'], f"({score_p2})"
                    )
                )
            print("")


