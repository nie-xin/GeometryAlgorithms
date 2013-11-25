class Fraction:
    # Constructor - self should always be first param
    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    def show(self):
        print(self.num, "/", self.den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __lt__(self, other):
        selfnum = self.num * other.den
        #print('selfnum' + str(selfnum))
        othernum = other.num * self.den
        #print('othernum' + str(othernum))
        return selfnum < othernum

    def __gt__(self, other):
        selfnum = self.num * other.den
        othernum = other.num * self.den
        return selfnum > othernum

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __floordiv__(self, other):
        otherNewNum, otherNewDen = other.den, other.num
        newOther = Fraction(otherNewNum, otherNewDen)
        return self * newOther

    def __sub__(self, other):
        newSelfNum = self.num * other.den
        newOtherNum = other.num * self.den
#        print(newSelfNum)
        #print(newOtherNum)
        newNum = newSelfNum - newOtherNum
        newDen = self.den * other.den
#        print(self.den)
        #print(other.den)
        #common = gcd(newNum, newDen)
        return Fraction(newNum, newDen)



def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn

    return n


# test drive
#mf = Fraction(3, 5)
#print(mf)
#f1 = Fraction(1, 4)
#f2 = Fraction(1, 2)
#f3 = f1 + f2
#print(f3)
#print gcd(20, 10)
x = Fraction(1, 2)
y = Fraction(2, 3)
print(x)
print(y)
#print(x + y)
#print(x == y)
#print(x < y)
#print(x > y)
#print(x * y)
print(x // y)
print(x - y)

