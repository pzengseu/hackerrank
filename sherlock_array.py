for _ in xrange(input()):
    s = 'NO'
    n = input()
    a = map(int, raw_input().split())
    b = a[0]
    c = sum(a[2:])
    if b == c:
        s = 'YES'
    for i in range(1, n-2):
        b += a[i]
        c -= a[i+1]
        if b == c:
            s = 'YES'
            break
    if n == 1:
        s = 'YES'
    print s
