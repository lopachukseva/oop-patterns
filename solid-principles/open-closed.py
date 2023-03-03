"""Согласно принципу открытости-закрытости (OCP), классы должны быть открыты для расширения,
но закрыты для модификации. Это подразумевает, что после того, как конкретный класс был написан
и протестирован, его не следует изменять для добавления нового функционала.
Вместо этого необходимо его расширять."""

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    YELLOW = 3
    ORANGE = 4


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

    def __str__(self):
        return f'Product: {self.name}, color: {self.color}, size: {self.size}'


class Specification:
    def is_match(self, item):
        pass


class Filter:
    def filter(self, items, specification):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_match(self, item):
        return self.color == item.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_match(self, item):
        return self.size == item.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.specifications = args

    def is_match(self, item):
        return all(map(lambda specification: specification.is_match(item), self.specifications))


class OrSpecification(Specification):
    def __init__(self, *args):
        self.specifications = args

    def is_match(self, item):
        return any(map(lambda specification: specification.is_match(item), self.specifications))


class FFilter(Filter):
    def filter(self, items, specification):
        for item in items:
            if specification.is_match(item):
                yield item


products = [
    Product('banana', Color.YELLOW, Size.MEDIUM),
    Product('apple', Color.GREEN, Size.MEDIUM),
    Product('cherry', Color.RED, Size.SMALL),
    Product('grapefruit', Color.ORANGE, Size.LARGE),
    Product('pear', Color.GREEN, Size.MEDIUM),
    Product('plum', Color.RED, Size.MEDIUM),
]

small = SizeSpecification(Size.SMALL)
medium = SizeSpecification(Size.MEDIUM)
large = SizeSpecification(Size.LARGE)

green = ColorSpecification(Color.GREEN)
red = ColorSpecification(Color.RED)
orange = ColorSpecification(Color.ORANGE)
yellow = ColorSpecification(Color.YELLOW)

small_red = AndSpecification(small, red)

small_or_large = OrSpecification(small, large)

f = FFilter()

for item in f.filter(products, small_or_large):
    print(item)
