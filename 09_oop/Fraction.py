import math


class Fraction:
    _numerator = 0
    _denominator = 1
    _neg = False

    def __init__(self, numerator=0, denominator=1) -> None:
        if denominator == 0:
            raise ArithmeticError("Denominator can't be 0")

        if numerator * denominator > 0:
            numerator = abs(numerator)
            denominator = abs(denominator)

        gcd = math.gcd(numerator, denominator)
        self._numerator = int(numerator / gcd)
        self._denominator = int(denominator / gcd)

    def __str__(self):
        if self.numerator == 0:
            return "0"

        prefix = self.numerator / self.denominator
        prefix = int(prefix)
        if prefix == 0:
            return str(self.numerator) + "/" + str(self.denominator)

        new_numerator = self.numerator - prefix * self.denominator
        prefix = abs(prefix)
        if new_numerator == 0:
            return str(prefix)

        return str(prefix) + " " + str(new_numerator) + "/" + str(self.denominator)

    def __repr__(self) -> str:
        return f"Fraction({self.numerator}, {self.denominator})"

    @property
    def numerator(self):
        return self._numerator

    @numerator.setter
    def numerator(self, numerator):
        self._numerator = numerator
        self = Fraction(numerator, self.denominator)

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, denominator):
        self._denominator = denominator
        self = Fraction(self.numerator, denominator)

    def __add__(self, other):
        if not isinstance(other, Fraction):
            return self.__add__(Fraction(other))

        numerator = (
            self.numerator * other.denominator + other.numerator * self.denominator
        )
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            return self.__sub__(Fraction(other))

        numerator = (
            self.numerator * other.denominator - other.numerator * self.denominator
        )
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return self.__mul__(Fraction(other))

        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)


if __name__ == "__main__":
    f = Fraction(2)
    f2 = Fraction(3)

    print(f * f2)
