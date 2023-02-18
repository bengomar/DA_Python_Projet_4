from datetime import datetime
from views import MainView, TournamentView, PlayerView, ReportsView
from modeles import Tournament, Player, SearchPlayerIdent
from databases import Tinydb
from samba.common import raw_input
import sys
import random

class Waiting:
    def wait():
        """Permet d'obtenir une pause du programme """
        print("")
        pause = raw_input("Appuyer sur ENTREE pour continuer ...")
        pause
        print("")
class MainControllers:
    list_of_player_of_tournament = []
    running_tournament = []
    players_pair = []
    def main_menu_choice(self):
        """Menu principal"""
        choice = MainView().main_menu()
        if choice == "1":
            # Lancer un tournoi
            self.create_tournament_action()
        elif choice == "2":
            # Menu joueurs
            self.menu_players()
        elif choice == "3":
            # Rapports
            self.menu_reports()
        elif choice == "4":
            # Résultats
            self.menu_admin()
            '''
            print("Liste des tournois (tournaments)")
            
            print("")
            print("Liste des joueurs participant au tournoi en cours (competitors)")
            
            print("")
            '''
            #self.main_menu_choice()
        elif choice == "5":
            # Sortir
            sys.exit()
        else:
            print("Saisie invalide, veuillez réessayer")
            Waiting.wait()
            self.main_menu_choice()

    def new_tournament(self):
        """Création d'un tournoi"""
        (
            name,
            location,
            date_start,
            date_end,
            nb_round,
        ) = TournamentView().get_tournament_data()
        self.current_tournament = Tournament(name, location, date_start, date_end, nb_round)
        Tinydb().add_tournament(
            self.current_tournament.name,
            self.current_tournament.location,
            datetime.strptime(self.current_tournament.date_start, "%d%m%Y-%H%M").strftime(
                "%d%m%Y-%H%M"
            ),
            self.current_tournament.date_end,
            self.current_tournament.nb_round,
        )

        print("")
        print(f'Le tournoi d\'échec "{self.current_tournament.name}" qui se déroule à {self.current_tournament.location} comprend {self.current_tournament.nb_round} rounds')
        self.running_tournament.append([self.current_tournament.name, self.current_tournament.location, self.current_tournament.nb_round])
    def menu_players(self):
        """Menu Joueurs"""
        choice = PlayerView().player_menu()
        if choice == "1":
            # Lister les joueurs
            PlayerView().print_player_list()
            Tinydb().players_list_ident()
            Waiting.wait()
            self.menu_players()
        elif choice == "2":
            # Ajouter un joueur
            self.new_player()
            Waiting.wait()
            self.menu_players()
        elif choice == "3":
            # Supprimer un joueur
            self.delete_player()
        elif choice == "4":
            # Retour
            self.main_menu_choice()
        else:
            print("Saisie invalide, veuillez réessayer")
            Waiting.wait()
            self.menu_players()

    def new_player(self):
        """Ajout d'un joueur dans la table Tinydb.players"""
        ident, surname, firstname, date_of_birth = PlayerView().get_player_data()
        current_player = Player(ident, surname, firstname, date_of_birth)
        Tinydb().add_player(
            current_player.ident,
            current_player.surname,
            current_player.firstname,
            current_player.date_of_birth,
        )
        print("")
        print(f"Le joueur {current_player.firstname} {current_player.surname} ({current_player.ident}) a été créé")
        print("")
        #Tinydb().check_table_players()
        self.menu_players()

    def delete_player(self):
        """Suppression d'un joueur dans la table Tinydb.players"""
        self.player_to_delete()
        ident = PlayerView().search_player_id_to_delete()
        current_search_player = SearchPlayerIdent(ident)
        Tinydb().del_player(current_search_player.ident)
        #Waiting.wait()
        self.menu_players()

    def player_to_delete(self):
        """Affichage personnalisé des joueurs depuis la table Tinydb.players"""
        PlayerView().print_player_list()
        Tinydb().players_list_ident()

    def print_players_by_num(self):
        """ Affichage des joueurs disponibles avec numérotation en préfixe"""
        list_player_tab = Tinydb().players_list()
        npa = 0
        for player in list_player_tab:
            npa += 1
            print(f"  {npa}. {player[0]} {player[1]} {player[2]}")

    def add_players_tournament(self):
        """ Ajout de joueurs disponibles dans le tournoi en cours"""
        list_player_tab = Tinydb().players_list()
        nb_player = len(list_player_tab)
        Tinydb().competitors.truncate()
        #print(list_player_tab)
        while nb_player > 0:
            num_player_list = PlayerView().add_players_to_tournament()
            self.list_of_player_of_tournament.append(list_player_tab[int(num_player_list) - 1])
            #print(f"{self.list_of_player_of_tournament=}")
            del list_player_tab[int(num_player_list) - 1]
            print("")
            print(f"Liste des joueurs participants au tournoi \"{self.running_tournament[0][0]}\" :")
            for play in self.list_of_player_of_tournament:
                print(f"  {play[0]} {play[1]} {play[2]}")
            print("")
            Tinydb().add_player_tournament(
                play[0],
                play[1],
                play[2],
            )
            if len(list_player_tab) == 0:
                pass
            else:
                print("Joueurs disponibles:")
            npa = 0
            for player_show in list_player_tab:
                npa += 1

                print(f"  {npa}. {player_show[0]} {player_show[1]} {player_show[2]}")
            nb_player -= 1

    def generate_players_pairs(self):
        """ Génération de pairs de joueurs (match) depuis la liste des joueurs selectionnés pour le tournoi """
        list_p_o = []

        for player in Tinydb.competitors:
            #print("******", player.get('ident'), player.get('surname'), player.get('firstname'))
            list_p_o.append((player.get('ident'), player.get('surname'), player.get('firstname')))
        print("                **********************")
        print(f"                * Match du 1er tour: *")
        print("                **********************")
        nb_match = len(list_p_o)//2
        while nb_match > 0:

            #player = list_p_o[0]
            #opponent = list_p_o[1]

            player = random.choice(list_p_o)
            opponent = random.choice(list_p_o)
            while player == opponent:
                player = random.choice(list_p_o)
                opponent = random.choice(list_p_o)

            matchs = [[player, 0], [opponent, 0]]
            player = matchs[0][0]
            opponent = matchs[1][0]


            print(f"  {player[0]} {player[1]} {player[2]} --vs-- {opponent[0]} {opponent[1]} {opponent[2]}")
            self.players_pair.append([player[0], opponent[0]])
            list_p_o.remove(player)
            list_p_o.remove(opponent)

            nb_match -= 1
    def match_score_player(self):
        dico_score_ident = {}
        list_player_tab = self.list_of_player_of_tournament
        nb_player = len(list_player_tab)

        while nb_player > 0:
            if len(self.list_of_player_of_tournament) == 0:
                pass
            else:
                self.generate_players_pairs()
                print("")
                print("Saisir les scores des matchs aux joueurs (Gagné = 1, Perdu = 0, Nul = 0.5)")
                npa = 0
                for play in list_player_tab:
                    npa += 1
                    player = f"  {npa}. {play[0]} {play[1]} {play[2]}"
                    print(player)

                choice = TournamentView().get_score_match()
                player_scored = self.list_of_player_of_tournament[int(choice)-1]

                if choice:
                    ident = list_player_tab[int(choice)-1][0]
                    #print(list_player_tab[int(choice) - 1])
                score_in = PlayerView().get_score_player()
                #print(score_in)
                dico_score_ident[ident] = score_in

                print(dico_score_ident)
                self.list_of_player_of_tournament.remove(player_scored)
            nb_player -= 1

    def next_rounds(self):
        #self.running_tournament.append(['tournoi_1', 'Paris', 4])
        self.running_tournament
        print(self.running_tournament)
        nb_rounds = (int(self.running_tournament[0][2]))-1

        print(f"{nb_rounds=}")
        n = 2
        while int(nb_rounds) > 0:
            """ Génération de pairs de joueurs (match) depuis la liste des joueurs selectionnés pour le tournoi """
            list_p_o = []

            for player in Tinydb.competitors:
                #print("******", player.get('ident'), player.get('surname'), player.get('firstname'))
                list_p_o.append((player.get('ident'), player.get('surname'), player.get('firstname')))
            print(f"{list_p_o=}")
            print("                **********************")
            print(f"                * Match du {n}eme tour: *")
            print("                **********************")

            nb_match = len(list_p_o) // 2
            while nb_match > 0:
                #player = list_p_o[0]
                #opponent = list_p_o[1]

                player = random.choice(list_p_o)
                opponent = random.choice(list_p_o)
                while player == opponent:
                    player = random.choice(list_p_o)
                    opponent = random.choice(list_p_o)

                matchs = [[player, 0], [opponent, 0]]
                gamer = matchs[0][0]
                gamer_versus = matchs[1][0]

                print(f"  {gamer[0]} {gamer[1]} {gamer[2]} --vs-- {gamer_versus[0]} {gamer_versus[1]} {gamer_versus[2]}")
                self.players_pair.append([gamer[0], gamer_versus[0]])
                list_p_o.remove(player)
                list_p_o.remove(opponent)

                nb_match -= 1

            n += 1
            nb_rounds -= 1

    def create_tournament_action(self):

        # créer une instance de tournoi
        self.new_tournament()

        # Ajouter des joueurs au tournoi
        PlayerView().print_player_list()
        self.print_players_by_num()
        self.add_players_tournament()

        # Génération des paires de joueurs
        #Liste de paires de joueurs (aléatoire)
        # créer le 1er tour
        # créer les matchs avec les paires de joueurs générés pour le 1er tour
        #self.generate_players_pairs()

        # rentrer les résultats du 1er tour
            #les scores seront enregistés dans l'instances de tournoi dans un dico {ident:score}
        self.match_score_player()

        # créer le 2ème tour
        self.next_rounds()
        # créer les matchs en fonction des points des joueurs.
        # 1- Génération des paires --> une liste de listes
        # 2- créer des instances de matchs
        # rentrer les résultats du 2ème tour

    def menu_admin(self):
        """Menu Administration"""
        choice = ReportsView().administation_menu()

        if choice == "1":
            # Lister la table "tournaments"
            Tinydb().check_table_tournaments()
            print("")
            self.menu_admin()
        elif choice == "2":
            # Lister la table "players
            Tinydb().check_table_players()
            print("")
            self.menu_admin()
        elif choice == "3":
            # Lister la table "competitors"
            Tinydb().check_table_competitors()
            print("")
            self.menu_admin()
        elif choice == "4":
            # Vider la table "tournaments"
            print("Veuillez confirmer (y/n)")
            confirm = MainView().confirm_yes_no()

            if (confirm == "y") or (confirm == "Y"):
                Tinydb().tournaments.truncate()
                print("")
                print(f"La table \"Tournaments\" a été vidé")
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
                Tinydb().players.truncate()
                print("")
                print(f"La table \"players\" a été vidé")
                print("")
            elif (confirm == "n") or (confirm == "N"):
                print("")
                print(f"Suppression des données annulées")
            else:
                print("Saisie incorrecte (y/n ou Y/N)")
            self.menu_admin()
        elif choice == "6":
            # Retour
            self.main_menu_choice()
        else:
            print("Saisie invalide, veuillez réessayer")
            Waiting.wait()
            self.menu_admin()

    def menu_reports(self):
        """Menu Rapports"""
        choice = ReportsView().reports_infos_menu()

        if choice == "1":
            # Liste des joueurs par ordre alphabétique
            Tinydb().players_list_ident()
            Waiting.wait()
            self.menu_reports()
        elif choice == "2":
            # Liste des tournois
            Tinydb().tournaments_list_formated()
            Waiting.wait()
            self.menu_reports()
        elif choice == "3":
            # Données d'un tournoi
            print("nom et dates d’un tournoi donné")
            Waiting.wait()
            self.menu_reports()
        elif choice == "4":
            # Liste des joueurs du dernier tournoi par ordre alphabétique
            Tinydb().check_table_competitors()
            Waiting.wait()
            self.menu_reports()
        elif choice == "5":
            # Liste des tours et matchs du dernier tournoi
            print("Liste des tours et matchs du dernier tournoi")
            Waiting.wait()
            self.menu_reports()
        elif choice == "6":
            # Retour
            self.main_menu_choice()
        else:
            print("Saisie invalide, veuillez réessayer")
            Waiting.wait()
            self.menu_reports()

#start programme
MainControllers().main_menu_choice()

#self.next_rounds()


# Lister la table
#Tinydb().check_table_tournaments()
#print("")
#Tinydb().check_table_players()
#print("")
#Tinydb().check_table_competitors()

# Vider une table
#Tinydb().tournaments.truncate()
#Tinydb().players.truncate()
#Tinydb().competitors.truncate()

