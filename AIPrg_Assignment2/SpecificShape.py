# import Shape class
from Shape import Shape

# create subclass one: triangle
class Triangle(Shape):
    def __init__(self, name, color,base, height):
        # call the constructor of the Shape class
        super().__init__(name, color)
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

    def get_perimeter(self):
        return 3 * self.base

triangle = Triangle("Triangle", "Red", 10, 5)
print('\ntriangle area is: ', triangle.get_area())
print('triangle perimeter is: ', triangle.get_perimeter())


# create subclass two: rectangle
class Rectangle(Shape):
    def __init__(self, name, color, length, width):
        # call the constructor of the Shape class
        super().__init__(name, color)
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

rectangle = Rectangle("Rectangle", "Blue", 10, 5)
print('\nrectangle area is: ', rectangle.get_area())
print('rectangle perimeter is: ', rectangle.get_perimeter())

# create subclass three: circle
class Circle(Shape):
    def __init__(self, name, color, radius):
        # call the constructor of the Shape class
        super().__init__(name, color)
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius

    def get_perimeter(self):
        return '{:.2f}'.format(2 * 3.14 * self.radius)

circle = Circle("Circle", "Green", 5)
print('\ncircle area is: ', circle.get_area())
print('circle perimeter is: ', circle.get_perimeter())

# create subclass four: trapezoid
class Trapezoid(Shape):
    def __init__(self, name, color, base1, base2, height):
        # call the constructor of the Shape class
        super().__init__(name, color)
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def get_area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def get_perimeter(self):
        return self.base1 + self.base2 + 2 * self.height

trapezoid = Trapezoid("Trapezoid", "Yellow", 10, 5, 5)
print('\ntrapezoid area is: ', trapezoid.get_area())
print('trapezoid perimeter is: ', trapezoid.get_perimeter())
