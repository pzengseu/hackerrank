n, m = map(int, raw_input().split())
a=[map(int, raw_input().split()) for _ in xrange(n)]
s=input()
for l in sorted(a, key=lambda x: x[s]):
    print ' '.join(map(str, l))
