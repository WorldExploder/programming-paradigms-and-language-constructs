import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'rk_01'))
from data import sample_data
from models import Orchestra
from queries import run_queries, salary_statistics, one_to_many, many_to_many


class QueryTests(unittest.TestCase):
    def setUp(self):
        self.conductors, self.orchestras, self.links = sample_data()

    def test_one_to_many_and_sorting(self):
        expected = [('Андреев', 80000, 'Академический оркестр'),
                    ('Сидоренко', 90000, 'Академический оркестр'),
                    ('Петров', 100000, 'Камерный оркестр'),
                    ('Иванов', 120000, 'Симфонический оркестр'),
                    ('Алексеев', 110000, 'Симфонический оркестр')]
        results = run_queries('А', self.conductors, self.orchestras, self.links)
        self.assertEqual(results[0], expected)

    def test_all_salary_aggregates(self):
        expected = {'А': [230000, 170000, 100000], 'Б': [1, 2, 2],
                    'В': [80000, 100000, 110000], 'Г': [90000, 100000, 120000],
                    'Д': [85000, 100000, 115000], 'Е': [85000, 100000, 115000]}
        for letter, values in expected.items():
            with self.subTest(letter=letter):
                results = run_queries(letter, self.conductors, self.orchestras, self.links)
                self.assertEqual([value for _, value in results[1]], values)

    def test_many_to_many_filters_and_empty_orchestra(self):
        results = run_queries('Е', self.conductors, self.orchestras, self.links)
        self.assertEqual(results[2], [('Андреев', 80000, 'Академический оркестр'),
                                      ('Андреев', 80000, 'Камерный оркестр')])
        self.assertEqual(len(many_to_many(self.conductors, self.orchestras, self.links)), 5)
        empty = self.orchestras + [Orchestra(4, 'Пустой оркестр')]
        rows = one_to_many(self.conductors, empty)
        self.assertEqual(len(salary_statistics(rows, empty, 'average')), 3)
        with self.assertRaises(ValueError):
            run_queries('Ж', self.conductors, empty, self.links)


if __name__ == '__main__':
    unittest.main()
