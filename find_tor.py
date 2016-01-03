import math


def vlen(v):
    return math.sqrt(sum(v[i]*v[i] for i in xrange(len(v))))


def cross(x, y):
    return x[1] * y[2] - y[1] * x[2], y[0] * x[2] - x[0] * y[2], x[0] * y[1] - y[0] * x[1]


def dot(x, y):
    return sum(x[i]*y[i] for i in xrange(3))


def vsub(x, y):
    return tuple(y[i] - x[i] for i in xrange(3))

if __name__ == '__main__':
    v = [map(float, raw_input().split()) for _ in xrange(4)]
    ab = vsub(v[0], v[1])
    bc = vsub(v[1], v[2])
    cd = vsub(v[2], v[3])

    x = cross(ab, bc)
    y = cross(bc, cd)

    vdot = dot(x, y)
    xlen = vlen(x)
    ylen = vlen(y)
    print('{0:.2f}'.format(math.acos(vdot/(xlen*ylen))/math.pi*180))
