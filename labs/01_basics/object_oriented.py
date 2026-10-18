from math import sqrt
from input_output import read_coefficients, show_result


class BiquadraticEquation:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    def solve(self):
        a, b, c = self.a, self.b, self.c
        if a == 0 and b == 0:
            return None if c == 0 else []
        if a == 0:
            values = [-c / b]
        else:
            d = self.discriminant()
            if d < 0:
                return []
            values = [(-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a)]
        return sorted({root for t in values if t >= 0
                       for root in (-sqrt(t), sqrt(t))})


if __name__ == '__main__':
    a, b, c = read_coefficients()
    equation = BiquadraticEquation(a, b, c)
    show_result(a, b, c, equation.solve())
