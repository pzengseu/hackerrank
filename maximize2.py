from itertools import product
k, m = map(int, raw_input().split())

print max(map(lambda y: sum(y) % m, list(product(*[map(lambda x: int(x)**2, raw_input().split()) for _ in xrange(k)]))))
