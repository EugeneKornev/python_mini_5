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
    >>> specialize(bisum, 1, 5)(6)
    Traceback (most recent call last):
     ...
    TypeError: bisum() takes 2 positional arguments but 3 were given
    >>> specialize(bisum, 1, 5)(a=6)
    Traceback (most recent call last):
     ...
    TypeError: bisum() got an unexpected keyword argument 'a'
    """
    return 0

