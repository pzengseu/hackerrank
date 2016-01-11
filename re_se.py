# import re
#
# s = raw_input().strip()
# k = raw_input().strip()
# result = []
# i = 0
# while i <= len(s) -len(k):
#     m = re.search(k, s[i:])
#     if m: result.append((m.start()+i, m.end()+i-1))
#     i += 1
#
# if not result: print (-1, -1)
# else:
#     for x in sorted(set(result), key = lambda x: x[0]):
#         print x

import re
S = raw_input()
k = raw_input()
anymatch = 'No'
for m in re.finditer(r'(?=('+k+'))',S):
    anymatch = 'Yes'
    print (m.start(0),m.end(0))
if anymatch == 'No':
    print (-1, -1)