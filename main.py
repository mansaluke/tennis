from tournament import Tournament

SHOW_SCORES = True  # set to True to show results of each point, game, set and match
NUMBER_OF_SIDES = 2  # number of sides (singles or doubles)


def main():
    # Starting new tournament
    t1 = Tournament(number_of_sides=NUMBER_OF_SIDES)

    # Play
    winner = t1.play(show_scores=SHOW_SCORES)
    print(f'winner: {winner}!')


if __name__=="__main__":
    main()
