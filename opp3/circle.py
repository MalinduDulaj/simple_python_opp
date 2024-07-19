class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return Circle.pi * self.radius * self.radius

    @staticmethod
    def calc_diameter(radius):
        return 2 * Circle.pi * radius

# Usage:
circle1 = Circle(5)
circle2 = Circle(8)


print(circle1.get_area())
print(Circle.calc_diameter(5))