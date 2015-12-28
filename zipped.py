from __future__ import print_function
m, n = map(int, raw_input().split())
[print('%.1f' % (sum(x)/n)) for x in zip(*[map(float, raw_input().split()) for _ in xrange(n)])]