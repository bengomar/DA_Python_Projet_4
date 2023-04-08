import sys
from controllers.player import PlayerController
from controllers.report import ReportController
from controllers.tournament import TournamentController
from controllers.admin import AdminController
from modeles import Player
from persistance import DatabasesTinydb
from views.main import MainView, Waiting
from views.common import Usefull


class MainController:
    def __init__(self):
        self.view = MainView()
        self.usefull = Usefull()
        self.database = DatabasesTinydb()

        self.tournament_controller = TournamentController()
        self.player_controller = PlayerController()
        self.report_controller = ReportController()
        self.admin_controller = AdminController()

    def run(self):

        self.usefull.clear()
        in_progress = True
        while in_progress:

            """Menu principal du programme"""
            choice = self.view.display_main_menu()
            if choice == "1":
                # Lancer un tournoi
                self.tournament_controller.start_tournament()
                self.usefull.wait()
                self.usefull.clear()
                return
            elif choice == "2":
                # Menu joueurs
                self.player_controller.display_menu_players()
            elif choice == "3":
                # Rapports
                self.report_controller.menu_reports()
            elif choice == "4":
                # Sortir
                in_progress = False
                #sys.exit()
            else:
                print("Saisie invalide, veuillez réessayer")
                Usefull.wait(self)
                self.run()
