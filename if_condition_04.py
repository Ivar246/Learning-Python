#converting pound into kg and kg into pound
weight = float(input('weight: '))
unit = input("Pound(P) or kilogram(k): ")

if unit.upper() == 'P':
    print(f"your weight is {0.45*weight} kg.")
elif unit.upper() == 'K':                      # -> upper() is used to convert whatever the user input ino upper case and check the value
    print(f"Your weight is {weight/0.45} pound")
else:
    print("Invalid input")