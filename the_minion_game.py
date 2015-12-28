s = raw_input().strip()
V = 'AEIOU'
consonant = 0
vowel = 0

for i, j in enumerate(s):
    if j in V:
        vowel += len(s) - i
    else:
        consonant += len(s) - i

if vowel < consonant:
    print 'Stuart', consonant
elif vowel == consonant:
    print 'Draw'
else:
    print 'Kevin', vowel
