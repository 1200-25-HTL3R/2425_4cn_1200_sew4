def read_all_words(filename: str) -> set[str]:
    with open(filename) as f:
        return set(w for w in f)


def split_word(wort: str) -> list[tuple[str, str]]:
    return [(wort[:i], wort[i:]) for i in range(0, len(wort) + 1)]


if __name__ == "__main__":
    print(split_word("abc"))
