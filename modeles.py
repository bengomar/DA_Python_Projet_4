
class Tournament:
    def __init__(
        self, name: str, location: str, date_start: int, date_end: int, nb_round: int
    ):
        self.name = name
        self.location = location
        self.date_start = date_start
        self.date_end = date_end
        self.nb_round = nb_round

class Player:
    def __init__(
        self, ident: str, surname: str, firstname: str, date_of_birth: str
    ):
        self.ident = ident
        self.surname = surname
        self.firstname = firstname
        self.date_of_birth = date_of_birth

class SearchPlayerIdent:
    def __init__(self, ident: str):
        self.ident = ident

class Rounds:
    def __init__(self, round_id, matchs):
        self.round_id = round_id
        self.matchs = matchs


class Matchs:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent
        self.players = [[player, 0], [opponent, 0]]
