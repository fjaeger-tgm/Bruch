class Bruch(object):
    """
    The class Bruch represents a fraction.
    Nearly all operator of this class are overloaded.
    """

    def __init__(self, *args):
        """
        Create a fraction or throw a exception if the parameters are not correct, for example Zero Division, Type Error.
        :param args: parameters for the fraction can be int, float or Bruch
        """
        if len(args) == 1:
            if isinstance(args[0], Bruch):
                self.zaehler = args[0].zaehler
                self.nenner = args[0].nenner
            elif isinstance(args[0], int):
                self.zaehler = args[0]
                self.nenner = 1
            else:
                raise TypeError()
        elif len(args) == 2:
            self.zaehler = args[0]
            self.nenner = args[1]
        else:
            raise ValueError
        if self.nenner == 0:
            raise ZeroDivisionError()
        elif isinstance(self.nenner, float):
            raise TypeError
        elif isinstance(self.zaehler, float):
            raise TypeError
        self.ergebnis = float(self.zaehler) / float(self.nenner)

    @staticmethod
    def __makeBruch(value):
        """
        Creates a fraction
        :param value: int or a fraction
        :return: a fraction
        """
        return Bruch(value)

    def __add__(self, other):
        """
        Adds other to self
        :param other: int or a fraction
        :return: a fraction
        """
        other = Bruch(other)
        if isinstance(other, float):
            return Bruch(self, other)
        var3 = int(kgv(min(self, other).nenner, max(self, other).nenner))
        a = var3 // min(self, other).nenner
        b = var3 // max(self, other).nenner
        return Bruch(min(self, other).zaehler * a + max(self, other).zaehler * b, var3)

    def __radd__(self, other):
        """
        Adds self to other
        :param other: int or a fraction
        :return: float
        """
        return other + self.ergebnis

    def __iadd__(self, other):
        """
        Adds self to other
        :param other: int or a fraction
        :return: float
        """
        return other + self

    def __iter__(self):
        """
        Iterator of the fraction
        :return: iterator
        """
        return iter([self.zaehler, self.nenner])

    def __rdiv__(self, other):
        """
        Divide self.zaehler through other
        :param other: int or a fration
        :return: float
        """
        return self.zaehler / other

    def __mul__(self, other):
        """
        Multiply self with other
        :param other: int or a fraction
        :return: float
        """
        if isinstance(other, int):
            return self.ergebnis * other
        elif isinstance(other, float):
            raise TypeError
        elif isinstance(other, Bruch):
            return self.ergebnis * other.ergebnis

    def __rmul__(self, other):
        """
        Multiply other with self
        :param other: int or a fraction
        :return: float
        """
        if isinstance(other, int):
            return self.ergebnis * other
        return other.ergebnis * self.ergebnis

    def __imul__(self, other):
        """
        Multiply self with other
        :param other: int or a fraction
        :return: float
        """
        if isinstance(other, str):
            raise TypeError
        if isinstance(other, int):
            return self.ergebnis * other
        return self.ergebnis * other.ergebnis

    def __div__(self, other):
        """
        Divide ergebnis through other
        :param other: int or a fraction
        :return: float
        """
        if isinstance(other, int):
            return self.ergebnis / other
        return self.ergebnis / other.ergebnis

    def __truediv__(self, other):
        """
        Multiply self to not other
        :param other: int or a fraction
        :return: float
        """
        other = Bruch(other)
        return self * ~other

    def __rtruediv__(self, other):
        """
        Multiply self to not other
        :param other: int or a fraction
        :return: float
        """
        if isinstance(other, int):
            if self == 0:
                raise ZeroDivisionError
        other = Bruch(other)
        return self * ~other

    def __itruediv__(self, other):
        """
        Divide self through other
        :param other: int or a fraction
        :return: float
        """
        return self.ergebnis / other

    def __sub__(self, other):
        """
        Substract other from self
        :param other: int or a fraction
        :return: float
        """
        return self.ergebnis - other

    def __rsub__(self, other):
        """
        Substract self from other
        :param other: int or a fraction
        :return: float
        """
        return -self + other

    def __isub__(self, other):
        """
        Substract other from self
        :param other: int or a fraction
        :return: float
        """
        return self - other

    def __float__(self):
        """
        Returns float of Bruch
        :return: float
        """
        return self.ergebnis

    def __int__(self):
        """
        Returns int of Bruch
        :return: int
        """
        return int(self.ergebnis)

    def __abs__(self):
        """
        Returns absolute value of Bruch
        :return: float
        """
        return abs(self.ergebnis)

    def __pow__(self, power, modulo=None):
        """
        Takes self up to tje power
        :param power: int
        :param modulo: None
        :return: a fraction
        """
        if isinstance(power, int):
            return Bruch(self.zaehler ** power, self.nenner ** power)
        raise TypeError()

    def __invert__(self):
        """
        Divide nenner through zaehler
        :return: float
        """
        return float(self.nenner) / float(self.zaehler)

    def __neg__(self):
        """
        Divide zaehler through zaehler and take it -1 times
        :return: float
        """
        return float(self.zaehler) / float(self.nenner) * -1

    def __str__(self):
        """
        Represented the fraction as (zaehler/nenner)
        :return: str
        """
        if self.nenner == 1:
            return "(" + str(self.zaehler) + ")"
        return "(" + str(abs(self.zaehler)) + "/" + str(abs(self.nenner)) + ")"

    def __eq__(self, other):
        """
        Test if self is equal to other
        :param other: int or a fraction
        :return: boolean
        """
        return float(self) == float(other)

    def __ge__(self, other):
        """
        Test if self is equal/bigger to other
        :param other: int or a fraction
        :return: boolean
        """
        return float(self) >= float(other)

    def __gt__(self, other):
        """
        Test if self is bigger than other
        :param other: int or a fraction
        :return: boolean
        """
        return float(self) > float(other)

    def __le__(self, other):
        """
        Test if self is smaller/equal to other
        :param other: int or a fraction
        :return: boolean
        """
        return float(self) <= float(other)

    def __lt__(self, other):
        """
        Test if self is smaller than other
        :param other: int or a fraction
        :return: boolean
        """
        return float(self) < float(other)

    def __ne__(self, other):
        """
        Test if self is not equal to other
        :param other: int or a fraction
        :return: boolean
        """
        return float(self) != float(other)


def ggt(num1, num2):
    """
    Calculates the ggt of num1 and num2
    :param num1: int
    :param num2: int
    :return: int
    """
    if num2 == 0:
        return num1
    else:
        return ggt(num2, num1 % num2)


def kgv(num1, num2):
    """
    Calculates the kgv of num1 and num2
    :param num1: int
    :param num2: int
    :return: int
    """
    result = ggt(num1, num2)
    return (num1 * num2) / result
