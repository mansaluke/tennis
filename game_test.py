import random
from side import Side, Points
from score import Score


class Game(Score):
    """
    Game implementation of Score class
    """
    def __init__(self, Side1, Side2):

        self.hierarchy_lvl1 = 'points'
        self.hierarchy_lvl2 = 'matches_won'
        self.ROUND_LIMITER = 100
        self._MIN_POINTS_TO_WIN = 4
        self._MIN_POINT_DIFFERENCE_TO_WIN = 2
        self.side1 = Side1
        self.side2 = Side2

    def _play_round(self) -> None:
        side_to_win_point = random.randint(0, 1)
        if side_to_win_point==0:
            self.side1.points += 1
        elif side_to_win_point==1:
            self.side2.points += 1
        else:
            raise ValueError('Non-binary number not valid')

    @property
    def found_winner(self) -> bool:
        return (self.total_wins>=self._MIN_POINTS_TO_WIN
            and self.point_difference>self._MIN_POINT_DIFFERENCE_TO_WIN)
