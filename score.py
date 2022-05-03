from abc import ABC, abstractmethod
from side import Side, Points


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

        self.hierarchy_lvl1 = 'points'
        self.hierarchy_lvl2 = 'matches_won'
        self.side1_secondary_var = None
        self.side2_secondary_var = None

    @abstractmethod
    def _play_round(self):
        pass

    def update_winning_side(self):
        self.winning_side[self.hierarchy_lvl2]+=1

    def _print_current_score(self) -> None:
        print(
            '{0} - {1}: {2} | {3}: {4}'.format(
                self.hierarchy_lvl1,
                self.side1.name,
                self.side1[self.hierarchy_lvl1],
                self.side2.name,
                self.side2[self.hierarchy_lvl1])
        )

    @property
    def point_difference(self) -> int:
        """
        returns the difference in points between both sides
        """
        return abs(self.side1.__dict__[self.hierarchy_lvl1] - self.side2.__dict__[self.hierarchy_lvl1])

    @property
    def total_wins(self) -> int:
        """
        returns the total number of wins of both sides
        """
        return self.side1.points + self.side2.points

    @property
    @abstractmethod
    def found_winner(self) -> bool:
        """
        returns True if winner has been found, else False
        """
        pass

    @property
    def winning_score(self) -> int:
        """
        returns score of winning side
        """
        return max(self.side1.points, self.side2.points)

    @property
    def winning_side(self) -> Side:
        """
        returns winning side
        """
        if self.side1.points==self.winning_score:
            return self.side1
        if self.side2.points==self.winning_score:
            return self.side2
