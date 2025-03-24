__author__ = "Benedikt Theuretzbachner"


class Caesar:
    key = None

    def __init__(self, key: str | None = None) -> None:
        self.key = self.assing_key(key)

    def assing_key(self, key: str | None = None) -> str:
        """
        Key prüfen, und wenn gültig key returnen, wenn nicht self.key returnen, ansonsten 'a' returnen
        :param key: input schlüssel
        :return: zugewiesener key
        """
        if key:
            if not key.isalpha() or not len(key) == 1:
                raise ValueError("key must be a single alphanumeric letter")
            return key.lower()
        elif self.key is not None:
            return self.key
        else:
            return "a"

    def to_lowercase_letter_only(self, plaintext: str) -> str:
        """Wandelt den plaintext in Kleinbuchstaben um und entfernt alle Zeichen, die keine
        Kleinbuchstaben aus dem Bereich [a..z] sind.
        >>> caesar = Caesar()
        >>> caesar.to_lowercase_letter_only("Wandelt den plaintext in Kleinbuchstaben um und entfernt alle Zeichen, die keine Kleinbuchstaben aus dem Bereich [a..z] sind.")
        'wandeltdenplaintextinkleinbuchstabenumundentferntallezeichendiekeinekleinbuchstabenausdembereichazsind'
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        return "".join(filter(lambda ch: ch in alphabet, plaintext.lower()))
        # return "".join(filter(lambda ch: ch.isalpha(), plaintext.lower()))

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
        plaintext = self.to_lowercase_letter_only(plaintext)
        key = self.assing_key(key)

        out = ""
        for ch in plaintext:
            out += chr(((ord(ch) - 97) + (ord(key) - 97)) % 26 + 97)

        return out

    def decrypt(self, crypttext: str, key: str | None = None) -> str:
        """key ist ein Buchstabe, der definiert, um wieviele Zeichen verschoben wird.
        Falls kein key übergeben wird, nimmt übernimmt decrypt den Wert vom Property.
        >>> caesar=Caesar("b")
        >>> caesar.key
        'b'
        >>> caesar.decrypt("ibmmp")
        'hallo'
        """
        crypttext = self.to_lowercase_letter_only(crypttext)
        key = self.assing_key(key)

        out = ""

        neg_key = 26 - (ord(key) - 97)
        for ch in crypttext:
            out += chr(((ord(ch) - 97) + neg_key) % 26 + 97)

        return out

    def crack(self, crypttext: str, elements: int = 1) -> list[str]:
        """
        Caesar chiffre mit häufigkeitsanalyse knacken
        :param crypttext: verschlüsselter text
        :param elements: wieviele der warscheinlichsten schlüssel zurückgegeben werdenKlen
        :return: wahrscheinlichsten schlüssel absteigend sortiert
        >>> str='Vor einem großen Walde wohnte ein armer Holzhacker mit seiner Frau und seinen zwei Kindern; das Bübchen hieß Hänsel und das Mädchen Gretel. Er hatte wenig zu beißen und zu brechen, und einmal, als große Teuerung ins Land kam, konnte er das tägliche Brot nicht mehr schaffen. Wie er sich nun abends im Bette Gedanken machte und sich vor Sorgen herumwälzte, seufzte er und sprach zu seiner Frau: "Was soll aus uns werden? Wie können wir unsere armen Kinder ernähren da wir für uns selbst nichts mehr haben?"'
        >>> caesar = Caesar()
        >>> caesar.crack(str)
        ['a']
        >>> caesar.crack(str, 100) # mehr als 26 können es nicht sein.
        ['a', 'f', 'j', 'r', 'n', 'q', 'u', 'w', 'm', 'z', 'e', 'b', 'k', 'p', 'l', 'g', 't', 'h', 's', 'o', 'y', 'i', 'v', 'x', 'd', 'c']
        >>> crypted = caesar.encrypt(str, "y")
        >>> caesar.crack(crypted, 3)
        ['y', 'h', 'd']
        """
        crypttext = self.to_lowercase_letter_only(crypttext)
        rel_ger_letter_frequency: dict[str, float] = {
            "a": 0.0651,
            "b": 0.0189,
            "c": 0.0306,
            "d": 0.0508,
            "e": 0.1740,
            "f": 0.0166,
            "g": 0.0301,
            "h": 0.0476,
            "i": 0.0755,
            "j": 0.0027,
            "k": 0.0121,
            "l": 0.0344,
            "m": 0.0253,
            "n": 0.0978,
            "o": 0.0251,
            "p": 0.0079,
            "q": 0.0002,
            "r": 0.0700,
            "s": 0.0727,
            "t": 0.0615,
            "u": 0.0435,
            "v": 0.0067,
            "w": 0.0189,
            "x": 0.0003,
            "y": 0.0004,
            "z": 0.0113,
        }
        rel_letter_freq: dict[str, float] = self.get_rel_letter_freq(crypttext)
        scores: dict[float, str] = {}
        for offset in range(26):
            score: float = 0
            for key in rel_ger_letter_frequency:
                offset_key: str = chr((ord(key) - 97 + offset) % 26 + 97)
                if offset_key in rel_letter_freq:
                    score += abs(
                        rel_letter_freq[offset_key] - rel_ger_letter_frequency[key]
                    )
            scores[score] = chr(ord("a") + offset)
        return list(dict(sorted(scores.items())).values())[:elements]

    def get_rel_letter_freq(self, text: str) -> dict[str, float]:
        """
        Berechnet die relative häufigkeit der buchstaben in text
        :param text: input text
        :return: buchstaben als key und rel. häufigkeit als value
        """
        text = self.to_lowercase_letter_only(text)

        frequencies: dict[str, float] = {}
        for ch in text:
            if ch not in frequencies:
                frequencies[ch] = 0
            frequencies[ch] += 1

        for key in frequencies:
            frequencies[key] = frequencies[key] / len(text)

        return frequencies


if __name__ == "__main__":
    import doctest

    doctest.testmod()
