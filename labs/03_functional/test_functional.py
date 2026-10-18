import unittest
from io import StringIO
from contextlib import redirect_stdout
from lab_python_fp.field import field
from lab_python_fp.unique import Unique
from lab_python_fp.gen_random import gen_random
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1, cm_timer_2
from lab_python_fp.process_data import f1, f2, f3, f4


class FunctionalTests(unittest.TestCase):
    def test_fields_skip_none_but_keep_zero(self):
        items = [{'a': 0, 'b': None}, {}, {'a': 2, 'b': 3}]
        self.assertEqual(list(field(items, 'a')), [0, 2])
        self.assertEqual(list(field(items, 'a', 'b')), [{'a': 0}, {'a': 2, 'b': 3}])
        with self.assertRaises(AssertionError):
            list(field(items))

    def test_unique_keeps_original_case_and_accepts_generator(self):
        data = (x for x in ['A', 'a', 'B', 'b'])
        self.assertEqual(list(Unique(data, ignore_case=True)), ['A', 'B'])
        self.assertEqual(list(Unique(['A', 'a'])), ['A', 'a'])

    def test_random_count_and_bounds(self):
        values = list(gen_random(100, 1, 3))
        self.assertEqual(len(values), 100)
        self.assertTrue(all(1 <= value <= 3 for value in values))
        self.assertEqual(list(gen_random(2, 5, 5)), [5, 5])

    def test_decorator_returns_value_and_prints_dictionary(self):
        output = StringIO()
        with redirect_stdout(output):
            result = print_result(lambda: {'a': 1})()
        self.assertEqual(result, {'a': 1})
        self.assertIn('a = 1', output.getvalue())

    def test_timers_do_not_suppress_exception(self):
        for timer in [cm_timer_1, cm_timer_2]:
            with self.assertRaises(ValueError), redirect_stdout(StringIO()):
                with timer():
                    raise ValueError('ошибка')

    def test_processing_chain(self):
        data = [{'job-name': 'Программист C#'}, {'job-name': 'программист c#'},
                {'job-name': 'Бухгалтер'}]
        with redirect_stdout(StringIO()):
            names = f3(f2(f1(data)))
            rows = f4(names)
        self.assertEqual(names, ['Программист C# с опытом Python'])
        self.assertEqual(len(rows), 1)
        salary = int(rows[0].split('зарплата ')[1].split()[0])
        self.assertTrue(100000 <= salary <= 200000)
