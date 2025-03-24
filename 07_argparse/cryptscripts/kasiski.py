from typing import Counter
from .caesar import Caesar
from .vigenere import Vigenere

__author__ = "Benedikt Theuretzbachner"


class Kasiski:
    def __init__(self, crypttext: str = ""):
        self.caesar = Caesar()
        self.crypttext = self.caesar.to_lowercase_letter_only(crypttext)

    def allpos(self, text: str, teilstring: str) -> list[int]:
        """Berechnet die Positionen von teilstring in text.
        Usage examples:
        >>> k = Kasiski()
        >>> k.allpos("heissajuchei, ein ei", "ei")
        [1, 10, 14, 18]
        >>> k.allpos("heissajuchei, ein ei", "hai")
        []"""
        poss: list[int] = []

        pos: int = text.find(teilstring)
        offset: int = 0
        while pos != -1:
            poss.append(pos + offset)

            text = text[pos + 1 :]
            offset += pos + 1
            pos = text.find(teilstring)

        return poss

    def alldist(self, text: str, teilstring: str) -> set[int]:
        """Berechnet die Abstände zwischen allen Vorkommnissen des Teilstrings im verschlüsselten Text.
        Usage examples:
        >>> k = Kasiski()
        >>> k.alldist("heissajuchei, ein ei", "ei")
        {4, 8, 9, 13, 17}
        >>> k.alldist("heissajuchei, ein ei", "hai")
        set()"""
        allposs = self.allpos(text, teilstring)
        dists = set()
        for i, n in enumerate(allposs):
            for j in range(i):
                dists.add(abs(n - allposs[j]))

        return dists

    def dist_n_tuple(self, text: str, laenge: int) -> set[tuple[str, int]]:
        """Überprüft alle Teilstrings aus text mit der gegebenen laenge und liefert ein Set
        mit den Abständen aller Wiederholungen der Teilstrings in text.
        Usage examples:
        >>> k = Kasiski()
        >>> k.dist_n_tuple("heissajuchei", 2) == {('ei', 9), ('he', 9)}
        True
        >>> k.dist_n_tuple("heissajuchei", 3) == {('hei', 9)}
        True
        >>> k.dist_n_tuple("heissajuchei", 4) == set()
        True
        >>> k.dist_n_tuple("heissajucheieinei", 2) == \
        {('ei', 5), ('ei', 14), ('ei', 3), ('ei', 9), ('ei', 11), ('he', 9), ('ei', 2)}
        True
        """
        tuples: set[tuple[str, int]] = set()
        substrings: set[str] = set()
        for i in range(len(text) - laenge + 1):
            substrings.add(text[i : i + laenge])

        for s in substrings:
            for dist in self.alldist(text, s):
                tuples.add((s, dist))

        return tuples

    def dist_n_list(self, text: str, laenge: int) -> list[int]:
        """Wie dist_tuple, liefert aber nur eine aufsteigend sortierte Liste der
        Abstände ohne den Text zurück. In der Liste soll kein Element mehrfach vorkommen.
        Usage examples:
        >>> k = Kasiski()
        >>> k.dist_n_list("heissajucheieinei", 2)
        [2, 3, 5, 9, 11, 14]
        >>> k.dist_n_list("heissajucheieinei", 3)
        [9]
        >>> k.dist_n_list("heissajucheieinei", 4)
        []"""
        return sorted(set(map(lambda tup: tup[1], self.dist_n_tuple(text, laenge))))

    def ggt(self, x: int, y: int) -> int:
        """Ermittelt den größten gemeinsamen Teiler von x und y.
        Usage examples:
        >>> k = Kasiski()
        >>> k.ggt(10, 25)
        5
        >>> k.ggt(10, 1)
        1
        """
        while y != 0:
            z = x % y
            x = y
            y = z
        return x

    def ggt_count(self, zahlen: list[int]) -> Counter:
        """Bestimmt die Häufigkeit der paarweisen ggt aller Zahlen aus list.
        Usage examples:
        >>> k = Kasiski()
        >>> k.ggt_count([12, 14, 16]) == Counter({2: 2, 12: 1, 4: 1, 14: 1, 16: 1})
        True
        >>> k.ggt_count([10, 25, 50, 100])
        Counter({10: 3, 25: 3, 50: 2, 5: 1, 100: 1})
        """
        ggts: list[int] = []
        for i in range(len(zahlen)):
            for j in range(i + 1):
                ggts.append(self.ggt(zahlen[i], zahlen[j]))

        return Counter(ggts)

    def get_nth_letter(self, s: str, start: int, n: int) -> str:
        """Extrahiert aus s jeden n. Buchstaben beginnend mit index start.
        Usage examples:
        >>> k = Kasiski()
        >>> k.get_nth_letter("Das ist kein kreativer Text.", 1, 4)
        'asektrx'"""

        out = ""
        for i, ch in enumerate(s):
            if i % n == start:
                out += ch

        return out

    def crack(self, len: int) -> str:
        """
        Crackt den key für einen Vigenere verschlüsselten text mit der Kasiski Methode
        :param len: Länge der Textfenster für die Kasiski methode
        :return: gekrackter key
        >>> cleartext = 'Familie Müller plant ihren Urlaub. Sie geht in ein Reisebüro und lässt sich von einem Angestellten beraten. Als Reiseziel wählt sie Mallorca aus. Familie Müller bucht einen Flug auf die Mittelmeerinsel. Sie bucht außerdem zwei Zimmer in einem großen Hotel direkt am Strand. Familie Müller badet gerne im Meer.Am Abflugtag fahren Herr und Frau Müller mit ihren beiden Kindern im Taxi zum Flughafen. Dort warten schon viele Urlauber. Alle wollen nach Mallorca fliegen. Familie Müller hat viel Gepäck dabei: drei große Koffer und zwei Taschen. Die Taschen sind Handgepäck. Familie Müller nimmt sie mit in das Flugzeug. Am Flugschalter checkt die Familie ein und erhält ihre Bordkarten. Die Angestellte am Flugschalter erklärt Herrn Müller den Weg zum Flugsteig. Es ist nicht mehr viel Zeit bis zum Abflug. Familie Müller geht durch die Sicherheitskontrolle. Als alle das richtige Gate erreichen, setzen sie sich in den Wartebereich. Kurz darauf wird ihre Flugnummer aufgerufen und Familie Müller steigt mit vielen anderen Passagieren in das Flugzeug nach Mallorca. Beim Starten fühlt sich Herr Müller nicht wohl. Ihm wird ein wenig übel. Nach zwei Stunden landet das Flugzeug. Am Gepäckband warten alle Passagiere noch auf ihr fehlendes Gepäck. Danach kann endlich der Urlaub beginnen.'
        >>> v = Vigenere("kasiski")
        >>> k = Kasiski(v.encrypt(cleartext))
        >>> k.crack_key(4)
        'kasiski'
        """
        dists: list[int] = self.dist_n_list(self.crypttext, len)
        key_len: int = self.ggt_count(dists).most_common(1)[0][0]
        key: str = ""
        for i in range(key_len):
            crypttext = self.get_nth_letter(self.crypttext, i, key_len)
            key += self.caesar.crack(crypttext, 1)[0]

        return key


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    with open("message.txt") as f:
        message: str = f.read()

    v = Vigenere("refrigerator")
    enc_text = v.encrypt(message)

    k = Kasiski(enc_text)
    print(k.crack(8))
