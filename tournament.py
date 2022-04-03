from typing import List
from match import Match, Side


class Tournament:
    """
    Implementation of tournament class which runs matches
    for a specified number of sides
    where the side is the player (single) or double
    """
    def __init__(self, number_of_sides: int=2):
        self.number_of_sides = self.check_number_of_sides(number_of_sides)
        self.sides = self.create_sides()
        print(f'All sides: {self.sides}')

    def check_number_of_sides(self, number_of_sides: int):
        if number_of_sides<2 or number_of_sides>64:
            raise ValueError("Out of bounds")
        return number_of_sides

    def create_sides(self):
        return [Side() for i in range(self.number_of_sides)]

    def _pair_sides(self, all_sides: List) -> List:
        pairs = []
        for i in range(0, len(all_sides), 2):
            try:
                new_pair = (all_sides[i+0], all_sides[i+1])
                pairs.append(new_pair)
            except IndexError:
                # when odd number of players
                single_side = (all_sides[i+0])
                # print(f'{single_side} does not have a pair')
                pairs.append(single_side)
        return pairs

    def play(self, show_scores=False) -> Side:
        sides_available = self.sides

        while len(sides_available)>1:
            _pairs = self._pair_sides(sides_available)
            sides_available = []
            for pair in _pairs:
                if isinstance(pair, tuple):
                    match_winner = Match(pair[0], pair[1], show_score=show_scores).play()
                else:
                    match_winner = pair
                sides_available.append(
                    match_winner
                )

        if len(sides_available)!=1:
            raise ValueError('Unexpected number of sides returned')
        return sides_available[0]
