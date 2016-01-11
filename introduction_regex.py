import re

pat = re.compile(r'^[+-]{0,1}(\d)*\.(\d)+$')
for _ in xrange(input()):
    print(True if re.match(pat, raw_input().strip()) else False)