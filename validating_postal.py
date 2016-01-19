import re

s = raw_input()
print len(re.findall(r'(?=(\d)\d\1)', s)) <= 1 and re.match(r'^[1-9][\d]{5}$',s) != None