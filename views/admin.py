from termcolor import colored

from views.common import Usefull


class AdminView:
    def __init__(self):
        self.usefull = Usefull()

    def admin_menu(self):
        """Menu Administration"""
        self.usefull.clear()
        print("*****************")
        print("* CENTRE ÉCHECS *")
        print("*****************")
        print(colored("-Menu Administration Tinydb-", "blue", attrs=["bold"]))
        print("Sélectionnez une option: ")
        print("")
        print('   1.  Lister la table "players"')
        print('   2.  Lister la table "tournaments"')
        print('   3.  Vider la table "players"')
        print('   4.  Vider la table "tournaments"')
        print('   5.  Créer la table "players" avec 8 joueurs')
        print("   6.  Retour")

        print("")
        option = input("Votre choix ---> ")
        print("")
        choice = option
        return choice
