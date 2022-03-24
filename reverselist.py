# def reverseList(list1):
#     if len(list1)  == 1:
#         return 1
#     else:
#         for index in range((int)(len(list1)/2)):
#             n = list1[index]
#             list1[index] = list1[len(list1)-1-index]
#             list1[len(list1)-1-index] = n
#         print(list1)

# list1 = [1, 2, 3, 4]
# reverseList(list1)

#another way
def reverse_fun(data_list):
    length = len(data_list)
    s = length

    new_list = [None] * length

    for item in data_list:
        s -= 1
        new_list[s] = item
    return new_list
    print(s)


list1 = [1, 2, 3, 4, 5]
print(reverse_fun(list1))