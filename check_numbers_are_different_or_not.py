list1 = [1, 2, 4, 4, 5]

# def check(a):
#     for i in range(len(a)):
#         for j in range(i+1, len(a)):
#             if a[i] == a[j]:
#                 return False
#     return True
    
# a = check(list1)
# print(a)
 
 
def check(a):
    if len(a) == len(set(a)):
        return False
    return -1

print(check(list1))
    