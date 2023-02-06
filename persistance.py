from tinydb import TinyDB, Query, where

class Tinydb:
    db = TinyDB('db.json')
    players = db.table('players')
    tournaments = db.table('tournaments')
    query = Query()
    def check_table_players():
        """Parcourir la table players"""
        for player in Tinydb.players:
            print(player)
    def check_table_tournaments():
        """Parcourir la table tournaments"""
        for tournament in Tinydb.tournaments:
            print(tournament)
    def add_player(self, ident: int, surname: int, firstname: int, date_of_birth: int, score: int):
        """Ajout d'un joueur à la table players"""
        self.ident = ident
        self.surname = surname
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.score = score

        Tinydb.players.insert({'ident': self.ident, 'surname': self.surname, 'firstname': self.firstname, 'date_of_birth': self.date_of_birth, 'score': self.score})
    def del_player(self, ident: str):
        """Supprime un joueur de la table players"""
        self.ident = ident

        Tinydb.players.remove(where('ident') == self.ident)

    def search_ident_player(self, ident: str):
        """Recherche d'un joueur dans la table players avec son identifiant"""
        self.ident = ident

        get_player_info = Tinydb.players.search(where('ident') == self.ident)
        return get_player_info
    def add_tournament(self, name: str, location: str, date_start: int, date_end: int, nb_round: int):
        """Ajout d'un tournoi à la table players"""
        self.name = name
        self.location = location
        self.date_start = date_start
        self.date_end = date_end
        self.nb_round = nb_round

        Tinydb.tournaments.insert({'name': self.name, 'location': self.location, 'date_start': self.date_start, 'date_end': self.date_end, 'nb_round': self.nb_round})

    def get_tournament(self, date_end: int):
        """ recherche de tournoi en cours (n'ayant pas de date de fin) """
        self.date_end = date_end

        end_date_get = Tinydb.tournaments.search(where('date_end') == self.date_end)

        for t in end_date_get:
            print(t)

        number_t = 0
        print("Tournoi(s) en cours:")
        for tournoi in end_date_get:
            number_t += 1
            name = tournoi.get('name')

            print(f"   {number_t}. Tournoi {tournoi.get('name')}, {tournoi.get('location')} ")


    def put_tournament_end_date(self, date_end):
        """ saisie manuelle de la fin d'un tournoi"""
        self.date_end = date_end

        Tinydb.tournaments.update({'date_end': self.date_end}, Tinydb.query.date_end == '')

