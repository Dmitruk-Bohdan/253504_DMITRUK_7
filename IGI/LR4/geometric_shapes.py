from abc import ABC, abstractmethod
import math

class GeometricFigure(ABC):
    def __init__(self):
        self._color = None

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def create_interactively(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def save_info_as_file(self):
        pass

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color


class FigureColor:
    def __init__(self, color=None):
        self._color = color
    
    @property
    def color(self):
        return self._color
    

class Rectangle(GeometricFigure):
    def __init__(self, width=None, height=None, color=None):
        super().__init__()
        self._width = width
        self._height = height
        self._color = FigureColor(color)

    def create_interactively(self):
        while True:
            try:
                width = float(input("Enter the width of the rectangle: "))
                height = float(input("Enter the height of the rectangle: "))
                color = FigureColor(input("Enter the color of the rectangle: "))
                if width <= 0 or height <= 0:
                    raise ValueError("Incorrect values of sides")
            except Exception as e:
                print(f"\nIncorrect input: {e}\nPlease, try again\n")
                continue
            else:
                self._width = width
                self._height = height
                self._color = color
                break
        
    def calculate_area(self):
        return self._width * self._height
    
    def get_info(self):
        return "Rectangle {} color, width: {}, height: {}, area: {}".format(
            self._color.color, self._width, self._height, self.calculate_area()
        )

    def save_info_as_file(self):
        with open ("rectangle_info.txt", 'w') as file:
            file.write(self.get_info())


class Circle(GeometricFigure):
    def __init__(self, radius=None, color=None):
        super().__init__()
        self._radius = radius
        self._color = FigureColor(color)

    def create_interactively(self):
        while True:
            try:
                raduis = float(input("Enter the radius of the circle: "))
                color = FigureColor(input("Enter the color of the circle: "))
                if raduis <= 0:
                    raise ValueError("Incorrect radius value")
            except Exception as e:
                print(f"\nIncorrect input: {e}\nPlease, try again\n")
                continue
            else:
                self._radius = raduis
                self._color = color
                break
    
    def calculate_area(self):
        return math.pi * (self._radius ** 2)
    
    def get_info(self):
        return "Circle {} color, radius: {}, area: {}".format(
        self._color.color, self._radius, self.calculate_area()
        )
    
    def save_info_as_file(self):
        with open ("circle_info.txt", 'w') as file:
            file.write(self.get_info())


class Rhombus(GeometricFigure):
    def __init__(self, diagonal1=None, diagonal2=None, color=None):
        super().__init__()
        self._diagonal1 = diagonal1
        self._diagonal2 = diagonal2
        self._color = FigureColor(color)

    def create_interactively(self):
        while True:
            try:
                diagonal1 = float(input("Enter the diagonal1 value of the rhombus: "))
                diagonal2 = float(input("Enter the diagonal2 value of the rhombus: "))
                color = FigureColor(input("Enter the color of the rhombus: "))

                if diagonal1 <= 0 or diagonal2 <= 0:
                    raise ValueError("Incorrect values of diagonals")
            except Exception as e:
                print(f"\nIncorrect input: {e}\nPlease, try again\n")
                continue
            else:
                self._diagonal1 = diagonal1
                self._diagonal2 = diagonal2
                self._color = color
                break
        
    def calculate_area(self):
        return (self._diagonal1 * self._diagonal2) / 2
    
    def get_info(self):
        return "Rhombus {} color, diagonal 1: {}, diagonal 2: {}, area: {}".format(
        self._color.color, self._diagonal1, self._diagonal2, self.calculate_area()
        )
    def save_info_as_file(self):
        with open ("rhombus_info.txt", 'w') as file:
            file.write(self.get_info())


class Square(GeometricFigure):
    def __init__(self, side=None, color=None):
        super().__init__()
        self._side = side
        self._color = FigureColor(color)

    def create_interactively(self):
        while True:
            try:
                raduis = float(input("Enter the side of the square: "))
                color = FigureColor(input("Enter the color of the square: "))
                if raduis <= 0:
                    raise ValueError("Incorrect side value")
            except Exception as e:
                print(f"\nIncorrect input: {e}\nPlease, try again\n")
                continue
            else:
                self._radius = raduis
                self._color = color
                break
    
 
    def calculate_area(self):
        return self._side ** 2
    
    def get_info(self):
        return "Square {} color, side: {}, area: {}".format(
        self._color.color, self._side, self.calculate_area()
        )
    
    def save_info_as_file(self):
        with open ("square_info.txt", 'w') as file:
            file.write(self.get_info())


class Triangle(GeometricFigure):
    def __init__(self, base=None, height=None, color=None):
        super().__init__()
        self._base = base
        self._height = height
        self._color = FigureColor(color)

    def create_interactively(self):
        while True:
            try:
                base = float(input("Enter the base value of the rhombus: "))
                height = float(input("Enter the height value of the rhombus: "))
                color = FigureColor(input("Enter the color of the rhombus: "))

                if base <= 0 or height <= 0:
                    raise ValueError("Incorrect values of sides")
            except Exception as e:
                print(f"\nIncorrect input: {e}\nPlease, try again\n")
                continue
            else:
                self._base = base
                self._height = height
                self._color = color
                break    
        
    def calculate_area(self):
        return (self._base * self._height) / 2
    
    def get_info(self):
        return "Triangle of {} color, base: {}, height: {}, area: {}".format(
        self._color.color, self._base, self._height, self.calculate_area()
        )
    
    def save_info_as_file(self):
        with open ("triangle_info.txt", 'w') as file:
            file.write(self.get_info())

  
class Hexagon(GeometricFigure):
    def __init__(self, a=None, color=None):
        super().__init__()
        self._side = a
        self._color = FigureColor(color)
    
    def create_interactively(self):
        while True:
            try:
                side = float(input("Enter the side of the circle: "))
                color = FigureColor(input("Enter the color of the circle: "))
                if side <= 0:
                    raise ValueError("Incorrect side value")
            except Exception as e:
                print(f"\nIncorrect input: {e}\nPlease, try again\n")
                continue
            else:
                self._side = side
                self._color = color
                break

    def calculate_area(self):
        return (3 * math.sqrt(3) * (self._side ** 2)) / 2
    
    def get_info(self):
        return "Hexagon {} color, side length: {}, area: {}".format(
            self._color.color, self._side, self.calculate_area()
        )
    
    def save_info_as_file(self):
        with open ("hexagon_info.txt", 'w') as file:
            file.write(self.get_info())
    
def demonstrate():

    key = str(input("Do you wanna create shapes by yourself?\nEnter 0 for NO\nEnter any other symblo for YES\n"))
    
    if key == "0":
        rectangle = Rectangle(5, 3, "blue")
        circle = Circle(4, "red")
        rhombus = Rhombus(6, 8, "green")
        square = Square(7, "yellow")
        triangle = Triangle(10, 5, "orange")
        hexagon = Hexagon(9, "purple")

        figures = [rectangle, circle, rhombus, square, triangle, hexagon]

        for figure in figures:
            print(figure.get_info())
    
    else:
        figures = []
        
        while True:
            shape_name = input("What shape do you  wanna create?\nChoose one of theese: rectangle, circle, rhombus, square, triangle, hexagon\nOr enter 'end' to finish\n")

            match shape_name:
                case "rectangle":
                    rectangle = Rectangle()
                    rectangle.create_interactively()
                    figures.append(rectangle)

                case "circle":
                    circle = Circle()
                    circle.create_interactively()
                    figures.append(circle)

                case "rhombus":
                    rhombus = Rhombus()
                    rhombus.create_interactively()
                    figures.append(rhombus)

                case "square":
                    square = Square()
                    square.create_interactively()
                    figures.append(square)

                case "triangle":
                    triangle = Triangle()
                    triangle.create_interactively()
                    figures.append(triangle)

                case "hexagon":
                    hexagon = Hexagon()
                    hexagon.create_interactively()
                    figures.append(hexagon)

                case "end":
                    break

                case _:
                    print("\nIncorrect input\nPlease, try again\n")
        
        for figure in figures:
            print(figure.get_info())

            