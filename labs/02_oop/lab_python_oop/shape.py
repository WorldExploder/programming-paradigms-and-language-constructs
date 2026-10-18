from abc import ABC, abstractmethod


class Shape(ABC):
    name = 'Геометрическая фигура'

    @classmethod
    def get_name(cls):
        return cls.name

    @abstractmethod
    def area(self):
        pass
