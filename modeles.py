
class Tournament:
    def __init__(
        self, name: str, location: str, date_start: int, date_end: int, nb_round: int
    ):
        self.name = name
        self.location = location
        self.date_start = date_start
        self.date_end = date_end
        self.nb_round = nb_round
        # TODO: How is link a tournament rounds?

class Player:
    def __init__(
        self, ident: str, surname: str, firstname: str, date_of_birth: str
    ):
        self.ident = ident
        self.surname = surname
        self.firstname = firstname
        self.date_of_birth = date_of_birth

# TODO: Is this one really necessary?
class SearchPlayerIdent:
    def __init__(self, ident: str):
        self.ident = ident

# TODO: Name using singular
# TODO: Not used in the project?
class Rounds:
    def __init__(self, round_id, matchs):
        self.round_id = round_id
        self.matchs = matchs

# TODO: Name using singular
#   Not used in the project?
class Matchs:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent
        self.players = [[player, 0], [opponent, 0]]
