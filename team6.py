####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'team_name' # Only 10 chars displayed.
strategy_name = 'Strategy Identification'
strategy_description = 'It tries to define the opponents strategy and react accordingly.'
    
def move(my_history, their_history, my_score, their_score):
    
   # If the other player has betrayed or this is the last half of the game, 
    if len(my_history) < 6: 
        return 'c'
        return 'b'
        return 'b'
        return 'c'
        return 'c'
        return 'b'
    else:
        if 'cbbcc' in their_history:
            if their_history[-1]=='b' and their_history[-2]=='b':
                return 'b'
            else:
                return 'c'
        elif 'cccccc' in their_history:
            return 'b'
        elif 'bbbbb' in their_history:
            return 'b'
        else:
            return 'b'
            
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             
