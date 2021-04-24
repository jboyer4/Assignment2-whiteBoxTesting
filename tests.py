import unittest
from contrived_func import contrived_func


class Test(unittest.TestCase):

    def test1(self):
        self.assertTrue(contrived_func(111))

    def test2(self):
        self.assertFalse(contrived_func(6))

    def test3(self):
        self.assertTrue(contrived_func(155))

    def test4(self):
        self.assertTrue(contrived_func(7))

    def test5(self):
        self.assertTrue(contrived_func(5))

    def test6(self):
        self.assertFalse(contrived_func(79))

    def test6(self):
        self.assertFalse(contrived_func(81))

    def test6(self):
        self.assertFalse(contrived_func(71))


if __name__ == '__main__':
    unittest.main()
