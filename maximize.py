from itertools import product
k, m = map(int, raw_input().split())
arr = []
for _ in xrange(k):
    arr.append(map(int, raw_input().split()))

print list(product(*arr))
s = []
for l in list(product(*arr)):
    s.append(sum(map(lambda x: x**2, l)))

print s
print max(s)