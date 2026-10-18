from math import pi
from .shape import Shape
from .color import Color


class Circle(Shape):
    name = 'Круг'

    def __init__(self, radius, color):
        if radius <= 0:
            raise ValueError('Радиус должен быть положительным')
        self.radius = radius
        self.color = Color(color)

    def area(self):
        return pi * self.radius ** 2

    def __repr__(self):
        return '{}: радиус={}, цвет={}, площадь={:.2f}'.format(
            self.get_name(), self.radius, self.color.value, self.area())
