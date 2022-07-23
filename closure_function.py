# function which return function 
from token import tok_name


def to_power(x):
    def calc_power(n):
        return n**x
    return calc_power


cube = to_power(3)
print(cube(5))

square = to_power(2)
print(square(5))

# explaination
'''
       cube = to_power(3), here to_power() return calc_power
       so, cube act as calc_power func and and we pass value in cube as arg for cal_power parameter n
'''