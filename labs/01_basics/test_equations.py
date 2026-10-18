import unittest
from unittest.mock import patch
from procedural import solve
from functional import solve as functional_solve
from object_oriented import BiquadraticEquation
from input_output import read_coefficients


class EquationTests(unittest.TestCase):
    def test_all_paradigms(self):
        examples = [(1, -5, 4, [-2, -1, 1, 2]), (1, 0, 1, []),
                    (1, -2, 1, [-1, 1]), (1, 1, 0, [0]),
                    (0, 2, -8, [-2, 2]), (0, 0, 0, None),
                    (0, 0, 2, []), (1, 5, 4, [])]
        for a, b, c, expected in examples:
            with self.subTest(coefficients=(a, b, c)):
                self.assertEqual(solve(a, b, c), expected)
                self.assertEqual(functional_solve(a, b, c), expected)
                self.assertEqual(BiquadraticEquation(a, b, c).solve(), expected)

    @patch('builtins.input', side_effect=['bad', '2'])
    def test_invalid_argument_is_retried(self, mocked_input):
        self.assertEqual(read_coefficients(['1', 'wrong', '4']), [1, 2, 4])

    @patch('builtins.input', side_effect=['nan', 'inf', '1', '-5', '4'])
    def test_keyboard_and_finite_values(self, mocked_input):
        self.assertEqual(read_coefficients([]), [1, -5, 4])


if __name__ == '__main__':
    unittest.main()
