def read_all_words(filename: str) -> set[str]:
    with open(filename) as f:
        return set(w for w in f)


def split_word(wort: str) -> list[tuple[str, str]]:
    return [(wort[:i], wort[i:]) for i in range(0, len(wort) + 1)]


def edit1(wort: str) -> set[str]:
    typos = set()
    for s_word in split_word(wort):
        l = s_word[0]
        r = s_word[1]
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        if len(r) >= 2:
            typos.add(l + r[1:])
            typos.add(l + r[1] + r[0] + r[2:])
        if len(r) >= 1:
            typos.update(set(l + ch + r[1:] for ch in alphabet))
        typos.update(set(l + ch + r for ch in alphabet))

    return typos


if __name__ == "__main__":
    print(edit1("abc"))
