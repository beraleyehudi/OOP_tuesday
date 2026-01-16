from shapes.shape import Shape
from shapes.shape_type import ShapeType


class Rectangle(Shape):
    def __init__(self, length, width):

        super().__init__()
        self.length = length
        self.width = width
        self.type = ShapeType.rectangle

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return (self.length + self.width) * 2

    def __add__(self, other):
        return Rectangle(self.length + other.legth, self.width + other.width)