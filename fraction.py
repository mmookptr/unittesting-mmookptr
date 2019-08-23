import math
import fraction
class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        #check if numerator is an integer
        if type(numerator) is not int:
            raise NameError
        #check if denominator is an integer
        elif type(denominator) is not int and denominator != 0:
            raise NameError
        # elif numerator == 0 or denumerator == 0:
            
        elif type(numerator) is int and type(denominator) is int :
            self.numerator = numerator
            self.denominator = denominator


    def get_fraction_gcd(self):
        """find gcd of two number to find fraction"""
        div = math.gcd(self.numerator, self.denominator)
        self.numerator = int(self.numerator/div)
        self.denominator = int(self.denominator/div)
        

    def __str__(self):
        self.get_fraction_gcd()
        if self.numerator == 0:
            return '0'

        elif self.denominator == 0:
            if numerator >= 1:
                return '1/0'
            elif numerator <= -1:
                return '-1/0'
            elif numerator == 0:
                return '0/0'
            

        elif self.denominator <= 1:
            if self.denominator == 1:
                return '{}'.format(self.numerator)
            elif self.denominator == -1:
                return '-{}'.format(self.numerator)
            elif self.denominator < -1 and self.numerator < -1:
                self.denominator *= -1
                return '-{}/{}'.format(self.numerator,self.denominator)
            elif self.denominator < -1 and self.numerator > -1:
                self.denominator *= -1
                return '-{}/{}'.format(self.numerator,self.denominator)

            elif self.denominator < -1 and self.numerator  < -1:
                self.denominator *= -1
                self.numerator *= -1
                return '{}/{}'.format(self.numerator,self.denominator)
        else:
            return '{}/{}'.format(self.numerator,self.denominator)


    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        self.numerator = (self.denominator*frac.numerator)+(self.numerator*frac.denominator)
        self.denominator = self.denominator * frac.denominator
        self.get_fraction_gcd()
        return self.numerator, self.denominator

    def __mul__(self,frac):
        """Return the multiple of two fractions as a new fraction."""
        self.numerator *= frac.numerator
        self.denominator *= frac.denominator
        self.get_fraction_gcd()
        return self.numerator,self.denominator

    def __div__(self,frac):
        self.numerator = self.numerator*frac.denominator
        self.denominator = self.denominator*frac.numerator
        self.get_fraction_gcd()
        return self.numerator,self.denominator

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        # return self.numerator == frac.numerator and self.denominator == frac.denominator
        if self.numerator < 0:
            self.numerator *= -1
        if self.denominator < 0:
            self.denominator *= -1
        if frac.numerator < 0:
            frac.numerator *= -1
        if frac.denominator < 0:
            frac.denominator *= -1
        if self.denominator == 0 or self.numerator == 0:
            if frac.numerator == 0 or frac.denominator == 0:
                return True
        elif self.get_fraction_gcd() == frac.get_fraction_gcd():
            return self.numerator == frac.numerator and self.denominator == frac.denominator








