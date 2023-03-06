from math import cos, sin


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))

    def __str__(self):
        return f'Точка с координатами x: {self.x}, y: {self.y}'


p1 = Point.new_cartesian_point(-3, 9)
p2 = Point.new_polar_point(31, 24)

print(p1, p2, sep='\n')
