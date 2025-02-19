def to_lowercase_letter_only(plaintext: str) -> str:
    """Wandelt den plaintext in Kleinbuchstaben um und entfernt alle Zeichen, die keine
    Kleinbuchstaben aus dem Bereich [a..z] sind.
    >>> caesar = Caesar()
    >>> caesar.to_lowercase_letter_only("Wandelt den plaintext in Kleinbuchstaben um und
    entfernt alle Zeichen, die keine Kleinbuchstaben aus dem Bereich [a..z] sind.")
    'wandeltdenplaintextinkleinbuchstabenumundentferntallezeichendiekeinekleinbuchstaben
    ausdembereichazsind'
    """

    letters = "abcdefghijklmnopqrstuvwxyz"
    return plaintext.lower()
