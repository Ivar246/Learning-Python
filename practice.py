numbers = ['2', '3', '4']

# numbers = list(map(int, numbers))


# for i in numbers:
#     numbers[numbers.index(i)] = int(i)

# print(numbers)


# def sq(a):
#     return a*a
 
# num = [2,3,4,5,6]
# # square = list(map(sq, num))
# # print(square)

# square = list(map(lambda x: x*x, num))
# print(square)

a = iter(numbers)
print(a)
print(next(a))
