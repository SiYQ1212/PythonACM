import decimal
from decimal import Decimal
from fractions import Fraction

if __name__ == '__main__':
    # Show one hundred decimal places
    decimal.getcontext().prec = 100
    print(Decimal(7) / Decimal(13))

    # Show the numerator denominator
    n = Fraction(2, 5)
    m = Fraction(10, 40)
    print(n, m)
    print(n * m, n + m, m + 6)

    # Get the numerator and denominator
    x = Decimal(m.numerator)
    y = Decimal(m.denominator)
    print(x, y)