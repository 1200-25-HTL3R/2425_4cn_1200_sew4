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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
