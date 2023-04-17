from persistance import DatabasesTinydb
from views.admin import AdminView
from views.common import Usefull


class AdminController:
    def __init__(self):
        self.database = DatabasesTinydb()
        self.usefull = Usefull()
        self.view = AdminView()

    def menu_admin(self):
        """Menu Rapports"""
        in_progress = False
        while in_progress is False:
            choice = self.view.admin_menu()
            if choice == "1":
                # Lister la table "players"
                self.database.check_table_players()
                self.usefull.wait()
                # self.menu_reports()
            elif choice == "2":
                # Lister la table "tournaments"
                self.database.check_table_tournaments()
                self.usefull.wait()
            elif choice == "3":
                #  Vider la table "players")
                self.database.truncate_table_players()
                self.usefull.wait()
            elif choice == "4":
                # Vider la table "tournaments")
                self.database.truncate_table_tournaments()
                self.usefull.wait()
            elif choice == "5":
                # Charger une table "players" de 8 joueurs")
                self.database.add_eight_players()
                self.usefull.wait()
            elif choice == "6":
                # Retour
                in_progress = True
            else:
                print("Saisie invalide, veuillez réessayer")
                self.usefull.wait()
