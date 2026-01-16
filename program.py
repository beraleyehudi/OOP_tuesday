from shapes.circle import Circle
from shapes.hexagon import Hexagon
from shapes.rectangle import Rectangle
from shapes.square import Square
from shapes.triangle import Triangle

my_circle = Circle(23)
my_square = Square(34)
my_rectangle = Rectangle(22, 20)
my_triangle = Triangle(12, 6)
my_hexagon = Hexagon(22)



shapes = [my_circle, my_square, my_rectangle, my_triangle, my_hexagon]

for i in shapes:
    print(i)

print(my_square + Square(2))