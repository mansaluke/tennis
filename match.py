from tennis_set import TennisSet, Side
from score import Score


class Match(Score):
    """
    Match implementation of Score class
    """
    TOTAL_SETS = 3

    def __init__(self,
                 side1: Side,
                 side2: Side,
                 show_score=False):

        self.show_score = show_score
        super().__init__(
            3,
            round_limiter=Match.TOTAL_SETS,
            side1=side1,
            side2=side2,
            show_score=show_score)

    def _play_round(self):
        new_set = TennisSet(self.side1, self.side2, self.show_score)
        new_set.play()

    @property
    def found_winner(self) -> bool:
        return self.rounds==self.TOTAL_SETS


if __name__=="__main__":
    a = Side()
    b = Side()

    g1 = Match(a, b, show_score=True)
    print(f'Winner: {g1.play()}')
