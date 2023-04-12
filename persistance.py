from pprint import pprint

from termcolor import colored
from tinydb import Query, TinyDB, where

from modeles import Player


class DatabasesTinydb:
    db = TinyDB("db.json")
    players = db.table("players")
    tournaments = db.table("tournaments")
    query = Query()

    def put_current_tournament_in_database(self, current_tournament, round_number):
        players_json = []
        round_json = []

        print("")
        for player in current_tournament.players:
            players_json.append(player.__dict__)

        for ronde in current_tournament.rounds:
            ronde_dict = ronde.__dict__
            round_matches = []
            for match in ronde.matches:
                players = [[player[0].__dict__, player[1]] for player in match.players]
                match.players = players
                round_matches.append(match)
            ronde_dict["matches"] = [
                {"players": match.players} for match in round_matches
            ]
            round_json.append(ronde_dict)
            # pprint(round_json)
        print("")
        self.tournaments.insert(
            {
                current_tournament.name: {
                    "location": current_tournament.location,
                    "date_start": current_tournament.date_start,
                    "date_end": current_tournament.date_end,
                    "nb_round": current_tournament.nb_round,
                    "current_round": round_number,
                    "players": players_json,
                    "round_list": round_json,
                    "description": current_tournament.description,
                }
            }
        )

    def check_table_tournaments(self):
        """Parcourir la table tournaments"""
        for tournament in self.tournaments:
            print(tournament)

    # def search_ident_player(self, ident: str):
    #     """Recherche d'un joueur dans la table players avec son identifiant"""
    #     self.ident = ident
    #
    #     # Tinydb.players.search(where('ident') == self.ident)
    #     find_player = DatabasesTinydb.players.search(where("ident") == self.ident)
    #     print(find_player)
    #

    #
    # def get_tournament(self):
    #     """recherche de tournoi en cours (n'ayant pas de date de fin)"""
    #
    #     end_date_get = DatabasesTinydb.tournaments.search(where("date_end") == "")
    #
    #     number_t = 0
    #     # TournamentView().running_tournament()
    #     print("")
    #     print("CENTRE ÉCHECS - Tournois")
    #     print("")
    #     print("Tournoi(s) en cours:")
    #
    #     for tournament_run in end_date_get:
    #         number_t += 1
    #         print(
    #             f"   {number_t}. Tournoi {tournament_run.get('name')}, {tournament_run.get('location')} "
    #         )
    #

    def tournaments_list_formated(self):
        """Parcourir la table tournaments"""
        form = "{0:20}{1:15}{2:10}{3:15}{4:15}{5:}"
        if not self.tournaments:
            print("Il n'y a actuellement aucun tournoi d'enregistré !!!")
        else:
            print("Liste des tournois:")
            head = form.format(
                "Nom du tournoi",
                "Lieu",
                "Rounds",
                "Date de début",
                "Date de fin",
                "Remarques générales"
            )
            print(colored(head, "blue", attrs=["bold"]))
            for tournament in self.tournaments:
                for key, data in tournament.items():
                    print(
                        form.format(
                            key,
                            data["location"],
                            f"{str(data['nb_round'])} tours",
                            data["date_start"],
                            data["date_end"],
                            data["description"]
                        )
                    )
