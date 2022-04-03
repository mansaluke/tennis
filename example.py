from tournament import Tournament

SHOW_SCORES = True  # set to True to show results of each point, game, set and match
NUMBER_OF_SIDES = 33  # number of sides (singles or doubles)

# Starting new tournament
t1 = Tournament(number_of_sides=NUMBER_OF_SIDES)

# Play
winner = t1.play(show_scores=SHOW_SCORES)
print(f'winner: {winner}!')
