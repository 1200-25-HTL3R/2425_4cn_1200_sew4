__author__ = 'Benedikt Theuretzbachner'

from time import time

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

    t0 = time()
    m_list = [M(n) for n in range(0, 200)]
    print(m_list)
    m_dict = {n: M(n) for n in range(0, 200)}
    print(m_dict)

    print("Took " + str((time() - t0)) + "s")
