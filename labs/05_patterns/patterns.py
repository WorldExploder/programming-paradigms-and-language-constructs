from abc import ABC, abstractmethod


class PlainText:
    def render(self, title):
        return title


class Markdown:
    def render(self, title):
        return '# ' + title


class DocumentCreator(ABC):
    """Фабричный метод: подклассы выбирают тип документа."""
    @abstractmethod
    def create_document(self):
        pass

    def render(self, title):
        return self.create_document().render(title)


class TextCreator(DocumentCreator):
    def create_document(self):
        return PlainText()


class MarkdownCreator(DocumentCreator):
    def create_document(self):
        return Markdown()


class LegacyPrinter:
    def print_line(self, text):
        print(text)


class PrinterAdapter:
    """Адаптер согласует send с методом старого принтера print_line."""
    def __init__(self, printer):
        self.printer = printer

    def send(self, text):
        self.printer.print_line(text)


def regular_price(pages):
    return pages * 5


def student_price(pages):
    return pages * 3


class PrintOrder:
    """Стратегия расчёта цены передаётся как функция."""
    def __init__(self, pricing=regular_price):
        self.pricing = pricing

    def total(self, pages):
        if pages < 0:
            raise ValueError('Число страниц не может быть отрицательным')
        return self.pricing(pages)
