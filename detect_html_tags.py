import re

s = list()
for _ in xrange(input()):
    r = raw_input()
    l = re.findall(r'<\s*([\w]+).*?>', r)
    s.extend(l)
    # if re.search(r'\[.*\]\(.*\)',r):
    #     s.append('a')

print reduce(lambda x,y: x+';'+y, sorted(set(s)))
