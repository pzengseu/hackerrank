def cmpSD(x):
    if x.islower():
        return '0' + x
    if x.isupper():
        return '1' + x
    if x.isdigit():
        if int(x) % 2:
            return '2' + x
        else:
            return '3' + x

print reduce(lambda x, y: x + y, sorted(raw_input(), key= lambda x: cmpSD(x)))
