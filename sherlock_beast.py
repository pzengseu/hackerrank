for _ in xrange(input()):
    x = input()
    y = x
    while(x%3): x-=5
    print(-1 if x<0 else x*'5'+(y-x)*'3')