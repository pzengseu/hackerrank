import re

for _ in xrange(input()):
    for m in re.finditer(r'(?<!^)#([a-f0-9]{6}|[a-f0-9]{3})', raw_input(), re.I):
        print m