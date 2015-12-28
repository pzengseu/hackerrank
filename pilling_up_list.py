#!/bin/python

from collections import  deque

for _ in xrange(input()):
    t = True
    n = input()
    d = deque(map(int, raw_input().split()))
    mi = 0
    for _ in xrange(n-1):
        mi = d.pop() if d[0]<d[-1] else d.popleft()
        if d[0] > mi or d[-1] > mi:
            t = False
            break
    if mi < d[0]:
        t = False

    if t:
        print 'Yes'
    else:
        print 'No'

