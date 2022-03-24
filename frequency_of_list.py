
random_list = ['A', 'A', 'B', 'C', 'B', 'D', 'D', 'A', 'B']
frequency = {}
for item in random_list:
    if item in frequency:
        frequency[item] += 1


    else:
        frequency[item] = 1

print(frequency)
