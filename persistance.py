from tinydb import Query, TinyDB, where
from modeles import Player


class DatabasesTinydb:
    db = TinyDB("db.json")
    players = db.table("players")
    tournaments = db.table("tournaments")
    query = Query()

    def put_current_tournament_in_database(self, current_tournament, round_number):
        print("")
        print(f"{current_tournament.name=}")
        print(f"{current_tournament.location=}")
        print(f"{current_tournament.date_start=}")
        print(f"{current_tournament.date_end=}")
        print(f"{current_tournament.nb_round=}")
        print(f"{round_number=}")
        print(f"{current_tournament.rounds=}")
        print(f"{current_tournament.players=}")
        print(f"{current_tournament.description=}")
        print("")
        self.tournaments.insert(
            {
                current_tournament.name:
                    {
                        "location": current_tournament.location,
                        "date_start": current_tournament.date_start,
                        "date_end": current_tournament.date_end,
                        "nb_round": current_tournament.nb_round,
                        "current_round": round_number,
                        # "round_list": current_tournament.rounds,
                        # "players": current_tournament.players,
                        # [{"round_list": ronde} for ronde in current_tournament.rounds],
                        # [{"players": player} for player in current_tournament.players],
                        "description": current_tournament.description
                    }
            }
        )




    #
    # def sorted_players_list_ident(self):
    #     """Liste des joueurs par ordre alphabétique"""
    #
    #     player_list_alpha = []
    #     for player in self.players:
    #         ident = player.get("ident")
    #         surname = player.get("surname")
    #         firstname = player.get("firstname")
    #         date_of_birth = player.get("date_of_birth")
    #
    #         player_list_alpha.append([surname, firstname, ident, date_of_birth])
    #         # print(f"     {ident} {surname},{firstname}")
    #
    #     for alpha in sorted(player_list_alpha):
    #         print(f"{alpha[2]} {alpha[0]} {alpha[1]} {alpha[3]}")
    #
    # def tournaments_list(self):
    #     """Liste des tournois"""
    #     list_of_tournament = []
    #     for tournoi in self.tournaments:
    #         name = tournoi.get("name")
    #         location = tournoi.get("location")
    #         date_start = tournoi.get("date_start")
    #         date_end = tournoi.get("date_end")
    #         nb_round = tournoi.get("nb_round")
    #         description = tournoi.get("description")
    #         tournament_info = [
    #             name,
    #             location,
    #             date_start,
    #             date_end,
    #             nb_round,
    #             description,
    #         ]
    #         list_of_tournament.append(tournament_info)
    #     return list_of_tournament
    #
    # def check_table_tournaments(self):
    #     """Parcourir la table tournaments"""
    #     for tournament in self.tournaments:
    #         print(tournament)
    #
    # def del_player(self, ident: str):
    #     """Supprime un joueur de la table players"""
    #     self.ident = ident
    #
    #     delete_player_id = DatabasesTinydb.players.remove(where("ident") == self.ident)
    #     if not delete_player_id:
    #         print(f"{self.ident} n'existe pas !")
    #         print("")
    #     else:
    #         print(f"Le joueur immatriculé {self.ident} a été supprimé")
    #         print("")
    #
    # def search_ident_player(self, ident: str):
    #     """Recherche d'un joueur dans la table players avec son identifiant"""
    #     self.ident = ident
    #
    #     # Tinydb.players.search(where('ident') == self.ident)
    #     find_player = DatabasesTinydb.players.search(where("ident") == self.ident)
    #     print(find_player)
    #
    # def tournament_not_finish(self):
    #     tournament_without_date_end = DatabasesTinydb.tournaments.search(
    #         where("date_end") == ""
    #     )
    #
    #     number = 0
    #     for tournament_run_info in tournament_without_date_end:
    #         number += 1
    #     # print(number)
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
    # def put_tournament_end_date(self, date_end):
    #     """saisie manuelle de la fin d'un tournoi"""
    #     self.date_end = date_end
    #
    #     print("Sélectionnez le tournoi")
    #     DatabasesTinydb().get_tournament("")
    #     # Tinydb.tournaments.update({'date_end': self.date_end}, Tinydb.query.date_end == '')
    #
    # def score_update_player(self, ident: str, score: int):
    #     """Mise à jour du score d'un joueur"""
    #     self.ident = ident
    #     self.score = score
    #
    #     DatabasesTinydb.players.update(
    #         {"score": self.score}, DatabasesTinydb.query.ident == self.ident
    #     )
    #
    # def add_competitors(
    #         self, ident: str, surname: str, firstname: str, score: int = 0
    # ):
    #     """Ajout d'un joueur à la table competitors"""
    #     self.ident = ident
    #     self.surname = surname
    #     self.firstname = firstname
    #     self.score = score
    #
    #     self.competitors.insert(
    #         {
    #             "ident": self.ident,
    #             "surname": self.surname,
    #             "firstname": self.firstname,
    #             "score": self.score,
    #         }
    #     )
    #
    # def tournaments_list_formated(self):
    #     """Parcourir la table tournaments"""
    #     print("Liste des tournois:")
    #     print("Nom du tournoi, Lieu, Date de début, Date de fin")
    #     for tournoi in self.tournaments:
    #         print(
    #             f"{tournoi.get('name')}, {tournoi.get('location')}, {tournoi.get('date_start')}, {tournoi.get('date_end')}, {tournoi.get('nb_round')} rounds"
    #         )
