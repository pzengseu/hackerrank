from collections import OrderedDict

od = OrderedDict()
for _ in xrange(input()):
    s = raw_input().split()
    od.setdefault(' '.join(s[:-1]), 0)
    od[' '.join(s[:-1])] += int(s[-1])

for x in od:
    print x, od[x]