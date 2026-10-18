from patterns import (TextCreator, MarkdownCreator, LegacyPrinter,
                      PrinterAdapter, PrintOrder, student_price)


if __name__ == '__main__':
    print('Фабричный метод:', MarkdownCreator().render('Отчёт'))
    PrinterAdapter(LegacyPrinter()).send(TextCreator().render('Документ'))
    print('Обычная цена за 17 страниц:', PrintOrder().total(17))
    print('Студенческая цена:', PrintOrder(student_price).total(17))
