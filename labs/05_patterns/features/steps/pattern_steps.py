from behave import given, when, then
from unittest.mock import Mock
from patterns import (MarkdownCreator, LegacyPrinter, PrinterAdapter,
                      PrintOrder, student_price)


@given('a Markdown creator')
def creator(context):
    context.creator = MarkdownCreator()


@when('I render the title {title}')
def render(context, title):
    context.document = context.creator.render(title)


@then('the document is {text}')
def document(context, text):
    assert context.document == text


@given('an adapted mock printer')
def printer(context):
    context.printer = Mock(spec=LegacyPrinter)
    context.adapter = PrinterAdapter(context.printer)


@when('I send {text} to the adapter')
def send(context, text):
    context.adapter.send(text)


@then('the old printer receives {text}')
def received(context, text):
    context.printer.print_line.assert_called_once_with(text)


@given('a student print order')
def order(context):
    context.order = PrintOrder(student_price)


@when('I calculate the price of {pages:d} pages')
def price(context, pages):
    context.price = context.order.total(pages)


@then('the price is {expected:d}')
def expected_price(context, expected):
    assert context.price == expected
