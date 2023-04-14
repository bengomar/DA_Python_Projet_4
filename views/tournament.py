from datetime import datetime
from typing import List

from modeles import Player
from views.common import Usefull
from views.player import PlayerView
from termcolor import colored


class TournamentView:
    def __init__(self):
        self.player_view = PlayerView()
        self.usefull = Usefull()

    def get_tournament_data(self):
        print("")
        name = input("Saisir le nom du tournoi: ").capitalize()
        location = input("Saisir le lieu du tournoi: ").capitalize()
        date_start = datetime.today().strftime("%d-%m-%Y")
        date_end = ""
        nb_round = 4
        description = ""

        return [name, location, date_start, date_end, nb_round, description]

    def get_score_match(self):
        print("")
        choice = input("Votre choix ---> ")
        return choice

    def select_players_for_tournament(self, players: List[Player]) -> List[Player]:
        """Ajout de joueurs disponibles dans le tournoi en cours"""

        players_not_selected = players
        selected_players = []

        add_player_ended = False
        while add_player_ended is False:
            if not selected_players:
                print(colored("Liste des joueurs disponibles:", 'blue', attrs=['bold']))
                print("   Id      Nom, Prénom")
                for index, player in enumerate(players_not_selected):
                    print(f"{index + 1}. {player}")
                print(f"{index + 2}. Ajouter tous les joueurs disponibles")

                if len(selected_players) % 2 == 0 and len(selected_players) >= 8:
                    print(f"{index + 3}. Fin de selection")
                print("")
                print("Ajoutez un joueur au tournoi:")
                choice = input("Votre choix ---> ")
                try:
                    int(choice)
                    choice = int(choice)
                except ValueError:
                    print("")
                    print(
                        "!!! Choix non valide, sélectionner un des chiffres de la liste !!!"
                    )
                    self.usefull.wait()
                    continue
                if abs(choice) > len(players_not_selected) + 1:
                    print("")
                    print(
                        "!!! Choix non valide, sélectionner un des chiffres de la liste !!!"
                    )
                    self.usefull.wait()
                    continue
                elif choice == len(players_not_selected) + 1:
                    selected_players = players_not_selected.copy()
                    print("")
                    print("Joueurs sélectionés pour le tournoi:")
                    print("Id      Nom, Prénom")
                    for index, player in enumerate(selected_players):
                        print(f"{player}")
                    print("")
                    del players_not_selected[:]
                    break
                else:
                    selected_players.append(players.pop(choice - 1))
            else:
                print("")
                print("Joueurs sélectionés pour le tournoi:")
                print("Id      Nom, Prénom")
                for index, player in enumerate(selected_players):
                    print(f"{player}")
                print("")
                if not players_not_selected:
                    break
                else:
                    print(colored("Liste des joueurs disponibles:", 'blue', attrs=['bold']))
                    print("   Id      Nom, Prénom")
                    for index, player in enumerate(players_not_selected):
                        print(f"{index + 1}. {player}")
                    if len(selected_players) % 2 == 0 and len(selected_players) >= 8:
                        print(f"{index + 2}. Fin de selection")
                    print("")
                    print("Ajoutez un joueur au tournoi:")
                    choice = input("Votre choix ---> ")
                    try:
                        int(choice)
                        choice = int(choice)
                    except ValueError:
                        print("")
                        print(
                            "!!! Choix non valide, sélectionner un des chiffres de la liste !!!"
                        )
                        self.usefull.wait()
                        continue

                    if abs(choice) > len(players_not_selected) + 1:
                        print("")
                        print(
                            "!!! Choix non valide, sélectionner un des chiffres de la liste !!!"
                        )
                        self.usefull.wait()
                        continue
                    elif (
                        abs(choice) == len(players_not_selected) + 1
                        and len(selected_players) < 8
                    ):
                        print("")
                        print(
                            "!!! Choix non valide, sélectionner un des chiffres de la liste !!!"
                        )
                        self.usefull.wait()
                        continue
                    elif (
                        abs(choice) == len(players_not_selected) + 1
                        and len(selected_players) % 2 == 0
                        and len(selected_players) >= 8
                    ):
                        break
                    else:
                        # print(selected_players)
                        selected_players.append(players.pop(choice - 1))

        add_player_ended = True
        self.usefull.wait()
        self.usefull.clear()
        return selected_players
