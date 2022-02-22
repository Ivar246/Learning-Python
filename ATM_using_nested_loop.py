print('....Welecome To The "StHa Bank Of Kathmandu"....')
balance = 60000
chances = 3;
restart = ('YES')

while chances >= 0:
    pin = int(input("Enter your four digit pin: "))
    if pin == 1234:
        print("You have enter the correct pin:")
        while restart not in ('NO'):
            print('''
            press <1> to check your balance
            press <2> to withdraw money
            press <3> to deposit amount
            press <4> to return card  
        ''')
        option = int(input("What would you like to choose?\n"))
        if option == 1:
            print(f"Your balance is ${balance}")
            restart = input("would you like to go back? \nEnter 'yes' or 'no': ").upper()
            if restart in ('NO'):
                print("Thank You")
                break
        elif option == 2:
            withdrawl = float(input("Enter the amount you want to withdraw($100 | $200 | $500 |$1000 | $2000|):"))
            if withdrawl == (100, 200, 500, 1000, 2000):
                balance = balance - withdrawl
                print(f"Your balance is now ${balance}")
                restart = input("would you like to go back? \nEnter 'yes' or 'no': ").upper()
                if restart in ('NO'):
                    print("Thank You")
                    break

            elif withdrawl != (100, 200, 500, 1000, 2000):
                print(f"Sorry,  you cannot withdraw {withdrawl} \nPlease, Enter the mentioned amount to withdraw..")
        elif option == 3:
            deposit = float(input("Enter the amount you want to deposit: "))
            balance += deposit
            print(f"your new balance is ${balance}")
            restart = input("would you like to go back? \nEnter 'yes' or 'no': ").upper()
            if restart in ('NO'):
                print("Thank You")
                break
    else:
        print('''sorry, Password is incorrect.... 
                 you cannot access..
        ''')
    chances-= 1
else:
    print('''
          Chances UP....
          Your account is temporarily freeze...
          Sorry Try again

    ''')




