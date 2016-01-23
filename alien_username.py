import re

for _ in xrange(input()):
    if re.match(r'^[\._][\d]+[a-zA-Z]*_?$', raw_input()):
        print "VALID"
    else:
        print 'INVALID'