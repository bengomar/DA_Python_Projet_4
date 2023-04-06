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