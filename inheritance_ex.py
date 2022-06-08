"""
Multiple Inheritance is used to provide reusability of functions and attributes
which the child class can inherit from the parent class.
This also avoids writing redundant code.
In example below, Square class is inheriting from two classes Shape and Quadilateral.
The attributes/functions of Shape/Quadilateral
class can be accessed/overriden in child class Sqaure
"""

class Shape():
    def get_name(self, name):
        """Returns the name of the polygon"""
        print(f'Name of the polygon: {name}')

    def number_of_sides(self, nos):
        """Prints the number of sides"""
        print(f'The number of sides in polygon is {nos}')

class Quadilateral():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f'Area : {self.length * self.width}')


class Square(Shape, Quadilateral):
    def __init__(self, side):
        super().__init__(side, side)
    

if __name__ == "__main__":
    sq = Square(2)
    sq.get_name('Square')
    sq.area()
