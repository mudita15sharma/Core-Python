from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def another_method(self):
        print('another method')


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Example usage
r = Rectangle(5, 10)
print("Area of Rectangle:", r.area())
r.another_method()

# Polymorphism: Shape type reference holding Rectangle object
shape: Shape = Rectangle(5, 10)
print("Area of Rectangle (using Shape reference):", shape.area())
shape.another_method()
