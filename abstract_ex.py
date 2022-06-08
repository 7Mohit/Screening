"""
Abstract classes are use to define the blueprint of a class.
The implementation of the abstract function is not defined in parent class.
Inheriting from an abstract class enforces the blueprint for the child class and also
allows them to provide their own implementation.
In example below: Shape is an abstract class which defines the blueprint for all child classes
to have area/diameter function implemented.
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Logic for calculating the area of a shape"""
        pass

    def diameter(self):
        """Logic for calculating the diameter of a shape"""
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        print('Calculating Area of Circle')
        print(f'Area : {3.14*self.radius*self.radius}')

    def diameter(self):
        print('Calculating Diameter of Circle')
        print(f'Diameter: {2*self.radius}')

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        print('Calculating Area of Square')
        print(f'Area : {self.side*self.side}')

    def diameter(self):
        print('Calculating Diameter of Square')
        print(f'Diameter: {4*self.side}')

if __name__ == "__main__":
    Circle(2).area()
    Square(2).diameter()
