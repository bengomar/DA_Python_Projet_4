from datetime import datetime

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

    def print_player_list(self):
        """Liste les joueurs"""
        print("")
        print("Liste des joueurs :")
        print("Id      Nom, Prénom")




    def get_player_data(self):
        """Saisie des données d'un nouveau joueur"""
        index = 1
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
        return [index, ident, surname, firstname, date_of_birth]

    def search_player_id_to_delete(self):
        """Saisie de l'identifiant d'un joueur à supprimer"""
        ident = input("Saisissez Id du joueur à supprimer :  ")
        return ident

    def add_players_to_tournament(self):
        """ajout de joueur au tournoi"""
        print("")
        num_player_list = input("Sélectionner une option  :  ")
        return num_player_list

    def get_score_player(self, family_name, name):
        """saisie du score joueur"""
        print("")
        score_in = input(f"Saisir le score du joueur {name} {family_name}: ")
        return score_in



