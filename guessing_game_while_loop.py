secret_number = 12
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Enter your guess number: "))
    guess_count +=1
    if(guess == secret_number):
        print("Hurrah! You won.")
        print("Thanks for playing...")
    break
else:
    print("You failed...")
    print("Try again!")