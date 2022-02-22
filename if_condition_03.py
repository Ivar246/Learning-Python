#criteria for length of user name  to fill the user form 
name = input('Enter the Your name: ')

if len(name) < 4:
    print("Name must of at leat 4 character")
elif len(name) > 20:
    print("Name must be of maximum 20 characters")
else: 
    print("Valid name")