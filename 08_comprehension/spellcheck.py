#!/bin/python

import doctest


def read_all_words(filename: str) -> set[str]:
    """
    Reads all words in a dictionary file
    :param filename: path to file
    :return: set with words of dictionary
    """
    with open(filename) as f:
        return set(w.strip().lower() for w in f)


def split_word(wort: str) -> list[tuple[str, str]]:
    """
    Returns a list of all possible ways to split a word
    :param word: word to split
    :return: list of tuples with the left and right part of the splitted word

    >>> split_word("abc")
    [('', 'abc'), ('a', 'bc'), ('ab', 'c'), ('abc', '')]
    """
    return [(wort[:i], wort[i:]) for i in range(0, len(wort) + 1)]


def edit1(wort: str) -> set[str]:
    """
    Get all variations of a word containing one mistake
    mistakes:
    - one letter missing
    - two letters swapped
    - one letter replaced
    - one addidtional letter
    :param wort: word to get possible mistakes for
    :return: a set with all forms of the word containing a mistake

    >>> edit1("ab") == {'db', 'aub', 'at', 'abr', 'acb', 'abk', 'vab', 'ib', 'abj', 'sb', 'av', 'gb', 'abx', 'wab', 'alb', 'b', 'am', 'adb', 'akb', 'ayb', 'aib', 'qab', 'ae', 'jb', 'pb', 'wb', 'nab', 'aw', 'xb', 'sab', 'anb', 'qb', 'eb', 'yab', 'ay', 'aq', 'fb', 'abb', 'abf', 'al', 'abw', 'tb', 'abd', 'ad', 'ub', 'axb', 'aqb', 'aob', 'avb', 'ax', 'as', 'hb', 'ag', 'ap', 'abc', 'eab', 'au', 'rb', 'abu', 'abp', 'arb', 'fab', 'abe', 'ah', 'cb', 'aj', 'asb', 'af', 'amb', 'awb', 'jab', 'uab', 'xab', 'zab', 'ob', 'ba', 'pab', 'kab', 'ac', 'bb', 'mb', 'aab', 'hab', 'abq', 'aa', 'ahb', 'abm', 'aba', 'ajb', 'cab', 'ai', 'apb', 'yb', 'an', 'bab', 'abv', 'abl', 'ak', 'lb', 'abt', 'abs', 'abi', 'atb', 'rab', 'gab', 'az', 'abh', 'mab', 'azb', 'afb', 'dab', 'tab', 'oab', 'ar', 'aby', 'ab', 'kb', 'abz', 'zb', 'ao', 'aeb', 'abo', 'nb', 'iab', 'vb', 'agb', 'abn', 'abg', 'lab'}
    True
    >>> edit1("")
    set()

    """
    if wort == "":
        return set()

    typos = set()

    for s_word in split_word(wort):
        head: str = s_word[0]
        tail: str = s_word[1]
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        if len(tail) >= 2:
            typos.add(head + tail[1:])
            typos.add(head + tail[1] + tail[0] + tail[2:])
        if len(tail) >= 1:
            typos |= set(head + ch + tail[1:] for ch in alphabet)
        typos |= set(head + ch + tail for ch in alphabet)

    return typos


def edit1_good(wort: str, alle_woerter: set[str]) -> set[str]:
    """
    Take the output of edit1() and filter it to only contain words from the dictionary
    :param wort: word containing one mistake
    :param alle_woerter: set with all correct words
    :return: a set with all correct forms of the word

    >>> woerter = read_all_words("de-en.txt")
    >>> edit1_good("Pyton", woerter) == {'python', 'pylon'}
    True
    >>> edit1_good("", woerter)
    set()
    """
    return edit1(wort.lower()) & alle_woerter


def edit2_good(wort: str, alle_woerter: set[str]) -> set[str]:
    """
    Like edit1_good() but account for two mistakes
    :param wort: word containing two mistake
    :param alle_woerter: set with all correct words
    :return: a set with all correct forms of the word

    >>> woerter = read_all_words("de-en.txt")
    >>> edit2_good("Pyton", woerter) == {'ton', 'proton', 'patron', 'photon', 'pylon', 'paten', 'patin', 'puten', 'ponton', 'python', 'phon', 'putin', 'eton', 'nylon', 'platon', 'beton', 'anton'}
    True
    >>> edit2_good("", woerter)
    set()
    """
    corrections = set()

    for w in edit1(wort.lower()):
        corrections |= edit1_good(w, alle_woerter)

    return corrections


def correct(word: str, alle_woerter: set[str]) -> list[str]:
    """
    Returns the correct form(s) of a word
    :param wort: word containing 0-2 mistakes
    :param alle_woerter: set with all correct words
    :return: a set with all correct forms of the word

    >>> woerter = read_all_words("de-en.txt")
    >>> sorted(correct("Aalsuppe", woerter))
    ['aalsuppe']
    >>> sorted(correct("Alsuppe", woerter))
    ['aalsuppe']
    >>> sorted(correct("Alsupe", woerter))
    ['aalsuppe', 'absude', 'alse', 'lupe']
    >>> correct("", woerter)
    []
    """
    word = word.lower()
    if word in alle_woerter:
        return [word]

    return list(edit1_good(word, alle_woerter) or edit2_good(word, alle_woerter))


if __name__ == "__main__":
    doctest.testmod()
