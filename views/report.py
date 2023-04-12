from termcolor import colored

from views.common import Usefull


class ReportsView:
    def __init__(self):
        self.usefull = Usefull()

    def reports_infos_menu(self):
        """Menu Rapport"""
        self.usefull.clear()
        print("*****************")
        print("* CENTRE ÉCHECS *")
        print("*****************")
        print(colored("Menu Rapports", "blue", attrs=["bold"]))
        print("Sélectionnez une option: ")
        print("")
        print("   1.  Liste de tous les joueurs par ordre alphabétique")
        print("   2.  Liste de tous les tournois ")
        print("   3.  Liste des joueurs d'un tournoi par ordre alphabétique")
        print("   4.  Liste des tours et des matchs de chaque tour d'un tournoi")
        print("   5.  Retour")

        print("")
        option = input("Votre choix ---> ")
        print("")
        choice = option
        return choice
