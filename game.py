import random
from side import Side
from score import Score


class Game(Score):
    """
    Game implementation of Score class
    """
    _MIN_POINTS_TO_WIN = 4
    _MIN_POINT_DIFFERENCE_TO_WIN = 2
    ROUND_LIMITER = 100

    def __init__(self,
                 side1: Side,
                 side2: Side,
                 show_score=False):

        super().__init__(
            lvl=1,
            round_limiter=self.ROUND_LIMITER,
            side1=side1,
            side2=side2,
            show_score=show_score)

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
        return (self.total_wins>=Game._MIN_POINTS_TO_WIN
            and self.point_difference>Game._MIN_POINT_DIFFERENCE_TO_WIN)


if __name__=="__main__":
    a = Side()
    b = Side()

    g1 = Game(a, b, True)
    print(f'Winner: {g1.play()}')
