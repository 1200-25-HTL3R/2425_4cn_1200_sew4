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

    def __str__(self):
        sign = ""
        if self._neg:
            sign = "-"

        num = self.numerator / self.denominator
        num = int(num)
        if num == 0:
            return sign + str(self.numerator) + "/" + str(self.denominator)

        self.numerator -= num * self.denominator
        num_str = str(num) + " "

        return sign + num_str + str(self.numerator) + "/" + str(self.denominator)

    def __repr__(self) -> str:
        return f"Fraction({self.numerator}, {self.denominator})"

    @property
    def numerator(self):
        return self._numerator

    @numerator.setter
    def numerator(self, numerator):
        self._numerator = numerator

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, denominator):
        self._denominator = denominator


if __name__ == "__main__":
    f = Fraction(1, -3)
    print(f)
