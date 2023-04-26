from pprint import pprint

from termcolor import colored
from tinydb import Query, TinyDB


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
            round_matches = []
            for match in ronde.matches:
                players = [[player[0].__dict__, player[1]] for player in match.players]
                round_matches.append({"players": players})
            ronde_dict = {"matches": round_matches, "name": ronde.name}
            round_json.append(ronde_dict)
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
                "description": current_tournament.description,
            }
        )

    def tournaments_list_formated(self):
        """Parcourir la table tournaments"""
        form = "{0:20}{1:15}{2:10}{3:15}{4:15}{5:}"

        print("Liste des tournois:")
        head = form.format(
            "Nom du tournoi",
            "Lieu",
            "Rounds",
            "Date de début",
            "Date de fin",
            "Remarques générales",
        )
        print(colored(head, "blue", attrs=["bold"]))
        for tournament in self.tournaments:
            print(
                form.format(
                    tournament.get("name"),
                    tournament.get("location"),
                    tournament.get("nb_round"),
                    tournament.get("date_start"),
                    tournament.get("date_end"),
                    tournament.get("description"),
                )
            )

    def check_table_players(self):
        """Parcourir la table players"""
        if not self.players:
            print(colored('La table "players" est vide !', "red", attrs=["bold"]))
        else:
            print(colored('Table "players":', "blue", attrs=["bold"]))
            for player in self.players:
                print(f"{player}")

    def check_table_tournaments(self):
        """Parcourir la table tournaments"""
        if not self.tournaments:
            print(colored('La table "tournaments" est vide !', "red", attrs=["bold"]))
        else:
            print(colored('Table "tournaments":', "blue", attrs=["bold"]))
            for tournament in self.tournaments:
                pprint(f"{tournament=}")

    def truncate_table_players(self):
        """Vider la table players"""
        self.players.truncate()
        print(colored('La table "players" a été vide !', "blue", attrs=["bold"]))

    def truncate_table_tournaments(self):
        """Vider la table tournaments"""
        self.tournaments.truncate()
        print(colored('La table "tournaments" a été vide !', "blue", attrs=["bold"]))

    def add_eight_players(self):
        """Charger la table \"players\" de 8 joueurs"""
        self.players.truncate()
        eight_players_list = [
            {
                "ident": "DZ12346",
                "surname": "BELLOUMI",
                "firstname": "Lakhdar",
                "date_of_birth": "21-02-1952",
            },
            {
                "ident": "CA12345",
                "surname": "CARLOS",
                "firstname": "Roberto",
                "date_of_birth": "01-06-2001",
            },
            {
                "ident": "ME45699",
                "surname": "MESSI",
                "firstname": "Lionel",
                "date_of_birth": "01-06-1999",
            },
            {
                "ident": "ZE99663",
                "surname": "ZINEDINE",
                "firstname": "Zidane",
                "date_of_birth": "01-02-1975",
            },
            {
                "ident": "BE66993",
                "surname": "BENZEMA",
                "firstname": "Karim",
                "date_of_birth": "06-12-1999",
            },
            {
                "ident": "VI22215",
                "surname": "VIERA",
                "firstname": "Patrick",
                "date_of_birth": "06-08-1982",
            },
            {
                "ident": "LI58871",
                "surname": "LIZARAZU",
                "firstname": "Bixente",
                "date_of_birth": "11-11-1980",
            },
            {
                "ident": "MA96333",
                "surname": "MADJER",
                "firstname": "Rabah",
                "date_of_birth": "16-05-1968",
            },
        ]

        print(colored('Table "players" créé:', "blue", attrs=["bold"]))
        for player in eight_players_list:
            self.players.insert(player)
            print(player)
