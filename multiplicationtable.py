def multiplicationTable(number):
    for i in range(1, 11):
        print(f'{number} * {i} = {number*i}')


number = int(input('multiplication Table of '))
multiplicationTable(number)