from shapes.shape import Shape
import math

from shapes.shape_type import ShapeType


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        self.type = ShapeType.circle

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 5

