from abc import ABC, abstractmethod
from side import Side


class NoWinnerException(Exception):
    """Raised when no winner is found"""
    pass


class Score(ABC):
    """
    Abstract class implementation of the scores and generic game characteristics
    These methods are used in game.py, match.py an side.py
    Contains abstract methods _play_round and found_winner which should be defined
    in the subclasses
    Also contains generic non-abstract method to ensure DRY code.
    """
    hierachy = {
        0: 'points',
        1: 'games_won',
        2: 'sets_won',
        3: 'matches_won'
    }

    def __init__(self,
                 lvl:int,
                 round_limiter: int,
                 side1: Side,
                 side2: Side,
                 show_score=False):

        self.lvl = lvl
        self.side1: Side = side1
        self.side2: Side = side2
        self.side1.points = 0
        self.side2.points = 0
        self.show_score = show_score
        self.rounds = 0
        self.round_limiter = round_limiter

        self.side1_secondary_var = None
        self.side2_secondary_var = None

    def get_vars(self, var: str):
        # e.g. for the game class the secondary var would be points
        self.side1_secondary_var = self.side1.__dict__[var]
        self.side2_secondary_var = self.side2.__dict__[var]

    def play(self):
        self.rounds = 0
        while not self.found_winner:
            self._play_round()
            if self.show_score:
                self._print_current_score()
            self.rounds += 1
            if self.rounds>self.round_limiter:
                raise NoWinnerException
        self.update_winning_player()
        return self.winning_player

    @abstractmethod
    def _play_round(self):
        pass

    def update_winning_player(self):
        self.winning_player.__dict__[self.hierachy[self.lvl]]+=1

    def _print_current_score(self) -> None:
        var = self.hierachy[self.lvl-1]
        self.get_vars(var)
        print(
            '{0} - {1}: {2} | {3}: {4}'.format(
                var,
                self.side1.name,
                self.side1_secondary_var,
                self.side2.name,
                self.side2_secondary_var)
        )

    @property
    def point_difference(self) -> int:
        self.get_vars(self.hierachy[self.lvl-1])
        return abs(self.side1_secondary_var - self.side2_secondary_var)

    @property
    def total_wins(self) -> int:
        self.get_vars(self.hierachy[self.lvl-1])
        return self.side1.points + self.side2.points

    @property
    @abstractmethod
    def found_winner(self) -> bool:
        pass

    @property
    def winning_score(self) -> Side:
        # self.get_vars(self.hierachy[self.lvl-1])
        return max(self.side1.points, self.side2.points)

    @property
    def winning_player(self) -> Side:
        self.get_vars(self.hierachy[self.lvl-1])
        if self.side1.points==self.winning_score:
            return self.side1
        if self.side2.points==self.winning_score:
            return self.side2
