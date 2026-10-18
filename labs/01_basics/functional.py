from math import sqrt
from input_output import read_coefficients, show_result


def solve(a, b, c):
    """Чистая функция с сопоставлением с образцом Python 3.10+."""
    match (a, b, c):
        case (0, 0, 0):
            return None
        case (0, 0, _):
            return []
        case (0, _, _):
            values = [-c / b]
        case _:
            d = b * b - 4 * a * c
            match d:
                case _ if d < 0:
                    return []
                case _:
                    values = [(-b + sqrt(d)) / (2 * a),
                              (-b - sqrt(d)) / (2 * a)]
    return sorted({x for t in filter(lambda t: t >= 0, values)
                   for x in (-sqrt(t), sqrt(t))})


if __name__ == '__main__':
    a, b, c = read_coefficients()
    show_result(a, b, c, solve(a, b, c))
