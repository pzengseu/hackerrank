import numpy

n, m = map(int, raw_input().split())
na = numpy.array([map(int, raw_input().split()) for _ in xrange(n)])

print numpy.mean(na, axis=1)
print numpy.var(na, axis=0)
print numpy.std(na)