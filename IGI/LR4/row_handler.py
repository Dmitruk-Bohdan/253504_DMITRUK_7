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

    def print_graph(self, x, eps):
        """
        Prints a graph showing the series expansion and the cos(x) function.
        
        Input:
        - x: float, the x value for which the series expansion and cos(x) function are plotted
        - eps: float, the desired precision (epsilon) for the series
        
        Output:
        - None
        """
        result, iterations = self.calculate_row(x, eps)

        x_values = range(iterations)
        y_row = self.row_members
        y_function = [m.cos(val) for val in x_values]

        plt.plot(x_values, y_row, label='Series expansion')
        plt.plot(x_values, y_function, label='cos(x) function')

        plt.xlabel('Iterations')
        plt.ylabel('Values')
        plt.title('Graphs of the series expansion and cos(x) function')
        plt.legend()

        plt.show()

    def demonstrate():
        handler = RowHandler()

        x = 1.0
        eps = 0.0001

        result, iterations = handler.calculate_row(x, eps)
        print("Result of cos(x) series expansion:", result)
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

        handler.print_graph(x, eps)
