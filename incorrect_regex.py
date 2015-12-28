import re
import exceptions

for _ in xrange(input()):
    try:
        re.compile(raw_input().strip())
    except exceptions.Exception as e:
        print False
    else:
        print True