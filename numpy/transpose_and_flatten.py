import numpy

n, m = map(int, raw_input().split())
l = []
for _ in xrange(n):
    l.append(map(int, raw_input().split()))

my_array = numpy.array(l)
print numpy.transpose(my_array)
print my_array.flatten()