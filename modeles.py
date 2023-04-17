class Tournament:
    rounds = []

    def __init__(
        self,
        name: str,
        location: str,
        date_start: str,
        date_end: str,
        nb_round: str,
        description: str,
    ):
        self.name = name
        self.location = location
        self.date_start = date_start
        self.date_end = date_end
        self.nb_round = nb_round
        self.description = description


class Player:
    score = 0

    def __init__(
        self,
        idx: int,
        ident: str,
        surname: str,
        firstname: str,
        date_of_birth: str
    ):
        self.idx = idx
        self.ident = ident
        self.surname = surname
        self.firstname = firstname
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f"{self.ident} {self.surname} {self.firstname}"

    def __repr__(self):
        return f"{self.ident} {self.surname} {self.firstname}"


class Match:
    def __init__(self, player: str, opponent: str):
        self.players = ([player, 0], [opponent, 0])

    def __repr__(self):
        return f"{self.players}"


class Round:
    matches = []

    def __init__(self, matches: list, rounds: str):
        self.matches = matches
        self.rounds = rounds
        self.name = "Round " + str(rounds)

    def __repr__(self):
        return f"{[self.name, self.matches]}"
