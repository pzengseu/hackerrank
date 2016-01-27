import re

text = []
[ text.append(raw_input().strip()) for _ in xrange(input()) ]
print reduce(lambda x,y: x+";"+y, sorted(set(re.findall(r'(?<![\w\.])[\w]+(?:\.\w+)*@[\w]+(?:\.\w+)*', ' '.join(text)))))