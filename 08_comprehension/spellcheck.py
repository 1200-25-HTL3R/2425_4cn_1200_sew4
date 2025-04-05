def read_all_words(filename: str) -> set[str]:
    with open(filename) as f:
        return set(w for w in f)


if __name__ == "__main__":
    s = read_all_words("de-en.txt")
    print(len(s))
