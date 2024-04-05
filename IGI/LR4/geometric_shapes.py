from abc import ABC, abstractmethod
import math

class GeometricFigure(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class FigureColor:
    def __init__(self, color):
        self._color = color
    
    @property
    def color(self):
        return self._color
    
class Rectangle(GeometricFigure):
    def __init__(self, width, height, color):
        super().__init__()
        self._width = width
        self._height = height
        self._color = FigureColor(color)
    
    def calculate_area(self):
        return self._width * self._height
    
    def get_info(self):
        return "Rectangle {} color, width: {}, height: {}, area: {}".format(
            self._color.color, self._width, self._height, self.calculate_area()
        )
    
    import math

class Circle(GeometricFigure):
    def __init__(self, radius, color):
        super().__init__()
        self._radius = radius
        self._color = FigureColor(color)
    
    def calculate_area(self):
        return math.pi * (self._radius ** 2)
    
    def get_info(self):
        return "Circle {} color, radius: {}, area: {}".format(
        self._color.color, self._radius, self.calculate_area()
        )

class Rhombus(GeometricFigure):
    def __init__(self, diagonal1, diagonal2, color):
        super().__init__()
        self._diagonal1 = diagonal1
        self._diagonal2 = diagonal2
        self._color = FigureColor(color)
        
    def calculate_area(self):
        return (self._diagonal1 * self._diagonal2) / 2
    
    def get_info(self):
        return "Rhombus {} color, diagonal 1: {}, diagonal 2: {}, area: {}".format(
        self._color.color, self._diagonal1, self._diagonal2, self.calculate_area()
        )
    
class Square(GeometricFigure):
    def __init__(self, side, color):
        super().__init__()
        self._side = side
        self._color = FigureColor(color)
 
    def calculate_area(self):
        return self._side ** 2
    
    def get_info(self):
        return "Square {} color, side: {}, area: {}".format(
        self._color.color, self._side, self.calculate_area()
        )

class Triangle(GeometricFigure):
    def __init__(self, base, height, color):
        super().__init__()
        self._base = base
        self._height = height
        self._color = FigureColor(color)
        
    def calculate_area(self):
        return (self._base * self._height) / 2
    
    def get_info(self):
        return "Triangle of {} color, base: {}, height: {}, area: {}".format(
        self._color.color, self._base, self._height, self.calculate_area()
        )
    
class Hexagon(GeometricFigure):
    def __init__(self, a, color):
        super().__init__()
        self._a = a
        self._color = FigureColor(color)
    
    def calculate_area(self):
        return (3 * math.sqrt(3) * (self._a ** 2)) / 2
    
    def get_info(self):
        return "Hexagon {} color, side length: {}, area: {}".format(
            self._color.color, self._a, self.calculate_area()
        )
    
def test_func():
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    color = input("Enter the color of the rectangle: ")
    
    rectangle = Rectangle(width, height, color)
    print(rectangle.get_info())
    
    a = float(input("Enter the side length of the hexagon: "))
    color = input("Enter the color of the hexagon: ")
    
    hexagon = Hexagon(a, color)
    print(hexagon.get_info())
