from cmath import polar

def mod(c):
    return polar(c)[0]

if __name__ == '__main__':
    x = complex(*map(float, raw_input().split()))
    y = complex(*map(float, raw_input().split()))

    xay = x + y
    print('{0:.2f}{1:+.2f}i'.format(xay.real, xay.imag))
    xsy = x - y
    print('{0:.2f}{1:+.2f}i'.format(xsy.real, xsy.imag))
    xmy = x * y
    print('{0:.2f}{1:+.2f}i'.format(xmy.real, xmy.imag))
    xdy = x / y
    if xdy.imag:
        print('{0:.2f}{1:+.2f}i'.format(xdy.real, xdy.imag))
    else:
        print('{0:.2f}+0.00i'.format(xdy.real, xdy.imag))
    print('{0:.2f}{1:+.2f}i'.format(mod(x).real, mod(x).imag))
    print('{0:.2f}{1:+.2f}i'.format(mod(y).real, mod(y).imag))