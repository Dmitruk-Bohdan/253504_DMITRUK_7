from abc import ABC, abstractmethod
import math
from matplotlib import patches, pyplot as plt

class MyMixin:
    def log(self):
        print("Mixin function activated")

class GeometricFigure(ABC):
    def __init__(self):
        self._color = None
        self._name = None

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

    @abstractmethod
    def draw(self):
        pass

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def name(self):
        return self._name

    @color.setter
    def color(self, name):
        self._name = name

    def get_name(self):
        return self.name


class FigureColor:
    def __init__(self, color=None):
        self._color = color
    
    @property
    def color(self):
        return self._color
    

class Rectangle(GeometricFigure):
    """
    A class representing a rectangle, inheriting from the GeometricFigure class.

    Attributes:
    - _width (float): The width of the rectangle.
    - _height (float): The height of the rectangle.
    - _color (FigureColor): The color of the rectangle.

    Methods:
    - __init__(self, width=None, height=None, color=None): Initializes the Rectangle object.
    - create_interactively(self): Prompts the user to input values for width, height, and color.
    - calculate_area(self): Calculates and returns the area of the rectangle.
    - get_info(self): Returns a string representation of the rectangle's information.
    - save_info_as_file(self): Saves the rectangle's information to a file named "rectangle_info.txt".
    """

    def __init__(self, width : float = None, height : float = None, color : str = None):
        """
        Initializes a Rectangle object.

        Args:
        - width (float): The width of the rectangle (default is None).
        - height (float): The height of the rectangle (default is None).
        - color (str): The color of the rectangle (default is None).
        """
        super().__init__()
        self._width = width
        self._height = height
        self._color = FigureColor(color)

    def create_interactively(self):
        """
        Prompts the user to input values for width, height, and color of the rectangle.
        If invalid input is provided, an appropriate error message is displayed.
        """
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
        self.draw()
        color_ = input()
        descr = input()
        self.recolor(color_, descr)
        
    def calculate_area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
        - float: The area of the rectangle.
        """
        return self._width * self._height
    
    def get_info(self):
        """
        Returns a string representation of the rectangle's information.

        Returns:
        - str: The string representation of the rectangle's information.
        """
        return "Rectangle {} color, width: {}, height: {}, area: {}".format(
            self._color.color, self._width, self._height, self.calculate_area()
        )

    def save_info_as_file(self):
        """
        Saves the rectangle's information to a file named "rectangle_info.txt".
        """
        with open("rectangle_info.txt", 'w') as file:
            file.write(self.get_info())

    def recolor(self, color_: str, signature : str = "Rectangle"):
        self.draw(color_, signature)

    def draw(self, color_: str = None, signature : str = "Rectangle"):
        """
        Draws a rectangle and saves it
        """
        if color_ is None:
            color_ = self._color.color

        try:
            fig, ax = plt.subplots()
            square1 = patches.Rectangle((1, 1), self._width + 1, self._height + 1, linewidth=1, edgecolor='black', facecolor=color_)
            ax.add_patch(square1)
            ax.set_xlim(0, self._width + 2)
            ax.set_ylim(0, self._height + 2)
            ax.set_aspect('equal')
            plt.text((2 + self._width) / 2, 0.5, signature, fontsize=12, ha='center')
            plt.savefig("rectangle.png")
            plt.show()
        except Exception as ex:
            print(ex)


class Circle(GeometricFigure):
    """
    A class representing a circle, inheriting from the GeometricFigure class.

    Attributes:
    - _radius (float): The radius of the circle.
    - _color (FigureColor): The color of the circle.

    Methods:
    - __init__(self, radius=None, color=None): Initializes the Circle object.
    - create_interactively(self): Prompts the user to input values for radius and color.
    - calculate_area(self): Calculates and returns the area of the circle.
    - get_info(self): Returns a string representation of the circle's information.
    - save_info_as_file(self): Saves the circle's information to a file named "circle_info.txt".
    """

    def __init__(self, radius : float = None, color : FigureColor = None):
        """
        Initializes a Circle object.

        Args:
        - radius (float): The radius of the circle (default is None).
        - color (str): The color of the circle (default is None).
        """
        super().__init__()
        self._radius = radius
        self._color = FigureColor(color)

    def recolor(self, color_: str, signature : str = "Circle"):
        self.draw(color_, signature)

    def draw(self, color_: str = None, signature : str = "Circle"):
        """
        Draws the circle using the radius and color fields of the object,
        and exports it as a PNG image file.
        """
        if color_ is None:
            color_ = self._color.color

        try:
            fig, ax = plt.subplots()
            square1 = patches.Circle((self._radius + 1, self._radius + 1), self._radius, linewidth=1, edgecolor='black', facecolor=color_)
            ax.add_patch(square1)
            ax.set_xlim(0, self._radius * 2 + 2)
            ax.set_ylim(0, self._radius * 2 + 2)
            ax.set_aspect('equal')
            plt.text(self._radius + 1, 0.5, signature, fontsize=12, ha='center')
            plt.savefig("circle.png")
            plt.show()
        except Exception as ex:
            print(ex)

    def create_interactively(self):
        """
        Prompts the user to input values for radius and color of the circle.
        If invalid input is provided, an appropriate error message is displayed.
        """
        while True:
            try:
                radius = float(input("Enter the radius of the circle: "))
                color = FigureColor(input("Enter the color of the circle: "))
                if radius <= 0:
                    raise ValueError("Incorrect radius value")
            except Exception as e:
                print(f"\nIncorrect input: {e}\nPlease, try again\n")
                continue
            else:
                self._radius = radius
                self._color = color
                break

        self.draw()
    
    def calculate_area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
        - float: The area of the circle.
        """
        return math.pi * (self._radius ** 2)
    
    def get_info(self):
        """
        Returns a string representation of the circle's information.

        Returns:
        - str: The string representation of the circle's information.
        """
        return "Circle {} color, radius: {}, area: {}".format(
            self._color.color, self._radius, self.calculate_area()
        )
    
    def save_info_as_file(self):
        """
        Saves the circle's information to a file named "circle_info.txt".
        """
        with open("circle_info.txt", 'w') as file:
            file.write(self.get_info())


