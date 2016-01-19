import re

pat = r'(?<=[A-Za-z0-9])[\s!@#$%&]{1,}(?=[A-Za-z0-9])'
n, m = map(int, raw_input().split())
origin = []
for _ in xrange(n):
    origin.append(list(raw_input()))

#change = ''.join(origin[j][i] for i in xrange(m) for j in xrange(n))
change = "".join("".join(decode) for decode in zip(*origin))
print re.sub(pat, ' ', change)