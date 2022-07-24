from functools import wraps


def print_function_data(function):
    @wraps
    def wrapper(*args, **kwargs):
        print(f"You are calling {function.__name__}")
        print(f"{function.__doc__}")
        return function(*args, **kwargs)
    
    return wrapper

@print_function_data
def addition(a, b):
    '''this function two numbers as a argument and return sum'''
    return a+b


print(addition(4, 5))