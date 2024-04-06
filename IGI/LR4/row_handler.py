import math as m
import matplotlib.pyplot as plt
import statistics

class RowHandler:
    def __init__(self):
        self.row_members = []

    def calculate_row(self, x, eps):
        """
        Calculates the value of the cos(x) function using a series.
        
        Input:
        - x: float, the x value for which the cos(x) function is calculated
        - eps: float, the desired precision (epsilon) for the series
        
        Output:
        - result: float, the calculated value of the cos(x) function
        - iterations: int, the number of iterations required to reach the desired precision
        """
        result = 0
        prev_result = 2147483647
        iterations = 0 
        self.row_members.clear()
        while abs(result - prev_result) > eps:
            prev_result = result
            self.row_members.append(m.pow(-1, iterations) * m.pow(x, 2 * iterations) / (m.factorial(2 * iterations)))
            result += self.row_members[-1]
            iterations += 1
            if iterations > 500:
                raise Exception("Iterations reached maximum limit")
        return result, iterations

    def get_additional_information(self):
        """
        Calculates additional information about the series.
        
        Output:
        - mean: float, the mean (average) of the series
        - median: float, the median value of the series
        - mode: float, the mode (most common value) of the series
        - variance: float, the variance of the series
        - stdev: float, the standard deviation of the series
        """
        mean = statistics.mean(self.row_members)
        median = statistics.median(self.row_members)
        mode = statistics.mode(self.row_members)
        variance = statistics.variance(self.row_members)
        stdev = statistics.stdev(self.row_members)

        return mean, median, mode, variance, stdev

    def print_graph(self, a, b, points_count, eps):
        """
        Prints a graph showing the series expansion and the cos(x) function.
        
        Input:
        - x: float, the x value for which the series expansion and cos(x) function are plotted
        - eps: float, the desired precision (epsilon) for the series
        
        Output:
        - None
        """
        step = (b - a) / points_count
        x_values = []
        current_value = a
        while current_value <= b:
            x_values.append(current_value)
            current_value += step

        y_series = []
        y_library = []
        for i in x_values:
            y_series.append(self.calculate_row(i, eps)[0])
            y_library.append(m.cos(i))

        plt.plot(x_values, y_series, label='Series expansion')
        plt.plot(x_values, y_library, label='cos(x) function')

        plt.xlabel('Iterations')
        plt.ylabel('Values')
        plt.title('Graphs of the series expansion and cos(x) function')
        plt.legend()

        plt.show()

    @staticmethod
    def demonstrate():
        handler = RowHandler()

        x = 1.0
        eps = 0.3

        result, iterations = handler.calculate_row(x, eps)
        print("Result of cos(x) series expansion:", result)
        print("Result of mathenatic library cos(x): ", m.cos(x))
        print("Number of iterations:", iterations)
        print()

        mean, median, mode, variance, stdev = handler.get_additional_information()
        print("Additional information:")
        print("Mean:", mean)
        print("Median:", median)
        print("Mode:", mode)
        print("Variance:", variance)
        print("Standard Deviation:", stdev)
        print()

        handler.print_graph(0, 3, 10, eps)
