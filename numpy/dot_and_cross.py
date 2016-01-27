import numpy

n = int(raw_input().strip())
na = numpy.array([map(int, raw_input().split()) for _ in xrange(n)])
nb = numpy.array([map(int, raw_input().split()) for _ in xrange(n)])

print numpy.dot(na, nb)