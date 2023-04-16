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
                "name": current_tournament.name,
                "location": current_tournament.location,
                "date_start": current_tournament.date_start,
                "date_end": current_tournament.date_end,
                "nb_round": str(current_tournament.nb_round),
                "current_round": str(round_number),
                "players": players_json,
                "round_list": round_json,
                "description": current_tournament.description
            }
        )

    def check_table_tournaments(self):
        """Parcourir la table tournaments"""
        for tournament in self.tournaments:
            print(tournament)

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
                print(
                    form.format(
                        tournament.get('name'),
                        tournament.get('location'),
                        tournament.get('nb_round'),
                        tournament.get('date_start'),
                        tournament.get('date_end'),
                        tournament.get('description')
                    )
                )

                # for key, data in tournament.items():
                #     print(
                #         form.format(
                #             key,
                #             data['location'],
                #             f"{str(data['nb_round'])} tours",
                #             data['date_start'],
                #             data['date_end'],
                #             data['description']
                #         )
                #     )
