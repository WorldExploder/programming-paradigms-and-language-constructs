from equation import solve


if __name__ == '__main__':
    for coefficients in [(1, -5, 4), (1, 0, 1), (1, -2, 1)]:
        print(coefficients, '->', solve(*coefficients))
