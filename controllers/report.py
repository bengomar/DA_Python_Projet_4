from termcolor import colored
from tinydb import where

from controllers.player import PlayerController
from persistance import DatabasesTinydb
from views.common import Usefull
from views.player import PlayerView
from views.report import ReportsView


class ReportController:
    def __init__(self):
        self.player_controller = PlayerController()
        self.database = DatabasesTinydb()
        self.usefull = Usefull()
        self.view = ReportsView()
        self.form = "{0:9}{1:12}{2:10}{3:10}"
        self.tournament_name = ""

    def menu_reports(self):
        """Menu Rapports"""
        in_progress = False
        while in_progress is False:
            choice = self.view.reports_infos_menu()
            if choice == "1":
                # Liste des joueurs par ordre alphabétique
                if not self.database.players:
                    print(colored('La table "players" est vide !',
                                  'red',
                                  attrs=['bold']))
                    self.usefull.wait()
                    # self.menu_reports()
                else:
                    PlayerView().print_player_list()
                    self.player_controller.players_list_sorted()
                    self.usefull.wait()
            elif choice == "2":
                # Liste des tournois
                if not self.database.tournaments:
                    print(colored("Il n'y a actuellement aucun"
                                  " tournoi d'enregistré !!!",
                                  'red',
                                  attrs=['bold']))
                    self.usefull.wait()
                else:
                    self.database.tournaments_list_formated()
                    self.usefull.wait()
            elif choice == "3":
                #  Classement des joueurs d'un tournoi par score
                if not self.database.tournaments:
                    print(colored("Il n'y a actuellement aucun"
                                  " tournoi d'enregistré !!!",
                                  'red',
                                  attrs=['bold']))
                    self.usefull.wait()
                else:
                    self.get_tournament_players()
                    self.usefull.wait()
            elif choice == "4":
                # Résultat des matchs de chaque tour d'un tournoi
                if not self.database.tournaments:
                    print(colored("Il n'y a actuellement aucun"
                                  " tournoi d'enregistré !!!",
                                  'red',
                                  attrs=['bold']))
                    self.usefull.wait()
                    # self.menu_reports()
                else:
                    self.get_tournaments_tournament()
                    self.get_tournament_matches_by_round(self.tournament_name)
                    self.usefull.wait()
            elif choice == "5":
                # Retour
                in_progress = True
            else:
                print("Saisie invalide, veuillez réessayer")
                self.usefull.wait()

    def get_tournaments_tournament(self):
        """Récupère les données d'un tournoi en utilisant le nom de tournoi"""
        indice = 1
        tournaments_list = []

        print(colored("Tournois existants",
                      "blue",
                      attrs=["bold"])
              )
        for tournament in self.database.tournaments:
            tournament_name = tournament.get("name")
            print(f"{indice}. {tournament_name}")
            tournaments_list.append(tournament_name)
            indice += 1
        print("")
        nb_tournament = len(tournaments_list)
        choose_tournament = False
        while choose_tournament is False:
            choice = input("Sélectionnez un tournoi ---> ")
            try:
                if (int(choice) > 0) and (int(choice) <= nb_tournament):
                    self.tournament_name = tournaments_list[int(choice) - 1]
                    choose_tournament = True
                else:
                    text = "!!! Entrée non valide, réessayez !!!"
                    print(colored(text, "red", attrs=["bold"]))
                    print("")

            except ValueError:
                text = "!!! Entrée non valide, réessayez !!!"
                print(colored(text, "red", attrs=["bold"]))
                print("")
        print("")
        return self.tournament_name

    def get_tournament_players(self):
        """Liste des joueurs d'un tournoi donné"""

        players_list = []
        self.get_tournaments_tournament()
        ask_tournament = self.database.tournaments.search(
            where("name") == self.tournament_name
        )
        players = ask_tournament[0]["players"]

        for player in players:
            players_list.append(
                [
                    player["ident"],
                    player["surname"],
                    player["firstname"],
                    player["score"],
                ]
            )
        score_sorted_players = sorted(players_list,
                                      key=lambda x: x[3],
                                      reverse=True
                                      )
        print(
            colored(
                f'Classement des joueurs du tournoi "'
                f'{self.tournament_name}" par score:',
                "blue",
                attrs=["bold"],
            )
        )
        print("")
        for gamer in score_sorted_players:
            print(self.form.format(gamer[0], gamer[1], gamer[2], gamer[3]))

    def get_tournament_matches_by_round(self, tournament_name):
        """Liste des matchs de chaque tour d'un tournoi donné"""
        self.tournament_name = tournament_name
        form = "{0:10}{1:10}{2:6}{3:8}{4:10}{5:10}{6:0}"

        print(colored("  ***************************************************",
                      "blue",
                      attrs=["bold"]))
        print(colored("  * Résultat des matchs de chaque tour d'un tournoi *",
                      "blue",
                      attrs=["bold"]))
        print(colored("  ***************************************************",
                      "blue",
                      attrs=["bold"]))

        print(colored(f'Tournoi "{self.tournament_name}"',
                      "blue",
                      attrs=["bold"])
              )
        ask_tournament = self.database.tournaments.search(
            where("name") == self.tournament_name
        )

        matches_data = ask_tournament[0]["round_list"]
        print("")

        for matches in matches_data:
            print(colored(f"{matches['name']}", "blue", attrs=["bold"]))
            print("-" * 60)
            match_players = matches["matches"]
            for match in match_players:
                player_1 = match["players"][0][0]
                player_2 = match["players"][1][0]
                score_p1 = match["players"][0][1]
                score_p2 = match["players"][1][1]
                print(
                    form.format(
                        player_1["surname"],
                        player_1["firstname"],
                        f"({score_p1})",
                        " -vs- ",
                        player_2["surname"],
                        player_2["firstname"],
                        f"({score_p2})",
                    )
                )
            print("-" * 60)
            print("")
