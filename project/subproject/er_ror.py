def sum(a,b,c,d):
    '''
    >>> sum(1,4,3,3)
    50
    >>> sum(111,88,2,2)
    19
    '''
    return (a + b)*(c + d)
if __name__ == '__main__':
    import doctest
    doctest.testmod()
