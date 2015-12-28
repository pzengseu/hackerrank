n = input()
N = 2*n - 1
M = 2*N - 1
A = 97

s = []
for i in xrange(1, N, 2):
    num = i/2
    x = n - i/2
    s.append('')
    for j in xrange(n, x, -1):
        s[num] = s[num] + chr(A + j - 1) + '-'
    s[num] = s[num] + chr(A + x - 1) + s[num][::-1]

for x in s:
    print x.center(M, '-')
s2 = ''
for i in xrange(n, 1, -1):
    s2 = s2 + chr(A + i - 1) + '-'
print s2 + chr(A) + s2[::-1]
for x in reversed(s):
    print x.center(M, '-')

