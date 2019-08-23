import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())

    def test_add(self):
        # 3/4 = 2/3 + 1/12
        f = Fraction(1,12)
        g = Fraction(2,3)
        self.assertEqual((3,4),f.__add__(g))
        f = Fraction(4,21)
        g = Fraction(6,3)
        self.assertEqual((46,21),f.__add__(g))
        f = Fraction(1,7)
        g = Fraction(-1,9)
        self.assertEqual((2,63),f.__add__(g))
        f = Fraction(6,7)
        g = Fraction(8,9)
        self.assertEqual((110,63),f.__add__(g))
        f = Fraction(1,1)
        g = Fraction(0,9)
        self.assertEqual((1,1),f.__add__(g))

    def test_eq(self):
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001)
        i = Fraction(625,25)
        j = Fraction(375,15) # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertTrue(i.__eq__(j))
        self.assertTrue(Fraction(-3,2).__eq__(Fraction(3,-2)))
        self.assertTrue(Fraction(0,0).__eq__(Fraction(0,1)))
        self.assertTrue(Fraction(24,7).__eq__(Fraction(72,21)))
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        self.assertFalse(Fraction(34,2).__eq__(Fraction(2,34)))
        
    def test_mul(self):
        f = Fraction(1,12)
        g = Fraction(2,3)
        self.assertEqual((1,18),f.__mul__(g))
        f = Fraction(2,3)
        g = Fraction(3,4)
        self.assertEqual((1,2),f.__mul__(g))
        f = Fraction(3,6)
        g = Fraction(18,9)
        self.assertEqual((1,1),f.__mul__(g))
        f = Fraction(4,7)
        g = Fraction(11,3)
        self.assertEqual((44,21),f.__mul__(g))
        f = Fraction(2,19)
        g = Fraction(8,3)
        self.assertEqual((16,57),f.__mul__(g))

    def test_div(self):
        f = Fraction(1,12)
        g = Fraction(2,3)
        self.assertEqual((1,8),f.__div__(g))
        f = Fraction(4,16)
        g = Fraction(16,1)
        self.assertEqual((1,64),f.__div__(g))
        f = Fraction(5,17)
        g = Fraction(9,3)
        self.assertEqual((5,51),f.__div__(g))
        f = Fraction(2,34)
        g = Fraction(68,3)
        self.assertEqual((3, 1156),f.__div__(g))
        f = Fraction(5,13)
        g = Fraction(7,26)
        self.assertEqual((10, 7),f.__div__(g))


        

if __name__ == "__main__":
    unittest.main('fraction_test')
