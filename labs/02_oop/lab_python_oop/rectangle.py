from .shape import Shape
from .color import Color


class Rectangle(Shape):
    name = 'Прямоугольник'

    def __init__(self, width, height, color):
        if width <= 0 or height <= 0:
            raise ValueError('Размеры должны быть положительными')
        self.width, self.height = width, height
        self.color = Color(color)

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return '{}: ширина={}, высота={}, цвет={}, площадь={:.2f}'.format(
            self.get_name(), self.width, self.height,
            self.color.value, self.area())
