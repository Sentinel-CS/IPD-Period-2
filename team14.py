# -*- coding: utf-8 -*-
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Ω' # Only 10 chars displayed.
strategy_name = 'Pavlov strategy'
strategy_description = 'Looks at what has worked out in the past'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    if len(my_history)<5:
        if len(my_history)== 0:
            return 'c'
        if len(my_history)>0:
            return their_history[-1]
    points = [0,1]
    index_B = 0
    index_C = 0
    for i in range(len(my_history)-6, len(my_history)):
        if my_history[i] == 'c' and their_history[i]=='b':
            points[0] += -500
            index_C += 1
        if my_history[i] == 'b' and their_history[i]=='b':
            points[1] += -250
            index_B += 1
        if my_history[i] == 'b' and their_history[i]=='c':
            points[1] += 100
            index_B += 1
        if my_history[i] == 'c' and their_history[i] == 'c':
            points[0] += 0
    if len(my_history)>=5:
        if index_B>0 and index_C>0 and (points[1]/index_B) > (points[0]/index_C):#more average points on b return b
            return 'b'
        elif index_B>0 and index_C>0 and (points[0]/index_C) > (points[1]/index_B):#more average points on c return c
            return 'c'
        else:
            return their_history[-1]
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
