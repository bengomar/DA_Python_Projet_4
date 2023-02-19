from tinydb import TinyDB, Query, where
#from views import PlayerView
from views import MainView

class Tinydb:
    db = TinyDB("db.json")
    players = db.table("players")
    tournaments = db.table("tournaments")
    competitors = db.table("competitors")
    query = Query()

    def players_list_ident(self):
        """Liste des joueurs par ordre alphabétique"""
        player_list_alpha = []
        for player in self.players:
            ident = player.get('ident')
            surname = player.get('surname')
            firstname = player.get('firstname')
            # TODO: Why do you convert a dictionary into a list here?
            player_list_alpha.append([surname, firstname, ident])
            #print(f"     {ident} {surname},{firstname}")
        for alpha in sorted(player_list_alpha):
            print(f"{alpha[2]} {alpha[0]} {alpha[1]}")
    def players_list(self):
        """Liste des joueurs """
        player_list_to_tournament = []
        for player in self.players:
            ident = player.get('ident')
            surname = player.get('surname')
            firstname = player.get('firstname')
            # TODO: Why do you convert a dictionary into a list here?
            #   Looks like a duplicate of the function above. is it needed?
            player_info = [ident, surname, firstname]
            player_list_to_tournament.append(player_info)
        #print(player_list_to_tournament)
        return player_list_to_tournament
    # TODO: One empty space between each function definition, use pylint to get more advanced syntax check
    def check_table_players(self):
        """Parcourir la table players"""
        for player in self.players:
            print(f"{player=}")
    def check_table_competitors(self):
        """Parcourir la table players"""
        for competitor in self.competitors:
            print(f"{competitor=}")

    def check_table_tournaments(self):
        """Parcourir la table tournaments"""
        for tournament in self.tournaments:
            print(f"{tournament=}")

    def add_tournament(
        self, name: str, location: str, date_start: int, date_end: int, nb_round: int
    ):
        """Ajout d'un tournoi à la table tournaments"""
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

    # TODO: replace del_player par delete_player
    def del_player(self, ident: str):
        # TODO: For docstrings, you can use this syntax
        #   https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html
        """Supprime un joueur de la table players"""
        self.ident = ident

        find_player = Tinydb.players.search(where("ident") == self.ident)

        if not find_player:
            print("")
            print(f"     !!! L'identifiant national \"{self.ident}\" n'existe pas !!!")
            print("")
        else:
            for player in find_player:
                print(f"Confirmez-vous la suppression de {player.get('surname')} {player.get('firstname')} (Y/N):")
            confirm = MainView().confirm_yes_no()

            if (confirm == "y") or (confirm == "Y"):
                Tinydb.players.remove(where("ident") == self.ident)
                print(f"{self.ident} {player.get('surname')}, {player.get('firstname')} a été supprimé")
                print("")
            elif (confirm == "n") or (confirm == "N"):
                print(f"Suppression de {self.ident} {player.get('surname')}, {player.get('firstname')} annulée")
            else:
                print("Saisie incorrecte (y/n ou Y/N)")
                Tinydb().del_player(self.ident)

    def add_player_tournament(
        self, ident: int, surname: int, firstname: int
    ):
        """Ajout d'un joueur à la table competitors"""
        self.ident = ident
        self.surname = surname
        self.firstname = firstname

        Tinydb.competitors.insert(
            {
                "ident": self.ident,
                "surname": self.surname,
                "firstname": self.firstname,
            }
        )

    def tournaments_list_formated(self):
        """Parcourir la table tournaments"""
        print("Liste des tournois:")
        print("Nom du tournoi, Lieu, Date de début, Date de fin")
        for tournoi in self.tournaments:
            print(f"{tournoi.get('name')}, {tournoi.get('location')}, {tournoi.get('date_start')}, {tournoi.get('date_end')}, {tournoi.get('nb_round')} rounds")