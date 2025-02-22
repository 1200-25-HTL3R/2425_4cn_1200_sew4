class Caesar:
    def __init__(self, key: str | None = None) -> None:
        if key:
            if not key.isalpha() or not len(key) == 1:
                raise ValueError("key must be a single alphanumeric letter")
            self.key = key
        else:
            self.key = "a"

    def to_lowercase_letter_only(self, plaintext: str) -> str:
        """Wandelt den plaintext in Kleinbuchstaben um und entfernt alle Zeichen, die keine
        Kleinbuchstaben aus dem Bereich [a..z] sind.
        >>> caesar = Caesar()
        >>> caesar.to_lowercase_letter_only("Wandelt den plaintext in Kleinbuchstaben um und entfernt alle Zeichen, die keine Kleinbuchstaben aus dem Bereich [a..z] sind.")
        'wandeltdenplaintextinkleinbuchstabenumundentferntallezeichendiekeinekleinbuchstabenausdembereichazsind'
        """
        letters = "abcdefghijklmnopqrstuvwxyz"
        return "".join(filter(lambda ch: ch.isalpha(), plaintext.lower()))

    def encrypt(self, plaintext: str, key: str | None = None) -> str:
        """key ist ein Buchstabe, der definiert, um wieviele Zeichen verschoben wird.
        Falls kein key übergeben wird, nimmt übernimmt encrypt den Wert vom Property.
        >>> caesar=Caesar("b")
        >>> caesar.key
        'b'
        >>> caesar.encrypt("hallo")
        'ibmmp'
        >>> caesar.decrypt("ibmmp")
        'hallo'
        >>> caesar.encrypt("hallo", "c")
        'jcnnq'
        >>> caesar.encrypt("xyz", "c")
        'zab'
        """
        if key is None:
            key = self.key

        out = ""
        for ch in plaintext:
            out += chr(((ord(ch) - 97) + (ord(key) - 97)) % 26 + 97)

        return out

    def decrypt(self, plaintext: str, key: str | None = None) -> str:
        """key ist ein Buchstabe, der definiert, um wieviele Zeichen verschoben wird.
        Falls kein key übergeben wird, nimmt übernimmt decrypt den Wert vom Property.
        >>> caesar=Caesar("b")
        >>> caesar.key
        'b'
        >>> caesar.decrypt("ibmmp")
        'hallo'
        """
        if key is None:
            key = self.key

        out = ""

        neg_key = 26 - (ord(key) - 97)
        for ch in plaintext:
            out += chr(((ord(ch) - 97) + neg_key) % 26 + 97)

        return out


if __name__ == "__main__":
    import doctest

    doctest.testmod()
