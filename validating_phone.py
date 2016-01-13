import re

pat = re.compile(r'^[7-9]\d{9}$')
for _ in xrange(input()):
    print 'YES' if re.match(pat, raw_input()) else 'NO'