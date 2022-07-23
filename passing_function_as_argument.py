l = [1, 2, 3]

def square(num):
    return num*num


def my_func(func, l):
    return [func(item) for item in l]


print(my_func(square, l))