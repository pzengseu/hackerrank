import numpy

n, m = map(int, raw_input().split())
na = numpy.array([map(int, raw_input().split()) for _ in xrange(n)])
nm = numpy.array([map(int, raw_input().split()) for _ in xrange(n)])

print numpy.add(na, nm)
print numpy.subtract(na, nm)
print numpy.multiply(na, nm)
print numpy.divide(na, nm, dtype=int)
print numpy.mod(na, nm, dtype=int)
print numpy.power(na, nm, dtype=int)