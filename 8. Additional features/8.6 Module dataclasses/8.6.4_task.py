from dataclasses import dataclass, field


@dataclass(order=True)
class FootballPlayer:
    name: str = field(compare=False)
    surname: str = field(compare=False)
    value: int = field(repr=False)


class FootballTeam:
    name: str
    players: list = field(repr=False, compare=False, init=False, default_factory=list)

    def add_players(self, *args):
        for player in args:
            self.players.append(player)