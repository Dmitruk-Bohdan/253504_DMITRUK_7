from functools import reduce
#This program allows you to calculate
#amount of series numbers bigger passed top border
#and product of list of elements located after the maximum modulo element

def calculate_function(number_list : list[float], top_border : float):
    """
    Calculates amount of series numbers bigger passer top border
    and product of list of elements located after the maximum modulo element
    Input(list of floats, float top_border)
    Output(u_int bigger_than_count, float product)
    """
    bigger_than_count = len([number for number in number_list if (number > top_border) and (number > 0)])
    max_abs_number_index = number_list.index(max(number_list, key=abs))
    product = reduce(lambda x, y: x * y, number_list[max_abs_number_index + 1 : ])
    return bigger_than_count, product

def executable_function():
    """
    User interface function
    Performs data input and output
    """
    number_list = []
    print("Please enter the values of the set of numbers\nTo finish entering, enter \"100\"")
    while(True):
        try:
            number = float(input())
            if(number == 100):
                break
            number_list.append(number)
        except ValueError:
            print("\nIncorrect input!\nTry again\n")

    while(True):
        try:
            top_border = float(input("Input top border:\n"))
            break
        except ValueError:
            print("\nIncorrect input!\nTry again\n")    
    
    bigger_than_count, product = calculate_function(number_list, top_border)
    print(f"Amount of series numbers bigger passer top border: {bigger_than_count}\nProduct of list of elements located after the maximum modulo element: {product}")
