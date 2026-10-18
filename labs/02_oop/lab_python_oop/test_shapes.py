import unittest
from math import pi
from .shape import Shape
from .rectangle import Rectangle
from .square import Square
from .circle import Circle
from .color import Color


class ShapeTests(unittest.TestCase):
    def test_areas_for_variant_17(self):
        self.assertEqual(Rectangle(17, 17, 'синий').area(), 289)
        self.assertEqual(Square(17, 'красный').area(), 289)
        self.assertAlmostEqual(Circle(17, 'зелёный').area(), 289 * pi)

    def test_inheritance_and_abstract_class(self):
        self.assertIsInstance(Square(17, 'красный'), Rectangle)
        with self.assertRaises(TypeError):
            Shape()

    def test_color_and_invalid_size(self):
        color = Color('синий')
        color.value = 'красный'
        self.assertEqual(color.value, 'красный')
        with self.assertRaises(ValueError):
            Circle(-1, 'синий')
