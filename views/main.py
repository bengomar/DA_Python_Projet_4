from views.common import Usefull
from termcolor import colored


class MainView:
    def __init__(self):
        self.usefull = Usefull()

    def display_main_menu(self):
        """Menu principal du programme"""
        self.usefull.clear()
        print("*****************")
        print("* CENTRE ÉCHECS *")
        print("*****************")
        print(colored("Menu principal", 'blue', attrs=['bold']))
        print("Sélectionnez une option: ")
        print("")
        print("   1.  Lancer un tournoi ")
        print("   2.  Gestion des Joueurs ")
        print("   3.  Rapports ")
        print("   4.  Sortir ")
        print("")

        option = input("Votre choix ---> ")
        choice = option
        return choice
