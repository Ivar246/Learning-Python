#checking elgibility according to the income range for particular organization

name = input("Enter the name of applicant:")
income = float(input("Enter the salary of applicant:"))
company = input("Enter your company name:")

#setting criteria
if income > 100000:
    has_high_income = True;
else: 
    has_high_income = False;

#displaying result
if(has_high_income and company== "ABC"):
    print(f"{name} is eligible for loan.")
elif(has_high_income and company != "ABC"):
    print(f"{name} is not a employee of ABC. \n Your request is terminated")
else:
    print(f"{name} is not eligible for loan")
