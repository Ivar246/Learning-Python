def  check(list1):
    return list1.count(19) == 2 and list1.count(5) >=3

list1 = []

size = int(input("Enter the size of list: "))

for i in range(size):
    a = int(input('Enter element in list: '))
    list1.append(a)

print(list1) 

x = check(list1)
print(x)