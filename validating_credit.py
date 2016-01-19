import re

for _ in xrange(input()):
    s = raw_input()
    ds = ''.join(s.split('-'))
    print 'Valid' if re.match(r'^[4-6][0-9]{3}(-[0-9]{4}|[0-9]{4}){3}$', s) and not re.search(r'.*(.)\1{3}.*', ds) else 'Invalid'
