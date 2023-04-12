from controllers.player import PlayerController
from views.common import Usefull
from views.player import PlayerView
from views.report import ReportsView
from persistance import DatabasesTinydb


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
            # Liste des joueurs du dernier tournoi par ordre alphabétique
            print("Liste des joueurs du dernier tournoi par ordre alphabétique")
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
