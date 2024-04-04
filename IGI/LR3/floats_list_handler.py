from functools import reduce

def calculate_function(number_list, top_border):
    """
    Calculates the count of numbers in the series that are greater than the given top border,
    and the product of the elements in the list that come after the maximum absolute value element.
    Input: list of floats, float top_border
    Output: count of numbers greater than the top border, product of elements after maximum absolute value
    """
    bigger_than_count = len([number for number in number_list if (number > top_border) and (number > 0)])
    max_abs_number_index = number_list.index(max(number_list, key=abs))
    product = reduce(lambda x, y: x * y, number_list[max_abs_number_index + 1:])
    return bigger_than_count, product

def executable_function():
    """
    User interface function.
    Performs data input and output.
    """
    number_list = []
    print("Please enter the values of the set of numbers\nTo finish entering, enter \"100\"")
    while True:
        try:
            number = float(input())
            if number == 100:
                break
            number_list.append(number)
        except ValueError:
            print("\nIncorrect input!\nTry again\n")

    while True:
        try:
            top_border = float(input("Input top border:\n"))
            break
        except ValueError:
            print("\nIncorrect input!\nTry again\n")    
    
    bigger_than_count, product = calculate_function(number_list, top_border)
    print(f"Amount of series numbers greater than the top border: {bigger_than_count}\nProduct of elements after the maximum absolute value: {product}")