class AdminView:
    def administation_menu(self):
        """Menu Administration"""
        print("Menu Administration")
        print("Sélectionnez une option: ")
        print("")
        print('   1.  Lister la table "tournaments"')
        print('   2.  Lister la table "players"')
        print('   3.  Lister la table "competitors"')
        print('   4.  Vider la table "tournaments"')
        print('   5.  Vider la table "players"')
        print("   6.  Retour")

        print("")
        option = input("Votre choix ---> ")
        print("")
        choice = option
        return choice
