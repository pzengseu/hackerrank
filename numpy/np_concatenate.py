import numpy

n, m, p = map(int, raw_input().split())

np = []
mp = []
for _ in xrange(n):
    np.append(map(int, raw_input().split()))

for _ in xrange(m):
    mp.append(map(int, raw_input().split()))

print np
print mp
np = numpy.array(np)
mp = numpy.array(mp)

print numpy.concatenate((np, mp))