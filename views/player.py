from datetime import datetime

from termcolor import colored

from views.common import Usefull


class PlayerView:
    def __init__(self):
        self.usefull = Usefull()
        self.form = "{0:9}{1:12}{2:10}{3:10}"

    def player_menu(self):
        """Menu Joueurs"""
        self.usefull.clear()
        print("*****************")
        print("* CENTRE ÉCHECS *")
        print("*****************")
        print(colored("Menu joueurs", "blue", attrs=["bold"]))
        print("Sélectionnez une option: ")
        print("")
        print("   1.  Ajouter un joueur ")
        print("   2.  Supprimer un joueur ")
        print("   3.  Lister les joueurs ")
        print("   4.  Retour ")

        print("")
        option = input("Votre choix ---> ")
        print("")
        choice = option
        return choice

    def print_player_list(self):
        """Liste les joueurs"""
        print("")
        print("Liste des joueurs enregistrés: ")
        head = self.form.format("Id", "Nom", "Prénom", "Date de naissance")
        print(colored(head, 'blue',  attrs=['bold']))

    def get_player_data(self):
        """Saisie des données d'un nouveau joueur"""
        index = 1
        ident = input("Identifiant national du joueur:  ")
        surname = input("Nom du joueur: ").upper()
        firstname = input("Prénom du joueur: ").capitalize()

        while True:
            date_entered = input("Date de naissance du joueur (jj-mm-aaaa): ")
            try:
                date_of_birth = datetime.strptime(date_entered, "%d-%m-%Y").strftime(
                    "%d-%m-%Y"
                )
                break
            except ValueError:
                print("Le date est invalide ")
        return [index, ident, surname, firstname, date_of_birth]
