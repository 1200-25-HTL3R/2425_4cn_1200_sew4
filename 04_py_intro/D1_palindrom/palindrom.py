__author__ = 'Benedikt Theuretzbachner'

def is_palindrom(s: str) -> bool:
    """
        :param number: input string
        :return: true if s is a palindrom

        >>> is_palindrom("lagerregal")
        True
        >>> is_palindrom("test")
        False
    """
    return s == str(s[::-1])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
