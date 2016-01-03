fib = lambda x : x if x < 2 else fib(x-2) + fib(x-1)
print map(lambda x: pow(x, 3), map(fib, xrange(input())))