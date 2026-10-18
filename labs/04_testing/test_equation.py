import unittest
from equation import solve


class EquationTests(unittest.TestCase):
    def test_four_real_roots(self):
        self.assertEqual(solve(1, -5, 4), [-2, -1, 1, 2])

    def test_no_real_roots(self):
        self.assertEqual(solve(1, 0, 1), [])

    def test_repeated_roots(self):
        self.assertEqual(solve(1, -2, 1), [-1, 1])


if __name__ == '__main__':
    unittest.main()
