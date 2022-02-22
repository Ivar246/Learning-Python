#WAP to remove dublicate in the list
numbers = [2, 5, 7, 9, 4, 12, 5, 7]
print(f"before removing duplicate:\n{numbers}")
print('\n')
number2 = []
for number in numbers:
    if number not in number2:
        number2.append(number)
print(f"After removing dubliate:\n{number2}")
