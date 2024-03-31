#This program allows you to
#Calculates amount of lowcase letters and digits in passed string

def my_decorator(func):
    def wrapper():
        print("main string handker function is running")
        func()
    return wrapper

def parse_string(str : str):
    """
    Calculates amount of lowcase letters and digits in passed string
    Input(string)
    Output(u_int lowercase_letters_count, u_int digits_count)
    """
    lowercase_letters_count = 0
    digits_count = 0
    for char in str:
        lowercase_letters_count += char.islower()
        digits_count += char.isdigit()

    return lowercase_letters_count, digits_count

@my_decorator
def executable_function():
    """
    User interface function
    Performs data input and output
    """
    str = input("Please enter the string:\n")
    lowercase_letters_count, digits_count = parse_string(str)

    print(f"Lowercase letters count: {lowercase_letters_count}\nDigits count: {digits_count}")
