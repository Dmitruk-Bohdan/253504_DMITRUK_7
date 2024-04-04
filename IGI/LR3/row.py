import math as m
 
 #The program allows you to calculate the value of the cos(x) function 
 #with a given accuracy using library functions and by decomposition into a mathematical series.
 #The program outputs to the console the number of iterations required
 #to achieve the specified accuracy, the passed function argument, the passed accuracy and the calculation results

def calculate_row(x : float, eps : float):
    """
    Calculats cos value through a series
    Input(float x, float eps)
    Output(float result, u_int iterations number)
    """
    result = 0
    prev_result = 2147483647
    loop_counter = 0 
    while abs(result - prev_result) > eps:
        prev_result = result
        result += m.pow(-1, loop_counter) * m.pow(x, 2 * loop_counter) / (m.factorial(2 * loop_counter))
        loop_counter += 1
        if loop_counter > 500:
            raise Exception("Iterations c")
    return result, loop_counter

def executable_function():
    """
    User interface function
    Performs data input and output
    """
    while(True):
        try:
            eps = float(input("Input eps value: "))
            x = float(input("Input x value: "))
            break
        except ValueError:
            print("\nIncorrect input!\nTry again\n")

    lib_result = m.cos(x)

    my_result, n = calculate_row(x, eps)

    print(f"x: {x}\nn: {n}\nF(x): {my_result}\nMath F(x): {lib_result}\neps: {eps}")


