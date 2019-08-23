import unittest
from listutil import unique

class ListTest(unittest.TestCase):

    def test_list(self):
        lst = unique(['d','f','f','t'])
        self.assertEqual(['d','f','t'], lst)
        lst = unique(['a','s','s','a','a','f'])
        self.assertEqual(['a','s','f'], lst)
        lst = unique([])
        self.assertEqual([], lst)
        lst = unique([1, 2, 2, 3,4])
        self.assertEqual([1,2,3,4], lst)
        lst = unique([1, 2, 2, [1,2,3]])
        self.assertEqual([1, 2,[1,2,3]], lst)


if __name__ == "__main__":
    unittest.main('listutil_test')