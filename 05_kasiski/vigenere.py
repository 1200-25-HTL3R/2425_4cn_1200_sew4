from caesar import Caesar


class Vigenere:
    def __init__(self, key: str | None = None) -> None:
        self.caesar = Caesar()

        if key:
            if not key.isalpha():
                raise ValueError("key must be a string of alphanumeric letters")
            self.key = key
        else:
            self.key = "abc"

    def encrypt(self, plaintext: str, key: str | None = None) -> str:
        if key is None:
            key = self.key

        plaintext = self.caesar.to_lowercase_letter_only(plaintext)
        out = ""
        for i, ch in enumerate(plaintext):
            out += self.caesar.encrypt(ch, key[i % len(key)])

        return out


if __name__ == "__main__":
    v = Vigenere()
