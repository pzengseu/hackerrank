import re

for _ in xrange(input()):
    pat = r'<a.*?href="(.*?)".*?>(.*?)</a>'
    m=re.findall(pat,raw_input())
    for x in m:
        pat2 = r'(<.*?>([^<>]+)<.*?>|(^[^<>]+$))'
        t=re.search(pat2,x[1])
        if t:
            if t.group(2):
                print x[0]+','+t.group(2).strip()
            else:
                print x[0]+','+t.group(3).strip()
        else:
            print x[0]+','