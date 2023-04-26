from controllers.admin import AdminController
from controllers.player import PlayerController
from controllers.report import ReportController
from controllers.tournament import TournamentController
from persistance import DatabasesTinydb
from views.common import Usefull
from views.main import MainView


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
                current_tournament =\
                    self.tournament_controller.start_tournament()
                Usefull.clear(self)
                if current_tournament is not None:
                    self.report_controller.get_tournament_matches_by_round(
                        current_tournament.name
                    )
            elif choice == "2":
                # Menu joueurs
                self.player_controller.display_menu_players()
            elif choice == "3":
                # Menu Rapports
                self.report_controller.menu_reports()
            elif choice == "4":
                # Menu Administration
                self.admin_controller.menu_admin()
            elif choice == "5":
                # Sortir
                in_progress = False
            else:
                print("Saisie invalide, veuillez réessayer")
                Usefull.wait(self)
