import math
import sys


def read_coefficients(arguments=None):
    arguments = sys.argv[1:] if arguments is None else arguments
    values = []
    for index, name in enumerate(('A', 'B', 'C')):
        raw = arguments[index] if index < len(arguments) else None
        while True:
            if raw is None:
                raw = input(f'{name} = ')
            try:
                value = float(raw)
                if not math.isfinite(value):
                    raise ValueError
                values.append(value)
                break
            except ValueError:
                print('Ошибка: введите конечное действительное число.')
                raw = None
    return values


def show_result(a, b, c, roots):
    print(f'Уравнение: {a:g}*x^4 + {b:g}*x^2 + {c:g} = 0')
    print(f'Дискриминант: {b * b - 4 * a * c:g}')
    if roots is None:
        print('Подходит любое действительное число.')
    elif roots:
        print('Действительные корни:', ', '.join(f'{x:g}' for x in roots))
    else:
        print('Действительных корней нет.')
