for _ in xrange(input()):
    n, m = map(int, raw_input().split())
    print('NO' if sum([1 if x<=0 else 0 for x in map(int, raw_input().split())])>= m else 'YES')

