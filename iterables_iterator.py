from itertools import combinations
n = int(raw_input())
s = raw_input().split()
ln = list(combinations(range(1, n+1), 2))

t = []
for i, j in enumerate(s):
    if j == 'a':
        t.append(i+1)

i = 0
for x in ln:
    if x[0] in t or x[1] in t:
        i += 1

print("%.4f" % (i/float(len(ln))))
print i/float(len(ln))