from functools import reduce
#This program allows you to calculate
#the sum of terms of the integer number series and
#the number of members of series less than ten

def calculate_function(number_list : list[int]):
    """
    Calculates amount of series numbers less 10 and sum of series
    Input(list of ints)
    Output(int sum_of_list members, u_int less_10_ampount)
    """
    less_ten = len([number for number in number_list if number < 10])
    list_sum = reduce(lambda x, y: x + y, number_list)
    return list_sum, less_ten

def executable_function():
    """
    User interface function
    Performs data input and output
    """
    number_list = []
    print("Please enter the values of the set of numbers\nTo finish entering, enter \"100\"")
    while(True):
        try:
            number = int(input())
            if(number == 100):
                break
            number_list.append(number)
        except ValueError:
            print("\nIncorrect input!\nTry again\n")
    
    list_sum, less_ten = calculate_function(number_list)
    print(f"Sum of terms of the number series: {list_sum}\nNumber of members of series less than ten: {less_ten}")
