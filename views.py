from datetime import datetime
import time

class TournamentView:
    def get_tournament_data(self):
        name = input("Nom du tournoi: ").capitalize()
        location = input("Lieu du tournoi: ").capitalize()
        date_start = datetime.today().strftime('%d%m%Y')
        date_end = ""
        nb_round = 4

        return [name, location, date_start, date_end, nb_round]

    def tournament_menu(self):
        """Menu Tournoi"""
        print("")
        print("Sélectionnez une option ")
        print("")
        print("   1.  Charger un tournoi ")
        print("   2.  Créer un tournoi ")
        print("   3.  Terminer un tournoi ")
        print("   4.  Retour ")

        print("")
        option = input("Votre choix ---> ")

        if option == "1":
            choice = option
            return choice
        elif option == "2":
            choice = option
            return choice
        elif option == "3":
            choice = option
            return choice
        else:
            choice = option
            return choice

    def get_end_date(self):
        """ Saisie de la date de fin d'un tournoi"""

        while True:
            end_date_entred = input("Saisir la date de fin du tournoi (jjmmaaaa): ")
            try:
                date_end = datetime.strptime(end_date_entred, "%d%m%Y").strftime(
                    "%d%m%Y"
                )
                break
            except ValueError:
                print("Le date est invalide ")
        return date_end

class PlayerView:
    def get_player_data(self):
        ident = input("Identifiant national du joueur:  ")
        surname = input("Nom du joueur: ").upper()
        firstname = input("Prénom du joueur: ").capitalize()

        while True:
            date_entered = input("Date de naissance du joueur (jjmmaaaa): ")
            try:
                date_of_birth = datetime.strptime(date_entered, "%d%m%Y").strftime(
                    "%d%m%Y"
                )
                break
            except ValueError:
                print("Le date est invalide ")
        score = 0
        return [ident, surname, firstname, date_of_birth, score]

    def player_menu(self):
        """Menu Joueurs"""
        print("")
        print("Sélectionnez une option ")
        print("")
        print("   1.  Ajouter un joueur ")
        print("   2.  Supprimer un joueur ")
        print("   3.  Saisir le score d'un joueur ")
        print("   4.  Retour ")

        print("")
        option = input("Votre choix ---> ")

        if option == "1":
            choice = option
            return choice
        elif option == "2":
            choice = option
            return choice
        elif option == "3":
            choice = option
            return choice
        elif option == "4":
            choice = option
            return choice
        else:
            choice = option
            return choice

    def menu_delete_player(self):
        ident = input("Identifiant du joueur à supprimer :  ")
        return ident

class MainView:
    def main_menu(self):
        """Menu principal du programme"""
        print("")
        print("Sélectionnez une option ")
        print("")
        print("   1.  Menu Joueurs ")
        print("   2.  Menu tournois ")
        print("   3.  Résultats ")
        print("   4.  Rapports ")
        print("   5.  Sortir ")
        print("")

        option = input("Votre choix ---> ")

        if option == "1":
            choice = option
            return choice
        elif option == "2":
            choice = option
            return choice
        elif option == "3":
            choice = option
            return choice
        elif option == "4":
            choice = option
            return choice
        elif option == "5":
            choice = option
            return choice
        else:
            choice = option
            return choice

