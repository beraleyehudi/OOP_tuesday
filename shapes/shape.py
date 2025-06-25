class Shape:
    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def __str__(self):
        try:
            print(f"the area is {self.get_area()}")
            print(f"the perimeter is {self.get_perimeter()}")

        except:
            print("please enter correct values")