import time

def timer(func):
    """
    Decorator function to measure the execution time of a function
    Input: function
    Output: result of the function
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Execution time: {time.time() - start}")
        return result
    return wrapper


def parse_string(str):
    """
    Function to calculate the count of lowercase letters and digits in the given string
    Input: string
    Output: count of lowercase letters, count of digits
    """
    lowercase_letters_count = 0
    digits_count = 0
    for char in str:
        lowercase_letters_count += char.islower()
        digits_count += char.isdigit()

    return lowercase_letters_count, digits_count


@timer
def executable_function():
    """
    User interface function
    Performs data input and output
    """
    str = input("Please enter the string:\n")
    lowercase_letters_count, digits_count = parse_string(str)

    print(f"Lowercase letters count: {lowercase_letters_count}\nDigits count: {digits_count}")