class Rhombus(GeometricFigure):
    """
    A class representing a rhombus, inheriting from the GeometricFigure class.

    Attributes:
    - _diagonal1 (float): The length of the first diagonal of the rhombus.
    - _diagonal2 (float): The length of the second diagonal of the rhombus.
    - _color (FigureColor): The color of the rhombus.

    Methods:
    - __init__(self, diagonal1=None, diagonal2=None, color=None): Initializes the Rhombus object.
    - create_interactively(self): Prompts the user to input values for diagonals and color.
    - calculate_area(self): Calculates and returns the area of the rhombus.
    - get_info(self): Returns a string representation of the rhombus's information.
    - save_info_as_file(self): Saves the rhombus's information to a file named "rhombus_info.txt".
    """

    def __init__(self, diagonal1 : float = None, diagonal2 : float = None, color : FigureColor = None):
        """
        Initializes a Rhombus object.

        Args:
        - diagonal1 (float): The length of the first diagonal of the rhombus (default is None).
        - diagonal2 (float): The length of the second diagonal of the rhombus (default is None).
        - color (str): The color of the rhombus (default is None).
        """
        super().__init__()
        self._diagonal1 = diagonal1
        self._diagonal2 = diagonal2
        self._color = FigureColor(color)

    def create_interactively(self):
        """
        Prompts the user to input values for diagonals and color of the rhombus.
        If invalid input is provided, an appropriate error message is displayed.
        """
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
        self.draw()

    def recolor(self, color_: str, signature : str = "Rhombus"):
        self.draw(color_, signature)

    def draw(self, color_: str = None, signature: str = "Rhombus"):
        """
        Draws a rhombus with the given diagonals and color,
        and exports it as a PNG image file.
        """
        if color_ is None:
            color_ = self._color.color
        try:
            fig, ax = plt.subplots()
            x = [0, self._diagonal1 / 2, self._diagonal1, self._diagonal1 / 2]
            y = [self._diagonal2 / 2, 0, self._diagonal2 / 2, self._diagonal2]

            rhombus = patches.Polygon(list(zip(x, y)), linewidth=1, edgecolor='black', facecolor=color_)
            ax.add_patch(rhombus)
            ax.set_xlim(0, max(self._diagonal1, self._diagonal2) * 1.2)
            ax.set_ylim(0, max(self._diagonal1, self._diagonal2) * 1.2)
            ax.set_aspect('equal')
            plt.text(self._diagonal1 / 2, -self._diagonal2 * 0.1, signature, fontsize=12, ha='center')
            plt.savefig("rhombus.png")
            plt.show()
        except Exception as ex:
            print(ex)
        
    def calculate_area(self):
        """
        Calculates and returns the area of the rhombus.

        Returns:
        - float: The area of the rhombus.
        """
        return (self._diagonal1 * self._diagonal2) / 2
    
    def get_info(self):
        """
        Returns a string representation of the rhombus's information.

        Returns:
        - str: The string representation of the rhombus's information.
        """
        return "Rhombus {} color, diagonal 1: {}, diagonal 2: {}, area: {}".format(
            self._color.color, self._diagonal1, self._diagonal2, self.calculate_area()
        )
    
    def save_info_as_file(self):
        """
        Saves the rhombus's information to a file named "rhombus_info.txt".
        """
        with open("rhombus_info.txt", 'w') as file:
            file.write(self.get_info())


