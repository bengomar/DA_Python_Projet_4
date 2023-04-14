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
            #  Liste des joueurs d'un tournoi par ordre alphabétique
            self.get_tournament_players()
            self.usefull.wait()
            self.menu_reports()
        elif choice == "4":
            # Liste des tours et matchs du dernier tournoi
            print("Liste des tours et matchs du dernier tournoi")
            self.usefull.wait()
            self.menu_reports()
        elif choice == "5":
            # Retour
            return
        else:
            print("Saisie invalide, veuillez réessayer")
            Usefull.wait()
            self.menu_reports()

    def get_tournament_players(self):
        """Liste des joueurs d'un tournoi donné"""
        indice = 1
        tournaments_list = []
        if not self.database.tournaments:
            print("Il n'y a actuellement aucun tournoi d'enregistré !!!")
        else:
            print(colored("Tournois enregistrés", "blue", attrs=["bold"]))
            for tournament in self.database.tournaments:
                for key in tournament:
                    print(f"{indice}. {key}")
                    tournaments_list.append(key)
                    indice += 1
        print("")
        choice = input("Votre choix ---> ")
        tournament_name = tournaments_list[int(choice) - 1]
        print(tournament_name)
        print("*"*50)
        for tournoi in self.database.tournaments:
            print(tournoi[str(tournament_name)])




