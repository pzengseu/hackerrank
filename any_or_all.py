n, s = input(), raw_input().split()
print all(map(lambda x: int(x) > 0, s)) and any(map(lambda x: x == ''.join(list(reversed(x))), s))