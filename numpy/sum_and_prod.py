import numpy

n, m = map(int, raw_input().split())
print numpy.prod(numpy.sum(numpy.array([map(int, raw_input().split()) for _ in xrange(n)]), axis=0))