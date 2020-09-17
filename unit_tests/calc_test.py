import unittest
from server import calc


class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)

    def test_double(self):
        self.assertEqual(calc.double(1, 2), 2)


if __name__ == '__main__':
    unittest.main()
