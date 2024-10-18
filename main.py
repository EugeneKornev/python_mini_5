import doctest
doctest.testmod()


def bisum(x, y):
    return x + y


def specialize(func, *args, **kwargs):
    def inner(*a, **k):
        return func(*args, *a, **kwargs, **k)
    return inner


def test():
    """
    >>> bisum(1, 2)
    3
    >>> specialize(bisum, 1)(2)
    3
    >>> specialize(bisum, 1, 5)()
    6
    >>> specialize(bisum)(6, 5)
    11
    """
    return 0