class Square(GeometricFigure):
    """
    A class representing a square, inheriting from the GeometricFigure class.

    Attributes:
    - _side (float): The length of the side of the square.
    - _color (FigureColor): The color of the square.

    Methods:
    - __init__(self, side=None, color=None): Initializes the Square object.
    - create_interactively(self): Prompts the user to input values for side and color.
    - calculate_area(self): Calculates and returns the area of the square.
    - get_info(self): Returns a string representation of the square's information.
    - save_info_as_file(self): Saves the square's information to a file named "square_info.txt".
    """

    def __init__(self, side : float = None, color : FigureColor = None):
        """
        Initializes a Square object.

        Args:
        - side (float): The length of the side of the square (default is None).
        - color (str): The color of the square (default is None).
        """
        super().__init__()
        self._side = side
        self._color = FigureColor(color)

    def create_interactively(self):
        """
        Prompts the user to input values for side and color of the square.
        If invalid input is provided, an appropriate error message is displayed.
        """
        while True:
            try:
                side = float(input("Enter the side of the square: "))
                color = FigureColor(input("Enter the color of the square: "))

                if side <= 0:
                    raise ValueError("Incorrect side value")
            except Exception as e:
                print(f"\nIncorrect input: {e}\nPlease, try again\n")
                continue
            else:
                self._side = side
                self._color = color
                break
        
        self.draw()

    def recolor(self, color_: str, signature: str = "Square"):
        """
        Recolors the square using the given color and redraws it.
        """
        self.draw(color_, signature)

    def draw(self, color_: str = None, signature: str = "Square"):
        """
        Draws the square using the side length and color fields of the object,
        and exports it as a PNG image file.
        """
        if color_ is None:
            color_ = self._color.color

        try:
            fig, ax = plt.subplots()
            square = patches.Rectangle((1, 1), self._side + 1, self._side + 1, linewidth=1, edgecolor='black', facecolor=color_)
            ax.add_patch(square)
            ax.set_xlim(0, self._side * 1.2)
            ax.set_ylim(0, self._side * 1.2)
            ax.set_aspect('equal')
            plt.text(self._side / 2 + 1, 0.5, signature, fontsize=12, ha='center')
            plt.savefig("square.png")
            plt.show()
        except Exception as ex:
           print(ex)
    
    def calculate_area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        - float: The area of the square.
        """
        return self._side ** 2
    
    def get_info(self):
        """
        Returns a string representation of the square's information.

        Returns:
        - str: The string representation of the square's information.
        """
        return "Square {} color, side: {}, area: {}".format(
            self._color.color, self._side, self.calculate_area()
        )
    
    def save_info_as_file(self):
        """
        Saves the square's information to a file named "square_info.txt".
        """
        with open("square_info.txt", 'w') as file:
            file.write(self.get_info())


class Triangle(GeometricFigure):
    """
    A class representing a triangle, inheriting from the GeometricFigure class.

    Attributes:
    - _base (float): The length of the base of the triangle.
    - _height (float): The height of the triangle.
    - _color (FigureColor): The color of the triangle.

    Methods:
    - __init__(self, base=None, height=None, color=None): Initializes the Triangle object.
    - create_interactively(self): Prompts the user to input values for base, height, and color.
    - calculate_area(self): Calculates and returns the area of the triangle.
    - get_info(self): Returns a string representation of the triangle's information.
    - save_info_as_file(self): Saves the triangle's information to a file named "triangle_info.txt".
    """

    def __init__(self, base : float = None, height : float = None, color : FigureColor = None):
        """
        Initializes a Triangle object.

        Args:
        - base (float): The length of the base of the triangle (default is None).
        - height (float): The height of the triangle (default is None).
        - color (str): The color of the triangle (default is None).
        """
        super().__init__()
        self._base = base
        self._height = height
        self._color = FigureColor(color)

    def create_interactively(self):
        """
        Prompts the user to input values for base, height, and color of the triangle.
        If invalid input is provided, an appropriate error message is displayed.
        """
        while True:
            try:
                base = float(input("Enter the base value of the triangle: "))
                height = float(input("Enter the height value of the triangle: "))
                color = FigureColor(input("Enter the color of the triangle: "))

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

        self.draw()  
        
    def recolor(self, color_: str, signature: str = "Right Triangle"):
        """
        Recolors the right triangle using the given color and redraws it.
        """
        self.draw(color_, signature)

    def draw(self, color_: str = None, signature: str = "Right Triangle"):
        """
        Draws the right triangle using the base, height, and color fields of the object,
        and exports it as a PNG image file.
        """
        if color_ is None:
            color_ = self._color.color

        try:
            fig, ax = plt.subplots()
            triangle = patches.Polygon([[1, 1], [self._base + 1, 1], [1, self._height + 1]], linewidth=1, edgecolor='black', facecolor=color_)
            ax.add_patch(triangle)
            ax.set_xlim(0, max(self._base, self._height) * 1.5)
            ax.set_ylim(0, max(self._base, self._height) * 1.5)
            ax.set_aspect('equal')
            plt.text(self._base / 2, -self._height * 0.1, signature, fontsize=12, ha='center')
            plt.savefig("right_triangle.png")
            plt.show()
        except Exception as ex:
            print(ex)

    def calculate_area(self):
        """
        Calculates and returns the area of the triangle.

        Returns:
        - float: The area of the triangle.
        """
        return (self._base * self._height) / 2
    
    def get_info(self):
        """
        Returns a string representation of the triangle's information.

        Returns:
        - str: The string representation of the triangle's information.
        """
        return "Triangle of {} color, base: {}, height: {}, area: {}".format(
            self._color.color, self._base, self._height, self.calculate_area()
        )
    
    def save_info_as_file(self):
        """
        Saves the triangle's information to a file named "triangle_info.txt".
        """
        with open("triangle_info.txt", 'w') as file:
            file.write(self.get_info())

  
class Hexagon(GeometricFigure, MyMixin):
    """
    A class representing a hexagon, inheriting from the GeometricFigure class.

    Attributes:
    - _side (float): The length of a side of the hexagon.
    - _color (FigureColor): The color of the hexagon.

    Methods:
    - __init__(self, a=None, color=None): Initializes the Hexagon object.
    - create_interactively(self): Prompts the user to input values for side and color.
    - calculate_area(self): Calculates and returns the area of the hexagon.
    - get_info(self): Returns a string representation of the hexagon's information.
    - save_info_as_file(self): Saves the hexagon's information to a file named "hexagon_info.txt".
    """

    def __init__(self, a : float = None, color : FigureColor = None):
        """
        Initializes a Hexagon object.

        Args:
        - a (float): The length of a side of the hexagon (default is None).
        - color (str): The color of the hexagon (default is None).
        """
        super().__init__()
        self.log()
        self._side = a
        self._color = FigureColor(color)
    
    def create_interactively(self):
        """
        Prompts the user to input values for side and color of the hexagon.
        If invalid input is provided, an appropriate error message is displayed.
        """
        while True:
            try:
                side = float(input("Enter the side length of the hexagon: "))
                color = FigureColor(input("Enter the color of the hexagon: "))

                if side <= 0:
                    raise ValueError("Incorrect side value")
            except Exception as e:
                print(f"\nIncorrect input: {e}\nPlease, try again\n")
                continue
            else:
                self._side = side
                self._color = color
                break
                
        self.draw()

    def recolor(self, color_: str, signature: str = "Hexagon"):
        """
        Recolors the hexagon using the given color and redraws it.
        """
        self._color = color_
        self.draw()

    def draw(self, color_: str = None, signature: str = "Hexagon"):
        """
        Draws the hexagon using the side length and color fields of the object,
        and exports it as a PNG image file.
        """
        if color_ is None:
            color_ = self._color.color

        try:
            fig, ax = plt.subplots()
            center = (self._side, self._side)
            points = []
            for i in range(6):
                angle_deg = 60 * i
                angle_rad = math.radians(angle_deg)
                x = center[0] + self._side * math.cos(angle_rad)
                y = center[1] + self._side * math.sin(angle_rad)
                points.append([x, y])

            hexagon = patches.Polygon(points, linewidth=1, edgecolor='black', facecolor=color_)
            ax.add_patch(hexagon)
            ax.set_xlim(0, self._side * 2)
            ax.set_ylim(0, self._side * 2)
            ax.set_aspect('equal')
            plt.text(self._side, -self._side * 0.2, signature, fontsize=12, ha='center', va='top')
            plt.savefig("hexagon.png")
            plt.show()
        except Exception as ex:
            print(ex)

    def calculate_area(self):
        """
        Calculates and returns the area of the hexagon.

        Returns:
        - float: The area of the hexagon.
        """
        return (3 * math.sqrt(3) * (self._side ** 2)) / 2
    
    def get_info(self):
        """
        Returns a string representation of the hexagon's information.

        Returns:
        - str: The string representation of the hexagon's information.
        """
        return "Hexagon of {} color, side length: {}, area: {}".format(
            self._color.color, self._side, self.calculate_area()
        )
    
    def save_info_as_file(self):
        """
        Saves the hexagon's information to a file named "hexagon_info.txt".
        """
        with open("hexagon_info.txt", 'w') as file:
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
            shape_name = input("What shape do you wanna create?\nChoose one of theese: rectangle, circle, rhombus, square, triangle, hexagon\nOr enter 'end' to finish\n")

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

            