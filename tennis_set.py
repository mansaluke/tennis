from game import Side, Game
from score import Score


class TennisSet(Score):
    """
    Match implementation of Score class
    """
    _MINIMUM_NUMBER_OF_GAMES = 6
    _MIN_POINT_DIFFERENCE_TO_WIN = 2
    ROUND_LIMITER = 100

    def __init__(self,
                 side1: Side,
                 side2: Side,
                 show_score=False):

        self.show_score = show_score

        super().__init__(
            2,
            round_limiter=self.ROUND_LIMITER,
            side1=side1,
            side2=side2,
            show_score=show_score
        )

    def _play_round(self):
        new_game = Game(self.side1, self.side2, self.show_score)
        new_game.play()

    @property
    def found_winner(self) -> bool:
        return (self.rounds>=TennisSet._MINIMUM_NUMBER_OF_GAMES
            and self.point_difference>TennisSet._MIN_POINT_DIFFERENCE_TO_WIN)


if __name__=="__main__":
    a = Side()
    b = Side()

    g1 = TennisSet(a, b, show_score=True)
    print(f'Winner: {g1.play()}')
