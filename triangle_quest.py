for i in range(1, int(raw_input())+1):
    print reduce(lambda x, y: x*10+y, range(1, i+1) + range(i-1,0, -1))