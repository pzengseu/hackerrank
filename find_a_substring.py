import re

nums = []
s= []
ss = []
for _ in xrange(input()):
    s.append(raw_input())

for _ in xrange(input()):
    ss.append(raw_input())

s = ' '.join(s)

for i in xrange(len(ss)):
    nums.append(len(re.findall(r'[\w]+'+ss[i]+'[\w]+', s)))

print reduce(lambda x,y: str(x)+'\n'+str(y), nums)


