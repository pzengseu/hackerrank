import re

pats = [
    r'^[a-zA-Z0-9]{10}$',
    r'([A-Z].*){2}',
    r'([\d].*){3}',
]
repeat = r'.*(.).*\1'
for _ in xrange(input()):
    s = raw_input()

    print("Valid" if all([re.search(r, s) for r in pats]) and not re.search(repeat, s) else 'Invalid')