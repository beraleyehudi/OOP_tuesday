from shapes.shape import Shape


class Hexagon(Shape):

    def __init__(self, side):
        self.side = side

    def get_area(self):
        return (3 * 3 ** 0.5 * self.side ** 2) / 2

