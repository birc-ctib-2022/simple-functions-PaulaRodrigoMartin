"""Exercises with simple functions"""


from math import sqrt
from re import X


def prod(a, b, c):
    """
    Compute the product of three numbers.

    >>> prod(1, 2, 3)
    6
    """
    x = a*b*c
    return x

## print(prod(1,2,3))

a = 7
def prod2(b):
    """
    Get a global a and write to a local c before computing prod(a, b, c)

    >>> prod2(42)
    882
    """
    c=3
    x= a*b*c
    return x

## print(prod2(42))

def longest(x, y):
    """
    Returning the longest of two lists.

    >>> longest([1, 2, 3], [4, 5])
    [1, 2, 3]
    """
    if len(x) > len(y):
        return x
    else:
        return y
## print(longest([1, 2, 3], [4, 5]))


def dist(p1, p2):
    """
    Compute the distance between p1 and p2.

    >>> dist((1,2), (3,4))
    'TEST ME'
    """
    x1, y1 = p1
    x2, y2 = p2
    result = sqrt((x1-x2)**2+(y1-y2)**2)
    return result
## print(dist((1,2), (3,4)))