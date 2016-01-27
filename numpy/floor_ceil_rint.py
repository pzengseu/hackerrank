import numpy

l = map(float, raw_input().split())
ln = numpy.array(l)
print numpy.floor(ln)
print numpy.ceil(ln)
print numpy.rint(ln)