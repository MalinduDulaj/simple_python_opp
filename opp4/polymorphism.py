class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width =  width
        self.height = height

    def area(self):
        return self.width * self.height
    

def calculate_area (shape : Shape) -> float:
    return shape.area()

circle1 = Circle(10.45)
rectangle1 = Rectangle(5,8)

print(calculate_area(circle1))
print(calculate_area(rectangle1))


    
        
        