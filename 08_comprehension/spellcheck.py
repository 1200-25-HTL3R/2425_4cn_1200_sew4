#!/bin/python

import doctest


def read_all_words(filename: str) -> set[str]:
    with open(filename) as f:
        return set(w.strip().lower() for w in f)


def split_word(wort: str) -> list[tuple[str, str]]:
    return [(wort[:i], wort[i:]) for i in range(0, len(wort) + 1)]


def edit1(wort: str) -> set[str]:
    typos = set()

    for s_word in split_word(wort):
        start: str = s_word[0]
        end: str = s_word[1]
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        if len(end) >= 2:
            typos.add(start + end[1:])
            typos.add(start + end[1] + end[0] + end[2:])
        if len(end) >= 1:
            typos |= set(start + ch + end[1:] for ch in alphabet)
        typos |= set(start + ch + end for ch in alphabet)

    return typos


def edit1_good(wort: str, alle_woerter: set[str]) -> set[str]:
    return edit1(wort.lower()) & alle_woerter


def edit2_good(wort: str, alle_woerter: set[str]) -> set[str]:
    corrections = set()

    for w in edit1(wort.lower()):
        corrections |= edit1_good(w, alle_woerter)

    return corrections


def correct(word: str, alle_woerter: set[str]) -> list[str]:
    """
    >>> woerter = read_all_words("de-en.txt")
    >>> sorted(correct("Aalsuppe", woerter))
    ['aalsuppe']
    >>> sorted(correct("Alsuppe", woerter))
    ['aalsuppe']
    >>> sorted(correct("Alsupe", woerter))
    ['aalsuppe', 'absude', 'alse', 'lupe']
    """
    word = word.lower()
    if word in alle_woerter:
        return [word]

    return list(edit1_good(word, alle_woerter) or edit2_good(word, alle_woerter))


if __name__ == "__main__":
    doctest.testmod()
