import math
from functools import total_ordering
import doctest
from types import NotImplementedType


@total_ordering
class Fraction:
    def __init__(self, numerator: int = 0, denominator: int = 1) -> None:
        """
        Constructor for Fraction class

        :param numerator: numerator for fraction
        :param denominator: denominator for fraction
        :raises ArithmeticError: when the denominator is zero

        >>> f = Fraction(1,2)
        >>> f == Fraction(2,4)
        True
        >>> Fraction(2) == Fraction(2,1)
        True
        >>> Fraction() == Fraction(0, 1)
        True
        """
        if denominator == 0:
            raise ArithmeticError("Denominator can't be 0")

        if numerator * denominator > 0:
            numerator = abs(numerator)
            denominator = abs(denominator)

        gcd: int = math.gcd(numerator, denominator)
        self._numerator: int = int(numerator / gcd)
        self._denominator: int = int(denominator / gcd)

    def __str__(self) -> str:
        """
        str method for Fraction class

        :return: str representation for Fraction object

        >>> str(Fraction(1))
        '1'
        >>> str(Fraction(4,8))
        '1/2'
        """
        if self.numerator == 0:
            return "0"

        prefix: int = int(self.numerator / self.denominator)
        if prefix == 0:
            return str(self.numerator) + "/" + str(self.denominator)

        new_numerator: int = self.numerator - prefix * self.denominator
        prefix = abs(prefix)
        if new_numerator == 0:
            return str(prefix)

        return str(prefix) + " " + str(new_numerator) + "/" + str(self.denominator)

    def __repr__(self) -> str:
        """
        Object representation for Fraction class

        :return: str with object representation of Fraction object

        >>> repr(Fraction(1,2))
        'Fraction(1, 2)'
        >>> repr(Fraction())
        'Fraction(0, 1)'
        """
        return f"Fraction({self.numerator}, {self.denominator})"

    @property
    def numerator(self) -> int:
        """
        Getter for numerator

        :return: numerator

        >>> Fraction(1,2).numerator
        1
        """
        return self._numerator

    @numerator.setter
    def numerator(self, numerator: int) -> None:
        """
        Setter for numerator

        >>> f = Fraction(3,8)
        >>> f.numerator = 4
        >>> f
        Fraction(1, 2)
        """
        self._numerator = numerator
        self = Fraction(numerator, self.denominator)

    @property
    def denominator(self) -> int:
        """
        Getter for denominator

        :return: denominator

        >>> Fraction(1,2).denominator
        2
        """
        return self._denominator

    @denominator.setter
    def denominator(self, denominator: int) -> None:
        """
        Setter for denominator

        >>> f = Fraction(3,8)
        >>> f.denominator = 9
        >>> f
        Fraction(1, 3)
        """
        self._denominator = denominator
        self = Fraction(self.numerator, denominator)

    def __add__(self, otherfraction: "int | Fraction") -> "Fraction":
        """
        Adds two fractions or a fraction and an integer.

        :param other: Fraction or int
        :return: New Fraction object

        >>> Fraction(1, 2) + Fraction(1, 4)
        Fraction(3, 4)
        >>> Fraction(1, 2) + 1.0
        Fraction(3, 2)
        """
        if not isinstance(otherfraction, Fraction):
            return self.__add__(Fraction(otherfraction))

        numerator = (
            self.numerator * otherfraction.denominator
            + otherfraction.numerator * self.denominator
        )
        denominator = self.denominator * otherfraction.denominator

        return Fraction(numerator, denominator)

    def __radd__(self, other: int) -> "Fraction":
        """
        Right-hand addition support.

        :param other: int or Fraction
        :return: New Fraction object

        >>> 1 + Fraction(1, 2)
        Fraction(3, 2)
        """
        return self.__add__(other)

    def __sub__(self, otherfraction: "int | Fraction") -> "Fraction":
        """
        Subtracts two fractions.

        :param other: Fraction or int
        :return: New Fraction object

        >>> Fraction(3, 4) - Fraction(1, 4)
        Fraction(1, 2)
        """
        if not isinstance(otherfraction, Fraction):
            return self.__sub__(Fraction(otherfraction))

        numerator = (
            self.numerator * otherfraction.denominator
            - otherfraction.numerator * self.denominator
        )
        denominator = self.denominator * otherfraction.denominator

        return Fraction(numerator, denominator)

    def __rsub__(self, other: int) -> "Fraction":
        """
        Right-hand subtraction support.

        :param other: int or Fraction
        :return: New Fraction object

        >>> 1 - Fraction(1, 2)
        Fraction(1, 2)
        """
        return Fraction(other).__sub__(self)

    def __mul__(self, otherfraction: "int | Fraction") -> "Fraction":
        """
        Multiplies two fractions.

        :param other: Fraction or int
        :return: New Fraction object

        >>> Fraction(2, 3) * Fraction(3, 4)
        Fraction(1, 2)
        """
        if not isinstance(otherfraction, Fraction):
            return self.__mul__(Fraction(otherfraction))

        numerator = self.numerator * otherfraction.numerator
        denominator = self.denominator * otherfraction.denominator

        return Fraction(numerator, denominator)

    def __rmul__(self, otherfraction: int) -> "Fraction":
        """
        Right-hand multiplication support.

        :param other: int or Fraction
        :return: New Fraction object

        >>> 3 * Fraction(2, 3)
        Fraction(2, 1)
        """
        return self.__mul__(otherfraction)

    def __truediv__(self, otherfraction: "int | Fraction") -> "Fraction":
        """
        Divides this fraction by another.

        :param other: Fraction or int
        :return: New Fraction object

        >>> Fraction(1, 2) / Fraction(1, 4)
        Fraction(2, 1)
        """
        if not isinstance(otherfraction, Fraction):
            return self.__truediv__(Fraction(otherfraction))

        numerator = self.numerator * otherfraction.denominator
        denominator = self.denominator * otherfraction.numerator

        return Fraction(numerator, denominator)

    def __rtruediv__(self, otherfraction: int) -> "Fraction":
        """
        Right-hand division support.

        :param other: int or Fraction
        :return: New Fraction object

        >>> 1 / Fraction(1, 2)
        Fraction(2, 1)
        """
        return Fraction(otherfraction).__truediv__(self)

    def __floordiv__(self, otherfraction: "int | Fraction") -> "Fraction":
        """
        Performs floor division between fractions.

        :param other: Fraction or int
        :return: Fraction with integer result

        >>> Fraction(5, 3) // Fraction(1, 2)
        Fraction(3, 1)
        """
        if not isinstance(otherfraction, Fraction):
            return self.__floordiv__(Fraction(otherfraction))

        numerator = self.numerator * otherfraction.denominator
        denominator = self.denominator * otherfraction.numerator

        return Fraction(numerator // denominator, 1)

    def __rfloordiv__(self, otherfraction: int) -> "Fraction":
        """
        Right-hand floor division support.

        :param other: int or Fraction
        :return: Fraction with integer result

        >>> 3 // Fraction(2, 3)
        Fraction(4, 1)
        """
        return Fraction(otherfraction).__floordiv__(self)

    def __eq__(self, otherfraction: object) -> bool | NotImplementedType:
        """
        Checks equality between two fractions.

        :param other: Fraction or int
        :return: True if both are equal

        >>> Fraction(1, 2) == Fraction(2, 4)
        True
        >>> Fraction(2, 1) == 2
        True
        """
        if not (isinstance(otherfraction, int) or isinstance(otherfraction, Fraction)):
            return NotImplemented
        if not isinstance(otherfraction, Fraction):
            return self.__eq__(Fraction(otherfraction))

        return (
            self.numerator == otherfraction.numerator
            and self.denominator == otherfraction.denominator
        )

    def __gt__(self, otherfraction: object) -> bool | NotImplementedType:
        """
        Checks if this fraction is greater than another.

        :param other: Fraction or int
        :return: True if this fraction is greater

        >>> Fraction(3, 4) > Fraction(2, 3)
        True
        >>> 1 > Fraction(2, 3)
        True
        """
        if not (isinstance(otherfraction, int) or isinstance(otherfraction, Fraction)):
            return NotImplemented
        if not isinstance(otherfraction, Fraction):
            return self.__gt__(Fraction(otherfraction))

        self_num = self.numerator / self.denominator
        other_num = otherfraction.numerator / otherfraction.denominator
        return self_num > other_num

    def __float__(self) -> float:
        """
        Converts the fraction to a float.

        :return: float number

        >>> float(Fraction(1, 2))
        0.5
        """
        return self.numerator / self.denominator


if __name__ == "__main__":
    doctest.testmod()
