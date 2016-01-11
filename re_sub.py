import re

def aosub(m):
    if m.group(0) == '&&':
        return 'and'
    else:
        return 'or'

for _ in xrange(input()):
    # m=re.search(r'(?<=\s)[&|]{2}(?=\s)', raw_input())
    # print m.group(0)
    print re.sub(r'(?<=\s)([&\|])\1(?=\s)', aosub, raw_input())