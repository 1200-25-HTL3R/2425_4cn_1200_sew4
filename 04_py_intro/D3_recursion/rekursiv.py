__author__ = 'Benedikt Theuretzbachner'

def M(n: int) -> int:
    """
        :param n: input for McCarthy-91 function
        :return: output for McCarthy-91 function
        >>> M(115)
        105
        >>> M(15)
        91
    """
    if n <= 100:
        return M(M(n + 11))

    return n - 10

if __name__ == "__main__":
    import doctest
    doctest.testmod()
