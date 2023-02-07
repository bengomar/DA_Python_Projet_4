class Tournament:
    def __init__(self, name: str, location: str, date_start: int, date_end: int, nb_round: int):
        self.name = name
        self.location = location
        self.date_start = date_start
        self.date_end = date_end
        self.nb_round = nb_round

class Player:
    def __init__(self, ident: str, surname: str, firstname: str, date_of_birth: str, score: int):
        self.ident = ident
        self.surname = surname
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.score = score

class SearchPlayerIdent:
    def __init__(self, ident: str):
        self.ident = ident
class Choice:
    def __init__(self, choice: str):
        self.choice = choice

class Match:
    def __init__(self, player: str, opponent: str):
        self.player = player
        self.opponent = opponent
        self.players = ([player, 0], [opponent, 0])

class Rounds:

    matches = []
    def __init__(self, round: int):
        self.round = round

    def add_match(self, match: Match):
        pass
