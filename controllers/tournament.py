import random

from modeles import Player, Tournament, Match, Round
from views.player import PlayerView
from views.tournament import TournamentView
from persistance import DatabasesTinydb
from typing import List
from termcolor import colored
from datetime import datetime
from views.common import Usefull


class TournamentController:
    players = [
        Player(1, "CA12345", "CARLOS", "Roberto", "11112011"),
        Player(2, "ME45699", "MESSI", "Lionel", "11112011"),
        Player(3, "ZE99663", "ZINEDINE", "Zidane", "11112011"),
        Player(4, "PE45781", "PETIT", "Emmanuel", "11112011"),
        Player(5, "ZO50001", "DESCHAMPS", "Didier", "11112011"),
        Player(6, "VI22215", "VIEIRA", "Patrick", "11112011"),
        Player(7, "LI58871", "LIZARAZU", "Bixente", "11112011"),
        Player(8, "BE66993", "BENZEMA", "Karim", "11112011")
        # Player(9, "NM00001", "BELLOUMI", "Lakhdar", "11112011"),
        # Player(10, "VI00002", "MADJER", "Rabah", "11112011"),
        # Player(11, "LI00004", "MARADONA", "Diego", "11112011"),
        # Player(12, "BE00005", "VAN BASTEN", "Marco", "11112011")
    ]

    opponents_by_player = {}
    list_of_matchs = []
    score_list_player = []
    players_score_sorted = []
    add_score_player = []
    score_players = []
    round_number = ""
    round_list = []

    def __init__(self):
        self.tournament_view = TournamentView()
        self.player_view = PlayerView()
        self.persistance = DatabasesTinydb()
        self.usefull = Usefull()

    def create_dico_player_playing(self, competitors):
        """Création du dictionnaire de joueurs/adversaires"""
        opponents_by_player = {}

        for player in competitors:
            list_players_playing = [i for i in competitors if i != player]
            opponents_by_player[player.ident] = list_players_playing

        return opponents_by_player

    def generate_pairs_randomly(self, selected_player: list) -> list:
        """Génération des pairs de joueurs aléatoirement pour le 1er round"""
        matchs_list = []
        list_1 = []
        list_2 = []
        random.shuffle(selected_player)
        nb_player = len(selected_player)

        for i in range(nb_player):
            if i % 2:
                list_1.append(selected_player[i])
            else:
                list_2.append(selected_player[i])

        # list_1 = selected_player[0:2]
        # list_2 = selected_player[2:4]
        nb_match = len(selected_player) // 2

        for i in range(0, nb_match):
            player_1 = list_1[i]
            player_2 = list_2[i]
            self.opponents_by_player[player_1.ident].remove(player_2)
            self.opponents_by_player[player_2.ident].remove(player_1)
            print(f"     {player_1} -vs- {player_2}")
            print("")
            matchs_list.append([player_1, player_2])
        # print("")
        # print(f"{self.opponents_by_player=}")
        return matchs_list

    def generate_pairs_for_round(self, players: list):
        """Génération des pairs de joueurs pour les autres rounds"""

        players_to_pair = []
        # print("Generate pairs for round:")
        # print("*" * 10)

        for player in players:
            players_to_pair.append(player)

        # print(f"{players_to_pair=}")

        # Generate new pairs from opponents_by_player

        pairs = []

        while players_to_pair:

            current_player = players_to_pair.pop()
            opponents = self.opponents_by_player[current_player.ident]

            #print(f"{current_player=}")
            #print(f"{opponents=}")

            for opponent in opponents:
                if (
                        opponent in players_to_pair
                        and opponent in self.opponents_by_player[current_player.ident]
                ):
                    new_opponent = opponent

                    # Create pair
                    pairs.append([current_player, new_opponent])
                    #print(f"{pairs=}")

                    players_to_pair.remove(opponent)
                    #print(f"{players_to_pair=}")

                    #print(f"{current_player.ident=}")
                    #print(f"{opponent.ident=}")

                    self.opponents_by_player[current_player.ident].remove(opponent)
                    self.opponents_by_player[opponent.ident].remove(current_player)
                    print(f"     {current_player} -vs- {new_opponent}")
                    break

            #print(f"     {current_player} -vs- {new_opponent}")
            print("")
        return pairs

    def create_matches(self, pairs) -> List[Match]:
        """Création de la liste des matchs depuis les pairs """

        matches = []

        for pair in pairs:
            new_match = Match(*pair)
            matches.append(new_match)

        return matches

    def enter_scores_for_match(self, match):
        """Saisie et incrémentation des scores"""

        for player_element in match.players:
            # This should be part of function in the view layer
            player_obj = player_element[0]
            score_progress = False
            while score_progress is False:
                player_match_score = input(f" Saisir le score du joueur {player_obj}: ")
                try:
                    float(player_match_score)
                    player_match_score = float(player_match_score)
                    score_progress = True
                except ValueError:
                    print("")
                    print("!!! Entrée non valide, saisir 0, 1 ou 0.5 !!!")
                    self.usefull.wait()
            player_element[1] = player_match_score
            player_obj.score += player_match_score

    def start_tournament(self):

        # Display view to get inputs for the new tournament
        tournament_data = self.tournament_view.get_tournament_data()
        current_tournament = Tournament(*tournament_data)
        # ----> current_tournament.save()

        # Presentation of tournament
        print("")
        print(f"     Tournoi d'échec:", colored(current_tournament.name, 'green', attrs=['bold']))
        print(f"     Lieu:", colored(current_tournament.location, 'green', attrs=['bold']))
        print(f"     Nombre de rounds:", colored(current_tournament.nb_round, 'green', attrs=['bold']))
        print(f"     Date du tournoi :", colored(current_tournament.date_start, 'green', attrs=['bold']))
        print("")
        # Display view to get players playing the tournament
        current_tournament.players = self.tournament_view.select_players_for_tournament(self.players)
        # ---> current_tournament.players.save()

        # print(f"{current_tournament.players}")

        # Create dictionary to store who played with who
        self.opponents_by_player = self.create_dico_player_playing(current_tournament.players)
        # print(f"{self.opponents_by_player = }")

        # For round in rounds:

        for self.round_number in range(1, current_tournament.nb_round + 1):

            if self.round_number == 1:
                print("                     *********************")
                print(f"                     * Matchs du Round {self.round_number} *")
                print("                     *********************")
                print("")

                round_date_start = datetime.today().strftime("%d%m%Y-%H%M")
                pairs = self.generate_pairs_randomly(current_tournament.players)
                # print(f"{pairs=}")

            else:
                print("                     *********************")
                print(f"                     * Matchs du Round {self.round_number} *")
                print("                     *********************")
                print("")

                round_date_start = datetime.today().strftime("%d%m%Y-%H%M")
                players_sorted_by_score = sorted(current_tournament.players, key=lambda p: p.score, reverse=True)
                # print(f"{players_sorted_by_score=}")
                pairs = self.generate_pairs_for_round(players_sorted_by_score)
                # print("New pairs generated:")

            # Create matches from pairs
            matches = self.create_matches(pairs)

            resultat = []
            # For match in matches:
            for i, match in enumerate(matches, 1):
                # Enter result for match
                print("")
                print(f"Match {i}")
                self.enter_scores_for_match(match)

                for player in match.players:
                    print(f"   Score de {player[0].firstname} {player[0].surname}: {player[0].score}")
                    resultat.append([f"{player[0].surname} {player[0].firstname}", player[0].score])

            print("")

            round_date_end = datetime.today().strftime("%d%m%Y-%H%M")

            # current_tournament.rounds[round_number].append(Round(matches))

        current_tournament.date_end = datetime.today().strftime("%d-%m-%Y")
        current_tournament.description = input("Remarques générales du tournoi: ")
        print("")
        print(f" Résumé des scores des joueurs du tournois ", colored(current_tournament.name, 'green', attrs=['bold']))
        print()
        # print(f"{resultat=}")
        sorted_resultat = sorted(resultat, key=lambda x: x[1], reverse=True)
        print(f"{sorted_resultat=}")

        print("")

        print(f"name: {current_tournament.name}")
        print(f"location: {current_tournament.location}")
        print(f"date_start: {current_tournament.date_start}")
        print(f"date_end: {current_tournament.date_end}")
        print(f"nb_round: {current_tournament.nb_round}")
        print(f"current_round: {self.round_number}")
        print(f"round_list: {self.round_list}")
        print(f"players: {current_tournament.players}")
        print(f"description: {current_tournament.description}")

        '''
        DatabasesTinydb.tournaments.insert(
            {
                "name": current_tournament.name,
                "location": current_tournament.location,
                "date_start": current_tournament.date_start,
                "date_end": current_tournament.date_end,
                "nb_round": current_tournament.nb_round,
                "current_round": self.round_number,
                "round_list": self.round_list,
                "players": current_tournament.players,
                "description": current_tournament.description
            }
        )
        '''

        for tournament in DatabasesTinydb.tournaments:
            print(tournament)

        print("Tournament is done")
        # Display all matches of all rounds in the tournament
