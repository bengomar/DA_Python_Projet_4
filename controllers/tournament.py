import random
from datetime import datetime
from typing import List

from termcolor import colored

from modeles import Match, Player, Round, Tournament
from persistance import DatabasesTinydb
from views.common import Usefull
from views.main import MainView
from views.player import PlayerView
from views.tournament import TournamentView


class TournamentController:
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

    def __init__(self):
        self.main_view = MainView()
        self.tournament_view = TournamentView()
        self.player_view = PlayerView()
        self.usefull = Usefull()
        self.persistance = DatabasesTinydb()

    def get_db_players(self):
        for index, player in enumerate(DatabasesTinydb().players):
            idx = index
            ident = player["ident"]
            surname = player["surname"]
            firstname = player["firstname"]
            date_of_birth = player["date_of_birth"]

            self.players.append(Player(idx,
                                       ident,
                                       surname,
                                       firstname,
                                       date_of_birth)
                                )

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
        nb_match = len(selected_player) // 2

        for i in range(0, nb_match):
            player_1 = list_1[i]
            player_2 = list_2[i]
            self.opponents_by_player[player_1.ident].remove(player_2)
            self.opponents_by_player[player_2.ident].remove(player_1)
            print(f"     {player_1} -vs- {player_2}")
            matchs_list.append([player_1, player_2])
        return matchs_list

    def generate_pairs_for_round(self, players: list):
        """Génération des pairs de joueurs pour les autres rounds"""

        players_to_pair = []
        for player in players:
            players_to_pair.append(player)
        pairs = []

        while players_to_pair:
            current_player = players_to_pair.pop()
            opponents = self.opponents_by_player[current_player.ident]
            for opponent in opponents:
                if (
                        opponent in players_to_pair
                        and opponent in
                        self.opponents_by_player[current_player.ident]
                ):
                    new_opponent = opponent
                    # Create pair
                    pairs.append([current_player, new_opponent])
                    players_to_pair.remove(opponent)
                    self.opponents_by_player[current_player.ident].remove(
                        opponent)
                    self.opponents_by_player[opponent.ident].remove(
                        current_player)
                    print(f"     {current_player} -vs- {new_opponent}")
                    break
        return pairs

    def create_matches(self, pairs) -> List[Match]:
        """Création de la liste des matchs depuis les pairs"""

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
                player_match_score = input(f" Saisir le score du joueur"
                                           f" {player_obj}: ")
                try:
                    if (
                        (float(player_match_score) == 0)
                        or (float(player_match_score) == 0.5)
                        or (float(player_match_score) == 1)
                    ):
                        score_progress = True
                    else:
                        print(
                            colored(
                                "!!! Entrée non valide, saisir "
                                "0 (perdu), "
                                "1 (gagné) ou "
                                "0.5 (nul) !!!",
                                "red",
                                attrs=["bold"],
                            )
                        )
                except ValueError:
                    print(
                        colored(
                            "!!! Entrée non valide, saisir "
                            "0 (perdu), "
                            "1 (gagné) ou "
                            "0.5 (nul) !!!",
                            "red",
                            attrs=["bold"],
                        )
                    )

            player_element[1] = float(player_match_score)
            player_obj.score += float(player_match_score)

    def get_round_list(self, matches: list, rounds: int):
        current_round = Round(matches, rounds)
        self.round_list.append([current_round.name, current_round.matches])

        return self.round_list

    def tournament_score_summary(self, current_tournament, resultat):
        """Affiche le résumé des scores des joueurs d'un tournoi"""
        print("")
        print(
            "Résumé des scores des joueurs du tournois",
            colored('"' + current_tournament.name + '"',
                    "blue",
                    attrs=["bold"])
            )
        sorted_resultat = sorted(resultat,
                                 key=lambda x: x[1],
                                 reverse=True
                                 )
        for score in sorted_resultat:
            print(colored(f" {score[0]} = {score[1]}", "blue", attrs=["bold"]))

    def start_tournament(self):
        self.get_db_players()
        # Display view to get inputs for the new tournament
        tournament_data = self.tournament_view.get_tournament_data()
        current_tournament = Tournament(*tournament_data)

        # Presentation of tournament
        print("")
        print(
            "     Tournoi d'échec:",
            colored(current_tournament.name,
                    "blue",
                    attrs=["bold"])
        )
        print(
            "     Lieu:", colored(current_tournament.location,
                                  "blue",
                                  attrs=["bold"]
                                  )
        )
        print(
            "     Nombre de rounds:",
            colored(current_tournament.nb_round,
                    "blue",
                    attrs=["bold"]
                    )
        )
        print(
            "     Date du tournoi :",
            colored(current_tournament.date_start,
                    "blue",
                    attrs=["bold"]
                    )
        )
        print("")
        # Display view to get players playing the tournament
        current_tournament.players = self.tournament_view.\
            add_players_tournament(self.players)

        # Create dictionary to store who played with who
        self.opponents_by_player = self.create_dico_player_playing(
            current_tournament.players
        )

        # For round in rounds:

        for self.round_number in range(1, current_tournament.nb_round + 1):
            if self.round_number == 1:
                print("                     *********************")
                print(f"                     * Matchs du Round"
                      f" {self.round_number} *")
                print("                     *********************")
                print("")

                # round_date_start = datetime.today().strftime("%d%m%Y-%H%M")
                # print("---round_date_start---->", round_date_start)
                pairs = self.generate_pairs_randomly(
                    current_tournament.players)

            else:
                print("                     *********************")
                print(f"                     * Matchs du Round"
                      f" {self.round_number} *")
                print("                     *********************")
                print("")

                # round_date_start = datetime.today().strftime("%d%m%Y-%H%M")
                # print("---round_date_start---->", round_date_start)
                players_sorted_by_score = sorted(
                    current_tournament.players,
                    key=lambda p: p.score,
                    reverse=True
                )
                pairs = self.generate_pairs_for_round(players_sorted_by_score)

            # Create matches from pairs
            matches = self.create_matches(pairs)

            # For match in matches:
            for i, match in enumerate(matches, 1):
                # Enter result for match
                print("")
                print(
                    colored(
                        f"Match {i}:"
                        f" {match.players[0][0]}"
                        f" -vs-"
                        f" {match.players[1][0]}",
                        "blue",
                        attrs=["bold"],
                    )
                )

                self.enter_scores_for_match(match)

                for player in match.players:
                    print(
                        f"   Score de {player[0].firstname}"
                        f" {player[0].surname}:",
                        colored(player[0].score,
                                "green",
                                attrs=["bold"]
                                )
                    )
                    self.resultat.append(
                        [
                            f"{player[0].surname}"
                            f" {player[0].firstname}", player[0].score
                        ]
                    )

            # rounds list
            current_tournament.rounds.append(Round
                                             (matches,
                                              str(self.round_number)
                                              )
                                             )

            # round_date_end = datetime.today().strftime("%d%m%Y-%H%M")
            # print("---round_date_end---->", round_date_end)
            print("")

        current_tournament.date_end = datetime.today().strftime("%d-%m-%Y")
        current_tournament.description = input(
            "Remarques générales"
            " du tournoi: "
        )
        print("")
        print(f"***************************** "
              f"Fin du tournoi ({current_tournament.date_end}) "
              f"******************************")

        # put tournament data in database
        self.persistance.put_current_tournament_in_database(
            current_tournament, self.round_number
        )

        # Result of the matches of each round of a tournament.
        from controllers.report import ReportController
        ReportController().get_tournament_matches_by_round(
            current_tournament.name
        )

        self.usefull.wait()
        # printing tournament player score summary after the last round.
        self.tournament_score_summary(current_tournament, self.resultat)
