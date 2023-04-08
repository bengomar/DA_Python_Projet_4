from views.report import ReportsView
from views.player import PlayerView
from views.common import Usefull
from controllers.player import PlayerController

class ReportController:

    def __init__(self):
        self.player_controller = PlayerController()
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
            DatabasesTinydb().tournaments_list_formated()
            Usefull.wait()
            self.menu_reports()
        elif choice == "3":
            # Données d'un tournoi
            print("nom et dates d’un tournoi donné")
            Usefull.wait()
            self.menu_reports()
        elif choice == "4":
            # Liste des joueurs du dernier tournoi par ordre alphabétique
            DatabasesTinydb().check_table_competitors()
            Usefull.wait()
            self.menu_reports()
        elif choice == "5":
            # Liste des tours et matchs du dernier tournoi
            print("Liste des tours et matchs du dernier tournoi")
            Usefull.wait()
            self.menu_reports()
        elif choice == "6":
            # Retour
            return
        else:
            print("Saisie invalide, veuillez réessayer")
            Usefull.wait()
            self.menu_reports()
