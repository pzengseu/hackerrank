#!/bin/python

from collections import Counter
for i in sorted(Counter(raw_input()).items(), key = lambda x:(-x[-1], x[0]))[:3]:
    print i[0], i[1]