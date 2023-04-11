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

    def run(self):
        self.usefull.clear()
        in_progress = True
        while in_progress:
            """Menu principal du programme"""
            choice = self.view.display_main_menu()
            if choice == "1":
                # Lancer un tournoi
                self.tournament_controller.start_tournament()
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
                # sys.exit()
            else:
                print("Saisie invalide, veuillez réessayer")
                Usefull.wait(self)
                self.run()
