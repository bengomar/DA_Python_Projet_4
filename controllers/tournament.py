import random
from pprint import pprint

from modeles import Player, Tournament, Match, Round
from views.player import PlayerView
from views.tournament import TournamentView
from persistance import DatabasesTinydb
from typing import List
from termcolor import colored
from datetime import datetime
from views.common import Usefull


class TournamentController:

    def __init__(self):
        self.tournament_view = TournamentView()
        self.player_view = PlayerView()
        self.usefull = Usefull()
        self.persistance = DatabasesTinydb()

    opponents_by_player = {}
    list_of_matchs = []
    score_list_player = []
    players_score_sorted = []
    add_score_player = []
    score_players = []
    round_number = ""
    round_list = []
    players = []
    resultat = []

    # players = [
    #     Player(1, "CA12345", "CARLOS", "Roberto", "11112011"),
    #     Player(2, "ME45699", "MESSI", "Lionel", "11112011"),
    #     Player(3, "ZE99663", "ZINEDINE", "Zidane", "11112011"),
    #     Player(4, "PE45781", "PETIT", "Emmanuel", "11112011"),
    #     Player(5, "ZO50001", "DESCHAMPS", "Didier", "11112011"),
    #     Player(6, "VI22215", "VIEIRA", "Patrick", "11112011"),
    #     Player(7, "LI58871", "LIZARAZU", "Bixente", "11112011"),
    #     Player(8, "BE66993", "BENZEMA", "Karim", "11112011")
    #     # Player(9, "NM00001", "BELLOUMI", "Lakhdar", "11112011"),
    #     # Player(10, "VI00002", "MADJER", "Rabah", "11112011"),
    #     # Player(11, "LI00004", "MARADONA", "Diego", "11112011"),
    #     # Player(12, "BE00005", "VAN BASTEN", "Marco", "11112011")
    # ]

    for index, player in enumerate(DatabasesTinydb().players):
        idx = index
        ident = player['ident']
        surname = player['surname']
        firstname = player['firstname']
        date_of_birth = player['date_of_birth']

        players.append(Player(idx, ident, surname, firstname, date_of_birth))

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

            # print(f"{current_player=}")
            # print(f"{opponents=}")

            for opponent in opponents:
                if (
                        opponent in players_to_pair
                        and opponent in self.opponents_by_player[current_player.ident]
                ):
                    new_opponent = opponent

                    # Create pair
                    pairs.append([current_player, new_opponent])
                    # print(f"{pairs=}")

                    players_to_pair.remove(opponent)
                    # print(f"{players_to_pair=}")

                    # print(f"{current_player.ident=}")
                    # print(f"{opponent.ident=}")

                    self.opponents_by_player[current_player.ident].remove(opponent)
                    self.opponents_by_player[opponent.ident].remove(current_player)
                    print(f"     {current_player} -vs- {new_opponent}")
                    break

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
                # try:
                #     float(player_match_score)
                #     player_match_score = float(player_match_score)
                #     score_progress = True
                # except ValueError:
                #     print("")
                #     print("!!! Entrée non valide, saisir 0, 1 ou 0.5 !!!")

                try:
                    if (float(player_match_score) == 0) or (float(player_match_score) == 0.5) or (
                            float(player_match_score) == 1):
                        # print(player_match_score)
                        score_progress = True
                    else:
                        print(colored("!!! Entrée non valide, saisir 0 (perdu), 1 (gagné) ou 0.5 (nul) !!!", 'red',
                                      attrs=['bold']))
                except:
                    print(colored("!!! Entrée non valide, saisir 0 (perdu), 1 (gagné) ou 0.5 (nul) !!!", 'red',
                                  attrs=['bold']))

            player_element[1] = float(player_match_score)
            player_obj.score += float(player_match_score)

    def get_round_list(self, matches: list, rounds: int):

        current_round = Round(matches, rounds)
        self.round_list.append([current_round.name, current_round.matches])

        return self.round_list

    def tournament_score_summary(self, current_tournament, resultat):
        """ Affiche le résumé des scores des joueurs d'un tournoi """
        print("")
        print(f"Résumé des scores des joueurs du tournois",
              colored('"' + current_tournament.name + '"', 'blue', attrs=['bold']))
        # print(f"{resultat=}")
        sorted_resultat = sorted(resultat, key=lambda x: x[1], reverse=True)
        for score in sorted_resultat:
            print(colored(f"          {score[0]} = {score[1]}", 'blue', attrs=['bold']))

    def start_tournament(self):

        # Display view to get inputs for the new tournament
        tournament_data = self.tournament_view.get_tournament_data()
        current_tournament = Tournament(*tournament_data)

        # ----> current_tournament.save()

        # Presentation of tournament
        print("")
        print(f"     Tournoi d'échec:", colored(current_tournament.name, 'blue', attrs=['bold']))
        print(f"     Lieu:", colored(current_tournament.location, 'blue', attrs=['bold']))
        print(f"     Nombre de rounds:", colored(current_tournament.nb_round, 'blue', attrs=['bold']))
        print(f"     Date du tournoi :", colored(current_tournament.date_start, 'blue', attrs=['bold']))
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

            else:
                print("                     *********************")
                print(f"                     * Matchs du Round {self.round_number} *")
                print("                     *********************")
                print("")

                round_date_start = datetime.today().strftime("%d%m%Y-%H%M")
                players_sorted_by_score = sorted(current_tournament.players, key=lambda p: p.score, reverse=True)
                pairs = self.generate_pairs_for_round(players_sorted_by_score)

            # Create matches from pairs
            matches = self.create_matches(pairs)

            # For match in matches:
            resultat = []
            for i, match in enumerate(matches, 1):
                # Enter result for match
                print("")
                print(colored(f"Match {i}: {match.players[0][0]} -vs- {match.players[1][0]}", 'blue', attrs=['bold']))

                self.enter_scores_for_match(match)

                for player in match.players:
                    print(f"   Score de {player[0].firstname} {player[0].surname}:",
                          colored(player[0].score, 'green', attrs=['bold']))
                    resultat.append([f"{player[0].surname} {player[0].firstname}", player[0].score])

            self.usefull.wait()
            # rounds list
            # current_round_data = self.get_round_list(matches, self.round_number)
            current_tournament.rounds.append(Round(matches, self.round_number))

            round_date_end = datetime.today().strftime("%d%m%Y-%H%M")
            print("")

        current_tournament.date_end = datetime.today().strftime("%d-%m-%Y")
        current_tournament.description = input("Remarques générales du tournoi: ")

        # printing tournament player score summary after the last round.
        self.tournament_score_summary(current_tournament, resultat)

        # put tournament data in database
        self.persistance.put_current_tournament_in_database(current_tournament, self.round_number)

        for tournament in self.persistance.tournaments:
            print(tournament)

        # print("")
        # print(f"{current_round_data}")
        # print(f"{current_tournament.rounds=}")

        print("Tournament is done")
        # Display all matches of all rounds in the tournament
