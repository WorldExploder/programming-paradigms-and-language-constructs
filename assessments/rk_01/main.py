import argparse
from pprint import pprint
from data import sample_data
from queries import run_queries


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='РК-1, вариант предметной области 17')
    parser.add_argument('--queries', choices=list('АБВГДЕ') + ['all'], default='all')
    args = parser.parse_args()
    letters = 'АБВГДЕ' if args.queries == 'all' else args.queries
    for letter in letters:
        for index, result in enumerate(run_queries(letter, *sample_data()), 1):
            print(f'Задание {letter}{index}')
            pprint(result, width=88, sort_dicts=False)
