#!/bin/python
from __future__ import print_function
from collections import deque

d = deque()
for _ in xrange(input()):
    s = raw_input().split()
    if s[0] == 'append':
        d.append(s[1])
    if s[0] == 'appendleft':
        d.appendleft(s[1])
    if s[0] == 'pop':
        d.pop()
    if s[0] == 'popleft':
        d.popleft()

[print(int(x), end=" ") for x in d]