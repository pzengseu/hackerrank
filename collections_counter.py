from collections import Counter

n, counts = input(), Counter(map(int, raw_input().split()))
sum = 0
for _ in xrange(input()):
    m, p = map(int, raw_input().split())
    if m in counts:
        if counts[m] > 0:
            counts[m] -= 1
            sum += p

print sum
