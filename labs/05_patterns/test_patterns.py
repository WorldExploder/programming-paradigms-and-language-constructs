import unittest
from unittest.mock import Mock
from patterns import (TextCreator, MarkdownCreator, PrinterAdapter,
                      LegacyPrinter, PrintOrder, student_price)


class PatternTests(unittest.TestCase):
    def test_factory_method(self):
        self.assertEqual(TextCreator().render('Отчёт'), 'Отчёт')
        self.assertEqual(MarkdownCreator().render('Отчёт'), '# Отчёт')

    def test_adapter_with_mock(self):
        printer = Mock(spec=LegacyPrinter)
        PrinterAdapter(printer).send('Отчёт')
        printer.print_line.assert_called_once_with('Отчёт')

    def test_strategy(self):
        self.assertEqual(PrintOrder().total(17), 85)
        self.assertEqual(PrintOrder(student_price).total(17), 51)
        with self.assertRaises(ValueError):
            PrintOrder().total(-1)


if __name__ == '__main__':
    unittest.main()
