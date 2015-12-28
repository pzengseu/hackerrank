from collections import defaultdict

n, m = map(int, raw_input().strip().split())
d = defaultdict(list)
for i in xrange(n):
    d[raw_input()].append(str(i+1))

for j in xrange(m):
    print(' '.join(d[raw_input()]))