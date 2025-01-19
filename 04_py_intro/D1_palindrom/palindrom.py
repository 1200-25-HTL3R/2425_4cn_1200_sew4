__author__ = 'Benedikt Theuretzbachner'

def is_palindrom(s: str) -> bool:
    """
        :param s: input string
        :return: true if s is a palindrom

        >>> is_palindrom("lagerregal")
        True
        >>> is_palindrom("test")
        False
    """
    return s == s[::-1]

def is_palindrom_sentence(s: str) -> bool:
    """
        :param s: input string
        :return: true if s is a palindrom sentence

        >>> is_palindrom_sentence("Was it a car or a cat I saw?")
        True
        >>> is_palindrom_sentence("Should return false.")
        False
    """
    reversed = ""
    for ch in s.lower():
        if ch.isalnum():
            reversed += ch
    return is_palindrom(reversed)

def palindrom_product(x: int) -> int:
    """
        :param x: value the palindrom product must be smaller than
        :return: the largest palindrom product smaller than x

        >>> palindrom_product(1000000)
        906609
        >>> palindrom_product(100000)
        99999
    """
    lp = -1
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            n: int = i*j
            if n >= x:
                continue
            if n < lp:
                break
            if is_palindrom(str(n)):
                lp = n

    return lp

def to_base(number: int, base: int) -> str:
    """
        :param number: Zahl im 10er-System
        :param base: Zielsystem (maximal 36)
        :return: Zahl im Zielsystem als String
        >>> to_base(1234,16)
        '4D2'
        >>> to_base(255,2)
        '11111111'
    """
    out: str = ""
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while number > 0:
        digit: int = number % base
        out += chars[digit]
        number = int((number - digit) / base)

    return out[::-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
