import numpy

n, m = map(int, raw_input().split())
print numpy.max(numpy.min(numpy.array([map(int, raw_input().split()) for _ in xrange(n)]), axis=1))