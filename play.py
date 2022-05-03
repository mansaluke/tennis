from score import Score
from side import Side, Points
from game_test import Game


class NoWinnerException(Exception):
    """Raised when no winner is found"""
    pass


class Executor:

    def __init__(self,
                 playable: Score,
                 show_score=False):

        self.playable: Score = playable
        self.show_score: bool = show_score
        self.rounds: int = 0
        # self.winning_side = None

    def get_vars(self, var: str):
        # e.g. for the game class the secondary var would be points
        self.playable.side1_secondary_var = self.playable.side1.__dict__[var]
        self.playable.side2_secondary_var = self.playable.side2.__dict__[var]

    def play(self):
        """
        plays rounds until winner is found
        """
        self.rounds = 0
        while not self.playable.found_winner:
            self.playable._play_round()
            if self.show_score:
                self._print_current_score()
            self.rounds += 1
            if self.rounds>self.playable.ROUND_LIMITER:
                raise NoWinnerException
        self.update_winning_side()
        return self.winning_side

    def update_winning_side(self):
        self.winning_side.__dict__[self.playable.hierarchy_lvl2]+=1

    def _print_current_score(self) -> None:
        print(
            '{0} - {1}: {2} | {3}: {4}'.format(
                self.playable.hierarchy_lvl1,
                self.playable.side1.name,
                self.playable.side1.__dict__[self.playable.hierarchy_lvl1],
                self.playable.side2.name,
                self.playable.side1.__dict__[self.playable.hierarchy_lvl2])
        )

    @property
    def point_difference(self) -> int:
        """
        returns the difference in points between both sides
        """
        return abs(
            self.playable.side1.__dict__[self.playable.hierarchy_lvl1] - self.playable.side2.__dict__[self.playable.hierarchy_lvl1])

    @property
    def total_wins(self) -> int:
        """
        returns the total number of wins of both sides
        """
        return self.playable.side1.__dict__[self.playable.hierarchy_lvl1] + self.playable.side2.__dict__[self.playable.hierarchy_lvl2]

    @property
    def winning_score(self) -> int:
        """
        returns score of winning side
        """
        # self.get_vars(self.hierachy[self.playable.hierarchy_lvl-1])
        return max(self.playable.side1.__dict__[self.playable.hierarchy_lvl1], self.playable.side2.__dict__[self.playable.hierarchy_lvl1])

    @property
    def winning_side(self) -> Side:
        """
        returns winning side
        """
        if self.playable.side1.__dict__[self.playable.hierarchy_lvl1]==self.winning_score:
            return self.playable.side1
        if self.playable.side2.__dict__[self.playable.hierarchy_lvl1]==self.winning_score:
            return self.playable.side2


if __name__=="__main__":
    a = Side()
    b = Side()

    g1 = Executor(Game(a, b), True)
    print(f'Winner: {g1.play()}')
