from shapes.shape import Shape
from shapes.shape_type import ShapeType


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height
        self.type = ShapeType.triangle

    def get_area(self):
        return (self.base * self.height) / 2

    def get_perimeter(self):
        return 23.55