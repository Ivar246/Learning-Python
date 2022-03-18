def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def multiplication(a, b):
    return a*b


def division(a, b):
    return a/b
exit = False

while True:
    a = int(input('a = '))
    b = int(input('b = '))
    operator = input("Please enter the mode of operation:")
    if operator == '+':
        add(a, b)
        exit = input("Do you want to exit(True or False): ").title()
        if exit:
            break
        else:
            exit = True
            continue
    elif operator == '-':
        subtract(a, b)
    elif operator == '*':
        multiplication(a, b)
    elif operator == '/':
        division(a, b)
    else:
        print('sorry, invalid mode of operation')   

