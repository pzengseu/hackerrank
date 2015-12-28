from collections import namedtuple
n = input()
score = namedtuple('score', raw_input().split())
print('%.2f' % (reduce(lambda x, y: x+y, [int(score(*raw_input().split()).MARKS) for _ in xrange(n)])/float(n)))