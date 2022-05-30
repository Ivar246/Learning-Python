
# import math
# def primefactors(n):
#    #even number divisible
#    while n % 2 == 0:
#       print (2),
#       n = n / 2
    
#    #n became odd
#    for i in range(3, int(math.sqrt(n))+1, 2):
     
#       while (n % i == 0):
#          print (i)
#          n = n / i
    
#    if n > 2:
#       print (n)
 
# n = int(input("Enter the number for calculating the prime factors :\n"))
# primefactors(n)


 
# n = int(input("Enter any Number for calculating the prime factors: "))
# i = 1
 
# while(i <= n):
#     c = 0
#     if(n % i == 0):
#         j = 1
#         while(j <= i):
#             if(i % j == 0):
#                 c = c + 1
#             j = j + 1
             
#         if (c == 2):
#             print(i)
#     i = i + 1
    
    
    
    
    
def unique_names(names1, names2):
    names = names1 + names2
    l = len(names)
    for i in range(l):
        print(l)
        print(names)
        for j in range(i+1, l):
            if names[i] == names[j]:
                print(names)
                names.remove(names[i])
                print(names)
                l = len(names)
    return names
        
        

if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia