class Fraction:
    def __init__(self, num=0, den=1) -> None:
        self.num = num
        self.den = den

    def printFraction(self):
        print(str(self.num)+"/"+str(self.den))

    def simplify(self):
        current = min(self.num, self.den)
        while(current > 1):
            if(self.num % current == 0 and self.den % current == 0):
                break
            current -= 1
        self.num = self.num // current
        self.den = self.den // current
        return self

    def add(self, otherFraction):
        self.num = self.num*otherFraction.den+otherFraction.num*self.den
        self.den = self.den*otherFraction.den
        self.simplify()
        return self

    def multiply(self, otherFraction):
        self.num = self.num * otherFraction.num
        self.den = self.den * otherFraction.den
        self.simplify()
        return self


fraction1 = Fraction(2, 5)
fraction2 = Fraction(1, 3)

fraction1.multiply(fraction2)

print(fraction1.printFraction())
