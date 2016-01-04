import re
pat = re.compile(r'^[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$')
print sorted(filter(lambda x:re.match(pat, x), [raw_input() for _ in xrange(input())]))
