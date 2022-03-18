numbers = [7, 5, 8, 6, 3, 1]
max = numbers[0]
for number in numbers:
    if max < number:
        max = number
print(max)