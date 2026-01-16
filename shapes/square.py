from shapes.rectangle import Rectangle
from shapes.shape import Shape
from shapes.shape_type import ShapeType


class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side
        self.type = ShapeType.square

    def get_area(self):
        return self.side ** 2

    def get_perimeter(self):
        return self.side * 4

    def __add__(self, other):
        return Rectangle(self.side, other.side)
