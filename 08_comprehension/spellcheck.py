def read_all_words(filename: str) -> set[str]:
    with open(filename) as f:
        return set(w.strip().lower() for w in f)


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
            typos |= set(l + ch + r[1:] for ch in alphabet)
        typos |= set(l + ch + r for ch in alphabet)

    return typos


def edit1_good(wort: str, alle_woerter: set[str]) -> set[str]:
    return edit1(wort.lower()) & alle_woerter


def edit2_good(wort: str, alle_woerter: set[str]) -> set[str]:
    corrections = set()
    for w in edit1(wort.lower()):
        corrections |= edit1_good(w, alle_woerter)

    return corrections


if __name__ == "__main__":
    print(edit2_good("Pyton", read_all_words("de-en.txt")))
