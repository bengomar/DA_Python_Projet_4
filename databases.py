from tinydb import TinyDB, Query, where
from views import PlayerView

class Tinydb:
    db = TinyDB("db.json")
    players = db.table("players")
    tournaments = db.table("tournaments")
    query = Query()

    def players_list(self):
        npa = 0
        player_list_to_tournament = []
        for player in self.players:
            npa += 1
            ident = player.get('ident')
            surname = player.get('surname')
            firstname = player.get('firstname')
            player_info = [npa, ident, surname, firstname]
            player_list_to_tournament.append(player_info)
        #print(player_list_to_tournament)
        for player in player_list_to_tournament:
            print(f"  {player[0]}. {player[1]} {player[2]},{player[3]}")
        print("")
        return player_list_to_tournament
    def check_table_players(self):
        """Parcourir la table players"""
        for player in self.players:
            print(player)

    def check_table_tournaments(self):
        """Parcourir la table tournaments"""
        for tournament in self.tournaments:
            print(tournament)

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

        find_player = Tinydb.players.search(where("ident") == self.ident)

        if not find_player:
            print(f"{self.ident} n'existe pas !")
        else:
            for player in find_player:
                print(f"Confirmez-vous la suppression de {player.get('surname')} {player.get('firstname')} (Y/N):")
            confirm = PlayerView().confirm_delete_player()

            if (confirm == "y") or (confirm == "Y"):
                Tinydb.players.remove(where("ident") == self.ident)
                print(f"{self.ident}{player.get('surname')}, {player.get('firstname')} a été supprimé")
                print("")
            elif (confirm == "n") or (confirm == "N"):
                print(f"Suppression de {self.ident}{player.get('surname')}, {player.get('firstname')} annulée")
            else:
                print("Saisie incorrecte (y/n ou Y/N)")
                Tinydb().del_player(self.ident)

