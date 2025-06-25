import math

from shapes.shape import Shape
from shapes.shape_type import ShapeType


class Hexagon(Shape):

    def __init__(self, side):
        super().__init__()
        self.side = side
        self.type = ShapeType.hexagon

    def get_area(self):
        return (3 * math.sqrt(3) * self.side ** 2) / 2

    def get_perimeter(self):
        return self.side * 6

    def __add__(self, other):
        return Hexagon(self.side + other.side)

