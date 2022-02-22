
#we get this  input in string 
a = input("Enter first number: \n")
b = input("Enter the second number: \n")
c = input("Enter third number: \n")

#changing into integer
num1= int(a)    
num2=int(b)
num3=int(c)
 


#conditional statement
if(num1>num2 and num2>num3):
    print("Number 1 is greatest")
elif(num2>num1 and num2>num3):
    print("Number 2 is geatest")
else:
    print("Number 3 is greatest")
