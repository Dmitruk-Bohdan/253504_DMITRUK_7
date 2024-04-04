import math as m
 
def calculate_row(x, eps):
    """
    Calculates the value of the cos(x) function using a series.
    Input: float x, float eps
    Output: float result, number of iterations
    """
    result = 0
    prev_result = 2147483647
    iterations = 0 
    while abs(result - prev_result) > eps:
        prev_result = result
        result += m.pow(-1, iterations) * m.pow(x, 2 * iterations) / (m.factorial(2 * iterations))
        iterations += 1
        if iterations > 500:
            raise Exception("Iterations reached maximum limit")
    return result, iterations


def executable_function():
    """
    User interface function.
    Performs data input and output.
    """
    while True:
        try:
            eps = float(input("Input epsilon (eps) value: "))
            x = float(input("Input x value: "))
            break
        except ValueError:
            print("\nIncorrect input!\nTry again\n")

    library_result = m.cos(x)

    my_result, n = calculate_row(x, eps)

    print(f"x: {x}\nIterations: {n}\nCos(x): {my_result}\nMath.cos(x): {library_result}\nEpsilon (eps): {eps}")