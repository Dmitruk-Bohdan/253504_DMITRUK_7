from functools import reduce

def calculate_function(number_list):
    """
    Calculates the sum of terms in the integer number series
    and the count of members in the series that are less than ten.
    
    Args:
    - number_list: list of integers
    
    Returns:
    - sum_of_list_members: sum of series members
    - less_ten_amount: count of members less than ten
    """
    less_ten_amount = len([number for number in number_list if number < 10])
    sum_of_list_members = reduce(lambda x, y: x + y, number_list)
    return sum_of_list_members, less_ten_amount


def executable_function():
    """
    User interface function.
    Performs data input and output.
    """
    number_list = []
    print("Please enter the values of the number series.\nTo finish entering, enter \"100\"")
    while True:
        try:
            number = int(input())
            if number == 100:
                break
            number_list.append(number)
        except ValueError:
            print("\nIncorrect input!\nTry again\n")
    
    sum_of_list_members, less_ten = calculate_function(number_list)
    print(f"Sum of terms of the number series: {sum_of_list_members}\nNumber of members in the series less than ten: {less_ten}")