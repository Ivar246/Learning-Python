numbers = [1, 2,3,4,5]
newList = []
length = len(numbers)
a = int(input('Enter Number: '))


def remove(desirednum,  numbers, length):
    for number in numbers:
        if number == desirednum:
            del numbers[numbers.index(number)]    


    print(numbers)


remove(a, numbers, length)
