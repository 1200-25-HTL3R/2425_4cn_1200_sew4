__author__ = 'Benedikt Theuretzbachner'

from typing import List, Tuple


def collatz(n: int) -> int:
    """
        :param n: input value
        :return: the iteration of the collaz sequence after n
        >>> collatz(4)
        2
        >>> collatz(9)
        28
    """
    if not n > 0:
        raise Exception("n must be > 0")

    if n % 2 == 0:
        return int(n / 2)
    else:
        return 3 * n + 1

def collatz_sequence(number: int) -> List[int]:
    """
        :param number: Startzahl
        :return: Collatz Zahlenfolge, resultierend aus n
        >>> collatz_sequence(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> collatz_sequence(5)
        [5, 16, 8, 4, 2, 1]
    """
    #c = collatz(number)
    if number == 1:
        return [number]
    
    return [number, *collatz_sequence(collatz(number))]

def longest_collatz_sequence(n: int) -> Tuple[int, int]:
    """
        :param number: Startzahl
        :return: Startwert und Länge der längsten Collatz Zahlenfolge deren Startwert <=n ist
        >>> longest_collatz_sequence(100)
        (97, 119)
        >>> longest_collatz_sequence(15)
        (9, 20)
    """
    max: int = 0
    max_input = 0
    for i in range(1, n+1):
        size: int = len(collatz_sequence(i))
        if size > max:
            max = size
            max_input = i
    return (max_input, max)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
