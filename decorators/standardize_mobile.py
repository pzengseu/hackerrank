def format(func):
    def inner(*args):
        lst = []
        for s in args:
            if len(s) == 10:
                lst.append(s)
            if len(s) == 11:
                lst.append(s[1:])
            if len(s) == 12:
                lst.append(s[2:])
            if len(s) == 13:
                lst.append(s[3:])
        lst = sorted(lst)
        return func(*lst)
    return inner

@format
def phone(*args):
    for s in args:
        print '+91', s[:5], s[5:]

phone(*[raw_input().strip() for _ in xrange(input())])