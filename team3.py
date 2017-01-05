team_name = "Team 3"
strategy_name = "A strange recent history meter with changing variables"
strategy_description = "At this point, we don't really know..."


def team3(my_history, their_history, my_score, their_score):
    if len(my_history) < 1:
        return 'b'
    else:
        choice = their_history[-1:]
        return choice
