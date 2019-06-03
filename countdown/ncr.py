import operator as op

def ncr(n, r):
    """Implementation of n choose r = n!/(r!*(n-r)!)"""
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom