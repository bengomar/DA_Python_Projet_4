from views.admin import AdminView
from views.common import Usefull

class AdminController:

    def menu_admin(self):
        """Menu Administration"""
        choice = AdminView().administation_menu()

        if choice == "1":
            # Lister la table "tournaments"
            DatabasesTinydb().check_table_tournaments()
            print("")
            self.menu_admin()
        elif choice == "2":
            # Lister la table "players
            DatabasesTinydb().check_table_players()
            print("")
            self.menu_admin()
        elif choice == "3":
            # Lister la table "competitors"
            DatabasesTinydb().check_table_competitors()
            print("")
            self.menu_admin()
        elif choice == "4":
            # Vider la table "tournaments"
            print("Veuillez confirmer (y/n)")
            confirm = MainView().confirm_yes_no()

            if (confirm == "y") or (confirm == "Y"):
                DatabasesTinydb().tournaments.truncate()
                print("")
                print(f'La table "Tournaments" a été vidé')
                print("")
            elif (confirm == "n") or (confirm == "N"):
                print("")
                print(f"Suppression des données annulées")
            else:
                print("Saisie incorrecte (y/n ou Y/N)")
            self.menu_admin()
        elif choice == "5":
            # Lister la table "players"
            print("Veuillez confirmer (y/n)")
            confirm = MainView().confirm_yes_no()

            if (confirm == "y") or (confirm == "Y"):
                DatabasesTinydb().players.truncate()
                print("")
                print(f'La table "players" a été vidé')
                print("")
            elif (confirm == "n") or (confirm == "N"):
                print("")
                print(f"Suppression des données annulées")
            else:
                print("Saisie incorrecte (y/n ou Y/N)")
            self.menu_admin()
        elif choice == "6":
            # Retour
            return
        else:
            print("Saisie invalide, veuillez réessayer")
            Usefull.wait()
            self.menu_admin()