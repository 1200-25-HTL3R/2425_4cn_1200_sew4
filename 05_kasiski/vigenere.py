from caesar import Caesar

__author__ = "Benedikt Theuretzbachner"


class Vigenere:
    key = None

    def __init__(self, key: str | None = None) -> None:
        self.caesar = Caesar()

        self.key = self.assing_key(key)

    def assing_key(self, key: str | None = None) -> str:
        """
        Key prüfen, und wenn gültig key returnen, wenn nicht self.key returnen, ansonsten 'a' returnen
        :param key: input schlüssel
        :return: zugewiesener key
        """
        if key:
            if not key.isalpha():
                raise ValueError("key must be an alphanumeric string")
            return key.lower()
        elif self.key is not None:
            return self.key
        else:
            return "a"

    def encrypt(self, plaintext: str, key: str | None = None) -> str:
        """
        Text mit vigenere chiffre verschlüsseln
        :param plaintext: text
        :param key: key
        :return: verschlüsselter text
        """
        key = self.assing_key(key)

        plaintext = self.caesar.to_lowercase_letter_only(plaintext)
        out = ""
        for i, ch in enumerate(plaintext):
            out += self.caesar.encrypt(ch, key[i % len(key)])

        return out

    def decrypt(self, crypttext: str, key: str | None = None) -> str:
        """
        Text mit vigenere chiffre entschlüsseln
        :param plaintext: text
        :param key: key
        :return: plaintext
        """
        key = self.assing_key(key)

        crypttext = self.caesar.to_lowercase_letter_only(crypttext)
        out = ""
        for i, ch in enumerate(crypttext):
            out += self.caesar.decrypt(ch, key[i % len(key)])

        return out


if __name__ == "__main__":
    import doctest

    doctest.testmod()
