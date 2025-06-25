from shapes.shape_type import ShapeType


class Shape:
    def __init__(self):
        self.type = None

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def __str__(self):
        try:
            return  f"""
                    i am a {self.type.value} \n
                    my area is {self.get_area()} \n
                    my perimeter is {self.get_perimeter()}
                    """
        except:
            return "please enter correct values"


