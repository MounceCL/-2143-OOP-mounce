"""
Christine Mounce
Homework 1
overload the addition operator
"""

class fraction(object):
    def __init__(self,n=None,d=None):
        self.numerator = n
        self.denominator = d

    def __str__(self):
        return "%s / %s" % (self.numerator , self.denominator)

    def numerator(self,n):
        self.numerator = n 

    def denominator(self,d):
        self.denominator = d

    def __mul__(self,rhs):
        x = self.numerator * rhs.numerator
        y = self.denominator * rhs.denominator
        return fraction(x,y)

    def __add__(self, f):
        f=fraction()
        f.denominator = self.denominator*b.denominator
        f.numerator = self.numerator + b.numerator
        return f

if __name__ == '__main__':
    a = fraction(1,2)
    b = fraction(4,5)
    c = a * b
    print(c)
    print(a+b)
