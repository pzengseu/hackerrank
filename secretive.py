'''
The program of Eight Queens problem.
'''

def conflict(state, nextX):
    nextY = len(state)
    for i in xrange(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False

def queens(num = 8, state = ()):
    for pos in xrange(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                print state + (pos,)
                return pos
            else:
                queens(num, state + (pos,))

queens(8)