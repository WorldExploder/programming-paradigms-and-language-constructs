from behave import given, when, then
from equation import solve


@given('coefficients {a}, {b}, {c}')
def coefficients(context, a, b, c):
    context.coefficients = tuple(map(float, (a, b, c)))


@when('I solve the equation')
def calculate(context):
    context.roots = solve(*context.coefficients)


@then('the roots are {values}')
def roots(context, values):
    assert context.roots == [float(value) for value in values.split(',')]


@then('there are no real roots')
def no_roots(context):
    assert context.roots == []
