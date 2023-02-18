from datetime import datetime

class MainView:
    def main_menu(self):
        """Menu principal du programme"""
        print("*****************")
        print("* CENTRE ÉCHECS *")
        print("*****************")
        print("Sélectionnez une option: ")
        print("")
        print("   1.  Lancer un tournoi ")
        print("   2.  Gestion des Joueurs ")
        print("   3.  Rapports ")
        print("   4.  Administration ")

        print("   5.  Sortir ")
        print("")

        option = input("Votre choix ---> ")
        choice = option
        return choice

    def confirm_yes_no(self):
        """ confirmation par Y/N ou y/n"""
        confirm = input("---> ")
        return confirm

class TournamentView:
    def get_tournament_data(self):
        name = input("Saisir le nom du tournoi: ").capitalize()
        location = input("Saisir le lieu du tournoi: ").capitalize()
        date_start = datetime.today().strftime("%d%m%Y-%H%M")
        date_end = ""
        nb_round = 4

        return [name, location, date_start, date_end, nb_round]

    def get_score_match(self):
        print("")
        choice = input("Votre choix ---> ")
        return choice

class PlayerView:
    def player_menu(self):
        """Menu Joueurs"""
        print("Menu joueurs")
        print("Sélectionnez une option: ")
        print("")
        print("   1.  Lister les joueurs ")
        print("   2.  Ajouter un joueur ")
        print("   3.  Supprimer un joueur ")
        print("   4.  Retour ")

        print("")
        option = input("Votre choix ---> ")
        print("")
        choice = option
        return choice
    def get_player_data(self):
        """Saisie des données d'un nouveau joueur"""
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
        return [ident, surname, firstname, date_of_birth]

    def search_player_id_to_delete(self):
        """Saisie de l'identifiant d'un joueur à supprimer"""
        ident = input("Saisissez Id du joueur à supprimer :  ")
        return ident

    def print_player_list(self):
        """Liste les joueurs """
        print("")
        print("Liste des joueurs inscrits :")
        print("     Id      Nom,Prénom")

    def add_players_to_tournament(self):
        """ ajout de joueur au tournoi"""
        print("")
        num_player_list = input("Ajouter un joueur au Tournoi :  ")
        return num_player_list

    def get_score_player(self):
        """saisie du score joueur"""
        print("")
        score_in = input("Saisir le score du joueur: ")
        return score_in

class ReportsView:
    def reports_infos_menu(self):
        """Menu Rapport"""
        print("Menu Rapports")
        print("Sélectionnez une option: ")
        print("")
        print("   1.  Liste des joueurs par ordre alphabétique")
        print("   2.  Liste des tournois ")
        print("   3.  Données d'un tournoi ")
        print("   4.  Liste des joueurs du dernier tournoi par ordre alphabétique")
        print("   5.  Liste des tours et matchs des tours du dernier tournoi")
        print("   6.  Retour")

        print("")
        option = input("Votre choix ---> ")
        print("")
        choice = option
        return choice

    def administation_menu(self):
        """Menu Administration"""
        print("Menu Administration")
        print("Sélectionnez une option: ")
        print("")
        print("   1.  Lister la table \"tournaments\"")
        print("   2.  Lister la table \"players\"")
        print("   3.  Lister la table \"competitors\"")
        print("   4.  Vider la table \"tournaments\"")
        print("   5.  Vider la table \"players\"")
        print("   6.  Retour")

        print("")
        option = input("Votre choix ---> ")
        print("")
        choice = option
        return choice

