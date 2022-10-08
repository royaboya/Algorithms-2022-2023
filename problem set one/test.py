# MV

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
        
        self.simplify()
        

    def __str__(self):
        return f"Fraction: {self.num}/{self.den}"

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def __add__(self, other):
        return Fraction(
            self.num * other.den + self.den * other.num, self.den * other.den
        )
    
    def simplify(self):
        common = gcd(self.num, self.den)
        self.num //= common
        self.den //= common
    @classmethod
    def unit_fraction(cls,den):
        return cls(1,den)
    @classmethod
    def from_decimal(cls, decimal):
        _, dec_str = str(decimal).split(".")
        pow_10 = 10 ** len(dec_str)
        num = int(decimal * pow_10)
        return cls(num, pow_10)

def main():
    f1 = Fraction(14, 8)
    f2 = Fraction(2, 1)

    print(f1)
    f1.simplify()
    print(f1)
    print("\n" + str(f1 * f2))
    print(Fraction(2, 3) + Fraction(1, 3))
    print(Fraction.from_decimal(3.14))
    print(Fraction.unit_fraction(2))

if __name__ == "__main__":
    main()
