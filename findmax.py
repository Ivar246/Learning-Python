number = [25, 50, 15, 10, 26, 13 ,45]
max = number[0]

for data in range(1, len(number)):
    if max < number[data]:
        max = number[data]
        
print(max)