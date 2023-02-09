from tinydb import TinyDB, Query, where


class Tinydb:
    db = TinyDB("db.json")
    players = db.table("players")
    tournaments = db.table("tournaments")
    query = Query()

    def check_table_players(self):
        """Parcourir la table players"""
        for player in self.players:
            print(player)

    def check_table_tournaments(self):
        """Parcourir la table tournaments"""
        for tournament in self.tournaments:
            print(tournament)

    def add_player(
        self, ident: int, surname: int, firstname: int, date_of_birth: int
    ):
        """Ajout d'un joueur à la table players"""
        self.ident = ident
        self.surname = surname
        self.firstname = firstname
        self.date_of_birth = date_of_birth

        Tinydb.players.insert(
            {
                "ident": self.ident,
                "surname": self.surname,
                "firstname": self.firstname,
                "date_of_birth": self.date_of_birth,
            }
        )

    def del_player(self, ident: str):
        """Supprime un joueur de la table players"""
        self.ident = ident

        delete_player_id = Tinydb.players.remove(where("ident") == self.ident)
        if not delete_player_id:
            print(f"{self.ident} n'existe pas !")
            print("")
        else:
            print(f"Le joueur immatriculé {self.ident} a été supprimé")
            print("")

    def search_ident_player(self, ident: str):
        """Recherche d'un joueur dans la table players avec son identifiant"""
        self.ident = ident

        # Tinydb.players.search(where('ident') == self.ident)
        find_player = Tinydb.players.search(where("ident") == self.ident)
        print(find_player)

    def add_tournament(
        self, name: str, location: str, date_start: int, date_end: int, nb_round: int
    ):
        """Ajout d'un tournoi à la table players"""
        self.name = name
        self.location = location
        self.date_start = date_start
        self.date_end = date_end
        self.nb_round = nb_round

        Tinydb.tournaments.insert(
            {
                "name": self.name,
                "location": self.location,
                "date_start": self.date_start,
                "date_end": self.date_end,
                "nb_round": self.nb_round,
            }
        )

    def tournament_not_finish(self):
        tournament_without_date_end = Tinydb.tournaments.search(where("date_end") == "")

        number = 0
        for tournament_run_info in tournament_without_date_end:
            number += 1
        #print(number)

    def get_tournament(self):
        """recherche de tournoi en cours (n'ayant pas de date de fin)"""

        end_date_get = Tinydb.tournaments.search(where("date_end") == '')

        number_t = 0
        # TournamentView().running_tournament()
        print("")
        print("CENTRE ÉCHECS - Tournois")
        print("")
        print("Tournoi(s) en cours:")

        for tournament_run in end_date_get:
            number_t += 1
            print(
                f"   {number_t}. Tournoi {tournament_run.get('name')}, {tournament_run.get('location')} "
            )

    def put_tournament_end_date(self, date_end):
        """saisie manuelle de la fin d'un tournoi"""
        self.date_end = date_end

        print("Sélectionnez le tournoi")
        Tinydb().get_tournament("")
        # Tinydb.tournaments.update({'date_end': self.date_end}, Tinydb.query.date_end == '')

    def score_update_player(self, ident: int, score: int):
        """Mise à jour du score d'un joueur"""
        self.ident = ident
        self.score = score

        Tinydb.players.update({"score": self.score}, Tinydb.query.ident == self.ident)
