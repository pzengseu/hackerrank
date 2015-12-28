#!/bin/python
from __future__ import print_function
from collections import  OrderedDict

od = OrderedDict()
for _ in xrange(input()):
    s = raw_input()
    if s in od:
        od[s] += 1
    else:
        od[s] = 1

print(len(od))
[print(od[x], end=' ') for x in od]