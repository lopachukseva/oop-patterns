class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def __str__(self):
        return f'Width: {self._width}, height: {self._height}'

    @property
    def area(self):
        return self._width * self._height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(r: Rectangle):
    a = r.width
    r.height = 10
    print(a * r.height, r.area, sep='/')


rect = Rectangle(10, 20)
sq = Square(5)

use_it(rect)
use_it(sq)
