class Fraction:
    _numerator = 0
    _denominator = 1
    _neg = False

    def __init__(self, zaehler=0, nenner=1) -> None:
        self._numerator = abs(zaehler)

        if nenner == 0:
            raise ArithmeticError("denominator can't be 0")
        self._denominator = abs(nenner)

        if zaehler * nenner < 0:
            self._neg = True
