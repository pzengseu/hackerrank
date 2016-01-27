import re

s = []
nums = []
[s.append(raw_input().strip()) for _ in xrange(input())]

for _ in xrange(input()):
    nums.append(len(re.findall(r'(?<![a-zA-Z\d_])'+raw_input().strip()+'(?![a-zA-Z\d_])',' '.join(s))))

print reduce(lambda x,y: str(x)+'\n'+str(y), nums)
